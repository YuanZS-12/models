不要运行 aerospace_bearing_003。
完整保留 _001、_002、_003，不得修改、覆盖或删除。

请把已安装的 nx-cad 更新到：

8825dab

更新后分别计算以下两个文件的 SHA256：

1.
C:\Users\z004n36r\.agents\skills\nx-cad\cadnx\builder.py

2.
C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\cadnx\builder.py

两者都必须等于：

e8cb0db81c691d520d651e2634f20914d383808d59d6bd26c07347869c6c564c

如果任一不匹配，停止，不要创建 workspace。

确认匹配后，继续复用 bearing-review-v2.json，不要重新调用 dc_*。

准备全新 workspace：

py -3 scripts\prepare-dc-mcp-journal `
  assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py `
  "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_004\bearing_support_housing.py" `
  --review-evidence bearing-review-v2.json `
  --manual-user-run

执行严格检查：

py -3 scripts\check-journal `
  "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_004\bearing_support_housing.py" `
  --strict-geometry

完成后停止，不要运行 Journal。

返回：

1. canonical cadnx\builder.py SHA256
2. aerospace asset cadnx\builder.py SHA256
3. prepared _004\cadnx\builder.py SHA256
4. prepare stdout/stderr 和退出码
5. check-journal stdout/stderr 和退出码
6. _004 递归文件列表
7. prepared Journal SHA256
8. 确认 _001、_002、_003 均未修改、删除或再次运行
9. 确认未调用 dc_run_snippet 或 dc_run_journal
