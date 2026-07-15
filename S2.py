Line 0 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\10_step_ap242.py", line 30, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\10_step_ap242.py", line 26, in main
    run_probe(__file__, "NX 2606", "10_step_ap242", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 51, in run_probe
    work_part = create_work_part_if_needed(session, probe_name)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 24, in create_work_part_if_needed
    result = session.Parts.NewDisplay(path, NXOpen.Part.Units.Millimeters)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'File already exists
'File already exists
