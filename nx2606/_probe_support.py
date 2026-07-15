"""Shared support for user-run nx-cad runtime probes.

This module does not start Siemens NX. Probe files import it only after the
user manually executes them inside NX.
"""

import json
import os

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities


def safe_dispose(value):
    if value is not None and hasattr(value, "Dispose"):
        value.Dispose()


def create_work_part_if_needed(session, stem):
    if session.Parts.Work is not None:
        return session.Parts.Work
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), stem)
    result = session.Parts.NewDisplay(path, NXOpen.Part.Units.Millimeters)
    status = None
    if isinstance(result, tuple):
        part = result[0]
        status = result[1] if len(result) > 1 else None
    else:
        part = result
    safe_dispose(status)
    return session.Parts.Work or part


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


def export_step(session, work_part, output_path):
    status = work_part.Save(
        NXOpen.BasePart.SaveComponents.TrueValue,
        NXOpen.BasePart.CloseAfterSave.FalseValue,
    )
    safe_dispose(status)
    dex_manager = session.DexManager
    if hasattr(dex_manager, "CreateStepCreator"):
        creator = dex_manager.CreateStepCreator()
        creator.ExportAs = NXOpen.StepCreator.ExportAsOption.Ap242
        creator.ExportFrom = NXOpen.StepCreator.ExportFromOption.DisplayPart
        creator.FileSaveFlag = False
        creator.ProcessHoldFlag = True
    elif hasattr(dex_manager, "CreateStep214Creator"):
        creator = dex_manager.CreateStep214Creator()
    else:
        raise RuntimeError("NX DexManager exposes neither CreateStepCreator nor CreateStep214Creator")
    try:
        creator.InputFile = work_part.FullPath
        creator.OutputFile = output_path
        creator.Commit()
    finally:
        creator.Destroy()
    if not os.path.isfile(output_path) or os.path.getsize(output_path) <= 0:
        raise RuntimeError("STEP export did not create a non-empty file: " + output_path)
    return output_path
