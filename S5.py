不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。不要执行 Git、下载、安装或更新操作。

请完成 aerospace_blade_001 运行后验证，并准备第二次资格运行目录 aerospace_blade_002。

第一部分：验证 `_001`

1. 报告以下文件的绝对路径、大小和 SHA256：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py
   - lofted_airfoil_blade.nxreport.json
   - lofted_airfoil_blade.prt
   - lofted_airfoil_blade.step

2. 运行：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\lofted_airfoil_blade.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_001\lofted_airfoil_blade.step"

分别报告完整 stdout、stderr 和退出码。

3. 确认 STEP 中存在真实几何实体，包括：
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - CLOSED_SHELL
   - B_SPLINE_SURFACE_WITH_KNOTS

4. 确认 `_001` Journal 仅由用户从 NX UI 手动运行一次，收集证据时没有重新运行。

第二部分：准备 `_002`

5. 创建全新目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_002

如果该目录或目标文件已经存在，立即停止，不得覆盖。

6. 从 `_001` 复制以下冻结文件到 `_002`，不要使用 `-Force`：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py

不得重新调用 MCP，不得重新运行 prepare-dc-mcp-journal，不得修改 Journal。

7. 验证 `_002` 中的 Journal SHA256 必须为：

ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902

Helper SHA256 必须为：

18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

8. 对 `_002` Journal 运行 check-journal --strict-geometry，分别报告完整命令、stdout、stderr 和退出码。

9. 输出 `_002` 的完整文件清单，包括绝对路径、大小和 SHA256。

完成后停止。不得运行 `_002` Journal，等待用户授权。
