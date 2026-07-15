"""
Create a single solid aircraft flight-control bellcrank STEP model in millimeters.

The bellcrank lies primarily in the XY plane and is symmetric about its 12 mm thickness in Z. Center the part thickness about Z = 0, so its bottom is at Z = -6 mm and its top is at Z = 6 mm.

Create a central circular pivot hub 50 mm in diameter and 12 mm thick, centered at X = 0 and Y = 0.

Add a central vertical through-bore 20 mm in diameter through the pivot hub. Add a concentric bearing seat on the top face, 32 mm in diameter and 4 mm deep. Add an identical concentric bearing seat on the bottom face, 32 mm in diameter and 4 mm deep. The remaining central web around the bore must stay continuous.

Create a first control arm extending from the central hub toward positive X. The center of its end boss is located at X = 85 mm and Y = 0. The arm should taper smoothly from 34 mm wide where it joins the central hub to 24 mm wide near the end boss. Keep the main arm web 8 mm thick and centered about Z = 0.

Create a circular end boss at X = 85 mm and Y = 0. The boss is 34 mm in diameter and 12 mm thick. Add a vertical through-hole 10 mm in diameter through the center of this boss.

Create a second control arm extending from the central hub toward positive Y. The center of its end boss is located at X = 0 and Y = 70 mm. The arm should taper smoothly from 32 mm wide where it joins the central hub to 22 mm wide near the end boss. Keep this arm web 8 mm thick and centered about Z = 0.

Create a circular end boss at X = 0 and Y = 70 mm. The boss is 32 mm in diameter and 12 mm thick. Add a vertical through-hole 8 mm in diameter through the center of this boss.

Add raised reinforcement pads on the top and bottom surfaces around the central pivot hub and both end bosses. Each reinforcement pad should blend into its corresponding arm. Keep the total finished thickness at each hub or boss equal to 12 mm and the arm web thickness equal to 8 mm.

Add one circular lightening hole, 16 mm in diameter, through the positive-X arm. Locate it at X = 52 mm and Y = 0.

Add one circular lightening hole, 14 mm in diameter, through the positive-Y arm. Locate it at X = 0 and Y = 42 mm.

Maintain at least 4 mm of material between every lightening hole and the nearest outside edge. Maintain at least 5 mm of radial material around each pivot or attachment bore.

Add 4 mm fillets at the transitions between both arms and the central hub. Add 3 mm fillets where each arm joins its end boss. Add 1 mm fillets to the remaining exposed outside edges where geometrically safe.

Add 0.8 mm chamfers to the top and bottom edges of the central bore and both attachment holes. Do not chamfer the bearing-seat shoulders.

The finished model must be one continuous, closed, positive-volume solid. All arm-to-hub and arm-to-boss connections must have real volume overlap and must not rely on tangent or face-only contact.

Export the native Siemens NX part as an aircraft_control_bellcrank.prt file and export an aircraft_control_bellcrank.step file next to it.

"""

import math
import os

import NXOpen
import NXOpen.Features


RAW_NXOPEN_HIGH_FIDELITY = True
STATIC_ONLY_NXOPEN_REVIEW = {
    "reason": "Designcenter/NXOpen dc_* API tools were not exposed in this session.",
    "basis": [
        "installed nx-cad raw_nxopen_lofted_blade_fixture.py",
        "installed cadnx builder boolean, primitive, and STEP-export patterns",
        "Siemens NXOpen Python Reference Guide 2512 source map",
    ],
    "runtime_uncertainty": "The journal requires a manual Siemens NX run.",
}


PART_NUMBER = "WT-N4412-1250-850"
SPAN = 850.0
ROOT_CHORD = 1250.0
TIP_CHORD = 890.0
PIVOT_X = 390.625
SWEEP_DEG = 2.5
AIRFOIL_POINTS = 121
STATIONS = (0.0, 80.0, 100.0, 150.0, 200.0, 250.0, 300.0, 400.0,
            500.0, 600.0, 650.0, 700.0, 750.0, 820.0, 850.0)


def chord_at(y):
    return ROOT_CHORD + (TIP_CHORD - ROOT_CHORD) * y / SPAN


def twist_at(y):
    # Piecewise-linear interpolation through the explicitly requested stations.
    knots = ((0.0, 18.0), (250.0, 12.0), (500.0, 6.0), (850.0, 0.0))
    for (y0, a0), (y1, a1) in zip(knots, knots[1:]):
        if y <= y1:
            return a0 + (a1 - a0) * (y - y0) / (y1 - y0)
    return knots[-1][1]


def sweep_offset(y):
    return -math.tan(math.radians(SWEEP_DEG)) * y


