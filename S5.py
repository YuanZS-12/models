不要运行 Journal，不要启动、关闭或操作 NX，不要调用 dc_run_snippet、dc_run_journal、run_journal.exe 或任何 NX 执行工具。不要执行 Git、下载、安装或更新操作。不要修改 nx-cad skill 文件，也不要生成正式 Journal。

本轮只执行 AngularLaw materially different API research。

创建研究证据目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_research_001\api-review-raw

已知并禁止重复提出的失败配置：

1. SweptBuilder1，两截面，显式 Spine，调用 AngularLaw.SetSpineIntoBuilder，再选择 ByAngularLaw。
2. SweptBuilder1，两截面，ByAngularLaw，但不调用 SetSpineIntoBuilder。
3. SweptBuilder1，两截面，无显式 Spine，选择 ByAngularLaw。
4. legacy SweptBuilder + ByAngularLaw。

这些配置已被 NX 2606 以 `Invalid orientation method specified` 或相关错误拒绝。旋转终端截面只是 fallback，不是 AngularLaw 成功证据。

请完成：

1. 使用 dc_lookup_pattern 查询真实 NX Journal 中“角度规律控制截面扭转”的成功模式。至少查询：
   - NXOpen successful sweep angular law twist journal
   - NXOpen angle law orientation sweep NX 2606
   - NXOpen law controlled twist along guide
   - NX Open recorded journal angular law sweep

2. 使用 dc_semantic_search 查询：
   - different NXOpen API family for law-controlled sweep twist
   - variational sweep or studio sweep with angle law
   - sweep section orientation controlled by expression or law

3. 使用 dc_search 搜索以下名称及相近类/方法：
   - ByAngularLaw
   - AngularLaw
   - LawBuilder
   - OrientationMethodBuilder
   - VariationalSweep
   - SweepAlongGuide
   - StudioSweep
   - SectionOrientation
   - Twist
   - AngleLaw

4. 根据 discovery 返回的真实候选，再调用 dc_get_api_info 检查完整类、builder factory、属性、枚举和方法签名。不要凭记忆补充不存在的 API。

5. 重点判断是否存在以下任一 materially different 候选：
   - 不使用 SweptBuilder/SweptBuilder1 的 API family
   - 使用另一种 law/orientation builder
   - NX UI 录制 Journal 展示了此前未测试的必要设置、顺序或关联对象
   - 通过表达式、spine law、section orientation law 或其他正式 API 实现连续角度规律，而不是预先旋转终端截面

6. 每次实际完成的 MCP 调用立即保存为独立 UTF-8 Markdown。失败查询也单独保存，不得合并或改写原始输出。

7. 创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_research_001\api-review-raw\api-review-manifest.json

每条记录包含：

- sequence
- tool
- exact_input
- raw_markdown_file
- raw_markdown_sha256
- original_cache_path（如果存在）

8. 创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_research_001\angular-law-research-v1.json

内容必须包括：

- target_nx_version
- tools
- rejected_configurations
- discovered_candidates
- materially_different_candidates
- required_api_objects
- unresolved_questions
- recommendation

每个事实必须关联到 manifest 中的实际原始查询，不得根据记忆或源代码伪造。

9. 用 check-mcp-review-evidence 验证 manifest 和 angular-law-research-v1.json，报告完整命令、stdout、stderr和退出码。

10. 最终给出明确结论之一：

A. `materially_different_candidate_found`
   - 报告 API family、完整调用顺序、所需对象以及对应原始证据。

B. `no_materially_different_candidate_found`
   - 保持 ByAngularLaw rejected，不生成新 probe。

不得把已失败配置换个参数后称为新候选，不得生成或运行 Journal。完成后停止。
