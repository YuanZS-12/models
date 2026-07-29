不要运行 Journal，不要启动或操作 NX。

只修正现有 _002 的：

api-review-raw\api-review-manifest.json

把 sequence 2、4、5 中包含字面量 `...` 的 original_cache_path 改为 null。

不要修改：
- 8 个原始 Markdown；
- duct-review-v2.json；
- curved_aerospace_duct.py；
- helper；
- 任何 SHA256 字段；
- _001。

重新执行 check-mcp-review-evidence。

返回：
1. 修正后的 api-review-manifest.json 完整原文；
2. manifest 新的大小和 SHA256；
3. evidence checker 的完整 stdout、stderr 和退出码；
4. 再次确认 Journal SHA256 仍为：
   f6e894b4500fee9464063bcc50a3daf10746bb71f1f66f1c033fdaacf047645a
5. 确认未运行 Journal、未操作 NX。

无需重新运行 prepare-dc-mcp-journal，也无需创建 _003。
完成后停止。
