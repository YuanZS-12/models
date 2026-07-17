使用 nx-cad 和 dc_mcp_server 审查 NX 2606 的
07_sweep_angular_law.py。

只允许调用 dc_lookup_pattern、dc_search、dc_semantic_search、
dc_get_api_info、dc_list_namespace。

重点确认：
CreateSweptBuilder1
SweptBuilder1.Spine
OrientationMethod.AngularLaw
LawBuilder.SetSpineIntoBuilder
LawBuilder.Type.Linear
StartValue 和 EndValue
OrientationOptions.ByAngularLaw
CommitFeature 和 Destroy

禁止调用 dc_run_snippet、dc_run_journal、run_journal.exe，
禁止启动或关闭 NX。

保存真实 review-evidence-07.json，然后使用
prepare-dc-mcp-journal 生成 manual_nx Journal，运行
check-journal --strict-geometry。最后只告诉我要在 NX UI
中手动运行的准确文件路径，不要替我执行。
