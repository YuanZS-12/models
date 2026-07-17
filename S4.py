Line 1 : Traceback (most recent call last):
  File "C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\07_sweep_angular_law.py", line 71, in <module>
    main()
  File "C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\07_sweep_angular_law.py", line 67, in main
    run_probe(__file__, "NX 2606", "07_sweep_angular_law", 1, operation, EXECUTION_POLICY, DESIGN_LEDGER["critical_features"])
  File "C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\_probe_support.py", line 92, in run_probe
    operation(session, work_part, report)
  File "C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\07_sweep_angular_law.py", line 56, in operation
    feature = builder.CommitFeature()
              ^^^^^^^^^^^^^^^^^^^^^^^
NXOpen.NXException: 'Invalid orientation method specified.
'Invalid orientation method specified.