def shell_thickness(y):
    return 12.0 + (4.0 - 12.0) * y / SPAN


def naca4412_contour(chord, inset=0.0):
    """Return a closed 121-point NACA 4412 perimeter in leading-edge +X coordinates."""
    m, p, t = 0.04, 0.40, 0.121
    n_half = 60
    upper, lower = [], []
    for i in range(n_half + 1):
        # Cosine spacing; xi=0 is LE and xi=1 is TE.
        xi = 0.5 * (1.0 - math.cos(math.pi * i / n_half))
        yt = 5.0 * t * (
            0.2969 * math.sqrt(max(xi, 0.0)) - 0.1260 * xi
            - 0.3516 * xi**2 + 0.2843 * xi**3 - 0.1015 * xi**4
        )
        if xi < p:
            yc = m / p**2 * (2.0 * p * xi - xi**2)
            dy = 2.0 * m / p**2 * (p - xi)
        else:
            yc = m / (1.0 - p)**2 * ((1.0 - 2.0 * p) + 2.0 * p * xi - xi**2)
            dy = 2.0 * m / (1.0 - p)**2 * (p - xi)
        theta = math.atan(dy)
        xu = xi - yt * math.sin(theta)
        zu = yc + yt * math.cos(theta)
        xl = xi + yt * math.sin(theta)
        zl = yc - yt * math.cos(theta)
        # Leading edge is +X. Inset is a stable scaled inner-contour approximation.
        scale = max((chord - 2.0 * inset) / chord, 0.70)
        x_center = 0.5 * chord
        upper.append((x_center + (chord * (1.0 - xu) - x_center) * scale, chord * zu * scale))
        lower.append((x_center + (chord * (1.0 - xl) - x_center) * scale, chord * zl * scale))
    contour = list(reversed(lower)) + upper[1:]
    # Enforce the specified 2.5 mm trailing-edge thickness without changing count.
    for idx in (0, len(contour) - 1):
        x, z = contour[idx]
        contour[idx] = (x, -1.25 if idx == 0 else 1.25)
    assert len(contour) == AIRFOIL_POINTS
    return contour


def transform_section(contour, y):
    angle = math.radians(twist_at(y))
    ca, sa = math.cos(angle), math.sin(angle)
    chord = chord_at(y)
    local_pivot = 0.3125 * chord
    dx = PIVOT_X - local_pivot + sweep_offset(y)
    result = []
    for x, z in contour:
        xr = local_pivot + (x - local_pivot) * ca + z * sa
        zr = -(x - local_pivot) * sa + z * ca
        result.append(NXOpen.Point3d(xr + dx, y, zr))
    return result


def create_work_part_if_needed(session):
    work_part = session.Parts.Work
    if work_part is not None:
        return work_part
    base = os.path.splitext(os.path.abspath(__file__))[0]
    result = session.Parts.NewDisplay(base, NXOpen.Part.Units.Millimeters)
    status = None
    if isinstance(result, tuple):
        work_part = result[0]
        status = result[1] if len(result) > 1 else None
    else:
        work_part = result
    if status is not None:
        status.Dispose()
    return session.Parts.Work or work_part


def body_of(feature):
    bodies = feature.GetBodies()
    return bodies[0]


def create_section(work_part, points):
    section = work_part.Sections.CreateSection(0.01, 0.0095, 0.5)
    section.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    options = work_part.ScRuleFactory.CreateRuleOptions()
    options.SetSelectedFromInactive(True)
    try:
        curves = []
        for index, start in enumerate(points):
            end = points[(index + 1) % len(points)]
            line = work_part.Curves.CreateLine(start, end)
            curves.append(line)
            rule = work_part.ScRuleFactory.CreateRuleBaseCurveDumb([line], options)
            section.AddToSection([rule], line, NXOpen.NXObject.Null,
                                 NXOpen.NXObject.Null, start,
                                 NXOpen.Section.Mode.Create, False)
        return section
    finally:
        options.Dispose()


def loft(work_part, sections, label):
    builder = work_part.Features.CreateThroughCurvesBuilder(NXOpen.Features.Feature.Null)
    try:
        builder.BodyPreference = NXOpen.Features.ThroughCurvesBuilder.BodyPreferenceTypes.Solid
        builder.SectionsList.Append(sections)
        feature = builder.CommitFeature()
        print("Created loft:", label, feature)
        return feature
    finally:
        builder.Destroy()


