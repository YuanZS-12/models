准备 aerospace frame 第三次且最后一次修复 workspace。

禁止 Git、下载、更新、NX 自动操作或 Journal 执行。
保留并不得修改 aerospace_frame_001 至 aerospace_frame_004。

确认 canonical frame SHA256：
2ADAAEFFAED4A331166DB2C44310E02779A20FE69BA46780FA4DA55759BC1215

确认代码同时包含：
borescope_angle_degrees = 270.0
borescope_x = 0.0
casing_wall = casing_or - casing_ir
hole_depth = boss_height + casing_wall + 2.0 * through_overcut

helper SHA256：
18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9

builder SHA256：
A14F3CB6ADECAEC3B49FB4A9BE53E6F620CB2F0BD144DDA895E24FDD77027BC8

API family 未变，复用 frame-review-v4.json，不重新调用 MCP。

创建全新目录：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_005

使用 prepare-dc-mcp-journal 创建 _005 Journal，参数：
--review-evidence frame-review-v4.json
--manual-user-run

随后只运行：
py -3 scripts\check-journal "<_005 Journal>" --strict-geometry

返回：
- prepare 与 strict check 的完整输出和退出码；
- canonical、prepared Journal、helper、builder SHA256；
- _005 完整文件清单；
- _001 至 _004 Journal SHA256；
- 确认旧 workspace 未修改；
- 确认尚未运行 Journal、未操作 NX。

完成后停止，等待用户授权。
