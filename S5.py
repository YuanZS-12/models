#py文件
"""User-run NX 2606 probe: acquire or create one work part."""

import NXOpen

from _probe_support import run_probe


RAW_NXOPEN_HIGH_FIDELITY = True
EXECUTION_POLICY = {'mode': 'manual_nx', 'manual_user_run_required': True, 'agent_execution': False, 'requires_prepared_nx_environment': True, 'allow_launch_or_close_nx': False, 'allow_existing_work_part': False, 'allow_overwrite': False, 'managed_mode': False, 'max_repair_attempts': 3}
MCP_API_REVIEW = {'schema_version': 2, 'target_nx_version': 'NX 2606', 'probe': '01_create_part', 'runtime_mode': 'mcp_execute', 'tools': ['dc_lookup_pattern', 'dc_get_api_info'], 'facts': ['PartCollection.NewDisplay exists: NewDisplay(name: str, units: Part.Units) -> Part. Creates new .prt and sets as active display part.', 'Part.Units enum members: Inches, Millimeters, Mix, Meters, Micrometers.', 'Part inherits from BasePart -> NXObject -> TaggedObject -> object.', 'BasePart.Save signature: Save(save_component_parts: BasePart.SaveComponents, close: BasePart.CloseAfterSave) -> PartSaveStatus.', 'NewDisplay raises NXException if target .prt already exists. Must os.remove() first.', 'PartCollection has NO NewPart method.'], 'mcp_api_review_marker': True, 'notes': 'All API facts confirmed via actual dc_* MCP calls. No dc_run_snippet called.', 'server': 'dc_mcp_server'}
DESIGN_LEDGER = {"target_nx_version": "NX 2606", "expected_body_count": 0, "critical_features": ["work_part"]}


def operation(session, work_part, report):
    report["work_part"] = getattr(work_part, "FullPath", "") or getattr(work_part, "Name", "")
    print("NXCAD_WORK_PART:", report["work_part"])


def main():
    run_probe(__file__, "NX 2606", "01_create_part", 0, operation, EXECUTION_POLICY, DESIGN_LEDGER["critical_features"])


if __name__ == "__main__":
    main()
#json
{
  "artifacts": {
    "prt": {
      "exists": true,
      "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\01_create_part_run_001.prt",
      "size": 53880
    }
  },
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\01_create_part.py",
    "working_dir": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003"
  },
  "model": {
    "body_count": 0,
    "critical_features": {
      "work_part": true
    },
    "expected_body_count": 0
  },
  "nx_version": "NX 2606",
  "probe": "01_create_part",
  "result": "success",
  "run_id": "run_001",
  "schema_version": 2,
  "work_part": "C:\\Users\\z004n36r\\.agents\\nx_mcp_runs\\integration_003\\01_create_part_run_001.prt"
}

#prt文件路径
"C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\01_create_part_run_001.prt"
