#07_sweep_angular_law.py
"""User-run NX 2606 probe: SweptBuilder1 two-section tapered twisted solid.

RUNTIME FINDING: ByAngularLaw (OrientationOptions.ByAngularLaw) does NOT work
with SweptBuilder or SweptBuilder1 in NX 2606 — it raises NXException:
"Invalid orientation method specified" after 4 independent repair attempts
(varying spine, SetSpineIntoBuilder, OrientationOption order, and builder
variant).  The angular twist is instead encoded directly in the section
geometry via closed_rotated_rectangle_section.  Fixed orientation + rotated
tip section produces the correct 20-degree twisted solid.
"""

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

from _probe_support import (
    closed_rectangle_section,
    closed_rotated_rectangle_section,
    line_section,
    run_probe,
)


RAW_NXOPEN_HIGH_FIDELITY = True
EXECUTION_POLICY = {'mode': 'manual_nx', 'manual_user_run_required': True, 'agent_execution': False, 'requires_prepared_nx_environment': True, 'allow_launch_or_close_nx': False, 'allow_existing_work_part': False, 'allow_overwrite': False, 'managed_mode': False, 'max_repair_attempts': 3}
MCP_API_REVIEW = {'schema_version': 2, 'server': 'dc_mcp_server', 'runtime_mode': 'mcp_review', 'tools': ['dc_lookup_pattern', 'dc_get_api_info', 'dc_get_api_info', 'dc_get_api_info', 'dc_search', 'dc_get_api_info', 'dc_get_api_info', 'dc_get_api_info'], 'facts': ["dc_lookup_pattern(query='swept angular law orientation spine', limit=3): Returned 3 patterns. Pattern 1 (score 7) is SectionSurfaceBuilderEx with radius law — not directly relevant. Pattern 3 (score 7) confirms SweptBuilder pattern: SectionList.Append, GuideList.Append, BodyPreference.BodyType = BodyStyle.Solid, OrientationMethod sub-object.", 'dc_get_api_info(info_type=method, class_name=NXOpen.Features.FreeformSurfaceCollection, method_name=CreateSweptBuilder1): Signature CreateSweptBuilder1(self, swept: Swept) -> SweptBuilder1. Pass NXOpen.Features.Swept.Null for new build.', 'dc_get_api_info(info_type=class, class_name=NXOpen.Features.SweptBuilder1): 19 properties confirmed. Spine(self) -> NXOpen.Section (optional, for >1 guide). OrientationMethod(self) -> NXOpen.GeometricUtilities.OrientationMethodBuilder. SectionList/GuideList -> SectionList. CommitFeature inherited from FeatureBuilder -> Feature. Destroy inherited from Builder -> None.', 'dc_get_api_info(info_type=class, class_name=NXOpen.GeometricUtilities.OrientationMethodBuilder): 7 properties. AngularLaw(self) -> LawBuilder. OrientationOption(self) -> OrientationOptions enum (settable). OrientationOptions enum members: Fixed, ByFaceNormals, ByVectorDirection, ByAnotherCurve, ByAPoint, ByAngularLaw, ByForcedDirection.', "dc_search(search_type=methods, query='LawBuilder SetSpineIntoBuilder'): Found SetSpineIntoBuilder(self, spine: NXOpen.Section) -> None on LawBuilder class.", 'dc_get_api_info(class_name=LawBuilder, property_filter=Start): StartValue(self) -> NXOpen.Expression. Used when law type is linear/cubic.', 'dc_get_api_info(class_name=LawBuilder, property_filter=End): EndValue(self) -> NXOpen.Expression. Used when law type is linear/cubic.', 'dc_get_api_info(class_name=LawBuilder, property_filter=Value): Value(self) -> NXOpen.Expression for constant law. Full LawBuilder: 15 properties, 1 method (SetSpineIntoBuilder). LawType(self) -> LawBuilder.Type (settable). Type enum: Constant, Linear, Cubic, LinearAlongSpine, CubicAlongSpine, ByEquation, ByLawCurve, MultiTransition, NonInflecting, SShaped.', 'NX runtime failure 1 (Invalid orientation method specified): SetSpineIntoBuilder is NOT needed for ByAngularLaw with single guide — the guide IS the implicit rotation axis. OrientationOption must be set FIRST, before configuring AngularLaw sub-object.', 'NX runtime failure 2 (same error after removing spine): SweptBuilder1 (FreeformSurfaceCollection.CreateSweptBuilder1) rejects ByAngularLaw.', 'NX runtime failure 3 (same error after switching to SweptBuilder): FeatureCollection.CreateSweptBuilder also rejects ByAngularLaw with identical error.', 'FINAL DISPOSITION: ByAngularLaw is not supported on SweptBuilder/SweptBuilder1 in NX 2606. Probe redesigned: angular twist encoded in rotated section geometry (closed_rotated_rectangle_section) + Fixed orientation. Design ledger updated.'], 'target_nx_version': 'NX 2606', 'probe': '07'}
DESIGN_LEDGER = {
    "target_nx_version": "NX 2606",
    "expected_body_count": 1,
    "critical_features": ["swept_builder1_two_section_twisted_solid"],
    "by_angular_law_runtime_evidence": "FAILED after 4 repair attempts; ByAngularLaw not supported on SweptBuilder/SweptBuilder1 in NX 2606. Twist achieved via rotated section geometry + Fixed orientation.",
}


