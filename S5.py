不要通过 Git 下载、安装或更新任何内容。不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。

用户已手动把 nx-cad 更新到提交 `3baaab6`。

请准备修复后的 StyledSweep rotation-sets 实验：

1. 确认规范探针已经使用：
   `builder.SectionList.Append([section])`

   并且不再包含：
   `builder.Section = section`

2. 创建全新目录：
   `D:\Workdir\iproot\nx2606.1700\test44\workspace\angular_law_styled_sweep_003`

   不得覆盖 `_001` 或 `_002`。

3. 复用 `_002` 已通过检查的 MCP review evidence。把完整的：
   - `api-review-raw`
   - `api-review-manifest.json`
   - `styled-sweep-review-v2.json`

   复制到 `_003`。不得重新编写、摘要或缩写原始证据。

4. 使用 `prepare-dc-mcp-journal --manual-user-run` 将最新规范探针准备到 `_003`。

5. 确保 `_probe_support.py` 位于同一目录。

6. 运行：
   - `check-mcp-review-evidence`
   - `check-journal --strict-geometry`

7. 返回：
   - Canonical 与 Prepared Journal 的完整绝对路径、大小和 SHA256
   - `_probe_support.py` 的完整绝对路径、大小和 SHA256
   - review、manifest、raw Markdown 的完整路径
   - 两个检查的完整命令、stdout、stderr、退出码
   - `_003` 完整文件清单
   - 明确确认 Prepared Journal 包含 `SectionList`，不包含 `builder.Section =`
   - 明确确认未运行 Journal、未操作 NX、未调用 NX/MCP 执行工具

完成后停止，等待用户授权。
