Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_005\aerospace_hpc_rear_frame.py", line 385, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_005\aerospace_hpc_rear_frame.py", line 352, in main
    builder, step_path = build(output)
                         ^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_005\aerospace_hpc_rear_frame.py", line 309, in build
    b.boolean_subtract(frame, tool)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_005\cadnx\builder.py", line 893, in boolean_subtract
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
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_005\\aerospace_hpc_rear_frame.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_frame_005"
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
  "run_id": "run_005",
  "schema_version": 2,
  "source_sha256": "fa29bb2fe72998f141558c6ca8ecd77380378742f38d28e9b517350808e72336",
  "warnings": []
}
