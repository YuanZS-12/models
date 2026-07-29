Starting: *Create _002/api-review-raw directory* (1/9)

Created [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/aerospace_duct_002/api-review-raw)

Ran terminal command: Copy-Item "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_001\*.md" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\api-review-raw" -Force

Starting: *Create corrected api-review-manifest.json* (3/9)

Ran terminal command: Write-Output "=== Copied raw Markdown (SHA256 verification) ==="; Get-ChildItem "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\api-review-raw\*.md" | Sort-Object Name | ForEach-Object { $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash; $size = (Get-Item $_.FullName).Length; Write-Output "$($_.Name) | $size bytes | $hash" }; Write-Output "=== Canonical SHA256 (re-verify) ==="; Get-FileHash "C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\curved_aerospace_duct.py" -Algorithm SHA256 | Select-Object Hash; Get-FileHash "C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\_nx_aerospace_probe_support.py" -Algorithm SHA256 | Select-Object Hash

All SHA256 match. Now creating the corrected manifest and review files.

Created [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/aerospace_duct_002/api-review-raw/api-review-manifest.json)

Starting: *Create corrected duct-review-v2.json* (4/9)

Created [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/aerospace_duct_002/duct-review-v2.json)

Now run the validation.

Starting: *Run check-mcp-review-evidence validation* (5/9)

Ran terminal command: py -3 "c:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-mcp-review-evidence" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\api-review-raw\api-review-manifest.json" --review-evidence "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\duct-review-v2.json" 2>&1

**Validation passed.** Now preparing the workspace Journal.

Starting: *Prepare workspace Journal from canonical + duct-review-v2* (6/9)

Ran terminal command: py -3 "c:\Users\z004n36r\.agents\skills\nx-cad\scripts\prepare-dc-mcp-journal" "C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\curved_aerospace_duct.py" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py" --review-evidence "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\duct-review-v2.json" --manual-user-run 2>&1

Ran terminal command: Copy-Item "C:\Users\z004n36r\.agents\skills\nx-cad\assets\runtime-probes\nx2606\aerospace\_nx_aerospace_probe_support.py" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\_nx_aerospace_probe_support.py" -Force

Starting: *Run check-journal --strict-geometry* (8/9)

Ran terminal command: py -3 "c:\Users\z004n36r\.agents\skills\nx-cad\scripts\check-journal" "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py" --strict-geometry 2>&1

All checks passed. Now gathering final summary data.

Ran terminal command: Write-Output "=== Complete _002 workspace file listing ==="; Get-ChildItem "D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002" -Recurse | Where-Object { -not $_.PSIsContainer } | Sort-Object FullName | ForEach-Object { $rel = $_.FullName.Replace('D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002', ''); $hash = (Get-FileHash $_.FullName -Algorithm SHA256).Hash; Write-Output "$rel | $($_.Length) bytes | $hash" }

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/aerospace_duct_002/api-review-raw/api-review-manifest.json)

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/workspace/aerospace_duct_002/duct-review-v2.json)

Completed: *Run check-journal --strict-geometry* (8/9)

---

## 最终报告 — `aerospace_duct_002` 修正证据准备

---

### 1. _002 完整文件清单、大小和 SHA256

```
aerospace_duct_002/
├── api-review-raw/
│   ├── 001_dc_lookup_pattern.md                          (6,429  B)  1E272D2222AEBC20DDF4A7BD315FA013F877FD674335C081F99982358D00087F
│   ├── 002_StudioSplineBuilderEx.md                      (8,515  B)  B37E023A57C3096515859B91A88122E6934E223792096C57A45A721D5FBB48CC
│   ├── 003_GeometricConstraintData.md                    (3,449  B)  4A32BCB00C7D644B0F09EF598DF57D21A6DD2ED5E9BE0EFEAF3546315385DC86
│   ├── 004_Section.md                                    (32,560 B)  03A45797087D0DF5E61563C51FF53A4E846961E41060C9DF860B85F34D147778
│   ├── 005_ScRuleFactory.md                              (9,892  B)  909EC13C0E8105050F17822724F1975EB242A345F08BB874B465D04BF18701A7
│   ├── 006_ThroughCurvesBuilder.md                       (7,827  B)  1E803E0EB46E70C5F0271E499229B4BE421D8EC5C61B37C9ABE3CBD4ABED55FE
│   ├── 007_CreateStudioSplineBuilderEx_method.md         (428    B)  C6A842E3878DEECD8DEAB90E835544F9C30F44ED37CACBAEAAFDBDCB5F40F456
│   ├── 008_CreateThroughCurvesBuilder_method.md          (438    B)  B8040EC97017C797D2221DF44A9333B79692534B2B169340A8D14C0824947839
│   └── api-review-manifest.json                          (3,977  B)  8C018C0329D1B733D5B4E1C51635D4D921520D8F0954F49D19E37EA6C6CED1FD
├── curved_aerospace_duct.py                              (12,325 B)  F6E894B4500FEE9464063BCC50A3DAF10746BB71F1F66F1C033FDAACF047645A
├── duct-review-v2.json                                   (3,847  B)  F261B898E033E62599BA5D52A36E34C96A57C252F5F4644AEC431FAEE16B47E3
└── _nx_aerospace_probe_support.py                        (2,410  B)  18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9
```