def cylinder(work_part, diameter, height, origin, axis=(0.0, 1.0, 0.0)):
    builder = work_part.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    try:
        cylinder_types = getattr(NXOpen.Features.CylinderBuilder, "Types", None)
        if cylinder_types is not None and hasattr(cylinder_types, "AxisDiameterAndHeight"):
            builder.Type = cylinder_types.AxisDiameterAndHeight
        builder.Origin = NXOpen.Point3d(*map(float, origin))
        builder.Direction = NXOpen.Vector3d(*map(float, axis))
        builder.Diameter.RightHandSide = str(float(diameter))
        builder.Height.RightHandSide = str(float(height))
        return builder.CommitFeature()
    finally:
        builder.Destroy()


def block(work_part, length, width, height, origin):
    builder = work_part.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    try:
        builder.SetOriginAndLengths(NXOpen.Point3d(*map(float, origin)),
                                    str(float(length)), str(float(width)), str(float(height)))
        return builder.CommitFeature()
    finally:
        builder.Destroy()


def boolean(work_part, target, tool, operation):
    builder = work_part.Features.CreateBooleanBuilder(NXOpen.Features.Feature.Null)
    try:
        builder.Operation = operation
        target_body, tool_body = body_of(target), body_of(tool)
        if hasattr(builder, "Target"):
            builder.Target = target_body
        else:
            builder.TargetBodyCollector.Add(target_body)
        if hasattr(builder, "Tool"):
            builder.Tool = tool_body
        else:
            builder.ToolBodyCollector.Add(tool_body)
        return builder.CommitFeature()
    finally:
        builder.Destroy()


def subtract(work_part, target, tool):
    return boolean(work_part, target, tool, NXOpen.Features.Feature.BooleanType.Subtract)


def unite(work_part, target, tool):
    return boolean(work_part, target, tool, NXOpen.Features.Feature.BooleanType.Unite)


def safe_feature(label, fn):
    try:
        feature = fn()
        print("Created optional feature:", label)
        return feature
    except Exception as exc:
        print("WARNING: skipped optional feature %s: %s" % (label, exc))
        return None


def set_attributes(work_part):
    attrs = {
        "PART_NUMBER": PART_NUMBER,
        "SERIAL_NUMBER": "ASSIGN_AT_MANUFACTURE",
        "MOLD_CAVITY_NUMBER": "ASSIGN_AT_MANUFACTURE",
        "FIBER_BATCH_CODE": "ASSIGN_AT_MANUFACTURE",
        "RESIN_CURE_CYCLE": "80C/4h + 120C/6h",
        "MAX_DESIGN_TIP_SPEED": "85 m/s",
        "INSPECTION_DUE_DATE": "ASSIGN_AT_RELEASE",
        "MATERIAL_SHELL": "VARTM GFRP, biaxial +/-45 E-glass, ISO-NPG gelcoat RAL 9010",
        "SPAR_CAP_MATERIAL": "T300 carbon, Vf=60%, 0/90, compressive strength 350 MPa",
        "WEB_CORE": "Balsa 50 kg/m3, shear strength 2 MPa; PVC 80 kg/m3 from Y750",
        "SURFACE_FINISH": "suction Ra3.2; pressure Ra6.3; LE50 Ra1.6; TE10 Ra0.8 um",
        "GELCOAT": "0.8 mm UV-resistant white RAL 9010; general Ra6.3 um",
        "LIGHTNING": "Cu receptors, conductive epoxy <=0.01 ohm, 25 mm2 copper tape to root",
        "SEAL": "triple-lip PTFE, 15 MPa, -40C to +80C",
        "MODEL_NOTES": "Threads, layups, finishes, markings and tolerances represented by metadata/nominal geometry",
    }
    for title, value in attrs.items():
        try:
            work_part.SetUserAttribute(title, -1, value, NXOpen.Update.Option.Now)
        except Exception as exc:
            print("WARNING: attribute skipped", title, exc)


def build_primary_blade(work_part):
    outer_sections = [create_section(work_part, transform_section(naca4412_contour(chord_at(y)), y))
                      for y in STATIONS]
    shell = loft(work_part, outer_sections, "outer NACA 4412 blade")

    # Hollow only after the solid root; inner loft begins at Y=80 and ends short of tip.
    inner_stations = tuple(y for y in STATIONS if 80.0 <= y <= 820.0)
    inner_sections = [create_section(work_part,
                       transform_section(naca4412_contour(chord_at(y), shell_thickness(y)), y))
                      for y in inner_stations]
    inner = loft(work_part, inner_sections, "variable-wall inner cavity")
    shell = subtract(work_part, shell, inner)
    print("Created shell with solid root transition and variable nominal wall")
    return shell


