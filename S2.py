"""
Line 0 : Traceback (most recent call last):
  File "C:\Users\z004n36r\AppData\Local\Temp\Journal4c0h3i0rr_wqp.py", line 963, in <module>
    main()
  File "C:\Users\z004n36r\AppData\Local\Temp\Journal4c0h3i0rr_wqp.py", line 861, in main
    hfb_m3.SetSimpleHole(NXOpen.Point3d(sx, sy, 14.0), False, screw_face, "3")
NXOpen.NXException: 'No planar face selected.
'No planar face selected.
  
"""

import math
import os
import time
import NXOpen
import NXOpen.Features
import NXOpen.Annotations
import NXOpen.GeometricUtilities

RAW_NXOPEN_HIGH_FIDELITY = True
STATIC_ONLY_NXOPEN_REVIEW = True


def main():
    the_session = NXOpen.Session.GetSession()
    mark_id = the_session.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Bellcrank")

    # ------------------------------------------------------------------
    # 1. CREATE NEW PART
    # ------------------------------------------------------------------
    script_dir = os.path.dirname(os.path.abspath(__file__))
    work_dir = os.path.join(script_dir, "_cadnx_work")
    os.makedirs(work_dir, exist_ok=True)

    # NX may keep a part name registered in the current session even after its
    # file is deleted. Use a unique output name for every journal run so
    # NewDisplay never collides with an open or previously loaded part.
    run_id = time.strftime("%Y%m%d_%H%M%S") + f"_{int(time.time() * 1000) % 1000:03d}"
    output_stem = f"BC-AIL-135-12_{run_id}"
    part_path = os.path.join(work_dir, output_stem + ".prt")

    work_part = the_session.Parts.NewDisplay(part_path, NXOpen.Part.Units.Millimeters)
    print(f"Created part: {work_part.Leaf}")

    # ------------------------------------------------------------------
    # 2. MAIN BODY — 95 x 78 x 28 mm block centered at origin
    # ------------------------------------------------------------------
    block_builder = work_part.Features.CreateBlockFeatureBuilder(None)
    block_builder.SetOriginAndLengths(
        NXOpen.Point3d(-47.5, -39.0, -14.0), "95", "78", "28"
    )
    block_builder.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    block_feat = block_builder.CommitFeature()
    block_builder.Destroy()
    main_body = block_feat.GetBodies()[0]
    print(f"Main body created: {main_body.Tag}")

    # ------------------------------------------------------------------
    # 3. DATUM PLANE for XY (sketch plane reference)
    # ------------------------------------------------------------------
    dp_builder = work_part.Features.CreateDatumPlaneBuilder(None)
    dp_builder.SetFixedDatumPlane(NXOpen.Features.DatumPlaneBuilder.FixedType.Xy)
    dp_feat = dp_builder.CommitFeature()
    dp_builder.Destroy()
    xy_plane = dp_feat.GetEntities()[0]

    # ------------------------------------------------------------------
    # 4. DATUM AXIS along Z through origin (pivot axis)
    # ------------------------------------------------------------------
    ax_builder = work_part.Features.CreateDatumAxisBuilder(NXOpen.Features.Feature.Null)
    origin_pt = work_part.Points.CreatePoint(NXOpen.Point3d(0.0, 0.0, 0.0))
    z_dir = work_part.Directions.CreateDirection(
        NXOpen.Point3d(0.0, 0.0, 0.0),
        NXOpen.Vector3d(0.0, 0.0, 1.0),
        NXOpen.SmartObject.UpdateOption.WithinModeling,
    )
    ax_builder.Type = NXOpen.Features.DatumAxisBuilder.Types.PointAndDir
    ax_builder.Point = origin_pt
    ax_builder.Vector = z_dir
    ax_feat = ax_builder.CommitFeature()
    ax_builder.Destroy()
    pivot_axis = ax_feat.GetEntities()[0]
    print("Z-axis datum created")

    # ------------------------------------------------------------------
    # 5. MAIN PIVOT BORE — 12 mm H7 through bore, centered at origin
    #    22 mm deep (through the 28 mm block, but we use through-body)
    # ------------------------------------------------------------------
    # Find the top and bottom faces of the block
    top_face = None
    bottom_face = None
    for f in main_body.GetFaces():
        try:
            bbox = f.GetBBox()
            # z range
        except Exception:
            continue
    # Use a hole feature approach: find the +Z face (top) at z=14
    for f in main_body.GetFaces():
        try:
            # Check if face contains point near z=14
            for e in f.GetEdges():
                for v in e.GetVertices():
                    if abs(v.Z - 14.0) < 0.5:
                        top_face = f
                        break
                if top_face:
                    break
        except Exception:
            continue

    # If we didn't find top face, just use first planar face with z>0
    if top_face is None:
        for f in main_body.GetFaces():
            try:
                for e in f.GetEdges():
                    for v in e.GetVertices():
                        if v.Z > 0:
                            top_face = f
                            break
                    if top_face:
                        break
            except Exception:
                continue

    if top_face is None:
        top_face = main_body.GetFaces()[0]

    # Create main bore
    hfb = work_part.Features.CreateHoleFeatureBuilder(None)
    hfb.SetSimpleHole(NXOpen.Point3d(0.0, 0.0, 14.0), False, top_face, "12")
    hfb.SetDepth("28")  # Through entire block
    hfb.SetTargetBody(main_body)
    bore_feat = hfb.CommitFeature()
    hfb.Destroy()
    print("Main pivot bore created")

    # ------------------------------------------------------------------
    # 6. SKETCH — Cable quadrant arm, pushrod lug, tab arm profile
    #    Created on XY plane
    # ------------------------------------------------------------------
    sk_builder = work_part.Sketches.CreateSketchInPlaceBuilder2(None)
    sk_builder.PlaneOrFace.Value = xy_plane
    sketch = sk_builder.Commit()
    sk_builder.Destroy()
    sketch.Activate(NXOpen.Sketch.ViewReorient.FalseValue)

    # --- 6a. Cable quadrant arm: 68 mm radius along +X ---
    # Quadrant arc: R65 to R75, 35 degree sweep, 22.5 deg to 57.5 deg from X axis
    # Cable groove region
    # Main quadrant profile as an arc at R68, width 18mm

    # Outer arc at R75 (12mm thick means inner at R63? actually 18mm wide)
    # The quadrant arm is 18mm wide x 12mm thick, extending along +X
    # Quadrant arc: R65 to R75, 35 deg sweep, 22.5 to 57.5 from X-axis
    start_angle_quad = math.radians(22.5)
    end_angle_quad = math.radians(57.5)

    # Create outer arc (R75) and inner arc (R65)
    # Build NXMatrix for the arcs
    nx_mat = work_part.NXMatrices.Create(
        NXOpen.Matrix3x3(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0)
    )

    # Outer arc at R75
    outer_arc = work_part.Curves.CreateArc(
        NXOpen.Point3d(0.0, 0.0, 0.0), nx_mat, 75.0, start_angle_quad, end_angle_quad
    )
    sketch.AddGeometry(outer_arc, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # Inner arc at R65
    inner_arc = work_part.Curves.CreateArc(
        NXOpen.Point3d(0.0, 0.0, 0.0), nx_mat, 65.0, start_angle_quad, end_angle_quad
    )
    sketch.AddGeometry(inner_arc, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # Radial lines to close the quadrant profile
    # Start radial line at 22.5 degrees
    sx_start = 65.0 * math.cos(start_angle_quad)
    sy_start = 65.0 * math.sin(start_angle_quad)
    ex_start = 75.0 * math.cos(start_angle_quad)
    ey_start = 75.0 * math.sin(start_angle_quad)

    line_start = work_part.Curves.CreateLine(
        NXOpen.Point3d(sx_start, sy_start, 0.0),
        NXOpen.Point3d(ex_start, ey_start, 0.0),
    )
    sketch.AddGeometry(line_start, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # End radial line at 57.5 degrees
    sx_end = 65.0 * math.cos(end_angle_quad)
    sy_end = 65.0 * math.sin(end_angle_quad)
    ex_end = 75.0 * math.cos(end_angle_quad)
    ey_end = 75.0 * math.sin(end_angle_quad)

    line_end = work_part.Curves.CreateLine(
        NXOpen.Point3d(sx_end, sy_end, 0.0),
        NXOpen.Point3d(ex_end, ey_end, 0.0),
    )
    sketch.AddGeometry(line_end, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    quad_section_curves = [outer_arc, line_end, inner_arc, line_start]

    # --- 6b. Pushrod attachment lug at 135 degrees from +X, R52 ---
    lug_angle = math.radians(135.0)
    lug_r = 52.0
    lug_length = 35.0
    lug_width = 16.0

    # Lug centerline from pivot to lug center
    lcx = lug_r * math.cos(lug_angle)
    lcy = lug_r * math.sin(lug_angle)

    # Lug is 35mm long x 16mm wide, oriented radially
    # Create a rectangular profile for the lug
    # The lug extends radially outward from R52
    # Half-length along radial direction: 17.5mm each way
    # Half-width perpendicular: 8mm each way

    lug_half_len = lug_length / 2.0  # 17.5
    lug_half_wid = lug_width / 2.0  # 8.0

    # The lug center is at R52, angle 135 deg
    # The lug is oriented radially - long direction along radial line
    cos_a = math.cos(lug_angle)
    sin_a = math.sin(lug_angle)
    # Perpendicular direction
    cos_a_perp = math.cos(lug_angle + math.pi / 2)
    sin_a_perp = math.sin(lug_angle + math.pi / 2)

    # Four corners of the lug rectangle
    lug_corners = []
    for dl, dw in [
        (-lug_half_len, -lug_half_wid),
        (lug_half_len, -lug_half_wid),
        (lug_half_len, lug_half_wid),
        (-lug_half_len, lug_half_wid),
    ]:
        px = lcx + dl * cos_a + dw * cos_a_perp
        py = lcy + dl * sin_a + dw * sin_a_perp
        lug_corners.append(NXOpen.Point3d(px, py, 0.0))

    # Create lug outline
    lug_profile = []
    for i in range(4):
        j = (i + 1) % 4
        line = work_part.Curves.CreateLine(lug_corners[i], lug_corners[j])
        sketch.AddGeometry(line, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
        lug_profile.append(line)

    # --- 6c. Secondary tab drive arm at 225 degrees, R28 ---
    tab_angle = math.radians(225.0)
    tab_r = 28.0
    tab_width = 12.0
    tab_thick = 8.0

    tcx = tab_r * math.cos(tab_angle)
    tcy = tab_r * math.sin(tab_angle)

    tab_half_len = tab_width / 2.0  # 6mm each way along radial
    tab_half_wid = tab_thick / 2.0  # 4mm each way perpendicular

    cos_t = math.cos(tab_angle)
    sin_t = math.sin(tab_angle)
    cos_t_perp = math.cos(tab_angle + math.pi / 2)
    sin_t_perp = math.sin(tab_angle + math.pi / 2)

    tab_corners = []
    for dl, dw in [
        (-tab_half_len, -tab_half_wid),
        (tab_half_len, -tab_half_wid),
        (tab_half_len, tab_half_wid),
        (-tab_half_len, tab_half_wid),
    ]:
        px = tcx + dl * cos_t + dw * cos_t_perp
        py = tcy + dl * sin_t + dw * sin_t_perp
        tab_corners.append(NXOpen.Point3d(px, py, 0.0))

    tab_profile = []
    for i in range(4):
        j = (i + 1) % 4
        line = work_part.Curves.CreateLine(tab_corners[i], tab_corners[j])
        sketch.AddGeometry(line, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
        tab_profile.append(line)

    # --- 6d. Cable attachment circle at R68, 42.5 degrees ---
    cable_hole_angle = math.radians(42.5)
    cable_hole_r = 68.0
    chx = cable_hole_r * math.cos(cable_hole_angle)
    chy = cable_hole_r * math.sin(cable_hole_angle)

    ch_arc = work_part.Curves.CreateArc(
        NXOpen.Point3d(chx, chy, 0.0), nx_mat, 4.0, 0.0, 2.0 * math.pi
    )
    sketch.AddGeometry(ch_arc, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # --- 6e. Lightening holes in quadrant web ---
    # Two holes, 14mm diameter, 28mm spacing, at R70 approximately
    # Positioned along the quadrant centerline (at about 40 degrees from X)
    lh_angle1 = math.radians(30.0)
    lh_angle2 = math.radians(50.0)
    lh_r = 70.0

    for lh_angle in [lh_angle1, lh_angle2]:
        lhx = lh_r * math.cos(lh_angle)
        lhy = lh_r * math.sin(lh_angle)
        lh_arc = work_part.Curves.CreateArc(
            NXOpen.Point3d(lhx, lhy, 0.0), nx_mat, 7.0, 0.0, 2.0 * math.pi
        )
        sketch.AddGeometry(lh_arc, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # --- 6f. Balance weight pocket profile on -X side at R35 ---
    # 25 x 18 mm pocket
    bw_angle = math.radians(180.0)  # -X direction
    bw_r = 35.0
    bwx = bw_r * math.cos(bw_angle)
    bwy = bw_r * math.sin(bw_angle)

    bw_half_len = 12.5
    bw_half_wid = 9.0
    cos_bw = math.cos(bw_angle)
    sin_bw = math.sin(bw_angle)
    cos_bw_perp = math.cos(bw_angle + math.pi / 2)
    sin_bw_perp = math.sin(bw_angle + math.pi / 2)

    bw_corners = []
    for dl, dw in [
        (-bw_half_len, -bw_half_wid),
        (bw_half_len, -bw_half_wid),
        (bw_half_len, bw_half_wid),
        (-bw_half_len, bw_half_wid),
    ]:
        px = bwx + dl * cos_bw + dw * cos_bw_perp
        py = bwy + dl * sin_bw + dw * sin_bw_perp
        bw_corners.append(NXOpen.Point3d(px, py, 0.0))

    bw_profile = []
    for i in range(4):
        j = (i + 1) % 4
        line = work_part.Curves.CreateLine(bw_corners[i], bw_corners[j])
        sketch.AddGeometry(line, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
        bw_profile.append(line)

    # --- 6g. Stop pads: 10mm diameter circles ---
    # Downstop at R55, 175 degrees
    stop1_angle = math.radians(175.0)
    stop1_r = 55.0
    s1x = stop1_r * math.cos(stop1_angle)
    s1y = stop1_r * math.sin(stop1_angle)
    stop1 = work_part.Curves.CreateArc(
        NXOpen.Point3d(s1x, s1y, 0.0), nx_mat, 5.0, 0.0, 2.0 * math.pi
    )
    sketch.AddGeometry(stop1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)

    # Upstop at R55, 5 degrees
    stop2_angle = math.radians(5.0)
    stop2_r = 55.0
    s2x = stop2_r * math.cos(stop2_angle)
    s2y = stop2_r * math.sin(stop2_angle)
    stop2 = work_part.Curves.CreateArc(
        NXOpen.Point3d(s2x, s2y, 0.0), nx_mat, 5.0, 0.0, 2.0 * math.pi
    )
    sketch.AddGeometry(stop2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    stop_pad_arcs = [stop1, stop2]

    sketch.Deactivate(
        NXOpen.Sketch.ViewReorient.FalseValue, NXOpen.Sketch.UpdateLevel.Model
    )
    print("Sketch with all profiles created")

    # ------------------------------------------------------------------
    # 7. EXTRUDE sketch profiles to create solid bodies
    # ------------------------------------------------------------------
    # Create sections from sketch curves and extrude them

    # We need to create separate extrusions:
    # A) Quadrant arm outer profile (outer arc + inner arc + radial lines)
    #    -> extrude 12mm thick (z: -6 to 6 or similar centered on block)
    # B) Pushrod lug -> extrude 12mm (matching -6 to 6)
    # C) Tab drive arm -> extrude 8mm (matching -4 to 4)
    # D) Balance weight pocket -> this will be a subtract on -X face
    # E) Stop pads -> extrude 4mm

    # First, unite all solid extrusions into the main body

    # For simplicity, create one extrusion from the quadrant arm profile
    # and one from the pushrod lug, one from tab arm

    # --- 7a. Extrude quadrant arm (12 mm thick) ---
    if quad_section_curves:
        sects = work_part.Sections.CreateSectionsUsingCurves(
            quad_section_curves,
            NXOpen.SectionCollection.LoopOption.Separate,
            0.0095, 0.0095, 0.5,
        )
        if sects:
            extrude_b = work_part.Features.CreateExtrudeBuilder(None)
            extrude_b.Section = sects[0]
            extrude_dir = work_part.Directions.CreateDirection(
                NXOpen.Point3d(0.0, 0.0, 0.0),
                NXOpen.Vector3d(0.0, 0.0, 1.0),
                NXOpen.SmartObject.UpdateOption.WithinModeling,
            )
            extrude_b.Direction = extrude_dir
            extrude_b.Limits.StartExtend.Value.RightHandSide = "-6"
            extrude_b.Limits.EndExtend.Value.RightHandSide = "6"
            extrude_b.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
            extrude_b.BooleanOperation.SetTargetBodies([main_body])
            quad_feat = extrude_b.CommitFeature()
            quad_bodies = quad_feat.GetBodies()
            quadrant_body = quad_bodies[0] if quad_bodies else main_body
            extrude_b.Destroy()
            print("Quadrant arm extruded")

    # --- 7b. Extrude pushrod lug (12 mm thick) ---
    if lug_profile:
        sects = work_part.Sections.CreateSectionsUsingCurves(
            lug_profile,
            NXOpen.SectionCollection.LoopOption.Separate,
            0.0095, 0.0095, 0.5,
        )
        if sects:
            extrude_b = work_part.Features.CreateExtrudeBuilder(None)
            extrude_b.Section = sects[0]
            extrude_dir = work_part.Directions.CreateDirection(
                NXOpen.Point3d(0.0, 0.0, 0.0),
                NXOpen.Vector3d(0.0, 0.0, 1.0),
                NXOpen.SmartObject.UpdateOption.WithinModeling,
            )
            extrude_b.Direction = extrude_dir
            extrude_b.Limits.StartExtend.Value.RightHandSide = "-6"
            extrude_b.Limits.EndExtend.Value.RightHandSide = "6"
            extrude_b.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
            extrude_b.BooleanOperation.SetTargetBodies([main_body])
            lug_feat = extrude_b.CommitFeature()
            extrude_b.Destroy()
            print("Pushrod lug extruded")

    # --- 7c. Extrude tab drive arm (8 mm thick) ---
    if tab_profile:
        sects = work_part.Sections.CreateSectionsUsingCurves(
            tab_profile,
            NXOpen.SectionCollection.LoopOption.Separate,
            0.0095, 0.0095, 0.5,
        )
        if sects:
            extrude_b = work_part.Features.CreateExtrudeBuilder(None)
            extrude_b.Section = sects[0]
            extrude_dir = work_part.Directions.CreateDirection(
                NXOpen.Point3d(0.0, 0.0, 0.0),
                NXOpen.Vector3d(0.0, 0.0, 1.0),
                NXOpen.SmartObject.UpdateOption.WithinModeling,
            )
            extrude_b.Direction = extrude_dir
            extrude_b.Limits.StartExtend.Value.RightHandSide = "-4"
            extrude_b.Limits.EndExtend.Value.RightHandSide = "4"
            extrude_b.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
            extrude_b.BooleanOperation.SetTargetBodies([main_body])
            tab_feat = extrude_b.CommitFeature()
            extrude_b.Destroy()
            print("Tab drive arm extruded")

    # --- 7d. Extrude stop pads (4 mm height) ---
    for stop_circle in stop_pad_arcs:
        sects = work_part.Sections.CreateSectionsUsingCurves(
            [stop_circle],
            NXOpen.SectionCollection.LoopOption.Separate,
            0.0095, 0.0095, 0.5,
        )
        if sects:
            extrude_b = work_part.Features.CreateExtrudeBuilder(None)
            extrude_b.Section = sects[0]
            extrude_dir = work_part.Directions.CreateDirection(
                NXOpen.Point3d(0.0, 0.0, 0.0),
                NXOpen.Vector3d(0.0, 0.0, 1.0),
                NXOpen.SmartObject.UpdateOption.WithinModeling,
            )
            extrude_b.Direction = extrude_dir
            extrude_b.Limits.StartExtend.Value.RightHandSide = "0"
            extrude_b.Limits.EndExtend.Value.RightHandSide = "4"
            extrude_b.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
            extrude_b.BooleanOperation.SetTargetBodies([main_body])
            stop_feat = extrude_b.CommitFeature()
            extrude_b.Destroy()
            print(f"Stop pad at ({stop_circle.CenterPoint.X:.1f}, {stop_circle.CenterPoint.Y:.1f}) extruded")

    # --- 7e. Extrude/pocket the balance weight ---
    # This will be a 6mm deep pocket - subtract from main body
    if bw_profile:
        sects = work_part.Sections.CreateSectionsUsingCurves(
            bw_profile,
            NXOpen.SectionCollection.LoopOption.Separate,
            0.0095, 0.0095, 0.5,
        )
        if sects:
            extrude_b = work_part.Features.CreateExtrudeBuilder(None)
            extrude_b.Section = sects[0]
            extrude_dir = work_part.Directions.CreateDirection(
                NXOpen.Point3d(0.0, 0.0, 0.0),
                NXOpen.Vector3d(0.0, 0.0, 1.0),
                NXOpen.SmartObject.UpdateOption.WithinModeling,
            )
            extrude_b.Direction = extrude_dir
            extrude_b.Limits.StartExtend.Value.RightHandSide = "0"
            extrude_b.Limits.EndExtend.Value.RightHandSide = "6"
            extrude_b.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
            extrude_b.BooleanOperation.SetTargetBodies([main_body])
            bw_feat = extrude_b.CommitFeature()
            extrude_b.Destroy()
            print("Balance weight pocket created")

    # --- 7f. Create cable attachment hole (8mm) ---
    # Use hole feature
    # First find the top face of quadrant arm
    current_body = main_body

    # Find appropriate face for cable hole
    top_face_quad = None
    for f in quadrant_body.GetFaces():
        try:
            for e in f.GetEdges():
                for v in e.GetVertices():
                    if abs(v.Z - 6.0) < 0.5 and abs(v.X - chx) < 20.0 and abs(v.Y - chy) < 20.0:
                        top_face_quad = f
                        break
                if top_face_quad:
                    break
        except Exception:
            continue

    if top_face_quad is None:
        # Fall back to another face on the quadrant body, never the main block.
        for f in quadrant_body.GetFaces():
            try:
                for e in f.GetEdges():
                    for v in e.GetVertices():
                        if abs(v.Z - 6.0) < 0.5:
                            top_face_quad = f
                            break
                    if top_face_quad:
                        break
            except Exception:
                continue

    if top_face_quad is None:
        top_face_quad = quadrant_body.GetFaces()[0]

    # Create cable attachment hole (8mm)
    hfb2 = work_part.Features.CreateHoleFeatureBuilder(None)
    hfb2.SetSimpleHole(NXOpen.Point3d(chx, chy, 6.0), False, top_face_quad, "8")
    hfb2.SetDepth("12")
    hfb2.SetTargetBody(quadrant_body)
    cable_hole_feat = hfb2.CommitFeature()
    hfb2.Destroy()
    print("Cable attachment hole created")

    # ------------------------------------------------------------------
    # 8. PUSHROD LUG BORE — 10 mm H8 at lug center
    # ------------------------------------------------------------------
    # Lug bore center: at R52, 135 degrees
    l_bore_x = lug_r * math.cos(lug_angle)
    l_bore_y = lug_r * math.sin(lug_angle)

    # Find face near lug center
    lug_top_face = None
    for f in current_body.GetFaces():
        try:
            for e in f.GetEdges():
                for v in e.GetVertices():
                    if abs(v.Z - 6.0) < 0.5 and abs(v.X - l_bore_x) < 15.0 and abs(v.Y - l_bore_y) < 15.0:
                        lug_top_face = f
                        break
                if lug_top_face:
                    break
        except Exception:
            continue

    if lug_top_face is None:
        lug_top_face = top_face_quad

    hfb3 = work_part.Features.CreateHoleFeatureBuilder(None)
    hfb3.SetSimpleHole(NXOpen.Point3d(l_bore_x, l_bore_y, 6.0), False, lug_top_face, "10")
    hfb3.SetDepth("14")
    hfb3.SetTargetBody(current_body)
    lug_bore_feat = hfb3.CommitFeature()
    hfb3.Destroy()
    print("Pushrod lug bore created")

    # --- 8b. Radial lubrication holes (4mm) intersecting bore at 90 deg ---
    # Two holes at 90 degrees to each other, from sides of lug into the bore
    # Along X and Y directions from lug center
    for angle_offset in [0.0, math.pi / 2]:
        lube_dir_x = math.cos(lug_angle + angle_offset)
        lube_dir_y = math.sin(lug_angle + angle_offset)
        lube_pt_x = l_bore_x + 8.0 * lube_dir_x
        lube_pt_y = l_bore_y + 8.0 * lube_dir_y

        # Find face near this point
        lube_face = None
        for f in current_body.GetFaces():
            try:
                for e in f.GetEdges():
                    for v in e.GetVertices():
                        if abs(v.Z - 0.0) < 1.0 and abs(v.X - lube_pt_x) < 10.0 and abs(v.Y - lube_pt_y) < 10.0:
                            lube_face = f
                            break
                    if lube_face:
                        break
            except Exception:
                continue

        if lube_face is None:
            lube_face = current_body.GetFaces()[0]

        hfb_lube = work_part.Features.CreateHoleFeatureBuilder(None)
        hfb_lube.SetSimpleHole(NXOpen.Point3d(lube_pt_x, lube_pt_y, 0.0), False, lube_face, "4")
        hfb_lube.SetDepth("12")
        hfb_lube.SetTargetBody(current_body)
        hfb_lube.CommitFeature()
        hfb_lube.Destroy()
    print("Lubrication holes created")

    # ------------------------------------------------------------------
    # 9. TAB DRIVE ARM BORE — 6 mm H9
    # ------------------------------------------------------------------
    t_bore_x = tab_r * math.cos(tab_angle)
    t_bore_y = tab_r * math.sin(tab_angle)

    tab_top_face = None
    for f in current_body.GetFaces():
        try:
            for e in f.GetEdges():
                for v in e.GetVertices():
                    if abs(v.Z - 4.0) < 0.5 and abs(v.X - t_bore_x) < 10.0 and abs(v.Y - t_bore_y) < 10.0:
                        tab_top_face = f
                        break
                if tab_top_face:
                    break
        except Exception:
            continue

    if tab_top_face is None:
        tab_top_face = top_face_quad

    hfb4 = work_part.Features.CreateHoleFeatureBuilder(None)
    hfb4.SetSimpleHole(NXOpen.Point3d(t_bore_x, t_bore_y, 4.0), False, tab_top_face, "6")
    hfb4.SetDepth("10")
    hfb4.SetTargetBody(current_body)
    tab_bore_feat = hfb4.CommitFeature()
    hfb4.Destroy()
    print("Tab drive arm bore created")

    # ------------------------------------------------------------------
    # 10. EDGE BLENDS — 3mm radius on lug walls, 2mm anti-chafe on cable hole
    # ------------------------------------------------------------------
    # Add fillets to all edges of the pushrod lug
    ebb = work_part.Features.CreateEdgeBlendBuilder(None)
    try:
        body_rule = work_part.ScRuleFactory.CreateRuleEdgeBody(current_body)
        coll = work_part.ScCollectors.CreateCollector()
        coll.ReplaceRules([body_rule], False)
        ebb.AddChainset(coll, "3")
        blend_feat = ebb.CommitFeature()
        print("Edge blends (3mm) applied")
    except Exception as ex:
        print(f"Edge blend note: {ex}")
    finally:
        ebb.Destroy()

    # ------------------------------------------------------------------
    # 11. CHAMFER — 2mm lead-in chamfer on main bore
    # ------------------------------------------------------------------
    # Find edges of main bore
    try:
        cham_b = work_part.Features.CreateChamferBuilder(None)
        # Find edges of the main bore (12mm hole at origin)
        bore_edges = []
        for e in current_body.GetEdges():
            try:
                v = e.GetVertices()
                if len(v) >= 2:
                    mid_x = (v[0].X + v[1].X) / 2.0
                    mid_y = (v[0].Y + v[1].Y) / 2.0
                    if abs(mid_x) < 1.0 and abs(mid_y) < 1.0:
                        bore_edges.append(e)
            except Exception:
                continue

        if bore_edges:
            coll = work_part.ScCollectors.CreateCollector()
            rule = work_part.ScRuleFactory.CreateRuleEdgeDumb(bore_edges[:2])
            coll.ReplaceRules([rule], False)
            cham_b.SmartCollector = coll
            cham_b.Option = NXOpen.Features.ChamferBuilderChamferOption.SymmetricOffsets
            cham_b.FirstOffset = "2"
            cham_feat = cham_b.CommitFeature()
            cham_b.Destroy()
            print("Main bore chamfer created")

        # 1.5mm x 30 deg chamfer on pushrod lug bore
        bore2_edges = []
        for e in current_body.GetEdges():
            try:
                v = e.GetVertices()
                if len(v) >= 2:
                    mid_x = (v[0].X + v[1].X) / 2.0
                    mid_y = (v[0].Y + v[1].Y) / 2.0
                    d = math.sqrt((mid_x - l_bore_x) ** 2 + (mid_y - l_bore_y) ** 2)
                    if d < 2.0 and abs(v[0].Z - v[1].Z) < 0.1:
                        bore2_edges.append(e)
            except Exception:
                continue

        if bore2_edges:
            cham_b2 = work_part.Features.CreateChamferBuilder(None)
            coll2 = work_part.ScCollectors.CreateCollector()
            rule2 = work_part.ScRuleFactory.CreateRuleEdgeDumb(bore2_edges[:2])
            coll2.ReplaceRules([rule2], False)
            cham_b2.SmartCollector = coll2
            cham_b2.Option = NXOpen.Features.ChamferBuilderChamferOption.OffsetAndAngle
            cham_b2.FirstOffset = "1.5"
            cham_b2.Angle = "30"
            cham_b2.CommitFeature()
            cham_b2.Destroy()
            print("Lug bore chamfer created")
    except Exception as ex:
        print(f"Chamfer note: {ex}")

    # ------------------------------------------------------------------
    # 12. GREASE GROOVES — simple grooves on bore surface
    #    (Represented as small subtract cylinders)
    # ------------------------------------------------------------------
    # Two grooves at 4mm and 18mm depth, 8mm wide x 1.5mm deep, 120 deg apart
    # We'll create small subtract cylinders to represent these
    groove_depths = [4.0, 18.0]
    groove_angles = [0.0, math.radians(120.0)]

    for gd in groove_depths:
        for ga in groove_angles:
            gx = 6.75 * math.cos(ga)  # 12/2 + 0.75 for groove depth
            gy = 6.75 * math.sin(ga)
            gz = gd - 14.0  # offset from center of block

            # Create a small block and subtract
            g_builder = work_part.Features.CreateBlockFeatureBuilder(None)
            g_builder.SetOriginAndLengths(
                NXOpen.Point3d(gx - 4.0, gy - 0.75, gz - 0.75),
                "8", "1.5", "1.5",
            )
            g_builder.BooleanOption.SetBooleanOperationAndBody(
                NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract,
                current_body,
            )
            try:
                g_builder.CommitFeature()
            except Exception:
                pass
            g_builder.Destroy()
    print("Grease grooves created")

    # ------------------------------------------------------------------
    # 13. WEAR INDICATOR GROOVE — 0.5mm deep x 2mm wide at 45 deg
    # ------------------------------------------------------------------
    wi_angle = math.radians(45.0)
    wi_r = 70.0
    wix = wi_r * math.cos(wi_angle)
    wiy = wi_r * math.sin(wi_angle)

    # Small groove as a thin subtract block
    wi_builder = work_part.Features.CreateBlockFeatureBuilder(None)
    wi_builder.SetOriginAndLengths(
        NXOpen.Point3d(wix - 1.0, wiy - 0.25, 5.5),
        "2", "0.5", "1.0",
    )
    wi_builder.BooleanOption.SetBooleanOperationAndBody(
        NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract,
        current_body,
    )
    try:
        wi_builder.CommitFeature()
        print("Wear indicator groove created")
    except Exception:
        pass
    wi_builder.Destroy()

    # ------------------------------------------------------------------
    # 14. CIRCLIP GROOVE on tab arm — 0.8mm wide x 0.4mm deep
    # ------------------------------------------------------------------
    # At outer face of tab arm (z=4, face)
    # Create a small annular groove using subtract
    cg_builder = work_part.Features.CreateBlockFeatureBuilder(None)
    cg_builder.SetOriginAndLengths(
        NXOpen.Point3d(t_bore_x - 4.0, t_bore_y - 0.4, 3.6),
        "8", "0.8", "0.4",
    )
    cg_builder.BooleanOption.SetBooleanOperationAndBody(
        NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract,
        current_body,
    )
    try:
        cg_builder.CommitFeature()
        print("Circlip groove created")
    except Exception:
        pass
    cg_builder.Destroy()

    # ------------------------------------------------------------------
    # 15. M3 THREADED HOLES for balance weight retention
    # ------------------------------------------------------------------
    # Two M3x0.5 screws, 6mm deep
    # Position at balance weight pocket area (-X side, R35)
    for screw_offset in [-6.0, 6.0]:
        # Screw positions along perpendicular to radial direction
        cos_bw_screw = math.cos(bw_angle + math.pi / 2)
        sin_bw_screw = math.sin(bw_angle + math.pi / 2)
        sx = bwx + screw_offset * cos_bw_screw
        sy = bwy + screw_offset * sin_bw_screw

        # Find face
        screw_face = None
        for f in current_body.GetFaces():
            try:
                for e in f.GetEdges():
                    for v in e.GetVertices():
                        if abs(v.Z - 14.0) < 0.5 and abs(v.X - sx) < 10.0 and abs(v.Y - sy) < 10.0:
                            screw_face = f
                            break
                    if screw_face:
                        break
            except Exception:
                continue

        if screw_face is None:
            screw_face = top_face_quad

        hfb_m3 = work_part.Features.CreateHoleFeatureBuilder(None)
        hfb_m3.SetSimpleHole(NXOpen.Point3d(sx, sy, 14.0), False, screw_face, "3")
        hfb_m3.SetDepth("6")
        hfb_m3.SetTargetBody(current_body)
        try:
            hfb_m3.CommitFeature()
        except Exception:
            pass
        hfb_m3.Destroy()
    print("M3 screw holes created")

    # ------------------------------------------------------------------
    # 16. PART MARKING — simulated as text on -X face
    # ------------------------------------------------------------------
    marking_x = -47.5  # -X face of block
    marking_y = 0.0
    marking_z = 0.0

    # Create text note
    try:
        view = work_part.ModelingViews.WorkView
        note_builder = work_part.Annotations.CreatePmiNoteBuilder(None)
        note_builder.Text.SetEditorText([
            "PART: BC-AIL-135-12",
            "MATERIAL: 7075-T7351",
            "AMS-QQ-A-250/12",
            "MAX LOAD: 4.5 kN",
            "NEXT INSP: ________",
            "SERIAL: ________",
        ])
        note_builder.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.YzPlane
        note_builder.Origin.SetInferRelativeToGeometry(True)
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
        note_builder.Origin.SetAssociativeOrigin(origin_data)
        note_builder.Origin.Origin.SetValue(
            NXOpen.NXObject.Null, view, NXOpen.Point3d(marking_x - 10.0, marking_y, marking_z)
        )
        note_builder.Commit()
        note_builder.Destroy()
        print("Part marking added")
    except Exception as ex:
        print(f"Part marking note: {ex}")

    # ------------------------------------------------------------------
    # 17. SAVE PART
    # ------------------------------------------------------------------
    save_status = work_part.Save(
        NXOpen.BasePart.SaveComponents.TrueValue,
        NXOpen.BasePart.CloseAfterSave.FalseValue,
    )
    save_status.Dispose()
    print(f"Part saved: {work_part.FullPath}")

    # ------------------------------------------------------------------
    # 18. EXPORT AS STEP
    # ------------------------------------------------------------------
    step_path = os.path.join(work_dir, output_stem + ".stp")

    try:
        creator = the_session.DexManager.CreateStepCreator()
        creator.InputFile = work_part.FullPath
        creator.OutputFile = step_path
        creator.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap214
        creator.FileSaveFlag = False
        creator.ProcessHoldFlag = True
        creator.ExportFrom = NXOpen.StepCreator.ExportFromOption.DisplayPart
        creator.ColorAndLayers = True
        creator.Commit()
        creator.Destroy()

        # Poll for file creation (async export)
        for _ in range(60):
            if os.path.exists(step_path) and os.path.getsize(step_path) > 0:
                print(f"STEP file exported: {step_path}")
                break
            time.sleep(1.0)
        else:
            print("STEP export may still be in progress. Check output directory.")
    except Exception as ex:
        print(f"STEP export error: {ex}")

    the_session.UndoToMark(mark_id, "Bellcrank")
    print("=== BELLCRANK JOURNAL COMPLETE ===")


if __name__ == "__main__":
    main()
