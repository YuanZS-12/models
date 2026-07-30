不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。不要执行 Git、下载、安装或更新操作。

准备 Frame redesign 第 2 次运行：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002

必须保留 `_001`，不得修改、覆盖或重新运行它。如果 `_002` 已存在，立即停止。

规范源：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\aerospace_hpc_rear_frame.py

期望 canonical SHA256：

a2e78b0637a7083c6e09e8c2116758f494b9ec49cfb829e8496a50365baa32cf

请完成：

1. 验证 canonical SHA256。若不匹配立即停止。

2. 本轮没有新增或改变底层 NXOpen API，只改变几何方向、参数和运行诊断，因此不要重新调用 MCP。将 `_001` 的以下不可变 API review 证据复制到 `_002`：
   - api-review-raw 完整目录
   - frame-redesign-review-v1.json

不得修改这些证据文件。报告复制前后每个文件的 SHA256，并运行 check-mcp-review-evidence 验证 `_002` 中的副本。

3. 使用 prepare-dc-mcp-journal --manual-user-run 准备：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\aerospace_hpc_rear_frame.py

review evidence 使用：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_002\frame-redesign-review-v1.json

4. 确保 `_002` 包含：
   - aerospace_hpc_rear_frame.py
   - _nx_aerospace_probe_support.py
   - cadnx\__init__.py
   - cadnx\builder.py
   - frame-redesign-review-v1.json
   - api-review-raw 完整证据

5. 验证准备后 Journal 包含：
   - `accessory_angle_degrees = 11.25`
   - `accessory_axial_pitch_tangential = 20.0`
   - `accessory_hole_radius`
   - accessory hole 的 `axis=x_axis`
   - `require_single_body`
   - `require_single_body("accessory_pad_and_axial_holes")`
   - `borescope_x = 0.0`

并确认不存在：
   - `accessory_hole_tangential_pitch`
   - 使用 `casing_od` 作为 accessory hole cutter depth
   - 旧的 accessory radial cutter 调用

6. 对准备后的 Journal 运行 check-journal --strict-geometry，报告完整命令、stdout、stderr和退出码。

7. 报告 canonical、prepared Journal、helper 和 cadnx 文件的完整路径、大小及 SHA256。

8. 输出 `_002` 完整文件清单，包含绝对路径、大小和 SHA256。

完成后停止，不得运行 `_002` Journal，等待用户授权。
