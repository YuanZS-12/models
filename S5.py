#traceback
Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001\aerospace_hpc_rear_frame.py", line 423, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001\aerospace_hpc_rear_frame.py", line 394, in main
    raise RuntimeError("Expected one final rear-frame body, found %d" % body_count)
RuntimeError: Expected one final rear-frame body, found 3
Expected one final rear-frame body, found 3
#json
{
  "artifacts": {
    "prt": {},
    "step": {}
  },
  "error": "Expected one final rear-frame body, found 3",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_redesign_001\\aerospace_hpc_rear_frame.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_redesign_001"
  },
  "model": {
    "body_count": 3,
    "critical_features": {
      "annular_casing": false,
      "central_bearing_hub": false,
      "flange_hole_patterns": false,
      "primary_and_secondary_struts": false
    },
    "expected_body_count": 1
  },
  "nx_version": "NX 2606",
  "probe": "aerospace_hpc_rear_frame",
  "result": "failure",
  "run_id": "run_001",
  "schema_version": 2,
  "source_sha256": "50e88ccd1b104eec9c016bbc2bf79aaf1194253b66ce1d60363a24f2c3ac23f5",
  "warnings": []
}
