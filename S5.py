不要通过 Git 下载、安装或更新任何内容。不要运行 Journal，不要启动、关闭或操作 NX，也不要调用 dc_run_snippet、dc_run_journal、run_journal.exe 或其他 NX 执行工具。

当前 nx-cad 已由用户手动更新到提交 d004409。

请准备 StyledSweep rotation-sets 的第一次实验运行：

1. 使用规范探针：
   C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\11_styled_sweep_rotation_sets.py

2. 使用已有研究目录：
   D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_research_002

3. 验证该目录的 MCP review evidence。重点确认：
   - FeatureCollection.CreateStyledSweepBuilder
   - StyledSweepBuilder
   - Types.OneGuide
   - SectionOrientationOptions.UserDefined
   - Section
   - FirstGuide
   - CreateRotationSet(value, path_par, path)
   - RotationSetList
   - RotationSetBuilderList.Append
   - CommitFeature

4. 如果现有证据没有明确证明 Section、FirstGuide、RotationSetList.Append 的准确绑定形式，只补查缺失 API，并将每次查询的原始 Markdown、manifest 和新的 review JSON 保存到一个新的研究目录。不得把推测写成已确认事实。

5. 创建全新且不存在的工作目录：
   D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_001

6. 使用 prepare-dc-mcp-journal 和 --manual-user-run，把规范探针准备到上述新目录。不得覆盖任何旧目录或旧文件。

7. 对准备后的 Journal 运行：
   check-journal --strict-geometry

8. 返回：
   - Journal 完整路径、大小和 SHA256
   - helper 完整路径、大小和 SHA256
   - review JSON、manifest、raw Markdown 的完整绝对路径
   - MCP evidence 检查的完整命令、stdout、stderr、退出码
   - check-journal 的完整命令、stdout、stderr、退出码
   - 新目录完整文件清单
   - 明确确认未运行 Journal、未操作 NX、未调用任何 NX 执行工具

完成准备后停止，等待用户授权从 NX UI 手动运行。
