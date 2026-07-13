import math
import os
import NXOpen
import NXOpen.Annotations
import NXOpen.Features

def naca4_contour_points(m, p, t, chord, samples=20):
    """Return a closed polyline contour for a NACA 4-digit airfoil.

    The point order starts at the trailing edge on the lower surface,
    walks to the leading edge, then returns on the upper surface.
    """

    def thickness(x):
        return (
            5.0
            * t
            * (
                0.2969 * math.sqrt(x)
                - 0.1260 * x
                - 0.3516 * x**2
                + 0.2843 * x**3
                - 0.1015 * x**4
            )
        )

    def camber(x):
        if p <= 0.0:
            return 0.0, 0.0
        if x < p:
            yc = m / (p**2) * (2.0 * p * x - x**2)
            dyc_dx = 2.0 * m / (p**2) * (p - x)
        else:
            yc = m / ((1.0 - p) ** 2) * ((1.0 - 2.0 * p) + 2.0 * p * x - x**2)
            dyc_dx = 2.0 * m / ((1.0 - p) ** 2) * (p - x)
        return yc, dyc_dx

    x_values = [0.5 * (1.0 - math.cos(math.pi * i / samples)) for i in range(samples + 1)]

    contour = []
    for x in reversed(x_values):
        yc, dyc_dx = camber(x)
        theta = math.atan(dyc_dx)
        yt = thickness(x)
        xu = x - yt * math.sin(theta)
        yu = yc - yt * math.cos(theta)
        contour.append((xu * chord, yu * chord))

    for x in x_values[1:]:
        yc, dyc_dx = camber(x)
        theta = math.atan(dyc_dx)
        yt = thickness(x)
        xl = x + yt * math.sin(theta)
        yl = yc + yt * math.cos(theta)
        contour.append((xl * chord, yl * chord))

    return contour


def transform_contour(contour, z_value, twist_degrees=0.0, x_offset=0.0, y_offset=0.0, pivot_ratio=0.25):
    twist_radians = math.radians(twist_degrees)
    cosine = math.cos(twist_radians)
    sine = math.sin(twist_radians)

    xs = [point[0] for point in contour]
    chord = max(xs) - min(xs)
    pivot_x = min(xs) + pivot_ratio * chord

    points_3d = []
    for x_value, y_value in contour:
        dx = x_value - pivot_x
        x_rot = pivot_x + dx * cosine - y_value * sine
        y_rot = dx * sine + y_value * cosine
        points_3d.append(NXOpen.Point3d(x_rot + x_offset, y_rot + y_offset, z_value))

    return points_3d


def create_section_from_points(work_part, points_3d, distance_tolerance=0.01, chaining_tolerance=0.0095):
    section = work_part.Sections.CreateSection(distance_tolerance, chaining_tolerance, 0.5)
    section.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    section.AllowSelfIntersection(True)
    section.AllowDegenerateCurves(False)

    rules_options = work_part.ScRuleFactory.CreateRuleOptions()
    rules_options.SetSelectedFromInactive(True)

    for index, start_point in enumerate(points_3d):
        end_point = points_3d[(index + 1) % len(points_3d)]
        line = work_part.Curves.CreateLine(start_point, end_point)
        rule = work_part.ScRuleFactory.CreateRuleBaseCurveDumb([line], rules_options)
        section.AddToSection([rule], line, NXOpen.NXObject.Null, NXOpen.NXObject.Null, start_point, NXOpen.Section.Mode.Create, False)

    rules_options.Dispose()
    return section


def face_near_z(body, target_z, tolerance=0.5):
    for face in body.GetFaces():
        try:
            for edge in face.GetEdges():
                for vertex in edge.GetVertices():
                    if abs(vertex.Z - target_z) <= tolerance:
                        return face
        except Exception:
            continue
    return body.GetFaces()[0]


def find_modeling_view(work_part):
    try:
        return work_part.ModelingViews.FindObject("Front")
    except Exception:
        return work_part.ModelingViews.WorkView

