开始 aerospace HPC rear frame 的资格运行准备。

重要限制：

- 不要执行任何 git 命令。
- 不要下载、安装或更新 nx-cad。
- 使用用户已经手动放置的当前 nx-cad。
- 不要启动、关闭或自动操作 NX。
- 不要调用 dc_run_snippet、dc_run_journal 或 run_journal.exe。
- 当前只做 API 查询、review evidence 和 workspace 准备。
- 不要运行 Journal。
- 不要修改安装目录中的规范 probe。

一、验证安装源文件 SHA256

1. assets\runtime-probes\nx2606\aerospace\aerospace_hpc_rear_frame.py

期望：
0556cdf708259c4e96795078c9accd2bd2f924d99addc2b2dd300fe82c7c317b

2. assets\runtime-probes\nx2606\aerospace\_nx_aerospace_probe_support.py

期望：
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

3. assets\runtime-probes\nx2606\aerospace\cadnx\builder.py

期望：
a14f3cb6adecaec3b49fb4a9be53e6f620cb2f0bd144dda895e24fdd77027bc8

4. canonical cadnx\builder.py 必须与 aerospace asset builder 哈希相同。

二、检查当前可用的 dc_* 查询工具

只列出真实暴露的工具。允许使用：

- dc_lookup_pattern
- dc_search
- dc_semantic_search
- dc_get_api_info
- dc_list_namespace

不要把未实际调用的工具写进 review evidence。

三、复用已有 bearing review 中已经验证的 API facts

可以复用：

- Session、Parts.Work、NewDisplay
- BasePart.Save/SaveAs
- CylinderBuilder
- BooleanBuilder
- ChamferBuilder
- StepCreator AP242
- ExportFrom ExistingPart
- InputFile
- ObjectTypes.Solids

四、针对 frame 新增路径做查询型 API review

至少查询并确认以下 API 或等价完整 pattern：

- NXOpen.CurveCollection.CreateLine
- NXOpen.SectionCollection.CreateSection
- NXOpen.ScRuleFactory.CreateRuleCurveDumb
- NXOpen.Section.AddToSection
- NXOpen.Section.Mode.Create
- NXOpen.Features.FeatureCollection.CreateExtrudeBuilder
- NXOpen.Features.ExtrudeBuilder.Section
- NXOpen.DirectionCollection.CreateDirection
- NXOpen.SmartObject.UpdateOption.WithinModeling
- ExtrudeBuilder.Direction
- ExtrudeBuilder.Limits.StartExtend.Value.RightHandSide
- ExtrudeBuilder.Limits.EndExtend.Value.RightHandSide
- ExtrudeBuilder.CommitFeature()
- ExtrudeBuilder.Destroy()

先使用一个 discovery 工具，再对实际用到的对象执行 dc_get_api_info。
如果某个完全限定名不同，记录查询结果中的真实名称，不要猜测。

五、创建 review evidence

保存为当前 nx-cad 工作目录下的新文件：

frame-review-v2.json

要求：

- schema_version: 2
- server: dc_mcp_server
- runtime_mode: mcp_review
- tools: 只列本轮及被明确复用的真实调用工具
- facts: 包含 STEP 既有事实和 frame extrude/section 新事实
- target_nx_version: NX 2606
- probe: aerospace_hpc_rear_frame

不要覆盖 bearing-review-v2.json。

六、准备全新 workspace

使用：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_001

运行 prepare-dc-mcp-journal，将：

assets\runtime-probes\nx2606\aerospace\aerospace_hpc_rear_frame.py

准备为：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_frame_001\aerospace_hpc_rear_frame.py

参数：

--review-evidence frame-review-v2.json
--manual-user-run

然后运行：

check-journal --strict-geometry

不要运行 Journal。

七、返回完整准备证据

请返回：

1. 三个安装源文件和 canonical builder 的 SHA256
2. 实际暴露的 dc_* 工具列表
3. 实际执行的每个 dc_* 查询及完整结果
4. frame-review-v2.json 完整原文
5. prepare 命令、完整输出和退出码
6. check-journal 命令、完整输出和退出码
7. aerospace_frame_001 内全部文件的：
   - 绝对路径
   - 大小
   - SHA256
8. prepared Journal SHA256
9. workspace builder SHA256
10. 确认没有运行 Journal
11. 确认没有执行 git、没有下载或更新 nx-cad
12. 确认 bearing 工作区 _002 到 _007 未被修改