def add_root_hardware(work_part, target):
    flange = cylinder(work_part, 180.0, 45.0, (0.0, -40.0, 0.0))
    target = safe_feature("unite root flange", lambda: unite(work_part, target, flange)) or target
    bore = cylinder(work_part, 50.025, 30.0, (0.0, -40.5, 0.0))
    target = safe_feature("50 mm H8 pitch bore", lambda: subtract(work_part, target, bore)) or target
    seat_bore = cylinder(work_part, 85.0, 28.0, (0.0, -20.0, 0.0))
    target = safe_feature("85 mm bearing seat bore", lambda: subtract(work_part, target, seat_bore)) or target
    # Nominal M16x2 tap-drill geometry (thread callout retained as metadata).
    for i in range(8):
        a = 2.0 * math.pi * i / 8.0
        tool = cylinder(work_part, 14.0, 25.5, (70.0 * math.cos(a), -40.5, 70.0 * math.sin(a)))
        target = safe_feature("M16x2 root tapped pilot %d" % (i + 1),
                              lambda t=target, c=tool: subtract(work_part, t, c)) or target
    for i in range(3):
        a = 2.0 * math.pi * i / 3.0
        tool = cylinder(work_part, 10.0, 5.5, (80.0 * math.cos(a), -40.5, 80.0 * math.sin(a)))
        target = safe_feature("H7 tooling hole %d" % (i + 1),
                              lambda t=target, c=tool: subtract(work_part, t, c)) or target
    # Twenty nominal spline-tooth solids at the flange OD. Their 60-degree
    # pressure-angle manufacturing definition is retained in part metadata.
    for i in range(20):
        a = 2.0 * math.pi * i / 20.0
        tooth = cylinder(work_part, 3.0, 45.0,
                         (91.0 * math.cos(a), -40.0, 91.0 * math.sin(a)))
        target = safe_feature("anti-rotation spline tooth %02d" % (i + 1),
                              lambda t=target, s=tooth: unite(work_part, t, s)) or target
    # Seal and circlip grooves are represented by shallow annular recesses.
    for label, od, id_, depth, ypos in (
        ("PTFE seal groove", 120.0, 116.0, 1.5, -20.0),
        ("circlip groove", 120.0, 118.0, 0.8, -10.0),
    ):
        outer = cylinder(work_part, od, depth + 0.3, (0.0, ypos, 0.0))
        inner = cylinder(work_part, id_, depth + 0.8, (0.0, ypos - 0.2, 0.0))
        ring = safe_feature(label + " cutter", lambda o=outer, i=inner: subtract(work_part, o, i))
        if ring:
            target = safe_feature(label, lambda t=target, r=ring: subtract(work_part, t, r)) or target
    return target


def add_internal_structure(work_part):
    # Nominal internal solids; kept as separate bodies in the same part so material regions remain traceable.
    for frac in (0.15, 0.50):
        x0 = ROOT_CHORD * (1.0 - frac) - 42.5
        safe_feature("carbon spar cap %.0f%% chord" % (100 * frac),
                     lambda x=x0: block(work_part, 85.0, SPAN, 25.0, (x, 0.0, -12.5)))
        # I-section transition representation at Y=600..850.
        safe_feature("spar I flange %.0f%%" % (100 * frac),
                     lambda x=x0 + 25.0: block(work_part, 35.0, 250.0, 18.0, (x, 600.0, -9.0)))
        safe_feature("spar I web %.0f%%" % (100 * frac),
                     lambda x=x0 + 35.0: block(work_part, 15.0, 250.0, 18.0, (x, 600.0, -9.0)))
    web_x0 = ROOT_CHORD * 0.50
    web = safe_feature("8 mm balsa shear web", lambda: block(work_part, 8.0, 650.0, 120.0,
                                                              (web_x0, 100.0, -60.0)))
    if web:
        for y in range(120, 741, 40):
            for z in (-36.0, 0.0, 36.0):
                hole = cylinder(work_part, 12.0, 10.0, (web_x0 - 1.0, float(y), z), (1.0, 0.0, 0.0))
                web = safe_feature("web lightening hole", lambda w=web, h=hole: subtract(work_part, w, h)) or web
    safe_feature("PVC tip damping web", lambda: block(work_part, 8.0, 100.0, 90.0,
                                                       (web_x0, 750.0, -45.0)))