---

### 2. api-review-manifest.json 完整原文

（同目录 `api-review-raw/` 下，raw_markdown_file 使用同目录相对文件名）

```json
{
  "schema_version": 2,
  "workspace": "aerospace_duct_002",
  "target_nx_version": "NX 2606",
  "probe": "aerospace_curved_duct",
  "calls": [
    {"sequence":1,"tool":"dc_lookup_pattern","exact_input":{"query":"NXOpen periodic studio spline annular sections ThroughCurves solid duct","limit":3},"raw_markdown_file":"001_dc_lookup_pattern.md","raw_markdown_sha256":"1E272D2222AEBC20DDF4A7BD315FA013F877FD674335C081F99982358D00087F","original_cache_path":null},
    {"sequence":2,"tool":"dc_get_api_info","exact_input":{"class_name":"NXOpen.Features.StudioSplineBuilderEx"},"raw_markdown_file":"002_StudioSplineBuilderEx.md","raw_markdown_sha256":"B37E023A57C3096515859B91A88122E6934E223792096C57A45A721D5FBB48CC","original_cache_path":"c:\\Users\\z004n36r\\...\\call_01_...\\content.txt"},
    {"sequence":3,"tool":"dc_get_api_info","exact_input":{"class_name":"NXOpen.Features.GeometricConstraintData"},"raw_markdown_file":"003_GeometricConstraintData.md","raw_markdown_sha256":"4A32BCB00C7D644B0F09EF598DF57D21A6DD2ED5E9BE0EFEAF3546315385DC86","original_cache_path":null},
    {"sequence":4,"tool":"dc_get_api_info","exact_input":{"class_name":"NXOpen.Section"},"raw_markdown_file":"004_Section.md","raw_markdown_sha256":"03A45797087D0DF5E61563C51FF53A4E846961E41060C9DF860B85F34D147778","original_cache_path":"c:\\Users\\z004n36r\\...\\call_03_...\\content.txt"},
    {"sequence":5,"tool":"dc_get_api_info","exact_input":{"class_name":"NXOpen.ScRuleFactory"},"raw_markdown_file":"005_ScRuleFactory.md","raw_markdown_sha256":"909EC13C0E8105050F17822724F1975EB242A345F08BB874B465D04BF18701A7","original_cache_path":"c:\\Users\\z004n36r\\...\\call_02_...\\content.txt"},
    {"sequence":6,"tool":"dc_get_api_info","exact_input":{"class_name":"NXOpen.Features.ThroughCurvesBuilder"},"raw_markdown_file":"006_ThroughCurvesBuilder.md","raw_markdown_sha256":"1E803E0EB46E70C5F0271E499229B4BE421D8EC5C61B37C9ABE3CBD4ABED55FE","original_cache_path":null},
    {"sequence":7,"tool":"dc_get_api_info","exact_input":{"info_type":"method","class_name":"NXOpen.Features.FeatureCollection","method_name":"CreateStudioSplineBuilderEx"},"raw_markdown_file":"007_CreateStudioSplineBuilderEx_method.md","raw_markdown_sha256":"C6A842E3878DEECD8DEAB90E835544F9C30F44ED37CACBAEAAFDBDCB5F40F456","original_cache_path":null},
    {"sequence":8,"tool":"dc_get_api_info","exact_input":{"info_type":"method","class_name":"NXOpen.Features.FeatureCollection","method_name":"CreateThroughCurvesBuilder"},"raw_markdown_file":"008_CreateThroughCurvesBuilder_method.md","raw_markdown_sha256":"B8040EC97017C797D2221DF44A9333B79692534B2B169340A8D14C0824947839","original_cache_path":null}
  ]
}
```

---

### 3. duct-review-v2.json 完整原文

**修正点：** 删除了错误的 `NXOpen.SectionAllowTypes.OnlyCurves`；facts 中 Section 枚举正确记录为 `NXOpen.Section.AllowTypes`（嵌套 enum）。

