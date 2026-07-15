#05
{
  "agent_execution": false,
  "api_generation": "SweptBuilder1",
  "body_count": 1,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "orientation": "Fixed",
  "probe": "05_sweep_fixed_orientation",
  "result": "success",
  "schema_version": 1,
  "section_count": 2
}

#07
Line 1 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 70, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 66, in main
    run_probe(__file__, "NX 2606", "07_sweep_angular_law", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 61, in run_probe
    operation(session, work_part, report)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 56, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Invalid orientation method specified.
'Invalid orientation method specified.
{
  "agent_execution": false,
  "body_count": null,
  "error": "'Invalid orientation method specified.",
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "07_sweep_angular_law",
  "result": "failure",
  "schema_version": 1
}
