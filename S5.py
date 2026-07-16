使用已安装的 nx-cad skill，执行 NX 2606 首轮 dc_mcp_server 集成验证。

环境：
- NX、Designcenter 和 dc_mcp_server 已由用户手动启动。
- dc_* 七个 MCP 工具在当前 Copilot 会话中均可见。
- 用户明确授权本任务进入 mcp_execute。
- canonical skill 路径：
  C:\Users\z004n36r\.agents\skills\nx-cad
- 本轮独立工作目录：
  C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002

硬性要求：
1. 先完整阅读：
   C:\Users\z004n36r\.agents\skills\nx-cad\SKILL.md
   C:\Users\z004n36r\.agents\skills\nx-cad\references\mcp-runtime.md
   C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\dc-mcp-integration-manifest.json
2. 不修改 canonical skill 内的任何文件。
3. 不启动或关闭 NX。
4. 不复用当前 work part。
5. 不覆盖任何 PRT、STEP、JSON、Markdown 或 Journal。
6. 不使用上一轮 review-evidence-01.json、review-evidence-06.json。
7. 只记录实际成功调用的 dc_* 工具；禁止模拟或推测 MCP 结果。
8. 如果任何 dc_* 工具实际不可调用，立即停止，不得伪造 review evidence。
9. 本轮只运行 probe 01 和 probe 06，不运行 07、10。
10. 每个 Journal 执行前必须通过 check-journal --strict-geometry。

第一阶段：probe 01 API review

实际调用：
- dc_lookup_pattern：
  query="create new part"
  limit=3
- dc_get_api_info：
  info_type="method"
  class_name="NXOpen.PartCollection"
  method_name="NewDisplay"
- 根据需要查询 NXOpen.Part、NXOpen.Part.Units 和 BasePart.Save 的真实签名。

将每次 MCP 查询的完整原始 Markdown 原样保存到：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01-api-review.md

根据实际返回创建：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-01.json

JSON 的 tools 只能包含实际成功调用的工具，facts 只能记录实际返回确认的事实。
没有调用 dc_run_snippet，就不能把它写入 tools。

准备 probe 01：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\prepare-dc-mcp-journal C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\01_create_part.py C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.py --review-evidence C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-01.json --user-authorized

静态检查：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.py --strict-geometry

只有检查通过后才调用 dc_run_journal：

journal_path=
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.py

working_dir=
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002

managed_mode=false
timeout=90

把 dc_run_journal 返回的完整 Markdown 原样保存为：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.dc-result.md

解析：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\parse-dc-mcp-result journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.dc-result.md --require-runtime-report --output C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\01_create_part.dc-result.json

找到实际生成的 .nxreport.json 后验证：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report <实际nxreport路径> --expected-bodies 0

probe 01 必须全部成功后才能继续 probe 06。

第二阶段：probe 06 API review

实际调用：
- dc_lookup_pattern：
  query="two section solid sweep with fixed orientation"
  limit=3
- dc_get_api_info：
  info_type="method"
  class_name="NXOpen.Features.FreeformSurfaceCollection"
  method_name="CreateSweptBuilder1"
- dc_get_api_info：
  info_type="class"
  class_name="NXOpen.Features.SweptBuilder1"
- 核对 SectionList、GuideList、BodyPreference、OrientationMethod 和 CommitFeature 的真实签名及 enum。

保存完整原始查询 Markdown到：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06-api-review.md

根据实际查询结果创建：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-06.json

准备 probe 06：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\prepare-dc-mcp-journal C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\06_sweep_two_sections.py C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.py --review-evidence C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-06.json --user-authorized

静态检查：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.py --strict-geometry

只有检查通过后调用 dc_run_journal：

journal_path=
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.py

working_dir=
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002

managed_mode=false
timeout=300

保存完整返回：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.dc-result.md

解析并验证：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\parse-dc-mcp-result journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.dc-result.md --require-runtime-report --output C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\06_sweep_two_sections.dc-result.json

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report <实际nxreport路径> --expected-bodies 1

最终返回：
- 实际调用的全部 dc_* 工具
- 所有 MCP 原始 Markdown 文件路径
- 两次 check-journal 输出
- 两次 dc_run_journal exit code、stdout、stderr、output files
- 两个 .nxreport.json 的完整内容与路径
- 两个 PRT 的完整路径和文件大小
- 是否发生修复以及修复次数
- 不得仅用 exit code 0 宣称几何成功
