不要通过 Git 下载、安装或更新内容。不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。

用户已手动将 nx-cad 更新到提交 `382ed14`。

请准备 StyledSweep rotation-sets 修复后的下一轮：

1. 验证规范探针：
   `C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\11_styled_sweep_rotation_sets.py`

2. 确认代码：
   - 包含 `require_attribute(builder, "FirstGuide")`
   - 使用 `add_curves_to_section` 填充 builder-owned FirstGuide
   - 不包含 `builder.FirstGuide =`
   - 不包含 `builder.Section =`

3. 创建全新目录：
   `D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_004`

   不得覆盖或重新运行 `_001`、`_002`、`_003`。

4. 复制 `_003` 中已通过验证的 MCP review evidence，包括：
   - `api-review-raw`
   - `api-review-manifest.json`
   - `styled-sweep-review-v2.json`

5. 使用 `prepare-dc-mcp-journal --manual-user-run` 准备最新规范探针，并复制 `_probe_support.py`。

6. 运行：
   - `check-mcp-review-evidence`
   - `check-journal --strict-geometry`

7. 返回：
   - Canonical、Prepared Journal、support 的完整绝对路径、大小和 SHA256
   - 两项检查的完整命令、stdout、stderr、退出码
   - `_004` 完整文件清单
   - 确认 Prepared Journal 使用 builder-owned FirstGuide
   - 确认未运行 Journal、未操作 NX、未调用 NX/MCP 执行工具

完成后停止，等待用户授权。
