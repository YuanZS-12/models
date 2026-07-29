不要重新运行 Journal，不要启动或操作 NX。

收集 aerospace_duct_005 最终证据：

1. 返回以下文件的大小和 SHA256：
   - curved_aerospace_duct.py
   - _nx_aerospace_probe_support.py
   - curved_aerospace_duct.nxreport.json
   - curved_aerospace_duct.prt
   - curved_aerospace_duct.step

2. 执行：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005\curved_aerospace_duct.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005\curved_aerospace_duct.step"

返回完整 stdout、stderr 和退出码。

3. 明确确认：
   - _005 Journal 只从 NX UI 手动运行了一次；
   - 收集证据时没有重新运行；
   - 没有调用任何 NX/MCP 执行工具。

不需要 snapshot、CAD Viewer 或 post-nx-review。
完成后停止。
