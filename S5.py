不要重新运行 aerospace_duct_004，不要启动或操作 NX。

第一部分：补齐 _004 证据

返回以下文件的大小和 SHA256：
- curved_aerospace_duct.py
- _nx_aerospace_probe_support.py
- curved_aerospace_duct.nxreport.json
- curved_aerospace_duct.prt
- curved_aerospace_duct.step

执行绝对路径检查：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_004\curved_aerospace_duct.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_004\curved_aerospace_duct.step"

返回 stdout、stderr 和退出码。

确认 _004 仅从 NX UI 手动运行了一次，收集证据时未重新运行。

第二部分：准备最终第 3 次连续运行

创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005

保留 _001 至 _004，不得覆盖。

直接复制成功冻结源：

aerospace_duct_004\curved_aerospace_duct.py
→ aerospace_duct_005\curved_aerospace_duct.py

aerospace_duct_004\_nx_aerospace_probe_support.py
→ aerospace_duct_005\_nx_aerospace_probe_support.py

不得重新调用 prepare-dc-mcp-journal，不重新查询 MCP。

要求 SHA256：

Journal
bc9ecb80716368984b2b46e82be78def16e09bca7d98037055bd2459891fc192

Helper
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

运行 check-journal --strict-geometry，但不要运行 Journal。

返回：
1. _004 哈希与 runtime 检查结果；
2. _005 完整路径和文件清单；
3. _005 两个文件的大小和 SHA256；
4. strict geometry 的完整输出和退出码；
5. 确认未运行 _005、未操作 NX、未覆盖旧目录。

完成后停止，等待授权。