def create_work_part_if_needed(the_session):
    work_part = the_session.Parts.Work
    if work_part is not None:
        return work_part
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    work_dir = os.path.join(script_dir, "_cadnx_work")
    os.makedirs(work_dir, exist_ok=True)
    part_name = os.path.join(work_dir, "S1_turbine_blade")
    
    result = the_session.Parts.NewDisplay(part_name, NXOpen.Part.Units.Millimeters)
    load_status = None
    if isinstance(result, tuple):
        new_part = result[0]
        if len(result)>1:
            load_status = result[1]
    else:
        new_part = result
        
    if load_status is not None:
        load_status.Dispose()
        
    work_part = the_session.Parts.Work or new_part
    if work_part is None:
        raise RuntimeError("Could not create an NX work part. Open a part and run the journal again.")
    return work_part
    
def create_pmi_span_dimension(work_part, root_face, tip_face, span, view):
    builder = work_part.Dimensions.CreatePmiLinearDimensionBuilder(None)
    try:
        builder.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XzPlane
        builder.Origin.SetInferRelativeToGeometry(True)

        root_point = NXOpen.Point3d(0.0, 0.0, 0.0)
        tip_point = NXOpen.Point3d(0.0, 0.0, span)

        builder.FirstAssociativity.SetValue(root_face, view, root_point)
        builder.SecondAssociativity.SetValue(tip_face, view, tip_point)

        associated_objects = [NXOpen.NXObject.Null] * 2
        associated_objects[0] = root_face
        associated_objects[1] = tip_face
        builder.AssociatedObjects.Nxobjects.SetArray(associated_objects)

        origin_data = NXOpen.Annotations.Annotation.AssociativeOriginData()
        origin_data.OriginType = NXOpen.Annotations.AssociativeOriginType.Drag
        origin_data.View = NXOpen.View.Null
        origin_data.ViewOfGeometry = NXOpen.View.Null
        origin_data.PointOnGeometry = NXOpen.Point.Null
        origin_data.VertAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.HorizAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.DimensionLine = 0
        origin_data.AssociatedView = NXOpen.View.Null
        origin_data.AssociatedPoint = NXOpen.Point.Null
        origin_data.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.XOffsetFactor = 0.0
        origin_data.YOffsetFactor = 0.0
        origin_data.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
        builder.Origin.SetAssociativeOrigin(origin_data)
        builder.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, view, NXOpen.Point3d(-40.0, -25.0, span * 0.5))

        return builder.Commit()
    finally:
        builder.Destroy()


def create_pmi_leader_note(work_part, target_face, anchor_point, view):
    builder = work_part.Annotations.CreatePmiNoteBuilder(None)
    try:
        builder.Text.SetEditorText(
            [
                "NACA 4412 TURBINE BLADE",
                "ROOT CHORD: 62.0 mm",
                "MID CHORD: 48.0 mm",
                "TIP CHORD: 34.0 mm",
                "TWIST: -20.0 DEG",
            ]
        )

        builder.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
        builder.Origin.SetInferRelativeToGeometry(True)

        associated_objects = [NXOpen.NXObject.Null]
        associated_objects[0] = target_face
        builder.AssociatedObjects.Nxobjects.SetArray(associated_objects)

        leader_data = work_part.Annotations.CreateLeaderData()
        leader_data.StubSize = 5.0
        leader_data.Arrowhead = NXOpen.Annotations.LeaderData.ArrowheadType.FilledArrow
        leader_data.VerticalAttachment = NXOpen.Annotations.LeaderVerticalAttachment.Center
        leader_data.Leader.SetValue(
            NXOpen.InferSnapType.SnapType.Surf,
            target_face,
            view,
            anchor_point,
            NXOpen.TaggedObject.Null,
            NXOpen.View.Null,
            anchor_point,
        )
        builder.Leader.Leaders.Append([leader_data])

        origin_data = NXOpen.Annotations.Annotation.AssociativeOriginData()
        origin_data.OriginType = NXOpen.Annotations.AssociativeOriginType.Drag
        origin_data.View = NXOpen.View.Null
        origin_data.ViewOfGeometry = NXOpen.View.Null
        origin_data.PointOnGeometry = NXOpen.Point.Null
        origin_data.VertAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.HorizAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.DimensionLine = 0
        origin_data.AssociatedView = NXOpen.View.Null
        origin_data.AssociatedPoint = NXOpen.Point.Null
        origin_data.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
        origin_data.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
        origin_data.XOffsetFactor = 0.0
        origin_data.YOffsetFactor = 0.0
        origin_data.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
        builder.Origin.SetAssociativeOrigin(origin_data)
        builder.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, view, NXOpen.Point3d(20.0, 35.0, anchor_point.Z))

        return builder.Commit()
    finally:
        builder.Destroy()

