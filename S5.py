使用当前已经安装好的 nx-cad skill，准备 curved bellcrank 的下一轮资格运行。

重要限制：
1. 不要执行任何 Git、下载、安装或更新命令。
2. 不要启动、关闭或自动控制 Siemens NX。
3. 不要调用 dc_run_snippet、dc_run_journal 或任何 Journal 执行工具。
4. 不要运行 Journal；最终由用户从 NX UI 手动运行。
5. 保留 aerospace_linkage_001 和 aerospace_linkage_002，不得覆盖任何旧文件。

目标：
创建全新的工作目录：

D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_003

从当前已安装 nx-cad skill 的 canonical runtime probe 复制：

assets\runtime-probes\nx2606\aerospace\curved_bellcrank.py
→ aerospace_linkage_003\curved_bellcrank.py

assets\runtime-probes\nx2606\aerospace\_nx_aerospace_probe_support.py
→ aerospace_linkage_003\_nx_aerospace_probe_support.py

复制后必须验证：

curved_bellcrank.py SHA256：
93e4aabaa6fdc4599df18b1a161c92acc2e7e4a64a37acac6b72eb2bd8f263a8

_nx_aerospace_probe_support.py SHA256：
18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

API review：
- 复用上一轮已经保存的 linkage-review-v2.json 及其原始 MCP review 证据。
- 本轮只修改了已经由 bearing 验证过的 STEP exporter 配置，没有修改几何 API。
- 不需要重新进行 MCP 查询。
- 不得把 MCP review 描述成 NX 运行证据。

静态检查：
使用当前已安装 skill 的 check-journal，对新目录中的 curved_bellcrank.py 执行 --strict-geometry 检查。

检查完成后停止，不要运行 Journal。

请反馈：
1. 新工作目录完整路径；
2. 两个复制文件的完整路径和 SHA256；
3. linkage-review-v2.json 的路径及其验证结果；
4. strict-geometry 检查的完整输出和退出码；
5. 新目录文件清单；
6. 明确确认没有启动 NX、没有运行 Journal、没有覆盖 _001/_002。
