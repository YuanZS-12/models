用户已经通过 Siemens NX 2606 UI 手工运行：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_007\bearing_support_housing.py

不要再次运行 Journal，不要启动或关闭 NX，不要调用 dc_run_snippet、
dc_run_journal 或 run_journal.exe。不要执行 git，不要下载或更新 nx-cad。
不要修改、覆盖或删除 _005、_006 或 _007 的任何文件。

请只收集 _007 的客观运行证据：

1. 返回 NX UI 完整输出和完整 traceback；没有 traceback时明确说明。
2. 列出 _007 下全部文件：
   - 绝对路径
   - 大小
   - 修改时间
   - SHA256
3. 返回 bearing_support_housing.nxreport.json 完整原文。
4. 返回 bearing_support_housing.log 完整原文。
5. 确认以下文件存在：
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
7. 返回以下 SHA256：
   - Journal
   - builder.py
   - helper
   - PRT
   - STEP
8. 对比 _005、_006、_007：
   - Journal SHA256
   - PRT 大小和 SHA256
   - STEP 大小和 SHA256
   - STEP entity、face、edge 计数
9. 如果 STEP 原始哈希不同，只报告差异，不自行判断几何失败。
10. 确认 _002 到 _006 未被本轮修改。
11. 明确记录：
    execution.actor=user
    execution.tool=nx_ui
    execution.transport=nx_ui
    agent_execution=false
12. 不要自行宣布三连跑或 fixture verified；最终判定由独立后处理完成。
