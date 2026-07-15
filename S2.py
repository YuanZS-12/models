#01
{
  "agent_execution": false,
  "body_count": 0,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "01_create_part",
  "result": "success",
  "schema_version": 1,
  "work_part": "C:\\apps\\devop_tools\\UDU\\test11\\models-main\\nx2606\\01_create_part.prt"
}
#02
{
  "agent_execution": false,
  "body_count": 0,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "02_closed_polyline_section",
  "result": "success",
  "schema_version": 1,
  "section_curve_count": 4
}
#03
{
  "agent_execution": false,
  "body_count": 0,
  "curve_entity_count": 1,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "03_closed_spline_section",
  "result": "success",
  "schema_version": 1
}
#04
{
  "agent_execution": false,
  "body_count": 1,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "through_curves_solid",
  "result": "success",
  "schema_version": 1
}
#08
{
  "agent_execution": false,
  "body_count": 1,
  "feature_overlap": 10.0,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "08_boolean_unite",
  "result": "success",
  "schema_version": 1
}
#09
{
  "agent_execution": false,
  "body_count": 1,
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "09_edge_blend",
  "result": "success",
  "schema_version": 1,
  "selected_edge_count": 1
}
#10
{
  "agent_execution": false,
  "body_count": null,
  "error": "'NXOpen.DexManager' object has no attribute 'CreateStep214Creator'",
  "manual_user_run": true,
  "nx_version": "NX 2606",
  "probe": "10_step_ap242",
  "result": "failure",
  "schema_version": 1
}
Line 0 : Traceback (most recent call last):
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\10_step_ap242.py", line 30, in <module>
    main()
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\10_step_ap242.py", line 26, in main
    run_probe(__file__, "NX 2606", "10_step_ap242", 1, operation)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 52, in run_probe
    operation(session, work_part, report)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\10_step_ap242.py", line 20, in operation
    export_step(session, work_part, output_path)
  File "C:\apps\devop_tools\UDU\test11\models-main\nx2606\_probe_support.py", line 119, in export_step
    creator = session.DexManager.CreateStep214Creator()
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NXOpen.DexManager' object has no attribute 'CreateStep214Creator'. Did you mean: 'CreateStepCreator'?
'NXOpen.DexManager' object has no attribute 'CreateStep214Creator'
