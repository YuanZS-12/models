不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。

`angular_law_styled_sweep_001` 暂不授权运行。请补齐准备证据：

1. 对以下实际使用的 API 做准确查询，不要用 `NXOpen.SectionList` 替代：
   - `NXOpen.Features.StyledSweepBuilder.Section`
   - `NXOpen.Features.StyledSweepBuilder.FirstGuide`
   - `NXOpen.Features.StyledSweepBuilder.RotationSetList`
   - `NXOpen.GeometricUtilities.RotationSetBuilderList.Append`
   - `NXOpen.Features.StyledSweepBuilder.CommitFeature`

2. 每个新增查询都必须：
   - 保存完整原始 Markdown
   - 写入 `api-review-raw`
   - 在 `api-review-manifest.json` 中记录 sequence、tool、exact_input、raw_markdown_file、raw_markdown_sha256 和完整 original_cache_path
   - 不得使用 `...` 或摘要代替原始内容

3. 可以复用 `angular_law_research_002` 的证据，但必须把被复用的原始 Markdown及其来源记录纳入可验证 manifest，不能只在 review JSON 中写 facts。

4. 更新 `styled-sweep-review-v1.json`，只保留原始查询实际证明的事实。若属性或 Append 签名仍无法查明，明确报告缺口并停止，不要授权运行。

5. 执行：
   py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-mcp-review-evidence" "<api-review-manifest.json完整路径>" --review-evidence "<styled-sweep-review-v1.json完整路径>"

6. 返回：
   - 完整验证命令
   - 完整 stdout
   - 完整 stderr
   - 退出码
   - manifest、review JSON、全部 raw Markdown 的完整绝对路径、大小和 SHA256
   - Journal 与 `_probe_support.py` 的完整绝对路径、大小和 SHA256
   - 工作目录完整文件清单
   - `check-journal --strict-geometry` 的完整命令、stdout、stderr 和退出码

不得修改或覆盖已准备的 Journal；如证据注入后必须重新准备，请创建全新的 `angular_law_styled_sweep_002`，不要覆盖 `_001`。完成后停止。
