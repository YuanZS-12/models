不要运行 Journal，不要启动、关闭或操作 NX，不要修改、移动、复制或另存任何文件。不得创建 `_004`。

请只读核验 aerospace_frame_redesign_003 的运行产物。

1. 递归列出以下目录内所有文件，报告完整绝对路径、大小、最后修改时间和 SHA256：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003

特别检查：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\_cadnx_work

2. 在以下范围递归搜索：

D:\Workdir\iproot\nx2606.1700\test44\workspace

查找名称匹配：

aerospace_hpc_rear_frame*.prt

对找到的每个 PRT 报告：

- 完整绝对路径
- 大小
- 创建时间
- 最后修改时间
- SHA256

重点标记时间接近 STEP 时间 `2026-07-30 10:26:37 +08:00` 的文件。

3. 原样输出：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\aerospace_hpc_rear_frame.nxreport.json

4. 运行 check-runtime-report：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\aerospace_hpc_rear_frame.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_003\aerospace_hpc_rear_frame.step"

报告完整 stdout、stderr 和退出码。

5. 报告 Journal、report、STEP 的大小和 SHA256，并确认 STEP 是否包含：

- ADVANCED_BREP_SHAPE_REPRESENTATION
- MANIFOLD_SOLID_BREP
- CLOSED_SHELL
- ADVANCED_FACE

6. 确认 Journal 只从 NX UI 手动运行一次，收集证据时未重新运行。

完成后停止。不得重新运行、不得另存 PRT、不得修改报告。
