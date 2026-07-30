不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX 执行工具。不要执行 Git、下载、安装或更新操作，不要生成正式 probe。

上一轮发现 `StyledSweepBuilder` 是 materially different API family，因此不能将最终结论写成 `no_materially_different_candidate_found`。本轮只补齐可编码所需的完整 API 证据。

创建新目录，不得修改 research_001：

D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_research_002\api-review-raw

请完成：

1. 调用 dc_lookup_pattern 查询：
   - NXOpen StyledSweepBuilder CreateRotationSet RotationSetList journal
   - NXOpen styled sweep rotation sets twist along guide
   - NX Open recorded Styled Sweep section rotation journal

2. 调用 dc_search 分别搜索：
   - CreateStyledSweepBuilder
   - CreateRotationSet
   - RotationSetList
   - StyledSweepBuilder Types
   - SectionOrientationOption
   - StyledSweep rotation set

3. 对以下类和方法执行 dc_get_api_info：
   - `NXOpen.Features.StyledSweepBuilder`
   - `FeatureCollection.CreateStyledSweepBuilder`
   - `StyledSweepBuilder.CreateRotationSet`
   - `StyledSweepBuilder.CommitFeature`
   - `NXOpen.SectionList`
   - StyledSweepBuilder.CreateRotationSet 返回的对象类型
   - RotationSetList 的实际集合类型及其 Append/Add 方法
   - 若 class info 暴露 BodyPreference、GuideList、SectionList、Spine、Type 或 SectionOrientationOption，获取其完整属性和枚举信息

4. 必须明确回答以下问题，并给出对应原始证据：
   - 正确的 builder factory 位于哪个 collection？
   - factory 的参数类型以及创建新 feature 时应传什么 Null？
   - `CreateRotationSet` 的精确参数顺序和类型是什么？
   - angle 参数是 float、Expression、字符串还是其他对象？
   - path parameter 的范围和类型是什么？
   - path 参数需要 Curve、Section、Guide、Spine 还是其他对象？
   - 返回对象的实际 NXOpen 类名是什么？
   - RotationSetList 如何加入 rotation set？
   - 截面如何加入 builder？
   - guide/path 如何加入 builder？
   - 如何请求 solid body？
   - builder 的 Type 和 SectionOrientationOption 应选择哪个枚举成员？
   - 是否需要至少两个 rotation sets，例如路径参数 0.0 与 1.0？
   - 是否有必须设置的 scaling、alignment、spine 或 tolerance 属性？

5. 不得把以下内容当作新候选：
   - SweptBuilder
   - SweptBuilder1
   - OrientationOptions.ByAngularLaw
   - LawBuilder.SetSpineIntoBuilder
   - 预先旋转终端截面

6. 每次实际 MCP 调用保存为独立 UTF-8 Markdown，并创建：
   - api-review-manifest.json
   - styled-sweep-research-v1.json

`styled-sweep-research-v1.json` 必须包含：

- `conclusion: materially_different_candidate_found` 或 `insufficient_signature_evidence`
- `api_family`
- `factory`
- `builder_properties`
- `exact_method_signatures`
- `enum_members`
- `minimal_probe_sequence`
- `unresolved_questions`
- 每条事实对应的 manifest sequence

7. 用 check-mcp-review-evidence 验证并报告完整命令、stdout、stderr和退出码。

8. 原样输出 `styled-sweep-research-v1.json` 的完整内容，并摘录所有包含下列词的原始 Markdown段落：
   - CreateStyledSweepBuilder
   - CreateRotationSet
   - RotationSetList
   - SectionOrientationOption
   - BodyPreference
   - SectionList
   - GuideList

完成后停止。不得生成或运行 Journal。
