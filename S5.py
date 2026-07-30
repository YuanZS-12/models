不要运行 Journal，不要启动、关闭或操作 NX，不要调用 dc_run_snippet、dc_run_journal、run_journal.exe 或其他 NX 执行工具。不要执行 Git、下载、安装或更新操作。

这是 materially different 的 Frame 新设计资格序列。不得创建 aerospace_frame_006，不得修改、覆盖或重新运行旧的 aerospace_frame_003、_004、_005。

创建全新工作目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001

规范源文件：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\aerospace_hpc_rear_frame.py

期望规范源 SHA256：

a3d1a7e9ebf79ceac82991b3088e14394e1c9fc322aca425fc0d3c3911e039da

请完成以下准备工作：

1. 首先验证规范源 SHA256。若不匹配，停止并报告，不得继续准备。

2. 检查可用的 dc_* 工具。只允许调用：
   - dc_lookup_pattern
   - dc_search
   - dc_semantic_search
   - dc_get_api_info
   - dc_list_namespace

3. 为新版局部径向建模执行持久化 MCP API review。至少审查：
   - CylinderBuilder 的 Origin、Direction、Diameter、Height 和 CommitFeature
   - BooleanBuilder Subtract 的 Target、Tool 和 CommitFeature
   - BlockFeatureBuilder 或 oriented-box 所使用的底层 NXOpen builder
   - FeatureCollection.CreateCylinderBuilder
   - FeatureCollection.CreateBooleanBuilder
   - STEP ExistingPart/AP242 recipe 可复用既有已验证证据，但必须记录真实来源

4. 每次完成的 MCP 查询立即保存为独立 UTF-8 Markdown，放入：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001\api-review-raw

5. 创建：
   - api-review-raw\api-review-manifest.json
   - frame-redesign-review-v1.json

Manifest 每条记录必须包含 sequence、tool、exact_input、raw_markdown_file、raw_markdown_sha256，以及存在时的 original_cache_path。所有路径必须为完整绝对路径，不得在文件中使用 `...`。

6. 使用 check-mcp-review-evidence 实际验证证据，返回完整命令、stdout、stderr 和退出码。

7. 使用 prepare-dc-mcp-journal --manual-user-run，从规范源准备：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001\aerospace_hpc_rear_frame.py

使用：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_redesign_001\frame-redesign-review-v1.json

不得覆盖文件。Wrapper probe 必须带完整 sibling `cadnx` 和 `_nx_aerospace_probe_support.py`。

8. 报告：
   - canonical probe 大小与 SHA256
   - prepared Journal 大小与 SHA256
   - helper 大小与 SHA256
   - cadnx\__init__.py 和 cadnx\builder.py 的大小与 SHA256

9. 对准备后的 Journal 运行 check-journal --strict-geometry，报告完整命令、stdout、stderr 和退出码。

10. 检查准备后 Journal，确认：
   - `accessory_angle_degrees = 11.25`
   - `accessory_pad_x = 0.0`
   - 存在 `local_radial_cutter`
   - 不存在 `accessory_hole_tangential_pitch`
   - 不存在以 `casing_od` 作为 accessory hole cutter depth 的代码
   - borescope_x 仍为 0.0

11. 输出新目录完整文件清单，包括绝对路径、大小和 SHA256。

完成后停止。不得运行 Journal，等待用户授权从 NX 2606 UI 手动运行。
