我们正在执行 nx-cad 的 NX 2606 航空部件资格运行。当前只处理 bearing support，
不要处理 frame、linkage、duct、blade、AngularLaw，也不要修改 canonical skill。

仓库已更新到：
2a1be0c36ca621e09ef2988c41ae2c97be292632

canonical Journal：
nx-cad\assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py

目标 workspace：
workspace\aerospace_bearing_001\bearing_support_housing.py

严格边界：

1. 你只能调用以下 API 查询工具：
   - dc_lookup_pattern
   - dc_search
   - dc_semantic_search
   - dc_get_api_info
   - dc_list_namespace

2. 绝对不得调用：
   - dc_run_snippet
   - dc_run_journal
   - run_journal.exe
   - 任何 NX 启动、关闭、GUI 自动化或 Journal 自动执行方式

3. 不得修改：
   - canonical nx-cad skill
   - canonical aerospace probe
   - 已有 workspace Journal
   - 已有 PRT、STEP、JSON、日志或证据

4. 不得删除旧文件来绕过冲突。

请按以下顺序执行：

A. 检查当前暴露了哪些 dc_* 工具。
如果五个允许的查询工具均不可用，停止并报告 static_only；不得伪造 API Review。

B. 使用至少一个 discovery 工具：
dc_lookup_pattern、dc_search 或 dc_semantic_search。

C. 审查 bearing support Wrapper 及其 cadnx 运行路径涉及的 NXOpen API，重点包括：
- Session.GetSession
- Parts.Work / Parts.NewDisplay
- Part.Units.Millimeters
- Block/Cylinder 创建
- Boolean unite/subtract
- Edge chamfer
- native Part.Save
- DexManager.CreateStepCreator
- StepCreator 的 ExportAs、ExportFrom、FileSaveFlag、
  ProcessHoldFlag、OutputFile、Commit、Destroy

对实际使用或可疑的 class、builder、property、enum 和 method 调用
dc_get_api_info。保存每次真实查询的原始 Markdown。

D. 创建 bearing-review.json，只记录实际完成的查询，不得捏造。
格式至少为：

{
  "schema_version": 2,
  "server": "dc_mcp_server",
  "runtime_mode": "mcp_review",
  "tools": [
    "实际调用成功的允许工具"
  ],
  "facts": [
    "从真实查询结果得到的具体 API 事实"
  ],
  "target_nx_version": "NX 2606",
  "probe": "nx_benchmark_bearing_housing"
}

tools 里不得出现 dc_run_snippet 或 dc_run_journal。

E. 用以下命令准备全新、不可覆盖的 workspace：

py -3 nx-cad\scripts\prepare-dc-mcp-journal `
  nx-cad\assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py `
  workspace\aerospace_bearing_001\bearing_support_housing.py `
  --review-evidence bearing-review.json `
  --manual-user-run

该命令应自动复制：
- _nx_aerospace_probe_support.py
- cadnx\__init__.py
- cadnx\builder.py

如果目标已存在，不得覆盖；停止并报告。

F. 严格静态检查：

py -3 nx-cad\scripts\check-journal `
  workspace\aerospace_bearing_001\bearing_support_housing.py `
  --strict-geometry

G. 完成后停止。不要运行 Journal，不要启动或操作 NX。

最终请返回：

1. git rev-parse HEAD
2. 当前可用的 dc_* 工具列表
3. 每个实际调用的 dc_* 工具名称和查询内容
4. 原始 API Review Markdown 的文件路径
5. bearing-review.json 的完整内容和路径
6. prepare-dc-mcp-journal 的完整 stdout/stderr 和退出码
7. check-journal 的完整 stdout/stderr 和退出码
8. 准备好的 Journal 的准确绝对路径
9. workspace 内所有文件的列表
10. 准备好的 Journal SHA256
11. 明确声明：
    - 未调用 dc_run_snippet
    - 未调用 dc_run_journal
    - 未自动运行 NX
    - 未覆盖或删除旧文件
    - Journal 仍需用户从 NX UI 手动运行
