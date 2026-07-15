"""Shared support for user-run nx-cad runtime probes.

This module does not start Siemens NX. Probe files import it only after the
user manually executes them inside NX.
"""

import json
import math
import os
import time

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities


def safe_dispose(value):
    if value is not None and hasattr(value, "Dispose"):
        value.Dispose()


def create_work_part_if_needed(session, stem):
    if session.Parts.Work is not None:
        return session.Parts.Work
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), stem)
    path = base_path
    suffix = 1
    while os.path.exists(path) or os.path.exists(path + ".prt"):
        path = "%s_run_%03d" % (base_path, suffix)
        suffix += 1
    result = session.Parts.NewDisplay(path, NXOpen.Part.Units.Millimeters)
    status = None
    if isinstance(result, tuple):
        part = result[0]
        status = result[1] if len(result) > 1 else None
    else:
        part = result
    safe_dispose(status)
    work_part = session.Parts.Work or part
    print("NXCAD_WORK_PART_PATH:", path)
    return work_part


def report_path(probe_file):
    return os.path.splitext(os.path.abspath(probe_file))[0] + ".nxreport.json"


def run_probe(probe_file, nx_version, probe_name, expected_body_count, operation):
    report = {
        "schema_version": 1,
        "nx_version": nx_version,
        "manual_user_run": True,
        "agent_execution": False,
        "probe": probe_name,
        "result": "running",
        "body_count": None,
    }
    try:
        session = NXOpen.Session.GetSession()
        work_part = create_work_part_if_needed(session, probe_name)
        operation(session, work_part, report)
        body_count = len(list(work_part.Bodies))
        report["body_count"] = body_count
        if body_count != expected_body_count:
            raise RuntimeError(
                "Expected %d final body/bodies, found %d" % (expected_body_count, body_count)
            )
        report["result"] = "success"
        print("NXCAD_PROBE_RESULT: success")
    except Exception as exc:
        report["result"] = "failure"
        report["error"] = str(exc)
        print("NXCAD_PROBE_RESULT: failure")
        raise
    finally:
        path = report_path(probe_file)
        with open(path, "w", encoding="utf-8") as stream:
            json.dump(report, stream, indent=2, sort_keys=True)
        print("NXCAD_RUNTIME_REPORT:", path)


def cylinder(work_part, diameter, height, origin=(0.0, 0.0, 0.0)):
    builder = work_part.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    try:
        builder.Type = NXOpen.Features.CylinderBuilder.Types.AxisDiameterAndHeight
        builder.Origin = NXOpen.Point3d(*origin)
        builder.Direction = NXOpen.Vector3d(0.0, 0.0, 1.0)
        builder.Diameter.RightHandSide = str(float(diameter))
        builder.Height.RightHandSide = str(float(height))
        builder.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
        return builder.CommitFeature()
    finally:
        builder.Destroy()


def body_of(feature):
    bodies = feature.GetBodies()
    if not bodies:
        raise RuntimeError("Committed feature returned no body")
    return bodies[0]


def unite(work_part, target_feature, tool_feature):
    builder = work_part.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    try:
        builder.Operation = NXOpen.Features.Feature.BooleanType.Unite
        target = body_of(target_feature)
        tool = body_of(tool_feature)
        if hasattr(builder, "Target"):
            builder.Target = target
        else:
            builder.TargetBodyCollector.Add(target)
        if hasattr(builder, "Tool"):
            builder.Tool = tool
        else:
            builder.ToolBodyCollector.Add(tool)
        return builder.CommitFeature()
    finally:
        builder.Destroy()


def add_curves_to_section(work_part, section, curves, help_points):
    section.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    options = work_part.ScRuleFactory.CreateRuleOptions()
    try:
        for curve, help_point in zip(curves, help_points):
            rule = work_part.ScRuleFactory.CreateRuleBaseCurveDumb([curve], options)
            section.AddToSection(
                [rule],
                curve,
                NXOpen.NXObject.Null,
                NXOpen.NXObject.Null,
                help_point,
                NXOpen.Section.Mode.Create,
                False,
            )
    finally:
        options.Dispose()
    return section


def _section_from_curves(work_part, curves, help_points):
    section = work_part.Sections.CreateSection(0.01, 0.0095, 0.5)
    return add_curves_to_section(work_part, section, curves, help_points)


def closed_polygon_section(work_part, points):
    curves = [
        work_part.Curves.CreateLine(point, points[(index + 1) % len(points)])
        for index, point in enumerate(points)
    ]
    return _section_from_curves(work_part, curves, points)


def closed_rectangle_section(work_part, z_value, half_width, half_height):
    return closed_polygon_section(
        work_part,
        [
            NXOpen.Point3d(-half_width, -half_height, z_value),
            NXOpen.Point3d(half_width, -half_height, z_value),
            NXOpen.Point3d(half_width, half_height, z_value),
            NXOpen.Point3d(-half_width, half_height, z_value),
        ],
    )


def closed_rotated_rectangle_section(
    work_part, z_value, half_width, half_height, pivot_x, pivot_y, angle_degrees
):
    angle = math.radians(angle_degrees)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    points = []
    for x_value, y_value in (
        (-half_width, -half_height),
        (half_width, -half_height),
        (half_width, half_height),
        (-half_width, half_height),
    ):
        delta_x = x_value - pivot_x
        delta_y = y_value - pivot_y
        points.append(
            NXOpen.Point3d(
                pivot_x + delta_x * cosine - delta_y * sine,
                pivot_y + delta_x * sine + delta_y * cosine,
                z_value,
            )
        )
    return closed_polygon_section(work_part, points)


def line_section(work_part, start, end):
    curve = work_part.Curves.CreateLine(start, end)
    return _section_from_curves(work_part, [curve], [start])


def add_line_to_section(work_part, section, start, end):
    curve = work_part.Curves.CreateLine(start, end)
    return add_curves_to_section(work_part, section, [curve], [start])


def export_step(session, work_part, output_path):
    status = work_part.Save(
        NXOpen.BasePart.SaveComponents.TrueValue,
        NXOpen.BasePart.CloseAfterSave.FalseValue,
    )
    safe_dispose(status)
    dex_manager = session.DexManager
    creator = None
    try:
        if hasattr(dex_manager, "CreateStepCreator"):
            creator = dex_manager.CreateStepCreator()
            creator.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap242
            creator.ExportFrom = NXOpen.StepCreator.ExportFromOption.DisplayPart
            # StepCreator object filters are not implicitly enabled. NX 2606
            # can otherwise translate the part envelope while emitting only
            # product metadata and no B-rep geometry.
            creator.ObjectTypes.Solids = True
            creator.FileSaveFlag = False
            creator.ProcessHoldFlag = True
            # Keep the 003 InputFile configuration unchanged so the 004 run
            # isolates ObjectTypes.Solids as the only export-setting change.
            creator.InputFile = work_part.FullPath
        elif hasattr(dex_manager, "CreateStep214Creator"):
            creator = dex_manager.CreateStep214Creator()
        else:
            raise RuntimeError("NX DexManager exposes neither CreateStepCreator nor CreateStep214Creator")
        creator.OutputFile = output_path
        creator.Commit()
    finally:
        if creator is not None:
            creator.Destroy()
    deadline = time.time() + 60.0
    while time.time() < deadline:
        if os.path.isfile(output_path) and os.path.getsize(output_path) > 0:
            return output_path
        time.sleep(0.25)
    raise RuntimeError(
        "STEP export did not create a non-empty file within 60 seconds: " + output_path
    )