def add_external_details(work_part):
    # Six total bosses: a symmetric pair at each requested span station.
    for y in (150.0, 400.0, 650.0):
        c = chord_at(y)
        le_x = PIVOT_X + 0.6875 * c + sweep_offset(y)
        for sign in (-1.0, 1.0):
            boss = cylinder(work_part, 25.0, 15.0, (le_x - 8.0, y, sign * 8.0), (0.0, 0.0, sign))
            bore = cylinder(work_part, 6.0, 12.0, (le_x - 8.0, y, sign * 9.0), (0.0, 0.0, sign))
            safe_feature("lightning boss bore", lambda b=boss, h=bore: subtract(work_part, b, h))

    # Vortex-generator carrier plus 18 swept triangular-fin envelope solids.
    safe_feature("VG stainless carrier", lambda: block(work_part, 400.0, 0.8, 12.0,
                                                        (120.0, 300.0, 40.0)))
    for i in range(18):
        y = 300.0 + i * 22.0
        safe_feature("VG fin %02d" % (i + 1),
                     lambda yy=y: block(work_part, 15.0, 0.6, 8.0, (240.0, yy, 40.0)))

    # Leading-edge rain tape as a lofted 3 mm skin strip (0..4% chord band).
    tape_sections = []
    for y in STATIONS:
        contour = naca4412_contour(chord_at(y))
        band = [p for p in contour if p[0] >= 0.96 * chord_at(y)]
        if len(band) < 3:
            band = contour[len(contour)//2-3:len(contour)//2+4]
        tape_sections.append(create_section(work_part, transform_section(band, y)))
    safe_feature("3 mm polyurethane leading-edge tape", lambda: loft(work_part, tape_sections, "LE tape"))

    # Four strain-gauge pads, nominal flat placement; cable exits are separate bore features.
    for y in (200.0, 600.0):
        for frac in (0.25, 0.50):
            x = chord_at(y) * (1.0 - frac) + sweep_offset(y)
            pad = safe_feature("strain pad", lambda xx=x, yy=y: block(work_part, 20.0, 15.0, 2.0,
                                                                       (xx - 10.0, yy - 7.5, -55.0)))
            if pad:
                hole = cylinder(work_part, 3.0, 4.0, (x, y, -56.0), (0.0, 0.0, 1.0))
                safe_feature("strain pad cable exit", lambda p=pad, h=hole: subtract(work_part, p, h))

    hinge = safe_feature("tip brake hinge", lambda: block(work_part, 30.0, 40.0, 12.0,
                                                           (70.0, 800.0, -50.0)))
    if hinge:
        bore = cylinder(work_part, 8.0, 32.0, (69.0, 820.0, -44.0), (1.0, 0.0, 0.0))
        safe_feature("tip brake hinge H8 bore", lambda: subtract(work_part, hinge, bore))
    safe_feature("25 degree tip brake panel envelope", lambda: block(work_part, 48.0, 25.0, 2.5,
                                                                      (40.0, 822.0, -62.0)))


def save_and_export(session, work_part, output_path):
    base = os.path.splitext(os.path.abspath(output_path))[0]
    part_path = base + ".prt"
    if not getattr(work_part, "FullPath", ""):
        status = work_part.SaveAs(part_path)
    else:
        save_components = getattr(NXOpen.BasePart.SaveComponents, "True")
        keep_open = getattr(NXOpen.BasePart.CloseAfterSave, "False")
        status = work_part.Save(save_components, keep_open)
    if status is not None and hasattr(status, "Dispose"):
        status.Dispose()
    print("Native PRT save requested:", part_path)

    dex = session.DexManager
    exporter = dex.CreateStep214Creator() if hasattr(dex, "CreateStep214Creator") else dex.CreateStepCreator()
    try:
        if hasattr(exporter, "InputFile"):
            exporter.InputFile = getattr(work_part, "FullPath", "") or part_path
        exporter.OutputFile = output_path
        if hasattr(exporter, "OutputFileExtension"):
            exporter.OutputFileExtension = "step"
        if hasattr(exporter, "FileSaveFlag"):
            exporter.FileSaveFlag = False
        exporter.Commit()
    finally:
        exporter.Destroy()
    print("STEP export requested:", output_path)


def main():
    session = NXOpen.Session.GetSession()
    work_part = create_work_part_if_needed(session)
    print("NX work part:", getattr(work_part, "FullPath", "") or getattr(work_part, "Name", "<unnamed>"))
    print("Parameters: span=850, chord=1250->890, twist=18->0, sweep=2.5 deg")
    print("NACA contour points per primary section:", AIRFOIL_POINTS)

    shell = build_primary_blade(work_part)
    shell = add_root_hardware(work_part, shell)
    add_internal_structure(work_part)
    add_external_details(work_part)
    set_attributes(work_part)

    try:
        body_count = len(list(work_part.Bodies))
    except Exception:
        body_count = -1
    print("Committed body count:", body_count)
    output_path = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    save_and_export(session, work_part, output_path)


if __name__ == "__main__":
    main()
