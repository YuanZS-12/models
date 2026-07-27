Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004\aerospace_hpc_rear_frame.py", line 385, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004\aerospace_hpc_rear_frame.py", line 352, in main
    builder, step_path = build(output)
                         ^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004\aerospace_hpc_rear_frame.py", line 286, in build
    radial_boss_with_hole(borescope_angle_degrees, borescope_x, borescope_boss_diameter, borescope_boss_height, borescope_hole_diameter)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004\aerospace_hpc_rear_frame.py", line 282, in radial_boss_with_hole
    b.boolean_subtract(frame, tool)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004\cadnx\builder.py", line 893, in boolean_subtract
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
'The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.
{
  "artifacts": {
    "prt": {},
    "step": {}
  },
  "error": "'The tool and target do not form a complete intersection or have a touch condition which will result in a region with zero wall thickness.",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_004\\aerospace_hpc_rear_frame.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_004"
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
  "run_id": "run_004",
  "schema_version": 2,
  "source_sha256": "5630ea896be2425e0aff0d816ae30a295113a9361d3df8d4be89d358af5c9d24",
  "warnings": []
}
