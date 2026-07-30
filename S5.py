#traceback
Line 1 : Traceback (most recent call last):
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_003\11_styled_sweep_rotation_sets.py", line 89, in <module>
    main()
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_003\11_styled_sweep_rotation_sets.py", line 77, in main
    run_probe(
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_003\_probe_support.py", line 102, in run_probe
    operation(session, work_part, report)
  File "D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_003\11_styled_sweep_rotation_sets.py", line 55, in operation
    builder.FirstGuide = guide_section
    ^^^^^^^^^^^^^^^^^^
AttributeError: attribute 'FirstGuide' of 'NXOpen.Features.StyledSweepBuilder' objects is not writable
attribute 'FirstGuide' of 'NXOpen.Features.StyledSweepBuilder' objects is not writable

#json
{
  "artifacts": {},
  "error": "attribute 'FirstGuide' of 'NXOpen.Features.StyledSweepBuilder' objects is not writable",
  "execution": {
    "actor": "user",
    "tool": "nx_ui",
    "transport": "nx_ui"
  },
  "journal": {
    "path": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\angular_law_styled_sweep_003\\11_styled_sweep_rotation_sets.py",
    "working_dir": "D:\\Workdir\\iproot\\nx2606.1700\\test44\\workspace\\angular_law_styled_sweep_003"
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
  "source_sha256": "0087a5049a8b9b31c14941bbcac4a56a1e461276f5b81ddca98c84b6d67cd214"
}
