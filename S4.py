继续 NX 2606 bearing support qualification，但现在只准备下一轮工作区，不要运行 Journal。

1. 更新/重新安装 nx-cad，必须来自：
   https://github.com/YuanZS-12/my-skillis
   branch: main
   commit: a529dcb50b880aebfe51f971954f0419687c9977

2. 验证以下 SHA256：
   canonical cadnx/builder.py:
   a14f3cb6adecaec3b49fb4a9be53e6f620cb2f0bd144dda895e24fdd77027bc8

   aerospace asset cadnx/builder.py:
   a14f3cb6adecaec3b49fb4a9be53e6f620cb2f0bd144dda895e24fdd77027bc8

   bearing_support_housing.py:
   200ff91707316e49f5d9ad9e63823b90d4abe59fe3e7e5f19bca1eb68cab4295

   _nx_aerospace_probe_support.py:
   18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9

3. 保留 aerospace_bearing_001 到 aerospace_bearing_004，不得覆盖、删除或复用。

4. 使用现有 bearing-review-v2.json。当前修复没有引入新的 NXOpen API，因此不需要重复 dc_* 查询。

5. 准备全新外部工作区：
   D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_bearing_005

6. 使用 prepare-dc-mcp-journal 准备：
   bearing_support_housing.py
   以及完整 sibling cadnx/ 和 _nx_aerospace_probe_support.py。

7. 准备完成后不要启动或关闭 NX，不要调用 dc_run_snippet、dc_run_journal、run_journal.exe，也不要自动运行 Journal。

8. 在授权手工运行前，返回：
   - 实际安装的 git commit
   - prepare 命令和完整输出
   - check-journal --strict-geometry 的完整输出
   - _005 中全部文件的绝对路径、大小和 SHA256
   - canonical builder 与 _005/cadnx/builder.py 的哈希比较
   - 确认 _001 到 _004 均未被修改
   - 确认 Journal 尚未运行
