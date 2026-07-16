使用最新版 nx-cad skill，准备 probe 01 的用户手动 NX 运行副本。

禁止调用 dc_run_snippet、dc_run_journal、run_journal.exe，禁止启动或关闭 NX。
只允许进行 API review、文件准备和静态检查。

canonical probe：
C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\01_create_part.py

复用上一轮真实查询证据：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-01.json

新工作目录：
C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003

执行：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\prepare-dc-mcp-journal C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\01_create_part.py C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\01_create_part.py --review-evidence C:\Users\z004n36r\.agents\nx_mcp_runs\integration_002\review-evidence-01.json --manual-user-run

然后执行：

py -3 C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-journal C:\Users\z004n36r\.agents\nx_mcp_runs\integration_003\01_create_part.py --strict-geometry

确认生成的 Journal 满足：
- mode=manual_nx
- manual_user_run_required=true
- agent_execution=false
- 不包含 mcp_execute
- check-journal 通过

完成后只返回要由用户手动运行的 Journal 路径，不要尝试执行 NX。
