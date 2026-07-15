"""Manual Siemens NX probe for a two-section ThroughCurves solid.

The agent may generate and statically check this file, but only the user may
run it manually through Siemens NX: File -> Execute -> NX Open.
"""

import json
import os

import NXOpen
import NXOpen.Features


RAW_NXOPEN_HIGH_FIDELITY = True
USER_MANUAL_NX_EXECUTION_REQUIRED = True
STATIC_ONLY_NXOPEN_REVIEW = {
    "recipe": "nx2606.through-curves.solid",
    "reason": "The complete recipe requires a manual user-run NX 2606 probe.",
}
DESIGN_LEDGER = {
    "capability_level": "experimental_raw",
    "target_nx_version": "NX 2606",
    "expected_body_count": 1,
    "critical_features": ["two_section_through_curves_solid"],
    "optional_features": [],
}


def report_path():
    return os.path.splitext(os.path.abspath(__file__))[0] + ".nxreport.json"


def write_report(report):
    with open(report_path(), "w", encoding="utf-8") as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
    print("NXCAD_RUNTIME_REPORT:", report_path())


def safe_dispose(value):
    if value is not None and hasattr(value, "Dispose"):
        value.Dispose()


def create_work_part_if_needed(session):
    if session.Parts.Work is not None:
        return session.Parts.Work
    base = os.path.splitext(os.path.abspath(__file__))[0]
    result = session.Parts.NewDisplay(base, NXOpen.Part.Units.Millimeters)
    status = None
    if isinstance(result, tuple):
        part = result[0]
        status = result[1] if len(result) > 1 else None
    else:
        part = result
    safe_dispose(status)
    return session.Parts.Work or part


def rectangle_points(z_value, half_width, half_height):
    return [
        NXOpen.Point3d(-half_width, -half_height, z_value),
        NXOpen.Point3d(half_width, -half_height, z_value),
        NXOpen.Point3d(half_width, half_height, z_value),
        NXOpen.Point3d(-half_width, half_height, z_value),
    ]


def closed_section(work_part, points):
    section = work_part.Sections.CreateSection(0.01, 0.0095, 0.5)
    section.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    options = work_part.ScRuleFactory.CreateRuleOptions()
    try:
        for index, start in enumerate(points):
            end = points[(index + 1) % len(points)]
            curve = work_part.Curves.CreateLine(start, end)
            rule = work_part.ScRuleFactory.CreateRuleBaseCurveDumb([curve], options)
            section.AddToSection(
                [rule],
                curve,
                NXOpen.NXObject.Null,
                NXOpen.NXObject.Null,
                start,
                NXOpen.Section.Mode.Create,
                False,
            )
    finally:
        options.Dispose()
    return section


def main():
    report = {
        "schema_version": 1,
        "nx_version": "NX 2606",
        "manual_user_run": True,
        "probe": "through_curves_solid",
        "result": "running",
        "agent_execution": False,
    }
    try:
        session = NXOpen.Session.GetSession()
        work_part = create_work_part_if_needed(session)
        root = closed_section(work_part, rectangle_points(0.0, 20.0, 12.0))
        tip = closed_section(work_part, rectangle_points(40.0, 12.0, 8.0))

        builder = work_part.Features.CreateThroughCurvesBuilder(NXOpen.Features.Feature.Null)
        try:
            builder.BodyPreference = NXOpen.Features.ThroughCurvesBuilder.BodyPreferenceTypes.Solid
            builder.SectionsList.Append([root, tip])
            feature = builder.CommitFeature()
            print("NXCAD_FEATURE_COMMITTED:", feature)
        finally:
            builder.Destroy()

        body_count = len(list(work_part.Bodies))
        report["body_count"] = body_count
        if body_count != DESIGN_LEDGER["expected_body_count"]:
            raise RuntimeError("Expected one final body, found %d" % body_count)
        report["result"] = "success"
        print("NXCAD_PROBE_RESULT: success")
    except Exception as exc:
        report["result"] = "failure"
        report["error"] = str(exc)
        print("NXCAD_PROBE_RESULT: failure")
        raise
    finally:
        write_report(report)


if __name__ == "__main__":
    main()
