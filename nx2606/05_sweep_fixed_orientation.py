"""User-run NX 2606 probe: SweptBuilder1 fixed-orientation solid."""

import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities

from _probe_support import closed_rectangle_section, line_section, run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
USER_MANUAL_NX_EXECUTION_REQUIRED = True
STATIC_ONLY_NXOPEN_REVIEW = {
    "recipe": "nx2606.sweep.fixed-orientation",
    "official_pages": ["a47559.html", "a44599.html", "a56995.html", "a56735.html"],
    "runtime": "manual user run required",
}
DESIGN_LEDGER = {
    "target_nx_version": "NX 2606",
    "expected_body_count": 1,
    "critical_features": ["swept_builder1_fixed_orientation_solid"],
}


def operation(session, work_part, report):
    section = closed_rectangle_section(work_part, 0.0, 10.0, 5.0)
    # The guide intersects the section at its upper-right corner. Sweep guide
    # strings that miss the profile are rejected as invalid section strings.
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
        builder.SectionList.Append(section)
        builder.GuideList.Append(guide)
        builder.OrientationMethod.OrientationOption = (
            NXOpen.GeometricUtilities.OrientationMethodBuilder.OrientationOptions.Fixed
        )
        builder.ScalingMethod.ScalingOption = (
            NXOpen.GeometricUtilities.ScalingMethodBuilder.ScalingOptions.Constant
        )
        feature = builder.CommitFeature()
        print("NXCAD_FEATURE_COMMITTED:", feature)
    finally:
        builder.Destroy()
    report["api_generation"] = "SweptBuilder1"
    report["orientation"] = "Fixed"


def main():
    run_probe(__file__, "NX 2606", "05_sweep_fixed_orientation", 1, operation)


if __name__ == "__main__":
    main()
