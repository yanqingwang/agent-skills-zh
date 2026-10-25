---
name: n8n-code-python
description: 在 n8n Code 节点中编写 Python（原生 Python，`language` pythonNative，n8n 2.x）。当用户明确想在 Code 节点中使用 Python 时、迁移使用过 _input/_json/_node/_now 的旧 Pyodide/"Python (Beta)" 代码时，或 Python Code 节点报出 NameError、"Security violations detected"、"Import of standard library module … is disallowed"、"__build_class__ not found"、"A 'json' property isn't a dictionary"、"Python runner unavailable" 等错误时使用。涵盖仅有的两个变量（_items/_item）、仅限 dict 的访问方式、默认被禁止的 import、沙箱拒绝的内建函数、可接受的返回形态，以及错误与 onError 的交互方式。JavaScript 是 Code 节点的默认语言——原生 Python 没有 n8n 辅助函数，且默认不能 import。例外——若要在可被 AI Agent 调用的 Custom Code Tool（@n8n/n8n-nodes-langchain.toolCode）中使用 Python，请改用 n8n-code-tool skill（输入是 _query，返回值必须是字符串）。
---

> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-python/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Python Code 节点（原生）

自 n8n 2.0 起，Code 节点的 Python 以**任务运行器中的原生 Python**方式运行（`language:
"pythonNative"`）。旧的 Pyodide "Python (Beta)" 已被移除，随之消失的还有它提供的一切 n8n 辅助函数：
`_input`、`_json`、`_node`、`_now`、`_today` 和 `_jmespath` 现在都会抛出 `NameError`。从旧模板、
论坛帖子或旧文档复制来的代码通常因此失效。

---

## JavaScript 优先：比以往更强

原生 Python 只给你两个变量和纯 Python，且**默认禁止任何 import**：没有
`json`、`datetime` 或 `re`。所有 n8n 特有的东西（`$('Node')`、`$jmespath`、Luxon、
`this.helpers.httpRequest`、静态数据）只存在于 JavaScript 中。只有当用户明确要求时才使用 Python。
即便如此，也先确认一个表达式、Edit Fields 或原生节点（Crypto、Date & Time、HTML、XML）能否完成
这项工作。参见 **n8n-code-javascript** 与 **n8n-expression-syntax** 中的 transform 守门规则。

---

## 快速开始

```python
# Run Once for All Items (default mode)
return [
    {"json": {"name": it["json"]["name"], "revenue": it["json"]["revenue"]}}
    for it in _items
    if it["json"].get("active")
]
```

```python
# Run Once for Each Item
row = _item["json"]
return {"json": {**row, "name_upper": (row.get("name") or "").upper()}}
```

节点配置：在 `n8n-nodes-base.code` typeVersion 2 上设置 `{"language": "pythonNative", "mode": "runOnceForAllItems" | "runOnceForEachItem",
"pythonCode": "..."}`。

---

## 仅有的输入：`_items` 与 `_item`

| 模式 | 变量 | 形态 |
|---|---|---|
| Run Once for All Items | `_items` | 由普通 dict 组成的 `list`：`{"json": {...}, "pairedItem": {...}}` |
| Run Once for Each Item | `_item` | 单个普通 dict：`{"json": {...}, "pairedItem": {...}}` |

- 每个变量**只存在于自己的模式中**。在每个条目模式下用 `_items`（或在
  所有条目模式下用 `_item`）会抛出 `NameError`。
- **仅限 dict 访问。** 用 `it["json"]["name"]` 或 `it["json"].get("name")`。`it.json.name` 会抛出
  `AttributeError: 'dict' object has no attribute 'json'`。
- **无法访问其他节点。** 没有 `_node` / `$('Node')` 的等价物。如果你需要来自其他分支的数据，
  先用 Merge 把它合并进来，或用 JavaScript 读取。
- **Webhook 载荷**位于 `["body"]` 之下：`_items[0]["json"].get("body", {}).get("email")`。
- **二进制数据**不在本文范围内。请在 JavaScript 中读写二进制（见 **n8n-binary-and-data**）。
- **pairedItem：** 原样返回 `_items` / `_item` 会保留它。当你构建新的 dict 且下游使用
  `$('Node').item` 时，给每个返回条目加上 `"pairedItem": {"item": i}`。这一点尚未在
  原生 Python 上验证，依赖它之前请先试运行。
