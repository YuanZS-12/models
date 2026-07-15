#05
Line 1 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\05_sweep_fixed_orientation.py", line 60, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\05_sweep_fixed_orientation.py", line 56, in main
    run_probe(__file__, "NX 2606", "05_sweep_fixed_orientation", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 60, in run_probe
    operation(session, work_part, report)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\05_sweep_fixed_orientation.py", line 47, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Unable to approximate guide string.
'Unable to approximate guide string.
{
  "agent_execution": false,
  "body_count": null,
  "error": "'Unable to approximate guide string.",
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "05_sweep_fixed_orientation",
  "result": "failure",
  "schema_version": 1
}
#06
{
  "agent_execution": false,
  "api_generation": "SweptBuilder1",
  "body_count": 1,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "06_sweep_two_sections",
  "result": "success",
  "schema_version": 1,
  "section_count": 2
}
#07
Line 1 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 59, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 55, in main
    run_probe(__file__, "NX 2606", "07_sweep_angular_law", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 60, in run_probe
    operation(session, work_part, report)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 46, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Unable to approximate guide string.
'Unable to approximate guide string.
{
  "agent_execution": false,
  "body_count": null,
  "error": "'Unable to approximate guide string.",
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "07_sweep_angular_law",
  "result": "failure",
  "schema_version": 1
}
