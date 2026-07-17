不要下载、更新或安装 nx-cad，不要执行任何 git 命令。
使用当前已经由用户手动更新好的 nx-cad 文件。

保留 aerospace_bearing_002 到 aerospace_bearing_005，不得修改、覆盖或删除。
创建全新工作区：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_006

使用现有 bearing-review-v2.json 和 prepare-dc-mcp-journal 准备：
assets\runtime-probes\nx2606\aerospace\bearing_support_housing.py

输出到：
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_006\bearing_support_housing.py

然后运行 check-journal --strict-geometry，但不要运行 Journal，不要启动或关闭 NX。

返回：
1. prepare 命令、完整输出和退出码
2. check-journal 命令、完整输出和退出码
3. _006 全部源文件的路径、大小和 SHA256
4. _006/bearing_support_housing.py SHA256
5. _006/cadnx/builder.py SHA256
6. 确认 builder SHA256 为：
   a14f3cb6adecaec3b49fb4a9be53e6f620cb2f0bd144dda895e24fdd77027bc8
7. 确认 Journal SHA256 是否与 _005 的以下值完全一致：
   d0e04f746814afde865ff00243a093152268e1e6ec41fd7554ebb56273ec4675
8. 确认 _002 到 _005 未修改
9. 确认尚未运行 Journal
10. 确认没有执行 git、没有下载或更新 nx-cad