- 缺失的键：优先用 `.get(key, default)`。`row["missing"]` 会抛出 `KeyError`。

旧代码迁移对照表：

| 旧（Pyodide） | 原生 |
|---|---|
| `_input.all()` | `_items` |
| `_input.first()["json"]` | `_items[0]["json"]`（用 `if _items` 保护） |
| `_input.item` / `_json` | `_item` / `_item["json"]` |
| `_node["X"]` | 不可用：在上游用 Merge，或用 JS |
| `_now`, `_today` | 不可用：通过 Edit Fields 传入 `{{ $now.toISO() }}`，或用 JS |
| `_jmespath(data, q)` | 不可用：在表达式中用 `$jmespath`，或用推导式 |
| `item.json.field` | `item["json"]["field"]` |

---

## import：默认被禁止

每一条 `import`（标准库和第三方）都会在**代码运行之前**对照允许清单检查。默认允许清单为空，
所以连 `import json` 都会让整个节点被拒绝：

```
Security violations detected
Line 1: Import of standard library module 'json' is disallowed. Allowed stdlib modules: none
```

- **n8n Cloud：** 完全不能 import。
- **自托管：** 管理员可以在 task-runner 配置中把模块加入允许清单（见
  **n8n-self-hosting** → `TASK_RUNNERS.md`）。因此有些实例允许 `json`、`datetime`
  和 `re`，而大多数实例不允许。
- **默认写不含 import 的代码。** 如果某个 import 确实有帮助，先确认：用一个
  单行测试节点 `import json` + `return [{"json": {"ok": True}}]`，或询问用户。永远不要假设。
- 没有 import 时：在上游解析 JSON 字符串（在 Edit Fields 中用 `{{ JSON.parse($json.payload) }}`）。
  用 Date & Time 节点或表达式中的 Luxon 做日期运算。ISO-8601 字符串作为
  普通字符串仍能正确比较和排序。哈希用 Crypto 节点。
- `requests`、`pandas` 和 `numpy` 永远不可用，除非管理员构建了自定义 runner 镜像。
  HTTP 请用 HTTP Request 节点。

---

## 沙箱限制（即使不 import 也会失败）

| 你写的 | 会发生什么 | 改用 |
|---|---|---|
| `eval`, `exec`, `compile`, `open`, `input`, `type`, `getattr`, `setattr`, `hasattr`, `vars`, `dir`, `globals`, `locals`, `object`, `memoryview`, `breakpoint` | `NameError: name 'type' is not defined`（运行时） | `isinstance(x, dict)`；`key in d` / `d.get(key)` |
| `class Foo: ...` | `__build_class__ not found`（运行时） | dict + 函数 |
| `x.__class__`, `"{0.__class__}".format(x)`, `__import__("json")` | `Security violations detected`（整个节点在运行前被拒绝） | — |
| 函数内的 `global counter` | `NameError: name 'counter' is not defined`，因为你的代码运行在一个包装函数内部 | `nonlocal counter` |

纯 Python 中的其他一切均正常工作（已验证）：推导式、生成器、lambda、闭包、
递归、`try`/`except`、f-string / `.format()` / `%`、`sorted`/`min`/`max`/`sum`/`any`/`all`/
`enumerate`/`zip`/`round`、集合、`isinstance`、`print()`（输出进入浏览器控制台）。

---

## 返回形态（已验证）

观察于 n8n 2.38.5。下述自动包装与直通行为没有官方文档，可能在
后续版本中改变。升级 n8n 后请用一次测试运行重新确认。

**Run Once for All Items**

| 返回值 | 结果 |
|---|---|
| `[{"json": {...}}, ...]` | 规范形态，N 个条目 |
| `[{...}, ...]`（普通 dict） | 自动包装到 `json` 之下，N 个条目 |
| `{"json": {...}}` 或单个普通 dict | 1 个条目 |
| `_items`（原地修改） | 直通，并带上你的修改 |
| `None` / 没有 `return` | 错误 `Cannot read properties of null (reading 'json')` |

**Run Once for Each Item**

| 返回值 | 结果 |
|---|---|
| `{"json": {...}}`、普通 dict 或 `_item` | 1 个条目 |
| `None` | 该条目被**丢弃**（相当于一个内建过滤器） |
| **list** | 错误 `A 'json' property isn't a dictionary [item 0]` |

