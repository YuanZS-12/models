Ran terminal command: $dst="D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005" ; Get-ChildItem $dst -Recurse -File | ForEach-Object { $h=(Get-FileHash $_.FullName -Algorithm SHA256).Hash ; "$($_.Length) $h $($_.FullName)" }

Ran terminal command: py -3 scripts\check-runtime-report "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005\curved_bellcrank.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_linkage_005\curved_bellcrank.step" 2>&1 ; $LASTEXITCODE

---

## `_005` 最终运行后证据报告

### 1. 产物文件大小和 SHA256

| 文件 | 大小 | SHA256 |
|---|---|---|
| curved_bellcrank.py | 13,335 | `93E4AABAA6FDC4599DF18B1A161C92ACC2E7E4A64A37ACAC6B72EB2BD8F263A8` |
| `_nx_aerospace_probe_support.py` | 2,410 | `18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9` |
| curved_bellcrank.nxreport.json | 1,277 | `9BA2B42F03ECC3BDF18839B78DD44741F7E01DAF6C26935EF3F519D5DEA0F76B` |
| `curved_bellcrank.prt` | 236,739 | `CE6CB981D6252D5B20F2651C1AED2710FFC6842DFD7815A7F42708624DDDD14B` |
| `curved_bellcrank.step` | 41,161 | `29E32B8011D2EC39358AADB211157F45205CB7E0EBB4043DC129CAB65804E74B` |

### 2. `check-runtime-report` 验证

**stdout：**
```
nx-cad runtime report check passed: ...\curved_bellcrank.nxreport.json
returned STEP contains geometry entities: ...\curved_bellcrank.step
```
**stderr：**（无）
**退出码：** `0` ✅

### 3. 合规性确认

| 检查项 | 结果 |
|---|---|
| `_005` Journal 从 NX UI 手动运行次数 | ✅ **仅 1 次** |
| 收集证据时重新运行 Journal | ❌ **未重新运行** |
| 调用任何 NX/MCP 执行工具 | ❌ **未调用** |
