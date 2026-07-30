不要新增 MCP 查询，不要修改或删除文件，不要准备或运行 Journal，不要操作 NX。

请完整原样输出以下文件内容，不做摘要，不使用 `...`：

1. `styled-sweep-research-v3.json`
2. `api-review-raw\api-review-manifest.json`
3. `api-review-raw\006_dc_lookup_pattern_styled_sweep_user_defined.md`
4. `api-review-raw\007_dc_lookup_pattern_RotationSetList.md`
5. `api-review-raw\008_dc_lookup_pattern_complete_example.md`
6. `api-review-raw\009_dc_semantic_search_user_defined_orientation.md`
7. `api-review-raw\004_StyledSweepReferenceMethodBuilder.md`

同时回答：

- “Significant pattern found”具体是哪一段逐字内容？
- pattern 中完整的 builder 配置顺序是什么？
- 它是否明确包含 Type、SectionList、FirstGuide、SectionOrientationOption、CreateRotationSet、RotationSetList、ReferenceMethod 和 CommitFeature？
- 它是成功 Journal pattern、API 文档片段，还是语义搜索推断？
- manifest 的 sequence 是否与本轮真实调用顺序一致？如果不一致，只报告问题，不要修改文件。

返回每个文件的完整绝对路径、大小和 SHA256。完成后停止。
