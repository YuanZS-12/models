#traceback
Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004\11_styled_sweep_rotation_sets.py", line 65, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Internal error: memory access violation

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004\11_styled_sweep_rotation_sets.py", line 90, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004\11_styled_sweep_rotation_sets.py", line 78, in main
    run_probe(
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004\_probe_support.py", line 102, in run_probe
    operation(session, work_part, report)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004\11_styled_sweep_rotation_sets.py", line 68, in operation
    builder.Destroy()
NXOpen.NXException: 'Attempt to delete an object which is still referenced
'Attempt to delete an object which is still referenced

#json
{
  "artifacts": {},
  "error": "'Attempt to delete an object which is still referenced",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\angular_law_styled_sweep_004\\11_styled_sweep_rotation_sets.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\angular_law_styled_sweep_004"
  },
  "model": {
    "body_count": null,
    "critical_features": {
      "styled_sweep_rotation_sets_twist": false
    },
    "expected_body_count": 1
  },
  "nx_version": "NX 2606",
  "probe": "11_styled_sweep_rotation_sets",
  "result": "failure",
  "run_id": "run_001",
  "schema_version": 2,
  "source_sha256": "96d2bc3e1fe627e73387de83c5354d3ae12ebf1ea38130603184467c02bddc9b"
}
