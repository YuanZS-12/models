Ran terminal command: Write-Output "=== _005 runtime artifacts ==="; @("curved_aerospace_duct.py","_nx_aerospace_probe_support.py","curved_aerospace_duct.nxreport.json","curved_aerospace_duct.prt","curved_aerospace_duct.step") | ForEach-Object { $p = "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005\$_"; if (Test-Path $p) { $f=Get-Item $p; $h=(Get-FileHash $p -Algorithm SHA256).Hash; Write-Output "EXISTS | $_ | $($f.Length) bytes | $h" } else { Write-Output "MISSING | $_" } }

Ran terminal command: py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005\curved_aerospace_duct.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_005\curved_aerospace_duct.step" 2>&1; $LASTEXITCODE

---

## aerospace_duct_005 — 最终证据

### 1. 文件大小与 SHA256

| 文件 | 大小 (bytes) | SHA256 |
|---|---|---|
| `curved_aerospace_duct.py` | 14,943 | `bc9ecb80716368984b2b46e82be78def16e09bca7d98037055bd2459891fc192` |
| `_nx_aerospace_probe_support.py` | 2,410 | `18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9` |
| curved_aerospace_duct.nxreport.json | 1,241 | `99a2bab283abae5e20e9bf45253a9e080ba807b1aa4d6da393dff480f6218ef1` |
| `curved_aerospace_duct.prt` | 243,605 | `5cab135f689b20aa0905c415c6bf00d2cbbb5fc22ef03b248df0038a2b1633e4` |
| `curved_aerospace_duct.step` | 25,770 | `934bd841f4c960b9e3444cf073e613f335b3241d42727549f68b6284b21ee901` |

### 2. check-runtime-report

**stdout：**
```
nx-cad runtime report check passed: ...\_005\curved_aerospace_duct.nxreport.json
returned STEP contains geometry entities: ...\_005\curved_aerospace_duct.step
```

**stderr：** 无  
**退出码：** `0`

### 3. 明确确认

- ✅ **_005 Journal 只从 NX UI 手动运行了一次**
- ✅ **收集证据时没有重新运行**
- ✅ **没有调用任何 NX/MCP 执行工具**
- ✅ **不需要 snapshot、CAD Viewer 或 post-nx-review**
