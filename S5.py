不要重新运行 Journal，不要启动或操作 NX。

对现有 aerospace_linkage_003 进行运行后证据收集：

1. 计算并返回以下文件的大小和 SHA256：
   - curved_bellcrank.py
   - _nx_aerospace_probe_support.py
   - curved_bellcrank.nxreport.json
   - curved_bellcrank.prt
   - curved_bellcrank.step

2. 使用 nx-cad 的 check-runtime-report 验证：
   - expected bodies = 1
   - 指定现有 curved_bellcrank.step
   返回完整命令、stdout、stderr 和退出码。

3. 使用 nx-cad 的 post-nx-review 对现有 _003 产物执行确定性 STEP 检查和快照流程。
   返回生成的 post-nx-review.json 路径、完整内容、命令输出和退出码。

4. 返回快照文件的绝对路径、大小和 SHA256。

5. 明确确认：
   - 本轮 Journal 只从 NX UI 手动运行了一次；
   - 收集证据时没有重新运行 Journal；
   - 没有调用任何 NX/MCP 执行工具。

完成后停止，不要准备 _004。
