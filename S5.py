#py文件
"""User-run NX 2606 probe: SweptBuilder1 two-section tapered solid."""

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

from _probe_support import closed_rectangle_section, line_section, run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
EXECUTION_POLICY = {'mode': 'mcp_execute', 'user_authorized': True, 'requires_prepared_nx_environment': True, 'allow_launch_or_close_nx': False, 'allow_existing_work_part': False, 'allow_overwrite': False, 'managed_mode': False, 'max_repair_attempts': 3}
MCP_API_REVIEW = {'server': 'dc_mcp_server', 'tools': ['dc_lookup_pattern', 'dc_get_api_info', 'dc_run_snippet'], 'facts': ['NXOpen.Features.FreeformSurfaceCollection.CreateSweptBuilder1 creates a SweptBuilder1 for freeform surface/solid operations', 'SweptBuilder1.BodyPreference.BodyType accepts NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Solid for solid output', 'SweptBuilder1.SectionList.Append accepts an ordered list of Section objects for multiple sections', 'SweptBuilder1.GuideList.Append accepts one or more guide Section objects', 'SweptBuilder1.OrientationMethod.OrientationOption accepts Fixed for fixed orientation along guide', 'closed_rectangle_section creates a rectangular Section at a given Z with width/height', 'line_section creates a linear Section between two Point3d coordinates', 'Section-to-guide correspondence is established by matching the order of points in sections and guides', 'CommitFeature on SweptBuilder1 returns the committed feature; Destroy must be called in finally block', 'known verified recipe nx2606.sweep.two-sections with status=verified in api-recipes registry']}
DESIGN_LEDGER = {
    "target_nx_version": "NX 2606",
    "expected_body_count": 1,
    "critical_features": ["swept_builder1_two_section_tapered_solid"],
}


def operation(session, work_part, report):
    root = closed_rectangle_section(work_part, 0.0, 10.0, 5.0)
    tip = closed_rectangle_section(work_part, 40.0, 6.0, 3.0)
    # A single diagonal guide intersects corresponding upper-right corners of
    # both sections, making section-to-guide correspondence explicit.
    guide = line_section(
        work_part,
        NXOpen.Point3d(10.0, 5.0, 0.0),
        NXOpen.Point3d(6.0, 3.0, 40.0),
    )

    builder = work_part.Features.FreeformSurfaceCollection.CreateSweptBuilder1(
        NXOpen.Features.Swept.Null
    )
    try:
        builder.BodyPreference.BodyType = NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Solid
        builder.SectionList.Append([root, tip])
        builder.GuideList.Append(guide)
        builder.OrientationMethod.OrientationOption = (
            NXOpen.GeometricUtilities.OrientationMethodBuilder.OrientationOptions.Fixed
        )
        feature = builder.CommitFeature()
        print("NXCAD_FEATURE_COMMITTED:", feature)
    finally:
        builder.Destroy()
    report["api_generation"] = "SweptBuilder1"
    report["section_count"] = 2


def main():
    run_probe(__file__, "NX 2606", "06_sweep_two_sections", 1, operation, EXECUTION_POLICY, DESIGN_LEDGER["critical_features"])


if __name__ == "__main__":
    main()
#json文件
{
  "api_generation": "SweptBuilder1",
  "artifacts": {
    "prt": {
      "exists": true,
      "path": "C:\\Users\\z004n36r\\.agents\\nx_runtime_probes\\nx2606\\06_sweep_two_sections_run_001.prt",
      "size": 77226
    }
  },
  "execution": {
    "actor": "agent",
    "tool": "dc_run_journal",
    "transport": "dc_mcp",
    "user_authorized": true
  },
  "journal": {
    "path": "C:\\Users\\z004n36r\\.agents\\nx_runtime_probes\\nx2606\\06_sweep_two_sections.py",
    "working_dir": "C:\\Users\\z004n36r\\.agents\\nx_runtime_probes\\nx2606"
  },
  "model": {
    "body_count": 1,
    "critical_features": {
      "swept_builder1_two_section_tapered_solid": true
    },
    "expected_body_count": 1
  },
  "nx_version": "NX 2606",
  "probe": "06_sweep_two_sections",
  "result": "success",
  "run_id": "run_001",
  "schema_version": 2,
  "section_count": 2
}
#prt路径
"C:\Users\z004n36r\.agents\nx_runtime_probes\nx2606\06_sweep_two_sections_run_001.prt"
