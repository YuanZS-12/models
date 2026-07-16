使用最新版 nx-cad，准备 probe 06 的用户手动 NX 运行副本。

禁止调用 dc_run_snippet、dc_run_journal、run_journal.exe，禁止启动或关闭 NX。
MCP 只用于真实 API 查询。

实际调用：
1. dc_lookup_pattern
   query="two section solid sweep with fixed orientation"
   limit=3

2. dc_get_api_info
   info_type="method"
   class_name="NXOpen.Features.FreeformSurfaceCollection"
   method_name="CreateSweptBuilder1"

3. dc_get_api_info
   info_type="class"
   class_name="NXOpen.Features.SweptBuilder1"

核对并记录以下对象的真实签名或 enum：
- BodyPreference.BodyType
- FeatureOptions.BodyStyle.Solid
- SectionList.Append
- GuideList.Append
- OrientationMethod.OrientationOption
- OrientationOptions.Fixed
- CommitFeature
- Destroy

将原始 MCP Markdown 保存到：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\06-api-review.md

创建：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\review-evidence-06.json

JSON 只能包含实际调用的查询工具，不得包含 dc_run_snippet、
dc_run_journal、mcp_execute 或 user_authorized。

然后运行：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\prepare-dc-mcp-journal C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\06_sweep_two_sections.py C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\06_sweep_two_sections.py --review-evidence C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\review-evidence-06.json --manual-user-run

静态检查：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\06_sweep_two_sections.py --strict-geometry

完成后停止，只告诉用户要在 NX 中手动运行哪个文件。
