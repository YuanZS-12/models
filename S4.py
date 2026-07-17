不要运行或修改 workspace\aerospace_bearing_001，完整保留它。

请更新已安装的 nx-cad 到提交：
f998a9a

由于当前机器没有 git，请使用原本安装/更新 skill 的机制刷新
C:\Users\z004n36r\.agents\skills\nx-cad。

更新后读取 canonical 文件：

C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py

必须确认其中同时存在：

run_base = os.path.splitext(os.path.abspath(__file__))[0]
b = NXBuilder(part_path=run_base, force_new_part=True)

不要重新执行 dc_* 查询。现有查询结果可以继续使用，但请创建新文件
bearing-review-v2.json，并从 tools 中删除未实际调用的
dc_semantic_search。不要覆盖旧 bearing-review.json。

然后创建全新的 workspace：

py -3 scripts\prepare-dc-mcp-journal `
  assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py `
  workspace\aerospace_bearing_002\bearing_support_housing.py `
  --review-evidence bearing-review-v2.json `
  --manual-user-run

再执行：

py -3 scripts\check-journal `
  workspace\aerospace_bearing_002\bearing_support_housing.py `
  --strict-geometry

完成后停止，不要运行 NX Journal。

返回：
1. canonical Journal 中上述两行的原文
2. bearing-review-v2.json 完整内容
3. prepare 命令 stdout/stderr 和退出码
4. check-journal stdout/stderr 和退出码
5. aerospace_bearing_002 完整文件列表
6. prepared Journal SHA256
7. 明确声明未修改/删除/运行 aerospace_bearing_001
8. 明确声明未调用 dc_run_snippet 或 dc_run_journal
