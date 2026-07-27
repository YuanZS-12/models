不要运行 Journal，也不要启动或操作 NX。

请补充 aerospace_linkage_003 的准备证据：

1. 查找并报告 linkage-review-v2.json 的绝对路径。
2. 使用 nx-cad 的 MCP review evidence 检查工具实际验证该文件或其证据目录。
3. 返回完整验证命令、stdout、stderr 和退出码；不能只写“已复用”。
4. 如果验证需要 raw Markdown、manifest 或其他配套文件，请报告它们的绝对路径。
5. 使用正确的 PowerShell 当前对象变量 $_ 重新输出 _003 文件清单：

$dst="D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_003"
Get-ChildItem $dst -Recurse | ForEach-Object {
    if ($_.PSIsContainer) {
        "(dir) $($_.FullName)"
    } else {
        $hash=(Get-FileHash $_.FullName -Algorithm SHA256).Hash
        "$($_.Length) $hash $($_.FullName)"
    }
}

完成后停止。不得运行 Journal，不得调用任何 NX 执行工具。
