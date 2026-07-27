不要重新运行 aerospace_linkage_004，也不要启动或操作 NX。

第一部分：补齐 _004 证据

1. 计算 curved_bellcrank.nxreport.json、PRT、STEP 的大小和 SHA256。
2. 执行：

py -3 scripts\check-runtime-report "<_004>\curved_bellcrank.nxreport.json" --expected-bodies 1 --step "<_004>\curved_bellcrank.step"

返回完整输出和退出码。
3. 确认 _004 Journal 只从 NX UI 手动运行了一次。
4. 不需要快照、CAD Viewer 或 post-nx-review。

第二部分：准备第 3 次连续资格运行

创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005

保留并不得覆盖 _001 至 _004。

从当前安装的 canonical nx-cad probe 复制：

curved_bellcrank.py
_nx_aerospace_probe_support.py

要求 SHA256：

curved_bellcrank.py
93e4aabaa6fdc4599df18b1a161c92acc2e7e4a64a37acac6b72eb2bd8f263a8

_nx_aerospace_probe_support.py
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

复用 _002 的 MCP review 证据，不重新查询 MCP。

对 _005 Journal 执行 check-journal --strict-geometry，返回：
- 完整路径；
- 文件大小和 SHA256；
- 完整检查输出及退出码；
- 目录文件清单；
- 合规性确认。

完成后停止。不要运行 _005 Journal，不要调用任何 NX 执行工具。