def try_create_pmi_annotations(work_part, root_face, tip_face, view):
    try:
        create_pmi_span_dimension(work_part, root_face, tip_face, 120.0, view)
    except Exception as exc:
        print(f"WARNING: skipped PMI leader note:{exc}")
        

def main():
    the_session = NXOpen.Session.GetSession()
    # work_part = the_session.Parts.Work
    work_part = create_work_part_if_needed(the_session)

    the_session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Turbine Blade")

    # NACA 4412 is a known, documented airfoil. The blade is intentionally simplified
    # into a printable lofted form with chord taper and twist.
    root_contour = naca4_contour_points(0.04, 0.40, 0.12, chord=62.0, samples=18)
    mid_contour = naca4_contour_points(0.04, 0.40, 0.12, chord=48.0, samples=18)
    tip_contour = naca4_contour_points(0.04, 0.40, 0.12, chord=34.0, samples=18)

    root_points = transform_contour(root_contour, z_value=0.0, twist_degrees=0.0, x_offset=0.0)
    mid_points = transform_contour(mid_contour, z_value=60.0, twist_degrees=-10.0, x_offset=4.0)
    tip_points = transform_contour(tip_contour, z_value=120.0, twist_degrees=-20.0, x_offset=8.0)

    root_section = create_section_from_points(work_part, root_points)
    mid_section = create_section_from_points(work_part, mid_points)
    tip_section = create_section_from_points(work_part, tip_points)

    loft_builder = work_part.Features.CreateThroughCurvesBuilder(NXOpen.Features.Feature.Null)
    try:
        loft_builder.BodyPreference = NXOpen.Features.ThroughCurvesBuilder.BodyPreferenceTypes.Solid
        loft_builder.Construction = NXOpen.Features.ThroughCurvesBuilder.ConstructionMethod.Normal
        loft_builder.PatchType = NXOpen.Features.ThroughCurvesBuilder.PatchTypes.Single
        loft_builder.ClosedInV = False
        loft_builder.NormalToEndSections = True
        loft_builder.PreserveShape = True
        loft_builder.PositionTolerance = 0.01
        loft_builder.CurvatureTolerance = 0.01
        loft_builder.TangentTolerance = 1.0

        loft_builder.SectionsList.Append([root_section, mid_section, tip_section])

        blade_feature = loft_builder.CommitFeature()
    finally:
        loft_builder.Destroy()

    blade_body = blade_feature.GetBodies()[0]
    root_face = face_near_z(blade_body, 0.0)
    tip_face = face_near_z(blade_body, 120.0)
    view = find_modeling_view(work_part)

    # create_pmi_span_dimension(work_part, root_face, tip_face, 120.0, view)
    # create_pmi_leader_note(work_part, tip_face, NXOpen.Point3d(8.0, 0.0, 120.0), view)
    
    try_create_pmi_annotations(work_part, root_face, tip_face, view)
    

    print("Created lofted NACA 4412 blade with PMI span dimension and leader note.")


if __name__ == "__main__":
    main()
