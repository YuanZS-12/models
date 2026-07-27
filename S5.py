重新执行 aerospace frame 的精简 API review，并在每次 MCP 查询完成后立即保存
逐字原始 Markdown。不要复用或改写旧聊天摘要。

禁止 Git、下载、安装、更新、NX 自动操作和任何 Journal 执行。

保留 aerospace_frame_001 和 aerospace_frame_002，不修改其中任何文件。
创建：
frame-review-v4.json
aerospace_frame_003
aerospace_frame_003\api-review-raw

只执行以下查询：

1. dc_lookup_pattern:
   section extrude builder create extrude from section NXOpen

2. dc_get_api_info:
   NXOpen.CurveCollection

3. dc_get_api_info:
   NXOpen.SectionCollection

4. dc_get_api_info:
   NXOpen.ScRuleFactory

5. dc_get_api_info:
   NXOpen.Section

6. dc_get_api_info:
   NXOpen.Features.FeatureCollection
   method_filter=CreateExtrudeBuilder

7. dc_get_api_info:
   NXOpen.Features.ExtrudeBuilder

8. dc_get_api_info:
   NXOpen.DirectionCollection

9. dc_get_api_info:
   NXOpen.SmartObject.UpdateOption

10. dc_get_api_info:
    NXOpen.Expression
    property_filter=RightHandSide

每次调用后立即将 tool、完整输入和工具返回的逐字 Markdown 保存为独立 .md。
不得总结、补写、删节或使用聊天记忆重建。

创建 api-review-manifest.json，顶层必须为：
{"calls": [...]}

每项必须包含：
sequence
tool
exact_input
raw_markdown_file
raw_markdown_sha256
original_cache_path

frame-review-v4.json 的 tools 只能是：
["dc_lookup_pattern", "dc_get_api_info"]

facts 只记录这次 10 个查询直接支持的 frame/oriented-box API 事实，不要加入
无法链接原始结果的 bearing reuse 摘要。

使用 frame-review-v4.json 准备全新 aerospace_frame_003 Journal，然后运行：

py -3 scripts\check-journal "<_003 Journal>" --strict-geometry

py -3 scripts\check-mcp-review-evidence `
  "<_003>\api-review-raw\api-review-manifest.json" `
  --review-evidence frame-review-v4.json

两个检查都必须退出码 0。

返回：
- 两个检查的完整输出和退出码；
- frame-review-v4.json 完整原文及 SHA256；
- manifest 完整原文及 SHA256；
- 10 份逐字 Markdown 完整内容及 SHA256；
- _003 Journal、helper、builder SHA256；
- 确认 _001/_002 未修改；
- 确认未运行 Journal、未操作 NX、未调用执行工具。

完成后停止，不要运行 NX。
