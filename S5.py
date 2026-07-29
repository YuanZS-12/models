开始 curved aerospace duct 的首次资格运行准备。

严格限制：
1. 不执行 Git、下载、安装或更新命令。
2. 不启动、关闭或自动操作 Siemens NX。
3. 不调用 dc_run_snippet、dc_run_journal、run_journal.exe。
4. 不运行 Journal；最终只能由用户从 NX UI 手动执行。
5. 不修改已安装 skill 中的 canonical probe。
6. 不删除或覆盖任何已有 workspace。
7. 不需要 snapshot、CAD Viewer、skills/cad 或 post-nx-review。

目标 workspace：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_001

Canonical 文件：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\curved_aerospace_duct.py

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\_nx_aerospace_probe_support.py

开始前验证 canonical SHA256：

curved_aerospace_duct.py
6edceda85adca9bc5c69d670811de65598b0397f3de3f825c2ef97a49ec36162

_nx_aerospace_probe_support.py
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

第一阶段：执行全新的精简 MCP API review

只允许使用以下五类查询工具：
- dc_lookup_pattern
- dc_search
- dc_semantic_search
- dc_get_api_info
- dc_list_namespace

建议完成以下查询：

1. dc_lookup_pattern
   exact input:
   {
     "query": "NXOpen periodic studio spline annular sections ThroughCurves solid duct",
     "limit": 3
   }

2. dc_get_api_info
   {
     "class_name": "NXOpen.Features.StudioSplineBuilderEx"
   }

3. dc_get_api_info
   {
     "class_name": "NXOpen.Features.GeometricConstraintData"
   }

4. dc_get_api_info
   {
     "class_name": "NXOpen.Section"
   }

5. dc_get_api_info
   {
     "class_name": "NXOpen.ScRuleFactory"
   }

6. dc_get_api_info
   {
     "class_name": "NXOpen.Features.ThroughCurvesBuilder"
   }

7. dc_get_api_info
   {
     "info_type": "method",
     "class_name": "NXOpen.Features.FeatureCollection",
     "method_name": "CreateStudioSplineBuilderEx"
   }

8. dc_get_api_info
   {
     "info_type": "method",
     "class_name": "NXOpen.Features.FeatureCollection",
     "method_name": "CreateThroughCurvesBuilder"
   }

如果某个完整类名查询失败：
- 保存失败返回的原始 Markdown；
- 使用一次 dc_search 定位实际名称；
- 再对实际名称调用 dc_get_api_info；
- 不得伪造或改写 MCP 返回。

每次实际查询完成后，立即把完整原始 Markdown 保存到：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_001\api-review-raw

要求一条调用对应一个 Markdown 文件。

创建 api-review-manifest.json，每条记录必须包含：
- sequence
- tool
- exact_input
- raw_markdown_file
- raw_markdown_sha256
- original_cache_path（存在时）

创建 duct-review-v1.json，必须如实记录：
- schema_version = 2
- server = dc_mcp_server
- runtime_mode = mcp_review
- 实际使用的查询工具集合
- 实际返回的 API facts
- target_nx_version = NX 2606
- probe = aerospace_curved_duct

使用 check-mcp-review-evidence 验证 manifest 和 duct-review-v1.json，返回完整输出及退出码。

第二阶段：准备 workspace Journal

使用 prepare-dc-mcp-journal 从 canonical probe 创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_001\curved_aerospace_duct.py

参数必须包含：
- --review-evidence duct-review-v1.json
- --manual-user-run

确认支持文件被复制到同一目录：

_nx_aerospace_probe_support.py

注意：
- prepare 工具注入 MCP review 后，workspace Journal SHA256 可能不同于 canonical SHA256。
- 必须同时报告 canonical SHA256 和最终 workspace Journal SHA256。
- 后续正式连续运行将以最终 workspace Journal SHA256 为冻结源。

第三阶段：静态验证

对 workspace Journal 执行：

py -3 scripts\check-journal "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_001\curved_aerospace_duct.py" --strict-geometry

不要运行 Journal。

最终返回：

1. workspace 绝对路径；
2. canonical probe、workspace Journal、helper 的大小和 SHA256；
3. 所有实际 MCP 调用的工具名与 exact input；
4. 每个 raw Markdown 的绝对路径、大小和 SHA256；
5. api-review-manifest.json 完整内容；
6. duct-review-v1.json 完整内容；
7. check-mcp-review-evidence 完整命令、stdout、stderr、退出码；
8. check-journal --strict-geometry 完整命令、stdout、stderr、退出码；
9. workspace 完整文件清单；
10. 预计：
    - body_count = 1
    - critical features：
      - five_annular_periodic_spline_sections
      - station_only_through_curves_duct
      - continuous_internal_passage
    - PRT 和 STEP 输出路径；
11. 明确确认：
    - 未运行 Journal；
    - 未启动、关闭或操作 NX；
    - 未调用任何 NX 执行工具；
    - 未修改 canonical probe；
    - 未删除或覆盖旧 workspace。

完成后停止，等待用户授权从 NX UI 手动运行。
