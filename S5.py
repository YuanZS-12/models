准备 curved bellcrank 第 2 次连续资格运行。

限制：
- 不执行 Git、下载、安装或更新命令。
- 不启动、关闭或操作 NX。
- 不运行 Journal。
- 不调用任何 NX/MCP 执行工具。
- 保留 aerospace_linkage_001、_002、_003，不得覆盖。
- 不需要快照、CAD Viewer、skills/cad 或 post-nx-review。

创建新目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_004

从当前已安装 nx-cad skill 的 canonical probe 复制：

curved_bellcrank.py
_nx_aerospace_probe_support.py

要求 SHA256：

curved_bellcrank.py
93e4aabaa6fdc4599df18b1a161c92acc2e7e4a64a37acac6b72eb2bd8f263a8

_nx_aerospace_probe_support.py
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

复用 aerospace_linkage_002 已验证的 linkage-review-v2.json 和 api-review-raw 证据，不重新调用 MCP，因为代码和 API 组合均未改变。

运行 check-journal --strict-geometry，但不要运行 Journal。

返回：
1. _004 完整路径；
2. 两个文件的路径、大小和 SHA256；
3. strict-geometry 完整输出及退出码；
4. 新目录完整文件清单；
5. 确认没有运行 Journal、没有操作 NX、没有覆盖旧目录。

完成后停止，等待用户授权。
