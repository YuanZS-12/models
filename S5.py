计算：

C:\Users\z004n36r\.agents\skills\nx-cad\cadnx\builder.py

的 SHA256。期望值：

e8cb0db81c691d520d651e2634f20914d383808d59d6bd26c07347869c6c564c

同时确认 builder.py 的 _configure_step_exporter 中存在：

if input_path:
    self._set_export_from_existing_part(exporter)
    self._set_optional_attr(exporter, "InputFile", input_path)

并确认 _set_export_from_existing_part 使用：

ExportFromOption.ExistingPart

可以继续使用现有 bearing-review-v2.json，因为真实 API Review 已经确认：
- ExportFromOption.ExistingPart
- StepCreator.InputFile
- ObjectTypes.Solids

不要重新调用 dc_* 工具，也不要修改旧 review 文件。

准备全新 workspace：

py -3 scripts\prepare-dc-mcp-journal `
  assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py `
  "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_003\bearing_support_housing.py" `
  --review-evidence bearing-review-v2.json `
  --manual-user-run

然后严格检查：

py -3 scripts\check-journal `
  "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_003\bearing_support_housing.py" `
  --strict-geometry

完成后停止。不要运行 Journal，不要操作 NX。

返回：

1. canonical cadnx\builder.py SHA256
2. 上述 ExistingPart/InputFile 代码片段
3. prepare 命令 stdout/stderr 和退出码
4. check-journal stdout/stderr 和退出码
5. aerospace_bearing_003 递归文件列表
6. prepared bearing_support_housing.py SHA256
7. prepared cadnx\builder.py SHA256
8. 确认 _001 和 _002 未修改、未删除、未再次运行
9. 确认未调用 dc_run_snippet 或 dc_run_journal
