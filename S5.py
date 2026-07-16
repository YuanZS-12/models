#json文件
{
  "api_generation": "SweptBuilder1",
  "artifacts": {
    "prt": {
      "exists": true,
      "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\06_sweep_two_sections_run_001.prt",
      "size": 77252
    }
  },
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\06_sweep_two_sections.py",
    "working_dir": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003"
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
#prt文件地址
"C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\06_sweep_two_sections_run_001.prt"

#py文件
"""User-run NX 2606 probe: SweptBuilder1 two-section tapered solid."""

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

from _probe_support import closed_rectangle_section, line_section, run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
EXECUTION_POLICY = {'mode': 'manual_nx', 'manual_user_run_required': True, 'agent_execution': False, 'requires_prepared_nx_environment': True, 'allow_launch_or_close_nx': False, 'allow_existing_work_part': False, 'allow_overwrite': False, 'managed_mode': False, 'max_repair_attempts': 3}
MCP_API_REVIEW = {'schema_version': 2, 'server': 'dc_mcp_server', 'runtime_mode': 'mcp_review', 'tools': ['dc_lookup_pattern', 'dc_get_api_info', 'dc_get_api_info'], 'facts': ["dc_lookup_pattern(query='two section solid sweep with fixed orientation', limit=3): confirmed SweptBuilder API. SectionList.Append, GuideList.Append, BodyPreference.BodyType = BodyStyle.Solid, OrientationMethod.OrientationOption = OrientationOptions.Fixed. Gotcha: property named BodyType but enum type named BodyStyle.", 'dc_get_api_info(info_type=method, class_name=NXOpen.Features.FreeformSurfaceCollection, method_name=CreateSweptBuilder1): Signature CreateSweptBuilder1(self, swept: Swept) -> SweptBuilder1. Pass NXOpen.Features.Swept.Null for new build.', 'dc_get_api_info(info_type=class, class_name=NXOpen.Features.SweptBuilder1): 19 properties. BodyPreference -> FeatureOptions. SectionList/GuideList -> SectionList. OrientationMethod -> OrientationMethodBuilder. CommitFeature inherited from FeatureBuilder. Destroy inherited from Builder. InterpolationOptions enum: Linear, Cubic, Blend. SectionLocationTypes enum: AnywhereAlongGuides, EndsOfGuides.'], 'target_nx_version': 'NX 2606', 'probe': '06'}
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
