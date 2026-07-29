不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。不要执行 Git、下载、安装或更新操作。

请验证 aerospace_blade_002 的运行证据，并准备第三次资格运行目录 aerospace_blade_003。

1. 报告 `_002` 以下文件的完整绝对路径、大小和 SHA256：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py
   - lofted_airfoil_blade.nxreport.json
   - lofted_airfoil_blade.prt
   - lofted_airfoil_blade.step

2. 运行：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_002\lofted_airfoil_blade.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_002\lofted_airfoil_blade.step"

报告完整 stdout、stderr 和退出码。

3. 确认 STEP 包含：
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - CLOSED_SHELL
   - B_SPLINE_SURFACE_WITH_KNOTS

4. 确认 `_002` Journal 仅由用户从 NX UI 手动运行一次，收集证据时没有重新运行。

5. 创建全新目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003

如果目录或目标文件已经存在，立即停止，不得覆盖。

6. 从 `_002` 复制以下冻结文件到 `_003`，不得使用 `-Force`：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py

不得修改 Journal、重新调用 MCP 或重新运行 prepare-dc-mcp-journal。

7. 验证 `_003` Journal SHA256：

ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902

Helper SHA256：

18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

8. 对 `_003` Journal 运行 check-journal --strict-geometry，报告完整命令、stdout、stderr和退出码。

9. 输出 `_003` 完整文件清单，包括绝对路径、大小和 SHA256。

完成后停止。不得运行 `_003` Journal，等待用户授权。
