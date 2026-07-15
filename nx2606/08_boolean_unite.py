"""User-run NX 2606 probe: unite two overlapping cylinders."""

import NXOpen
import NXOpen.Features

from _probe_support import cylinder, run_probe, unite


RAW_NXOPEN_HIGH_FIDELITY = True
USER_MANUAL_NX_EXECUTION_REQUIRED = True
STATIC_ONLY_NXOPEN_REVIEW = {"recipe": "nx2606.boolean.unite", "runtime": "manual user run required"}
DESIGN_LEDGER = {"target_nx_version": "NX 2606", "expected_body_count": 1, "critical_features": ["boolean_unite"]}


def operation(session, work_part, report):
    feature_overlap = 10.0
    target = cylinder(work_part, 30.0, 20.0, (0.0, 0.0, 0.0))
    tool = cylinder(work_part, 20.0, 20.0, (10.0, 0.0, 0.0))
    feature = unite(work_part, target, tool)
    report["feature_overlap"] = feature_overlap
    print("NXCAD_BOOLEAN_COMMITTED:", feature)


def main():
    run_probe(__file__, "NX 2606", "08_boolean_unite", 1, operation)


if __name__ == "__main__":
    main()
