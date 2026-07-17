用户已经通过 Siemens NX 2606 UI 手工运行：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_005\bearing_support_housing.py

不要再次运行 Journal，不要启动或关闭 NX，不要调用 dc_run_snippet、
dc_run_journal 或 run_journal.exe。不要修改、覆盖或删除任何工作区文件。

请只收集和报告本次 _005 的运行证据：

1. NX UI 显示的完整输出和完整 traceback；如果没有 traceback，明确说明。
2. 列出 aerospace_bearing_005 下全部文件：
   - 绝对路径
   - 文件大小
   - 最后修改时间
   - SHA256
3. 返回 bearing_support_housing.nxreport.json 的完整原文。
4. 返回 STEP translator 日志的完整原文。
5. 确认以下文件是否存在：
   - bearing_support_housing.prt
   - bearing_support_housing.step
   - bearing_support_housing.nxreport.json
6. 对 STEP 做只读文本统计并返回：
   - 文件总大小
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - BREP_WITH_VOIDS
   - CLOSED_SHELL
   - ADVANCED_FACE
   - EDGE_CURVE
   - 总实体记录数（以 # 开头的 STEP entity）
7. 不要把 STEP 标记为通过，只报告客观统计。
8. 确认 _002、_003、_004 未被本轮修改。
9. 明确记录执行来源为 user:nx_ui，agent_execution=false。
