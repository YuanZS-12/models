不要重新运行 Journal，不要启动或操作 NX。

收集 aerospace_linkage_005 的最终证据：

1. 返回以下文件的大小和 SHA256：
   - curved_bellcrank.py
   - _nx_aerospace_probe_support.py
   - curved_bellcrank.nxreport.json
   - curved_bellcrank.prt
   - curved_bellcrank.step

2. 执行：

py -3 scripts\check-runtime-report "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005\curved_bellcrank.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005\curved_bellcrank.step"

返回完整 stdout、stderr 和退出码。

3. 明确确认：
   - _005 Journal 只从 NX UI 手动运行了一次；
   - 收集证据时未重新运行；
   - 未调用任何 NX/MCP 执行工具。

不需要快照、CAD Viewer 或 post-nx-review。完成后停止。
