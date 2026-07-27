继续 aerospace HPC rear frame 资格运行准备。

重要边界：
1. 不执行任何 Git、下载、安装或 nx-cad 更新命令；用户已经手动完成更新。
2. 不调用 dc_run_snippet、dc_run_journal、run_journal.exe。
3. 不启动、关闭或自动操作 Siemens NX。
4. 不运行任何 Journal。
5. 不修改 canonical probe。
6. 不删除、覆盖或修改 aerospace_frame_001 及任何 bearing workspace。

上一轮 aerospace_frame_001 尚未运行。其 strict check 失败已经确认是旧版
check-journal 对 CreateRuleCurveDumb 的假阳性，不是几何失败，也不允许通过添加
LOW_FIDELITY_FALLBACK 绕过。

请执行以下准备工作：

A. 确认当前 check-journal 已包含修复：
其 validate_misleading_primitive_approximation 中应使用带词边界的正则匹配，
避免 CreateRuleCurveDumb 被识别为 curved。
只读检查，不要执行 Git 命令。

B. 创建新的 frame-review-v3.json：
- schema_version: 2
- server: dc_mcp_server
- runtime_mode: mcp_review
- target_nx_version: NX 2606
- probe: aerospace_hpc_rear_frame
- tools 只能列出本轮或有保存原始结果的实际调用工具。
- 根据上一轮记录，实际调用工具应为：
  dc_lookup_pattern
  dc_search
  dc_get_api_info
- 不得列入未调用的 dc_list_namespace 或 dc_semantic_search。
- facts 必须是完整事实，不得使用 “...” 省略。
- 保存每次查询返回的原始 Markdown，并在最终报告中给出文件路径、SHA256
  和完整原文或完整附件内容。

C. 不得覆盖 aerospace_frame_001。创建全新目录：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_002

使用 prepare-dc-mcp-journal 从 canonical probe 创建：
aerospace_frame_002\aerospace_hpc_rear_frame.py

review evidence 使用 frame-review-v3.json，并保持 --manual-user-run。

D. 对 _002 Journal 执行：
py -3 scripts\check-journal "<_002 Journal绝对路径>" --strict-geometry

只执行静态检查，不运行 Journal。

E. 返回以下完整证据：
1. 当前 check-journal 文件 SHA256。
2. frame-review-v3.json 完整原文和 SHA256。
3. 每份原始 MCP Markdown 的路径、SHA256 和内容。
4. prepare 命令、完整 stdout/stderr 和退出码。
5. strict check 命令、完整 stdout/stderr 和退出码。
6. _002 全部文件清单、大小、时间和 SHA256。
7. canonical probe 和 workspace Journal SHA256 对照。
8. helper 和 builder SHA256。
9. 明确确认 _001 与所有 bearing workspace 未修改。
10. 明确确认尚未运行 Journal，也未操作 NX。

预期 canonical 哈希：
frame probe:
0556cdf708259c4e96795078c9accd2bd2f924d99addc2b2dd300fe82c7c317b

helper:
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

builder:
a14f3cb6adecaec3b49fb4a9be53e6f620cb2f0bd144dda895e24fdd77027bc8

完成后停下等待，不要运行 NX Journal。