**输出时的值转换：** `tuple` 变成 list，`set` 变成*字符串* `"{1, 2}"`，
`datetime` 变成 `str(dt)`（`"2026-09-16 10:18:00.025792"`，不是 ISO）。请显式转换
（`sorted(s)`、`dt.isoformat()`）。

在所有条目模式下优先使用显式的 `[{"json": ...}]`，在每个条目模式下优先使用 `{"json": ...}`。
自动包装可以工作，但显式形态能让下一个读者一眼看出意图。

---

## 错误与 `onError`

普通的 `raise ValueError("bad row")` 会以该消息使节点失败。当节点设置了
`onError` continue 模式时，三类失败的表现**各不相同**（已验证）：

| 失败类型 | `continueErrorOutput` | `continueRegularOutput` |
|---|---|---|
| 运行时异常（`raise`、`KeyError`、`NameError`、被拒绝的内建函数） | 错误输出上出现 `{"error": "<message>"}`（`main[1]`）✅ | 主输出上出现 `{"error": "<message>"}` |
| 静态拒绝（`Security violations detected`：import、dunder） | 节点被标记为失败，但**输入条目原封不动地从成功输出流出**；`main[1]` 保持为空 | 输入条目原封不动地出现在主输出上 |
| 错误的返回形态（每个条目模式下返回 list，所有条目模式下返回 `None`） | 同上：**成功输出上是原封不动的输入** | 同上 |

后两种是静默数据陷阱：下游节点收到的输入仿佛代码已经运行过一样（实际未被处理），
而执行仍显示成功。没有错误分支能捕获它们。预防它们（除非已确认否则不 import、
返回形态正确），并用一次真实的测试运行确认，检查
Code 节点的状态和输出（见 **n8n-error-handling**）。

其他消息：

- `Python runner unavailable: Python 3 is missing from this system`：自托管实例没有
  Python task runner（原厂镜像不带）。这是基础设施问题，不是代码
  问题。见 **n8n-self-hosting** → `TASK_RUNNERS.md`。
- `validate_node` / `validate_workflow` 能捕获少量 Python 错误（`import requests`、缺少
  `return`、`return None`）。它们**不能**捕获 `_input`/`_json`、点号访问、被禁止的标准库
  import、dunder 访问或类。真实测试执行是唯一可靠的检查。

---

## 性能

每个 Python Code 节点大约耗时 0.4 s（runner 冷启动时约 1 s），明显高于
JS Code 节点或表达式。处理列表时使用 **Run Once for All Items** 模式而不是
逐条处理，并且不要把一个节点能完成的工作拆成多个小 Python 节点串联。

---

## 清单

- [ ] 用户确实要求了 Python。否则用 JS、表达式或原生节点。
- [ ] 模式与变量匹配：`_items`（所有条目）/ `_item`（每个条目）。
- [ ] 只用 dict 访问。不用 `_input`、`_json`、`_node`、`_now` 或 `_jmespath`。
- [ ] 没有 `import`，除非已确认在*这个*实例上被允许。
- [ ] 没有类、`type()`、`getattr`/`hasattr` 或 dunder。用 `nonlocal` 而不是 `global`。
- [ ] 返回形态符合模式。set 和 datetime 已显式转换。
- [ ] 跑过一次真实的测试执行并检查了输出条目（仅靠验证无法捕获上述陷阱）。

---

## 参考

- **[COMMON_PATTERNS.md](COMMON_PATTERNS.md)**：12 个不含 import 的模式，每个都在真实
  n8n 实例上验证过（过滤、聚合、分组、去重、Top N、展平、校验、丢弃条目、文本
  报告、安全嵌套访问、累计值、ISO 时间戳）。

## 相关 skills

- **n8n-code-javascript**：Code 节点的默认选择，拥有全部 n8n 辅助函数。
- **n8n-expression-syntax**：`$jmespath`、Luxon 与 transform 守门规则，往往比任何 Code 节点都更合适。
- **n8n-code-tool**：AI-agent Custom Code Tool 中的 Python（`_query`，返回字符串）。
- **n8n-error-handling**：连接错误输出；即上文的直通陷阱。
- **n8n-self-hosting**：启用 Python task runner 与配置模块允许清单。
