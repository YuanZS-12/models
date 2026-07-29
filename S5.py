不要运行 aerospace_duct_001，不要启动或操作 NX。

这是准备证据修正，不是 NX 失败修复。保留 _001，创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002

不重新调用 MCP。复用 _001 的 8 个真实原始返回，但按正确归档结构复制到：

aerospace_duct_002\api-review-raw\
  001_dc_lookup_pattern.md
  002_StudioSplineBuilderEx.md
  003_GeometricConstraintData.md
  004_Section.md
  005_ScRuleFactory.md
  006_ThroughCurvesBuilder.md
  007_CreateStudioSplineBuilderEx_method.md
  008_CreateThroughCurvesBuilder_method.md
  api-review-manifest.json

要求：
1. manifest 与所有 raw Markdown 位于同一个 api-review-raw 目录。
2. manifest 的 raw_markdown_file 使用同目录相对文件名。
3. 保留每个文件原始内容和原 SHA256，不改写 MCP 返回。
4. manifest 的 exact_input 必须与实际 8 次调用一致。
5. original_cache_path 有真实绝对路径时写完整路径；未知时用 null，不得使用 `...` 伪装成绝对路径。

在 _002 根目录创建修正后的：

duct-review-v2.json

修正规则：
- tools 必须仍为实际工具集合：
  ["dc_lookup_pattern", "dc_get_api_info"]
- 删除错误陈述：
  NXOpen.SectionAllowTypes.OnlyCurves
- 正确记录 Journal 实际使用的嵌套 enum：
  NXOpen.Section.AllowTypes.OnlyCurves
- facts 只能来自已保存的原始 Markdown。
- 不得改变或美化失败的 MCP 返回。

验证：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-mcp-review-evidence" ^
  "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\api-review-raw\api-review-manifest.json" ^
  --review-evidence "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\duct-review-v2.json"

然后使用 canonical probe 和 duct-review-v2.json 创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py

同时复制：

_nx_aerospace_probe_support.py

Canonical SHA256 必须为：

curved_aerospace_duct.py
6edceda85adca9bc5c69d670811de65598b0397f3de3f825c2ef97a49ec36162

helper
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

运行 check-journal --strict-geometry，但不要运行 Journal。

正确的预计输出路径应为：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.prt

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.step

返回：
1. _002 完整文件清单、大小和 SHA256；
2. api-review-manifest.json 和 duct-review-v2.json 完整原文；
3. evidence checker 的完整输出和退出码；
4. strict geometry 检查的完整输出和退出码；
5. canonical、最终 workspace Journal、helper 的 SHA256；
6. 确认未运行 Journal、未操作 NX、未覆盖 _001、未重新调用 MCP。

完成后停止，等待授权。
