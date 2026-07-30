#traceback
Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\aerospace_hpc_rear_frame.py", line 442, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\aerospace_hpc_rear_frame.py", line 409, in main
    builder, step_path = build(output)
                         ^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\aerospace_hpc_rear_frame.py", line 227, in build
    require_single_body("rings_and_bearing_seats")
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\aerospace_hpc_rear_frame.py", line 202, in require_single_body
    raise RuntimeError(
RuntimeError: Rear-frame body-count checkpoint rings_and_bearing_seats found 3 bodies
Rear-frame body-count checkpoint rings_and_bearing_seats found 3 bodies
#json
{
  "artifacts": {
    "prt": {},
    "step": {}
  },
  "error": "Rear-frame body-count checkpoint rings_and_bearing_seats found 3 bodies",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_redesign_002\\aerospace_hpc_rear_frame.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_redesign_002"
  },
  "model": {
    "body_count": null,
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
  "run_id": "run_002",
  "schema_version": 2,
  "source_sha256": "5df25ece563cef14c7eff2c812ce36c550226f340318ab77f19e5b4eeda2ced6",
  "warnings": []
}
