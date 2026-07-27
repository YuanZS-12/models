Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 383, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 350, in main
    builder, step_path = build(output)
                         ^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 284, in build
    radial_boss_with_hole(borescope_angle_degrees, borescope_x, borescope_boss_diameter, borescope_boss_height, borescope_hole_diameter)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\aerospace_hpc_rear_frame.py", line 280, in radial_boss_with_hole
    b.boolean_subtract(frame, tool)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_003\cadnx\builder.py", line 893, in boolean_subtract
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
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_003\\aerospace_hpc_rear_frame.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_003"
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
  "run_id": "run_003",
  "schema_version": 2,
  "source_sha256": "e067265c235fe020071917f284c8b108d0b5190cff6848db7ce8157d0cc70141",
  "warnings": []
}
