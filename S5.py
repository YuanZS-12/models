不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX 执行工具，也不要修改现有文件。

请补充 aerospace_blade_001 的准备证据：

1. 原样输出以下两个 JSON 文件的完整内容：
   - D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\api-review-raw\api-review-manifest.json
   - D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\blade-review-v1.json

2. 检查这两个 JSON 是否包含字面量 `...`，分别报告计数。必须为 0。

3. 输出 manifest 的每一条记录，至少包括：
   - sequence
   - tool
   - exact_input
   - raw_markdown_file 完整绝对路径
   - raw_markdown_sha256
   - original_cache_path 完整绝对路径（如果存在）

4. 重新运行 check-mcp-review-evidence。分别捕获并报告：
   - 完整命令
   - 完整 stdout，不得缩写路径
   - 完整 stderr
   - 退出码

5. 重新运行 check-journal --strict-geometry。分别报告完整命令、stdout、stderr 和退出码，不得缩写路径。

6. 不要重新运行 prepare-dc-mcp-journal。请从现有记录或终端历史报告它上一次执行的完整命令、stdout、stderr 和退出码。如果无法恢复这些信息，明确写“无法恢复”，不要伪造，也不要重新准备或创建新目录。

7. 说明 `_nx_aerospace_probe_support.py` 是否先由 prepare-dc-mcp-journal 自动复制，随后又被 Copy-Item -Force 覆盖。报告覆盖源与当前目标的 SHA256，确认是否 bit-for-bit 相同。

8. 原样输出以下三个文件的大小和 SHA256：
   - canonical probe
   - prepared Journal
   - workspace helper

完成后停止。不得运行 Journal，不得修改文件。
