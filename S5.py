Searched for text `dc_run_journal|dc_run_snippet|dc_search|dc_semantic_search|dc_get_api_info|dc_list_namespace|dc_lookup_pattern` (`**/wntx64\kits\dc_mcp_server\dc_mcp_server.py`), 20 results

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/wntx64/kits/dc_mcp_server/dc_mcp_server.py#490-490), lines 490 to 800

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/wntx64/kits/dc_mcp_server/dc_mcp_server.py#800-800), lines 800 to 900

Searched for text `def _handle_` (`**/wntx64\kits\dc_mcp_server\dc_mcp_server.py`), 6 results

Read [](file:///d%3A/Workdir/iproot/nx2606.1700/test44/wntx64/kits/dc_mcp_server/dc_mcp_server.py#907-907), lines 907 to 970

以下是 `dc_mcp_server` 中七个工具的完整参数与返回结构总结：

---

## 1. `dc_lookup_pattern` — 最佳实践查询（STEP 1，首选入口）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `query` | string | ✅ | 自然语言描述要做的操作，如 `"create new part"`, `"edge blend all edges"`, `"color palette full list"` |
| `limit` | integer | ❌ | 返回结果条数，默认 3，最大 5 |

**返回结构：**
```
# Designcenter journal Patterns matching: `<query>`
## 1. 标题 (score: N)
**Solution:** 解决方案文字描述
```python
代码示例
```
## 2. ...
```
格式为 Markdown 文本，每个 pattern 包含标题、得分、解决方案描述和 Python 代码示例。

---

## 2. `dc_search` — 名称搜索（STEP 2，已知名称时使用）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `query` | string | ✅ | 搜索词（类名、方法名、关键词），如 `"ExtrudeBuilder"`, `"CommitFeature"` |
| `search_type` | string | ❌ | 结果类型限定：`"classes"` / `"methods"` / `"all"`（默认） |
| `limit` | integer | ❌ | 最大结果数，默认 15 |
| `category` | string | ❌ | 分类过滤：General, Features, Builders, Collections, Manufacturing 等 |
| `class_filter` | string | ❌ | 按所属类名过滤方法 |
| `return_type_filter` | string | ❌ | 按返回类型过滤方法 |

**返回结构：**
```
# Search Results for '<query>'
## Classes (N)
1. **ClassName** (Category)
   Full name: `NXOpen.xxx.ClassName`
   Module: `NXOpen.xxx`
   Description: 描述文字
   Methods: N, Properties: N
   Sample members: member1, member2, ...

## Methods (N)
1. **MethodName** in `ClassName`
   Signature: `MethodName(self, ...) -> ReturnType`
   Category: xxx
   Description: 描述文字
   Usage: obj.MethodName()
```

---

## 3. `dc_semantic_search` — 语义搜索（STEP 2，未知名称时使用）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `query` | string | ✅ | 自然语言描述，如 `"extrude a sketch profile"`, `"chamfer an edge"` |
| `limit` | integer | ❌ | 最大结果数，默认 15 |
| `use_vector_embeddings` | boolean | ❌ | 是否使用向量嵌入相似度，默认 true（不可用时降级为关键词） |

**返回结构：**
```
# Semantic Search Results for: '<query>'
Found N relevant items

## Classes (N)
- **ClassName** (`NXOpen.xxx.ClassName`)
  Relevance: 0.xx
  Description: 描述文字
  Usage: 用法说明
```
与 `dc_search` 类似但附带相关性评分。

---

## 4. `dc_get_api_info` — 类/方法签名查询（STEP 3）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `info_type` | string | ❌ | `"class"`（默认）/ `"method"` |
| `class_name` | string | ✅ | 完整类名，如 `"NXOpen.Part"` |
| `method_name` | string | ❌ | 方法名，`info_type="method"` 时必需 |
| `method_filter` | string | ❌ | 按前缀过滤方法，如 `"Create"` |
| `property_filter` | string | ❌ | 按前缀过滤属性，如 `"Thread"` |

**返回结构（`info_type="class"`）：**
```
# ClassName
**Full name:** `NXOpen.xxx.ClassName`
**Module:** `NXOpen.xxx`
**Category:** xxx
**Description:** 描述文字
**Inherits from:** 父类链

## Properties (N)
- `PropertyName(self) -> Type` *(settable)*
  说明文字

## Methods (N)
- `MethodName(self, ...) -> ReturnType`
  说明文字

## Nested Types (N)
### `NXOpen.xxx.ClassName.EnumName` *(enum)*
  Members Include: |Member1| desc |Member2| desc
  **Members:** `Member1`, `Member2`
```

---

## 5. `dc_list_namespace` — 命名空间浏览（STEP 2，领域探索）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `namespace` | string | ❌ | 命名空间，如 `"NXOpen.Features"`；省略则返回所有命名空间概览 |
| `limit` | integer | ❌ | 最大返回类数，默认 50 |
| `include_submodules` | boolean | ❌ | 是否包含子命名空间，默认 false |
| `category` | string | ❌ | 分类过滤（同 `dc_search`） |

**返回结构（指定 namespace 时）：**
```
# Classes in NXOpen.xxx (N total)

## Category1 (N)
- ClassName (N methods, N properties)
  Description: 描述

## Category2 (N)
...
```
省略 namespace 时返回所有命名空间及其类数量统计。

---

## 6. `dc_run_journal` — 执行完整 journal 文件（STEP 6）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `journal_path` | string | ✅ | journal 文件绝对路径（.py / .vb / .cs） |
| `args` | string[] | ❌ | 传递给 journal `main()` 的 `-args` 参数 |
| `managed_mode` | boolean | ❌ | Teamcenter 管理模式，默认 false |
| `timeout` | integer | ❌ | 超时秒数，默认 300 |
| `working_dir` | string | ❌ | 工作目录，默认 journal 所在目录 |

**返回结构：**
```
# Journal Execution Result
**Journal:** `<path>`
**Exit code:** `<code>`        # 0=成功
**Duration:** `<N> s`
**Working directory:** `<path>`

## Output files (N)
- `<file_path>`

## stdout
```
stdout 文本
```

## stderr
```
stderr 文本
```
```

---

## 7. `dc_run_snippet` — 执行内联代码片段（STEP 4，兜底方案）

**参数：**
| 参数 | 类型 | 必需 | 说明 |
|---|---|---|---|
| `code` | string | ✅ | Python 代码。auto_wrap 模式写纯语句（theSession/workPart 已绑定）；raw 模式写完整脚本 |
| `mode` | string | ❌ | `"auto_wrap"`（默认）/ `"raw"` |
| `timeout` | integer | ❌ | 超时秒数，默认 90 |

**返回结构：**
```
# Snippet Result
**Exit code:** `0`
**Duration:** `<N> s`

## stdout
```
print 输出文本
```

## stderr
```
错误输出（如有）
```
```

---

### 总结表

| 工具 | 步骤 | 用途 | 必需参数 | 返回格式 |
|---|---|---|---|---|
| `dc_lookup_pattern` | STEP 1 | 查最佳实践/坑 | `query` | Markdown 段落 + 代码 |
| `dc_search` | STEP 2 | 按名称搜 API | `query` | 类/方法列表 |
| `dc_semantic_search` | STEP 2 | 按意图发现 API | `query` | 带相关性评分的类列表 |
| `dc_list_namespace` | STEP 2 | 浏览命名空间 | 无（可选 namespace） | 类列表/命名空间统计 |
| `dc_get_api_info` | STEP 3 | 查类/方法完整签名 | `class_name` | 属性/方法/嵌套类型详情 |
| `dc_run_snippet` | STEP 4 | 执行内联代码探测 | `code` | 执行结果 + stdout/stderr |
| `dc_run_journal` | STEP 6 | 执行完整 journal 文件 | `journal_path` | 退出码 + 输出文件 + 日志 |
