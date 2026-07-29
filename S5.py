准备 curved aerospace duct 第 1 次修复 workspace。

限制：
- 不执行 Git、下载、安装或更新命令。
- 不启动、关闭或操作 NX。
- 不运行 Journal。
- 不调用 dc_run_snippet、dc_run_journal、run_journal.exe。
- 不修改 canonical probe。
- 保留 aerospace_duct_001 和 aerospace_duct_002，不得覆盖。
- _002 是第一次真实 NX 失败，不能重跑。

创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003

验证 canonical：

curved_aerospace_duct.py
b73942faf8f1c9f3fb7c46e920e8533e557824fec644d153a8de3c5ae6d7a75b

_nx_aerospace_probe_support.py
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

API review：

复用 _002 中已经通过验证的 8 个原始 MCP Markdown，但由于新代码增加了 raw BooleanBuilder subtract，必须进行以下新增查询并立即保存完整原始 Markdown：

1. dc_get_api_info
{
  "class_name": "NXOpen.Features.BooleanBuilder"
}

2. dc_get_api_info
{
  "info_type": "method",
  "class_name": "NXOpen.Features.FeatureCollection",
  "method_name": "CreateBooleanBuilder"
}

3. dc_get_api_info
{
  "class_name": "NXOpen.Features.Feature",
  "property_filter": "BooleanType"
}

如果第 3 个查询不能返回 BooleanType：
- 保存原始失败 Markdown；
- 使用 dc_search 查询 BooleanType；
- 再对实际类名执行 dc_get_api_info；
- 如实记录新增调用，不伪造结果。

将旧 8 个和所有新增 Markdown 放入：

aerospace_duct_003\api-review-raw

创建新的 api-review-manifest.json：
- 包含全部实际调用；
- sequence 连续；
- exact_input 完整；
- raw_markdown_file 使用同目录相对路径；
- SHA256 与实际文件一致；
- original_cache_path 必须是真实完整路径或 null。

创建 duct-review-v3.json：
- schema_version = 2
- server = dc_mcp_server
- runtime_mode = mcp_review
- probe = aerospace_curved_duct
- tools 与 manifest 的实际工具集合完全一致
- 保留已验证的 spline、Section、ThroughCurves facts
- 新增 BooleanBuilder、CreateBooleanBuilder、BooleanType.Subtract、Target/Tool 或 collector fallback 的真实查询事实
- 不得把本次 API 查询描述成 NX runtime 成功

使用 check-mcp-review-evidence 验证 manifest 和 duct-review-v3.json。

然后使用 prepare-dc-mcp-journal 从新 canonical 创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003\curved_aerospace_duct.py

参数：
- --review-evidence duct-review-v3.json
- --manual-user-run

复制 helper，并执行 check-journal --strict-geometry。

预计模型契约：

body_count = 1

critical features：
- five_outer_and_five_inner_periodic_spline_sections
- outer_and_inner_station_only_through_curves
- continuous_internal_passage

预计输出：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003\curved_aerospace_duct.prt

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003\curved_aerospace_duct.step

返回：
1. canonical、最终 workspace Journal、helper 的大小和 SHA256；
2. 所有实际 MCP 调用及 exact input；
3. 所有 raw Markdown 的路径、大小和 SHA256；
4. manifest 和 duct-review-v3.json 完整原文；
5. evidence checker 完整输出和退出码；
6. strict geometry 完整输出和退出码；
7. _003 完整文件清单；
8. 确认未运行 Journal、未操作 NX、未覆盖 _001/_002。

完成后停止，等待用户授权。
