不要运行 Journal，不要启动、关闭或操作 NX，也不要调用 dc_run_snippet、dc_run_journal、run_journal.exe 或其他 NX 执行工具。不要执行 Git、下载、安装或更新操作。

按照 nx-cad skill，为 lofted airfoil blade 创建第一次资格运行准备目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001

规范源文件：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\lofted_airfoil_blade.py

请完成以下工作：

1. 检查当前可用的 dc_* 工具，只允许使用：
   - dc_lookup_pattern
   - dc_search
   - dc_semantic_search
   - dc_get_api_info
   - dc_list_namespace

2. 执行一次全新的、可持久验证的 MCP API review。至少审查：
   - periodic StudioSplineBuilderEx 建立三段 NACA 翼型曲线
   - GeometricConstraintData
   - Section
   - ScRuleFactory
   - ThroughCurvesBuilder
   - FeatureCollection.CreateStudioSplineBuilderEx
   - FeatureCollection.CreateThroughCurvesBuilder

3. STEP 导出可以复用已经验证的 NX 2606 ExistingPart/AP242 recipe，但必须在 review evidence 中写明所复用证据的真实来源。不得把 MCP 查询当作 NX 运行证据。

4. 每次实际完成的 MCP 查询都立即保存为独立 UTF-8 Markdown，放入：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\api-review-raw

5. 创建 api-review-manifest.json。每条记录必须包含：
   - sequence
   - tool
   - exact_input
   - raw_markdown_file
   - raw_markdown_sha256
   - original_cache_path（如果存在）

所有路径必须是完整真实绝对路径，不得使用“...”缩写。

6. 根据真实 MCP 返回内容创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\blade-review-v1.json

不得根据代码、记忆或推测伪造 MCP 证据。

7. 使用 nx-cad 的 check-mcp-review-evidence 实际验证 manifest 和 blade-review-v1.json，并返回：
   - 完整命令
   - stdout
   - stderr
   - 退出码

8. 使用 prepare-dc-mcp-journal --manual-user-run，将规范 probe 准备到：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\lofted_airfoil_blade.py

不得覆盖既有文件。复制所需的同目录支持文件。

9. 报告规范源文件、准备后 Journal 和支持文件各自的大小与 SHA256。特别报告最终准备后 Journal 的 SHA256。

10. 对准备后的 Journal 执行 check-journal --strict-geometry，并返回完整 stdout、stderr 和退出码。

11. 最后输出 aerospace_blade_001 的完整文件清单，包括绝对路径、大小和 SHA256。

完成准备后立即停止，等待我授权从 NX 2606 UI 手动运行。不得自行运行 Journal。
