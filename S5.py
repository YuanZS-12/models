Searching codebase for "不要运行 Journal，不要启动、关闭或操作 NX，不要调用任何 NX/MCP 执行工具，不要修改或覆盖任何文件。

请收集 aerospace_blade_003 的最终运行后证据。

1. 报告以下文件的完整绝对路径、大小和 SHA256：
   - lofted_airfoil_blade.py
   - _nx_aerospace_probe_support.py
   - lofted_airfoil_blade.nxreport.json
   - lofted_airfoil_blade.prt
   - lofted_airfoil_blade.step

2. 运行：

py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.step"

报告完整命令、stdout、stderr 和退出码。

3. 检查并报告 STEP 是否包含：
   - ADVANCED_BREP_SHAPE_REPRESENTATION
   - MANIFOLD_SOLID_BREP
   - CLOSED_SHELL
   - ADVANCED_FACE
   - B_SPLINE_SURFACE_WITH_KNOTS

4. 确认：
   - `_003` Journal 仅由用户从 NX UI 手动运行一次
   - 收集证据时没有重新运行
   - 没有调用任何 NX/MCP 执行工具
   - Journal SHA256 为 `ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902`

完成后停止。"

Ran terminal command: Write-Output "=== _003 runtime artifacts ==="; @("lofted_airfoil_blade.py","_nx_aerospace_probe_support.py","lofted_airfoil_blade.nxreport.json","lofted_airfoil_blade.prt","lofted_airfoil_blade.step") | ForEach-Object { $p = "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\$_"; if (Test-Path $p) { $f=Get-Item $p; $h=(Get-FileHash $p -Algorithm SHA256).Hash; Write-Output "EXISTS | $p | $($f.Length) bytes | $h" } else { Write-Output "MISSING | $p" } }

Ran terminal command: py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.nxreport.json" --expected-bodies 1 --step "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.step" 2>&1; $LASTEXITCODE

Ran terminal command: Write-Output "=== _003 STEP geometry entities ==="; Select-String -Pattern "ADVANCED_BREP_SHAPE_REPRESENTATION|MANIFOLD_SOLID_BREP|CLOSED_SHELL|ADVANCED_FACE|B_SPLINE_SURFACE_WITH_KNOTS" -Path "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.step" | ForEach-Object { [regex]::Matches($_.Line, '(ADVANCED_BREP_SHAPE_REPRESENTATION|MANIFOLD_SOLID_BREP|CLOSED_SHELL|ADVANCED_FACE|B_SPLINE_SURFACE_WITH_KNOTS)').Value } | Sort-Object -Unique

---

## aerospace_blade_003 — 最终运行后证据

### 1. 文件绝对路径、大小和 SHA256

| 文件 | 绝对路径 | 大小 (B) | SHA256 |
|---|---|---|---|
| Journal | `D:\...\aerospace_blade_003\lofted_airfoil_blade.py` | 11,214 | `ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902` |
| Helper | `D:\...\aerospace_blade_003\_nx_aerospace_probe_support.py` | 2,410 | `18fe036f8f0c83af2f7b0df0cc9f795d1f184b5b8a60da0c7f675b08a0bce0f9` |
| nxreport | `D:\...\aerospace_blade_003\lofted_airfoil_blade.nxreport.json` | 1,178 | `b55aaae96a793c0c04b47b285391e38e20e0afa95d6597ce806c0ac52a1dd742` |
| PRT | `D:\...\aerospace_blade_003\lofted_airfoil_blade.prt` | 133,230 | `8a609b5791930b5676541ff07f027e462804aa39cd4bac3dba2378ac5aca54a9` |
| STEP | `D:\...\aerospace_blade_003\lofted_airfoil_blade.step` | 18,692 | `48feeb708050bb13c6ee68f62ead1f70254fcb305749e6b783c295c4ce92ccfd` |

### 2. check-runtime-report

**命令：**
```
py -3 "C:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-runtime-report"
  "D:\...\aerospace_blade_003\lofted_airfoil_blade.nxreport.json"
  --expected-bodies 1
  --step "D:\...\aerospace_blade_003\lofted_airfoil_blade.step"
```

**stdout：**
```
nx-cad runtime report check passed: D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.nxreport.json
returned STEP contains geometry entities: D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_blade_003\lofted_airfoil_blade.step
```

**stderr：** 无  
**退出码：** `0`

### 3. STEP 几何实体

| 实体 | 存在 |
|---|---|
| `ADVANCED_BREP_SHAPE_REPRESENTATION` | ✅ |
| `MANIFOLD_SOLID_BREP` | ✅ |
| `CLOSED_SHELL` | ✅ |
| `ADVANCED_FACE` | ✅ |
| `B_SPLINE_SURFACE_WITH_KNOTS` | ✅ |

### 4. 确认

- ✅ **`_003` Journal 仅由用户从 NX UI 手动运行一次**
- ✅ **收集证据时没有重新运行**
- ✅ **没有调用任何 NX/MCP 执行工具**
- ✅ **Journal SHA256：** `ffad37e3cefca9df11f14d6a9af1108bdaa8a7321b8992d56e4a1b5b08057902`
