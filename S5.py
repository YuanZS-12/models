用户已经通过 Siemens NX 2606 UI 手工运行：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_006\bearing_support_housing.py

不要再次运行 Journal，不要启动或关闭 NX，不要调用 dc_run_snippet、
dc_run_journal 或 run_journal.exe。不要执行 git，不要下载或更新 nx-cad。
不要修改、覆盖或删除任何 _005 或 _006 文件。

请只收集 _006 的运行证据：

1. 返回 NX UI 的完整输出和完整 traceback；没有 traceback时明确说明。
2. 列出 _006 下全部文件：
   - 绝对路径
   - 大小
   - 修改时间
   - SHA256
3. 返回 bearing_support_housing.nxreport.json 完整原文。
4. 返回 bearing_support_housing.log 完整原文。
5. 确认以下实际文件：
   - _cadnx_work\bearing_support_housing.prt
   - bearing_support_housing.step
   - bearing_support_housing.nxreport.json
6. 对 STEP 做只读统计：
   - 文件大小
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - BREP_WITH_VOIDS
   - CLOSED_SHELL
   - ADVANCED_FACE
   - EDGE_CURVE
   - STEP entity 总数
7. 重新计算并报告：
   - Journal SHA256
   - PRT SHA256
   - STEP SHA256
   - builder.py SHA256
8. 对比 _005 与 _006：
   - Journal SHA256 是否一致
   - PRT SHA256 是否一致
   - STEP SHA256 是否一致
   - 文件大小是否一致
9. 确认 _002 到 _005 未被本轮修改。
10. 明确记录：
    execution.actor=user
    execution.tool=nx_ui
    execution.transport=nx_ui
    agent_execution=false
11. 不要自行判定正式三连跑通过，只返回客观证据。
