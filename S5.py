为 aerospace_frame_002 补齐 API review 原始证据。只做只读证据归档，
不要重新 prepare Journal，不要创建 _003，不要修改 _001 或 _002 Journal。

禁止：
- 任何 Git、下载、安装或更新命令；
- dc_run_snippet、dc_run_journal、run_journal.exe；
- 启动、关闭或自动操作 NX；
- 运行 Journal；
- 修改 canonical probe、builder、helper 或 frame-review-v3.json；
- 覆盖任何已有文件。

请执行：

1. 在以下目录中新建证据子目录：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_002\api-review-raw

2. 从 VS Code 会话缓存中找到 frame review 实际调用产生的全部原始结果。
必须覆盖：
- 2 次 dc_lookup_pattern；
- 实际执行的 dc_search；
- 所有实际执行的 dc_get_api_info。
不要归档无关会话结果，也不要补写或改写 MCP 返回内容。

3. 每次查询保存为独立 UTF-8 Markdown 文件。文件内容必须包含：
- tool 名称；
- 完整输入参数；
- MCP 返回的原始 Markdown，逐字保存，不得摘要或省略。

4. 创建 api-review-manifest.json，逐项记录：
- sequence；
- tool；
- exact_input；
- raw_markdown_file；
- raw_markdown_sha256；
- original_cache_path。

manifest 中的工具集合必须严格等于：
dc_lookup_pattern
dc_search
dc_get_api_info

5. 返回：
- api-review-raw 的完整文件清单、大小和 SHA256；
- api-review-manifest.json 完整原文；
- 每份 Markdown 的完整原文；
- 查询总数及按工具统计；
- frame-review-v3.json SHA256；
- _002 Journal、helper、builder 的当前 SHA256。

6. 再次确认：
- _002 Journal SHA256 仍为
  3E3A511E66E4A277BAE39EBCDD4999235E8B9776883FF0F144099CEED4FA9E19
- 未重新 prepare；
- 未修改 _001；
- 未运行 Journal；
- 未操作 NX；
- 未调用任何执行工具。

完成后停止并等待，不要运行 NX。
