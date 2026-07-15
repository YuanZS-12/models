"""User-run NX 2606 probe: acquire or create one work part."""

import NXOpen

from _probe_support import run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
USER_MANUAL_NX_EXECUTION_REQUIRED = True
STATIC_ONLY_NXOPEN_REVIEW = {"recipe": "nx2606.part.create", "runtime": "manual user run required"}
DESIGN_LEDGER = {"target_nx_version": "NX 2606", "expected_body_count": 0, "critical_features": ["work_part"]}


def operation(session, work_part, report):
    report["work_part"] = getattr(work_part, "FullPath", "") or getattr(work_part, "Name", "")
    print("NXCAD_WORK_PART:", report["work_part"])


def main():
    run_probe(__file__, "NX 2606", "01_create_part", 0, operation)


if __name__ == "__main__":
    main()
