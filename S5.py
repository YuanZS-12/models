不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具。不要执行 Git、下载、安装或更新操作。

这是 Frame redesign 序列第三次也是最后一次允许的失败尝试。准备：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003

必须保留 `_001` 和 `_002`。如果 `_003` 已存在，立即停止，不得覆盖。

规范源：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\aerospace_hpc_rear_frame.py

期望 canonical SHA256：

47bcdae26788bc9dac6587293e963388b12e429704c59ce5df40695e5beea77a

请完成：

1. 验证 canonical SHA256，不匹配则立即停止。

2. 本轮没有新增底层 NXOpen API。不要重新调用 MCP。将 `_002` 中以下证据原样复制到 `_003`：
   - api-review-raw 完整目录
   - frame-redesign-review-v1.json

逐文件验证复制前后 SHA256 相同，并在 `_003` 上运行 check-mcp-review-evidence。

3. 使用 prepare-dc-mcp-journal --manual-user-run 准备：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\aerospace_hpc_rear_frame.py

review evidence 使用：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\frame-redesign-review-v1.json

4. 确保完整复制 helper 和 cadnx 依赖。

5. 验证 Prepared Journal 包含：
   - `def make_annulus`
   - `def require_body_count`
   - `require_body_count("outer_frame_and_hub_before_bridge", 2)`
   - `hub = make_annulus`
   - `hub = b.boolean_unite(hub, inner_flange)`
   - bearing seats 对 `hub` 执行 subtract
   - `hub_bridge = b.boolean_unite(hub, strut)`
   - `frame = b.boolean_unite(frame, hub_bridge)`
   - `require_single_body("first_primary_strut_bridge")`
   - 附件孔仍使用 `axis=x_axis`
   - `borescope_x = 0.0`

确认不存在旧的 `unite_annulus(frame, hub...)` 建模顺序。

6. 对 Prepared Journal 运行 check-journal --strict-geometry，报告完整命令、stdout、stderr 和退出码。

7. 报告 canonical、Prepared Journal、helper、cadnx 文件的完整路径、大小和 SHA256。

8. 输出 `_003` 完整文件清单。

完成后停止。不得运行 `_003` Journal，等待用户授权。
