不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具，不要修改或覆盖任何文件。

请收集 aerospace_blade_003 的最终运行后证据。

1. 报告以下文件的完整绝对路径、大小和 SHA256：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py
   - lofted_airfoil_blade.nxreport.json
   - lofted_airfoil_blade.prt
   - lofted_airfoil_blade.step

2. 运行：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.step"

报告完整命令、stdout、stderr 和退出码。

3. 检查并报告 STEP 是否包含：
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - CLOSED_SHELL
   - ADVANCED_FACE
   - B_SPLINE_SURFACE_WITH_KNOTS

4. 确认：
   - `_003` Journal 仅由用户从 NX UI 手动运行一次
   - 收集证据时没有重新运行
   - 没有调用任何 NX/MCP 执行工具
   - Journal SHA256 为 `ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902`

完成后停止。