```json
{
  "schema_version": 2,
  "server": "dc_mcp_server",
  "runtime_mode": "mcp_review",
  "target_nx_version": "NX 2606",
  "probe": "aerospace_curved_duct",
  "tools": ["dc_lookup_pattern","dc_get_api_info"],
  "facts": [
    {"class":"NXOpen.Features.StudioSplineBuilderEx","key_properties":["Type (ThroughPoints/ByPoles)","IsPeriodic (bool, settable)","Degree (int, settable)","IsAssociative (bool, settable)","ConstraintManager (GeometricConstraintDataManager)","Curve (NXOpen.Spline, read-only after commit)"],"key_methods":["CommitFeature() -> Feature","Destroy()"]},
    {"class":"NXOpen.Features.GeometricConstraintData","key_properties":["Point (NXOpen.Point, settable) — minimum required data"],"notes":"Created via ConstraintManager.CreateGeometricConstraintData(); set Point to NXOpen.Point (smart object, not Point3d), then Append to manager"},
    {"class":"NXOpen.Section","key_properties":["ChainingTolerance (float, settable)","DistanceTolerance (float, settable)","AngleTolerance (float, settable)"],"key_methods":["SetAllowedEntityTypes(allowed_entity_types: Section.AllowTypes)","AddToSection(rules, seed, startConnector, endConnector, helpPoint, mode, bool)"],"key_enums":{"NXOpen.Section.AllowTypes":["Uninitialized","OnlyCurves","OnlyPoints","CurvesAndPoints"],"NXOpen.Section.Mode":["Create","Edit"]}},
    {"class":"NXOpen.ScRuleFactory","key_methods":["CreateRuleBaseCurveDumb(curves: List[IBaseCurve]) -> CurveDumbRule"],"notes":"Method name is CreateRuleBaseCurveDumb, NOT CreateRuleBaseCurve. Takes list of IBaseCurve."},
    {"class":"NXOpen.Features.ThroughCurvesBuilder","key_properties":["BodyPreference (Solid/Sheet, settable — direct enum, NOT PreferenceList)","ClosedInV (bool, settable)","Construction (Normal/SplinePoints/Simple, settable)","PatchType (Single/Multiple/MatchString, settable)","NormalToEndSections (bool, settable)","PreserveShape (bool, settable)","PositionTolerance (float, settable)","CurvatureTolerance (float, settable)","TangentTolerance (float, settable)","SectionsList (NXOpen.SectionList) — append sections here"],"key_methods":["CommitFeature() -> Feature","Destroy()"]},
    {"class":"NXOpen.Features.FeatureCollection","methods":{"CreateStudioSplineBuilderEx":"CreateStudioSplineBuilderEx(spline: NXOpen.NXObject) -> StudioSplineBuilderEx. Pass NXObject.Null for new spline.","CreateThroughCurvesBuilder":"CreateThroughCurvesBuilder(through_curves: Feature) -> ThroughCurvesBuilder. Pass Feature.Null for new feature."}}
  ],
  "confirmed_gotchas":["ScRuleFactory.CreateRuleBaseCurveDumb (not CreateRuleBaseCurve)","GeometricConstraintData.Point requires NXOpen.Point (smart object), NOT Point3d","Point3d constructor requires float arguments","StudioSplineBuilderEx default Degree is 5 — must set Degree=3","cm.Length is int property, not a method","ThroughCurvesBuilder.BodyPreference is direct enum — no PreferenceList","ThroughCurvesBuilder.SectionsList.Append() accepts single or list"]
}
```

---

### 4. evidence checker 输出

**命令：**
```
py -3 "...\check-mcp-review-evidence" "...\_002\api-review-raw\api-review-manifest.json" --review-evidence "...\_002\duct-review-v2.json"
```

**stdout：**
```
nx-cad MCP review evidence check passed: D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\api-review-raw\api-review-manifest.json
```

**stderr：** 无  
**退出码：** `0`

---

### 5. strict geometry 检查输出

**命令：**
```
py -3 "...\check-journal" "...\_002\curved_aerospace_duct.py" --strict-geometry
```

**stdout：**
```
nx-cad journal check passed: D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py
```

**stderr：** 无  
**退出码：** `0`

---

### 6. SHA256 汇总

| 文件 | SHA256 |
|---|---|
| Canonical `curved_aerospace_duct.py` (9,847 B) | `6EDCEDA85ADCA9BC5C69D670811DE65598B0397F3DE3F825C2EF97A49EC36162` |
| Workspace Journal `curved_aerospace_duct.py` (12,325 B) | `F6E894B4500FEE9464063BCC50A3DAF10746BB71F1F66F1C033FDAACF047645A` |
| Canonical `_nx_aerospace_probe_support.py` (2,410 B) | `18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9` |
| Copied helper `_nx_aerospace_probe_support.py` (2,410 B) | `18FE036F8F0C83AF2F7B0DF0CC9F795D1F184B5B8A60DA0C7F675B08A0BCE0F9` |

---

### 7. 确认

- ✅ **未运行 Journal**
- ✅ **未启动、关闭或操作 NX**
- ✅ **未覆盖 _001** — `aerospace_duct_001` 完整保留
- ✅ **未重新调用 MCP** — 8 个原始 Markdown 从 _001 复用，SHA256 一致
- ✅ **facts 仅来自已保存的原始 Markdown** — 修正了 `SectionAllowTypes` → `Section.AllowTypes` 枚举路径
- ✅ **预计输出路径：**
  - `...\_002\curved_aerospace_duct.prt`
  - `...\_002\curved_aerospace_duct.step`

---

**准备完成。等待用户授权从 NX UI 手动运行：**

```
D:\Workdir\iproot\nx2606.1700\test44\workspace\aerospace_duct_002\curved_aerospace_duct.py
```

Made changes.
