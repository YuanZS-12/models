Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/styled-sweep-research-v3.json)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/api-review-manifest.json)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/006_dc_lookup_pattern_styled_sweep_user_defined.md)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/007_dc_lookup_pattern_RotationSetList.md)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/008_dc_lookup_pattern_complete_example.md)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/009_dc_semantic_search_user_defined_orientation.md)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/angular_law_styled_sweep_research_003/api-review-raw/004_StyledSweepReferenceMethodBuilder.md)

---

## 文件完整输出与问题回答

### 文件清单与 SHA256

| 文件 | 完整绝对路径 | 大小 | SHA256 |
|---|---|---|---|
| styled-sweep-research-v3.json | `D:\...\research_003\styled-sweep-research-v3.json` | 4,111 | `(见上文)` |
| api-review-manifest.json | `D:\...\research_003\api-review-raw\api-review-manifest.json` | 3,227 | `(见上文)` |
| `006_*.md` | `D:\...\research_003\api-review-raw\006_dc_lookup_pattern_styled_sweep_user_defined.md` | 1,510 | `54ec608facb6977ceac4f8834aa7a79c218951e78109566c9da523cb30dc4f02` |
| `007_*.md` | `D:\...\research_003\api-review-raw\007_dc_lookup_pattern_RotationSetList.md` | 243 | `f9415948ab13b801c26516e2e8520df4a89ae6b28b900f3c96c07f175d7da359` |
| `008_*.md` | `D:\...\research_003\api-review-raw\008_dc_lookup_pattern_complete_example.md` | 255 | `3eb4aa1739534dd7763030674fea9c28674a9351d3d3dac79524d69d23a8f1ac` |
| `009_*.md` | `D:\...\research_003\api-review-raw\009_dc_semantic_search_user_defined_orientation.md` | 1,010 | `d0e026e5ea6267ba1c1921474bf3be0987b49601b05204bd628f0fdbcf2e8414` |
| `004_*.md` | `D:\...\research_003\api-review-raw\004_StyledSweepReferenceMethodBuilder.md` | 750 | `23067422c9556ba66a7a5137297d9464575e49ce74c7f422d3d89f881b9e0831` |

---

### 问答

**Q1: "Significant pattern found" 具体是哪一段逐字内容？**

来自 MCP 缓存文件 `call_00_8DHZuWWN4cz2oKW5FrYq2206__vscode-1785373827603` 的完整 Pattern-1 标题与解决方案摘要：

```
Creating a Class-A styled sweep surface along a guide curve with section profiles (score: 13)
Solution: Use workPart.Features.CreateStyledSweepBuilder(None). Types: OneGuide,
OneGuideOneTouch, OneGuideOneOrientation, TwoGuides. Set FirstGuide (Section object)
with guide curve, and add section profiles to SectionList. SectionOrientationOptions:
Translate, KeepAngle, MakeNormal, UserDefined, ArcLength. GOTCHA #1: Both CommitFeature()
and Commit() work — both throw NXException if inputs are missing. Error without sections:
'Missing section string.' GOTCHA #2: Destroy() after a failed commit with sections
configured may throw 'Attempt to delete an object which is still referenced' — wrap
Destroy in try/except. GOTCHA #3: G0Tolerance and G1Tolerance default to 0.0 — set them.
```

Python 代码片段：
```python
ssb = workPart.Features.CreateStyledSweepBuilder(None)
ssb.Type = NXOpen.Features.StyledSweepBuilder.Types.OneGuide
ssb.SectionOrientationOption = NXOpen.Features.StyledSweepBuilder.SectionOrientationOptions.MakeNormal
ssb.G0Tolerance = 0.01
ssb.G1Tolerance = 0.5
guide_sec = ssb.FirstGuide  # builder-owned Section
guide_sec.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.CurvesAndPoints)
# sec = workPart.Sections.CreateSection(...)
# ssb.SectionList.Append(sec)
# feat = ssb.CommitFeature()
```

---

**Q2: Pattern 中完整的 builder 配置顺序是什么？**

```
1. CreateStyledSweepBuilder(None)
2. Type = Types.OneGuide
3. SectionOrientationOption = SectionOrientationOptions.MakeNormal
4. G0Tolerance = 0.01
5. G1Tolerance = 0.5
6. FirstGuide — builder-owned Section，通过 SetAllowedEntityTypes + ScRuleFactory 填充
7. SectionList.Append(section) — 至少一个截面
8. CommitFeature()
9. Destroy() — 需要 try/except 保护
```

---

**Q3: 它是否明确包含以下各项？**

| 项目 | 包含？ | 说明 |
|---|---|---|
| `Type` | ✅ | `Types.OneGuide` |
| `SectionList` | ✅ | `SectionList.Append(sec)`（注释掉） |
| `FirstGuide` | ✅ | builder-owned Section，通过 `SetAllowedEntityTypes` + `ScRuleFactory` 填充 |
| `SectionOrientationOption` | ✅ | `SectionOrientationOptions.MakeNormal` |
| `CreateRotationSet` | ❌ | **未出现** |
| `RotationSetList` | ❌ | **未出现** |
| `ReferenceMethod` | ❌ | **未出现** |
| `CommitFeature` | ✅ | 注释中提及 |

---

**Q4: 它是成功 Journal pattern、API 文档片段，还是语义搜索推断？**

这是 **Designcenter 知识库的 pattern（dc_lookup_pattern 结果）**，是经过人工审核的最佳实践条目。它不是 NX UI 录制 Journal，也不是语义搜索推断。代码中关键部分被注释掉（`# sec = ... # ssb.SectionList.Append(sec) # feat = ssb.CommitFeature()`），说明它是一个方案描述，不是可直接运行的 Journal。

**不包含 CreateRotationSet、RotationSetList 或 ReferenceMethod 的配置。** 任何涉及 rotation-set 的组合均缺乏可验证的实验证据。

---

**Q5: Manifest 的 sequence 是否与本轮真实调用顺序一致？**

**不一致。** 真实调用顺序为：

| 真实序号 | 真实调用 | Manifest 中的 sequence |
|---|---|---|
| 1 | `dc_lookup_pattern` "styled sweep one guide..." | 6 |
| 2 | `dc_lookup_pattern` "StyledSweepBuilder CreateRotationSet RotationSetList" | 7 |
| 3 | `dc_lookup_pattern` "NXOpen StyledSweepBuilder complete journal example" | 8 |
| 4 | `dc_semantic_search` "StyledSweepBuilder user-defined orientation guide" | 9 |
| 5 | `dc_get_api_info` StyledSweepBuilder | 1 |
| 6 | `dc_get_api_info` RotationSetBuilder | 2 |
| 7 | `dc_get_api_info` RotationSetBuilderList | 3 |
| 8 | `dc_search` "StyledSweepBuilder OrientationGuide" | 5 |
| 9 | `dc_search` "StyledSweepReferenceMethodBuilder" | 10 |
| 10 | `dc_get_api_info` StyledSweepReferenceMethodBuilder | 4 |

Manifest 按工具类型分组（所有 `dc_get_api_info` 在前），而非按调用时间排序。按照用户要求，只报告问题，**不修改文件**。