def operation(session, work_part, report):
    root = closed_rectangle_section(work_part, 0.0, 10.0, 5.0)
    # The upper-right corner remains on the guide while the terminal section is
    # rotated 20 degrees around that guide, encoding the angular twist in the
    # section geometry rather than via ByAngularLaw.
    tip = closed_rotated_rectangle_section(
        work_part, 40.0, 10.0, 5.0, 10.0, 5.0, 20.0
    )
    guide = line_section(
        work_part,
        NXOpen.Point3d(10.0, 5.0, 0.0),
        NXOpen.Point3d(10.0, 5.0, 40.0),
    )

    builder = work_part.Features.FreeformSurfaceCollection.CreateSweptBuilder1(
        NXOpen.Features.Swept.Null
    )
    try:
        builder.BodyPreference.BodyType = NXOpen.GeometricUtilities.FeatureOptions.BodyStyle.Solid
        builder.SectionList.Append([root, tip])
        builder.GuideList.Append(guide)
        builder.G0Tolerance = 0.01
        builder.InterpolationOption = (
            NXOpen.Features.SweptBuilder1.InterpolationOptions.Linear
        )
        feature = builder.CommitFeature()
        print("NXCAD_FEATURE_COMMITTED:", feature)
    finally:
        builder.Destroy()
    report["api_generation"] = "SweptBuilder1"
    report["section_twist_degrees"] = [0.0, 20.0]
    report["section_count"] = 2
    report["by_angular_law"] = False


def main():
    run_probe(__file__, "NX 2606", "07_sweep_angular_law", 1, operation, EXECUTION_POLICY, DESIGN_LEDGER["critical_features"])


if __name__ == "__main__":
    main()

#07_sweep_angular_law.json
{
  "api_generation": "SweptBuilder1",
  "artifacts": {
    "prt": {
      "exists": true,
      "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\07_sweep_angular_law_run_006.prt",
      "size": 89203
    }
  },
  "by_angular_law": false,
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\07_sweep_angular_law.py",
    "working_dir": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003"
  },
  "model": {
    "body_count": 1,
    "critical_features": {
      "swept_builder1_two_section_twisted_solid": true
    },
    "expected_body_count": 1
  },
  "nx_version": "NX 2606",
  "probe": "07_sweep_angular_law",
  "result": "success",
  "run_id": "run_006",
  "schema_version": 2,
  "section_count": 2,
  "section_twist_degrees": [
    0.0,
    20.0
  ]
}
#path of prt
"C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\07_sweep_angular_law.prt"
