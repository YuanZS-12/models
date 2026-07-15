"""User-run NX 2606 probe: native save and non-empty STEP export."""

import os

import NXOpen
import NXOpen.Features

from _probe_support import cylinder, export_step, run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
USER_MANUAL_NX_EXECUTION_REQUIRED = True
STATIC_ONLY_NXOPEN_REVIEW = {"recipe": "nx2606.export.step", "runtime": "manual user run required"}
DESIGN_LEDGER = {"target_nx_version": "NX 2606", "expected_body_count": 1, "critical_features": ["native_save", "step_export"]}


def operation(session, work_part, report):
    cylinder(work_part, 20.0, 10.0)
    output_path = os.path.splitext(os.path.abspath(__file__))[0] + ".step"
    export_step(session, work_part, output_path)
    report["step"] = {"path": output_path, "exists": True, "size": os.path.getsize(output_path)}
    print("NXCAD_STEP_EXPORTED:", output_path)


def main():
    run_probe(__file__, "NX 2606", "10_step_ap242", 1, operation)


if __name__ == "__main__":
    main()
