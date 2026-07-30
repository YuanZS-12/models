不要通过 Git 下载、安装或更新内容。不要运行 Journal，不要创建运行工作区，不要启动、关闭或操作 NX，不要调用 dc_run_snippet、dc_run_journal 或任何 NX 执行工具。

用户已手动将 nx-cad 更新到 `5cc95f9`。

StyledSweep 已失败两次，只剩最后一次运行机会。本轮只能进行 MCP API 研究，不得准备或运行 `_005`。

已知主错误：

`StyledSweepBuilder.CommitFeature(): Internal error: memory access violation`

次生清理错误：

`Attempt to delete an object which is still referenced`

请创建全新研究目录：

`D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_research_003`

研究目标是查明一套完整、可提交的 StyledSweepBuilder rotation-set 配置，而不是只确认单个属性存在。

至少执行并保存以下查询：

1. `dc_lookup_pattern`
   - styled sweep one guide user defined rotation sets
   - StyledSweepBuilder CreateRotationSet RotationSetList
   - NXOpen StyledSweepBuilder complete journal example

2. `dc_search` / `dc_semantic_search`
   - StyledSweepBuilder user-defined orientation guide
   - StyledSweepBuilder rotation law along guide
   - StyledSweepBuilder required inputs before CommitFeature

3. 不带 property_filter，获取完整类信息：
   - `NXOpen.Features.StyledSweepBuilder`
   - `NXOpen.GeometricUtilities.RotationSetBuilder`
   - `NXOpen.GeometricUtilities.RotationSetBuilderList`

4. 精确检查：
   - `StyledSweepBuilder.Type`
   - `StyledSweepBuilder.SectionOrientationOption`
   - `StyledSweepBuilder.FirstGuide`
   - `StyledSweepBuilder.OrientationGuide`
   - `StyledSweepBuilder.SectionList`
   - `StyledSweepBuilder.CreateRotationSet`
   - `StyledSweepBuilder.RotationSetList`
   - `RotationSetBuilder.Value`
   - `RotationSetBuilder.ResetExtraData`
   - `RotationSetBuilderList.Append`
   - 是否存在 Validate、GetContents、Remove、Clear、Delete 或类似生命周期方法

重点回答：

- `Types.OneGuide` 与 `SectionOrientationOptions.UserDefined` 是否为合法组合？
- UserDefined 是否必须配合 `OrientationGuide`？
- rotation sets 应在什么 Type/OrientationOption 下使用？
- `CreateRotationSet` 返回的对象是否应直接 Append？
- Append 后 rotation-set builder 是否需要 ResetExtraData、Destroy 或保持存活？
- `path` 应传原始 guide curve、FirstGuide 中的 curve，还是其他对象？
- 是否需要两个截面而不是一个截面？
- StyledSweepBuilder 是否只能生成 sheet，或是否存在 solid/closed-profile控制项？
- Commit 前是否存在 Validate 方法或必填 builder 属性？

证据要求：

- 每次查询保存一份完整原始 Markdown
- 建立 `api-review-manifest.json`
- 记录完整 exact_input、文件 SHA256 和 original_cache_path
- 不得用 `...`、摘要或手写 facts 代替原始证据
- 创建独立 research JSON，只记录查询实际证明的事实
- 运行 `check-mcp-review-evidence`
- 返回完整命令、stdout、stderr、退出码
- 返回所有文件的完整绝对路径、大小和 SHA256

如果没有找到完整配置模式，请明确结论为“证据不足”，不要猜测修复，也不要准备 `_005`。完成研究后停止。
