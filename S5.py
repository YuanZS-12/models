补齐 linkage API review 证据，不重新调用 MCP，不运行 NX。

禁止修改或覆盖 aerospace_linkage_001。
创建全新：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_002
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_002\api-review-raw

从当前会话缓存逐字归档全部 10 次实际调用：

1. dc_lookup_pattern
2. dc_get_api_info NXOpen.Features.StudioSplineBuilderEx
3. dc_get_api_info NXOpen.GeometricConstraintData（失败结果也必须保存）
4. dc_get_api_info NXOpen.Section
5. dc_get_api_info NXOpen.ScRuleFactory
6. dc_get_api_info NXOpen.Features.ThroughCurvesBuilder
7. dc_get_api_info FeatureCollection/CreateStudioSplineBuilderEx
8. dc_get_api_info FeatureCollection/CreateThroughCurvesBuilder
9. dc_search GeometricConstraintData
10. dc_get_api_info NXOpen.Features.GeometricConstraintData

不得重新总结或改写原始 Markdown。

创建 linkage-review-v2.json：
tools 必须为：
["dc_lookup_pattern", "dc_get_api_info", "dc_search"]

facts 中明确记录：
- NXOpen.GeometricConstraintData 查询未找到；
- dc_search 将类定位到 NXOpen.Features.GeometricConstraintData；
- 最终正确类信息来自 NXOpen.Features.GeometricConstraintData。

创建 manifest：
{"calls": [...]}

必须有连续的 sequence 1 至 10，每项包含：
tool
exact_input
raw_markdown_file
raw_markdown_sha256
original_cache_path

用 linkage-review-v2.json 从相同 canonical probe 准备：
aerospace_linkage_002\curved_bellcrank.py

运行：

py -3 scripts\check-journal "<_002 Journal>" --strict-geometry

py -3 scripts\check-mcp-review-evidence `
  "<_002>\api-review-raw\api-review-manifest.json" `
  --review-evidence linkage-review-v2.json

返回：
- 两个检查的完整输出和退出码；
- v2 review 与 manifest 完整原文和 SHA256；
- 10 份 Markdown 清单、大小和 SHA256；
- canonical、prepared Journal、helper SHA256；
- 确认没有 cadnx；
- 确认 _001 及所有旧 workspace 未修改；
- 确认尚未运行 Journal、未操作 NX。

完成后停止等待授权。
