#traceback
Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py", line 261, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py", line 226, in main
    feature = create_duct(work_part)
              ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py", line 175, in create_duct
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Gaps in string or multiple loops.
'Gaps in string or multiple loops.
#json
{
  "artifacts": {
    "prt": {},
    "step": {}
  },
  "error": "'Gaps in string or multiple loops.",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_duct_002\\curved_aerospace_duct.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\aerospace_duct_002"
  },
  "model": {
    "body_count": null,
    "critical_features": {
      "continuous_internal_passage": false,
      "five_annular_periodic_spline_sections": false,
      "station_only_through_curves_duct": false
    },
    "expected_body_count": 1
  },
  "nx_version": "NX 2606",
  "probe": "aerospace_curved_duct",
  "result": "failure",
  "run_id": "run_002",
  "schema_version": 2,
  "source_sha256": "f6e894b4500fee9464063bcc50a3daf10746bb71f1f66f1c033fdaacf047645a",
  "warnings": []
}
