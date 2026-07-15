

#07
Line 1 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 82, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 78, in main
    run_probe(__file__, "NX 2606", "07_sweep_angular_law", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 61, in run_probe
    operation(session, work_part, report)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\07_sweep_angular_law.py", line 67, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Invalid orientation method specified.
'Invalid orientation method specified.
