开始 curved aerospace bellcrank/linkage 第一次资格运行准备。

边界：
- 不执行 Git、下载、安装或更新命令。
- 不调用 dc_run_snippet、dc_run_journal、run_journal.exe。
- 不启动、关闭或自动操作 NX。
- 不运行 Journal。
- 不修改 canonical probe。
- 不修改或删除任何 frame/bearing workspace。

Canonical probe：
C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\curved_bellcrank.py

期望 SHA256：
19505AB1BA6F0AEF5098E8CDD6D5E2A297AF9FC77787072A739AC3A3F50A5C63

Helper SHA256：
18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9

这是 raw NXOpen probe，不得复制或导入 cadnx。

创建：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_001
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_001\api-review-raw

执行以下精简 API review，每次查询完成后立即保存 tool、完整输入和逐字原始
Markdown，不能事后根据聊天摘要重建：

1. dc_lookup_pattern
   query:
   NXOpen StudioSplineBuilderEx periodic through points ThroughCurves solid

2. dc_get_api_info
   class_name: NXOpen.Features.StudioSplineBuilderEx

3. dc_get_api_info
   class_name: NXOpen.GeometricConstraintData

4. dc_get_api_info
   class_name: NXOpen.Section

5. dc_get_api_info
   class_name: NXOpen.ScRuleFactory

6. dc_get_api_info
   class_name: NXOpen.Features.ThroughCurvesBuilder

7. dc_get_api_info
   class_name: NXOpen.Features.FeatureCollection
   method_filter: CreateStudioSplineBuilderEx

8. dc_get_api_info
   class_name: NXOpen.Features.FeatureCollection
   method_filter: CreateThroughCurvesBuilder

创建 linkage-review-v1.json：
- schema_version: 2
- server: dc_mcp_server
- runtime_mode: mcp_review
- tools 只能为：
  dc_lookup_pattern
  dc_get_api_info
- target_nx_version: NX 2606
- probe: curved_bellcrank_repaired
- facts 只能记录本轮原始结果直接支持的事实
- 可记录 linked_verified_recipes：
  nx2606.section.periodic-spline
  nx2606.section.closed-polyline
  nx2606.through-curves.solid
  nx2606.boolean.unite
  nx2606.export.step-creator

创建 api-review-manifest.json，顶层必须为：
{"calls": [...]}

每项包含：
sequence
tool
exact_input
raw_markdown_file
raw_markdown_sha256
original_cache_path

使用 prepare-dc-mcp-journal 创建：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_001\curved_bellcrank.py

参数：
--review-evidence linkage-review-v1.json
--manual-user-run

随后只运行两个只读检查：

py -3 scripts\check-journal "<workspace Journal>" --strict-geometry

py -3 scripts\check-mcp-review-evidence `
  "<workspace>\api-review-raw\api-review-manifest.json" `
  --review-evidence linkage-review-v1.json

返回：
- 两个检查的完整输出和退出码；
- linkage-review-v1.json 完整原文和 SHA256；
- manifest 完整原文和 SHA256；
- 8 份逐字 Markdown、大小和 SHA256；
- canonical、prepared Journal、helper SHA256；
- workspace 递归文件清单；
- 确认没有 cadnx；
- 确认未运行 Journal、未操作 NX、未调用执行工具；
- 确认所有旧 workspace 未修改。

完成后停止，等待用户授权。
