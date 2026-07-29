不要重新运行 aerospace_duct_003，不要启动或操作 NX。

第一部分：补齐 _003 证据

计算并返回以下文件的大小和 SHA256：
- curved_aerospace_duct.py
- _nx_aerospace_probe_support.py
- curved_aerospace_duct.nxreport.json
- curved_aerospace_duct.prt
- curved_aerospace_duct.step

执行：

py -3 scripts\check-runtime-report "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003\curved_aerospace_duct.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_003\curved_aerospace_duct.step"

返回完整 stdout、stderr 和退出码。

确认：
- _003 Journal 只从 NX UI 手动运行了一次；
- 收集证据时没有重新运行；
- 没有调用任何 NX/MCP 执行工具。

第二部分：准备第 2 次连续正式运行

创建：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_004

保留 _001、_002、_003，不得覆盖。

为确保三轮 source_sha256 完全一致，不要重新调用 prepare-dc-mcp-journal，不要从 canonical 重新注入 review。

直接复制 `_003` 中已经成功运行的冻结文件：

aerospace_duct_003\curved_aerospace_duct.py
→ aerospace_duct_004\curved_aerospace_duct.py

aerospace_duct_003\_nx_aerospace_probe_support.py
→ aerospace_duct_004\_nx_aerospace_probe_support.py

要求：

curved_aerospace_duct.py SHA256
bc9ecb80716368984b2b46e82be78def16e09bca7d98037055bd2459891fc192

helper SHA256
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

API review 继续引用 `_003` 已通过验证的 duct-review-v3.json 和 api-review-raw；不重新调用 MCP。

对 `_004` Journal 执行 check-journal --strict-geometry。

返回：
1. _003 的最终哈希和 runtime 检查结果；
2. _004 完整路径；
3. _004 两个文件的大小和 SHA256；
4. strict geometry 完整输出和退出码；
5. _004 完整文件清单；
6. 确认没有运行 _004、没有操作 NX、没有覆盖旧目录。

不需要 snapshot、CAD Viewer 或 post-nx-review。
完成后停止，等待用户授权。
