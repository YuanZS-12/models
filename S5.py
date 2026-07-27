准备 aerospace HPC rear frame 修复后的全新 workspace。

禁止：
- Git、下载、安装或更新命令；
- 修改或删除 aerospace_frame_001、_002、_003；
- 修改 canonical probe；
- 调用 dc_run_snippet、dc_run_journal、run_journal.exe；
- 启动、关闭、自动操作 NX；
- 运行 Journal。

1. 只读确认 canonical frame SHA256 必须为：
5D267ECDA6EA2FD5F320038E49DA5DF0A3BAE1DB4F59A6B3FE6D95190F1FBA18

helper 必须为：
18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9

builder 必须为：
A14F3CB6ADECAEC3B49FB4A9BE53E6F620CB2F0BD144DDA895E24FDD77027BC8

2. 确认修复代码包含：
casing_wall = casing_or - casing_ir
hole_depth = boss_height + casing_wall + 2.0 * through_overcut

并确认不再包含：
b.cylinder(hole_diameter, casing_od, ...)

3. API family 与 API 调用没有变化，复用已通过的 frame-review-v4.json。
不要重新调用 MCP，也不要创建新的 review 事实。

4. 创建全新目录：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_004

使用 prepare-dc-mcp-journal 从新 canonical probe 准备：
aerospace_frame_004\aerospace_hpc_rear_frame.py

参数：
--review-evidence frame-review-v4.json
--manual-user-run

5. 运行且只运行静态检查：
py -3 scripts\check-journal "<_004 Journal绝对路径>" --strict-geometry

6. 返回：
- canonical、prepared Journal、helper、builder SHA256；
- prepare 命令、完整输出和退出码；
- strict check 命令、完整输出和退出码；
- _004 递归文件清单、大小、时间及 SHA256；
- _001、_002、_003 Journal 当前 SHA256；
- 确认旧 workspace 未修改；
- 确认未运行 Journal、未操作 NX、未调用执行工具；
- 确认本轮只是准备，等待用户授权。

完成后停止，不要运行 NX。
