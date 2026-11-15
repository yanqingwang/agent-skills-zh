> **中文汉化版** · 上游：[czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) · 原文件：`skills/n8n-code-python/COMMON_PATTERNS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 常用模式（原生 Python Code 节点）

十二个无需 import 的模式。下面每个代码块都在 n8n 2.38.5 的 Code 节点（`language: "pythonNative"`）中逐字运行过，输入为所示样例，记录的输出均为实测。它们只用 `_items` / `_item`、字典访问和沙箱允许的内建能力：不 import、不用类、不用 `type()`、不用 dunder（见 SKILL.md → Sandbox limits）。

使用之前，先重读本 Skill 的第一条规则：**用户要求的真的是 Python 吗？**在 JavaScript 优先的工作流里，这些大多只相当于一个表达式、一个 Edit Fields 字段，或一个原生节点（Filter、Aggregate、Split Out、Remove Duplicates、Sort、Limit）。

**样例输入**（3 个 item，例如 Split Out 之后）：

```json
[
  {"name": "Acme", "country": "PL", "revenue": 120000, "active": true,  "contact": {"email": "a@acme.pl", "first-name": "Jan"},  "orders": [{"id": "A1", "total": 500}, {"id": "A2", "total": 1500}]},
  {"name": "Foo",  "country": "DE", "revenue": 30000,  "active": false, "contact": {"email": "f@foo.de", "first-name": "Hans"}, "orders": [{"id": "F1", "total": 90}]},
  {"name": "Bar",  "country": "PL", "revenue": 80000,  "active": true,  "contact": {"email": null, "first-name": "Ola"},       "orders": []}
]
```

| # | 模式 | 执行模式 |
|---|---|---|
| 1 | 过滤并重塑 | All Items |
| 2 | 汇总与平均 | All Items |
| 3 | 按字段分组 | All Items |
| 4 | 按键去重 | All Items |
| 5 | 按字段取 Top N | All Items |
| 6 | 每个嵌套元素一个 item | All Items |
| 7 | 校验并标记 | Each Item |
| 8 | 只保留部分 item（逐 item 模式） | Each Item |
| 9 | 文本报告 | All Items |
| 10 | 安全嵌套访问 | All Items |
| 11 | 用 nonlocal 维护运行状态 | All Items |
| 12 | 不用 datetime 处理 ISO 时间戳 | All Items |

---

## 1. 过滤并重塑

**Mode:** Run Once for All Items。保留收入超过阈值的活跃客户，只输出下游需要的字段。

```python
return [
    {"json": {"name": it["json"]["name"], "revenue": it["json"]["revenue"]}}
    for it in _items
    if it["json"].get("active") and it["json"].get("revenue", 0) >= 50000
]
```

**Output:** 2 个 item：Acme 和 Bar 的 `{name, revenue}`。

---

## 2. 汇总与平均

**Mode:** Run Once for All Items。把所有输入 item 汇成一个统计 item。`max(..., default=0)` 和 `if count` 保护让空输入不会抛错。

```python
revenues = [it["json"].get("revenue") or 0 for it in _items]
count = len(revenues)
return [{"json": {
    "count": count,
    "total": sum(revenues),
    "average": round(sum(revenues) / count, 2) if count else 0,
    "max": max(revenues, default=0),
}}]
```

**Output:** `{count: 3, total: 230000, average: 76666.67, max: 120000}`

---

## 3. 按字段分组

**Mode:** Run Once for All Items。用 `setdefault` 建桶；每组输出一个 item，并排序。

```python
groups = {}
for it in _items:
    row = it["json"]
    key = row.get("country") or "unknown"
    groups.setdefault(key, {"country": key, "customers": [], "revenue": 0})
    groups[key]["customers"].append(row["name"])
    groups[key]["revenue"] += row.get("revenue") or 0
return [{"json": g} for g in sorted(groups.values(), key=lambda g: g["revenue"], reverse=True)]
```

**Output:** `{country: "PL", customers: ["Acme", "Bar"], revenue: 200000}`，然后是 DE。

---

## 4. 按键去重

**Mode:** Run Once for All Items。每个归一化后的键保留第一个 item，返回原始 item，所有字段得以保留。

```python
seen = set()
unique = []
for it in _items:
    key = (it["json"].get("country") or "").lower()
    if key in seen:
        continue
    seen.add(key)
    unique.append(it)
return unique
```

**Output:** 2 个 item（第一个 PL、第一个 DE）。

---

## 5. 按字段取 Top N

**Mode:** Run Once for All Items。先 `sorted(..., key=..., reverse=True)[:N]`，再用 `enumerate` 排名。

```python
top = sorted(_items, key=lambda it: it["json"].get("revenue") or 0, reverse=True)[:2]
return [{"json": {"rank": i + 1, "name": it["json"]["name"]}} for i, it in enumerate(top)]
```

**Output:** `{rank: 1, name: "Acme"}`，`{rank: 2, name: "Bar"}`

---

## 6. 每个嵌套元素一个 item

**Mode:** Run Once for All Items。把每个 item 内部的数组扇出成独立 item，相当于带父字段附加的 Split Out 的 Python 版。

```python
out = []
for it in _items:
    customer = it["json"]
    for order in customer.get("orders", []):
        out.append({"json": {"customer": customer["name"], "order_id": order["id"], "total": order["total"]}})
return out
```

**Output:** 3 个 item：`{customer, order_id, total}`

---

## 7. 校验并标记

**Mode:** Run Once for Each Item。逐 item 模式：给 item 附加 `valid` + `problems`，而不是让运行失败；之后用 IF 节点按 `valid` 路由。

```python
row = _item["json"]
problems = []
if not row.get("name"):
    problems.append("name missing")
email = (row.get("contact") or {}).get("email")
if not email or "@" not in email:
    problems.append("email missing or invalid")
return {"json": {**row, "valid": not problems, "problems": problems}}
```

**Output:** Bar 得到 `valid: false, problems: ["email missing or invalid"]`。

---

## 8. 只保留部分 item（逐 item 模式）

**Mode:** Run Once for Each Item。逐 item 模式下 `return None` 会丢弃该 item，相当于代码版的 Filter 节点。

```python
if _item["json"].get("country") != "PL":
    return None
return _item
```

**Output:** 2 个 item（那些 PL 客户）。

---

## 9. 文本报告

**Mode:** Run Once for All Items。用带格式说明符（`:,`）的 f-string 和 `"\n".join` 生成消息正文（Slack、邮件）。

```python
lines = [
    f"- {it['json']['name']} ({it['json']['country']}): {it['json']['revenue']:,} PLN"
    for it in sorted(_items, key=lambda it: it["json"]["name"])
]
return [{"json": {"report": "Customers:\n" + "\n".join(lines), "lines": len(lines)}}]
```

**Output:** `"Customers:\n- Acme (PL): 120,000 PLN\n- Bar (PL): 80,000 PLN\n- Foo (DE): 30,000 PLN"`

---

## 10. 安全嵌套访问

**Mode:** Run Once for All Items。用一个小的 `dig()` 辅助函数，代替在缺键/越界时会抛错的链式 `[...]` 取值。被禁用的 `type()` 用 `isinstance` 替代。

```python
def dig(data, *path, default=None):
    for key in path:
        if isinstance(data, dict) and key in data:
            data = data[key]
        elif isinstance(data, list) and isinstance(key, int) and -len(data) <= key < len(data):
            data = data[key]
        else:
            return default
    return data

return [{"json": {
    "first_order_total": dig(it["json"], "orders", 0, "total", default=0),
    "first_name": dig(it["json"], "contact", "first-name", default=""),
}} for it in _items]
```

**Output:** Bar（没有订单）得到 `first_order_total: 0`。

---

## 11. 用 nonlocal 维护运行状态

**Mode:** Run Once for All Items。代码运行在一个包装函数里，`global` 无效：与辅助函数共享状态请用 `nonlocal`。

```python
running = 0
def add(value):
    nonlocal running
    running += value
    return running

return [{"json": {"name": it["json"]["name"], "cumulative": add(it["json"]["revenue"])}} for it in _items]
```

**Output:** cumulative 120000 → 150000 → 230000

---

## 12. 不用 datetime 处理 ISO 时间戳

**Mode:** Run Once for All Items。*示例性质，无需输入*（时间戳直接写在代码里）。没有 `datetime` import 时，同一时区的 ISO-8601 字符串作为字符串排序和比较仍然正确；按年/月分桶用切片。真正的日期运算应放在表达式（Luxon）或 JS 里。

```python
stamps = ["2026-09-16T10:00:00Z", "2026-01-02T08:30:00Z", "2025-12-31T23:59:59Z"]
return [{"json": {
    "latest": max(stamps),
    "in_2026": [s for s in stamps if s[:4] == "2026"],
    "by_month": sorted({s[:7] for s in stamps}),
}}]
```

**Output:** `latest: "2026-09-16T10:00:00Z"`，`by_month: ["2025-12", "2026-01", "2026-09"]`

---

## 未覆盖的内容，以及原因

- **解析 JSON 字符串、正则、哈希、真正的日期运算**需要 `json` / `re` / `hashlib` / `datetime`，除非实例把它们加入白名单，否则被禁止。先用原生节点或表达式完成（Date & Time 或 Luxon、`.parseJson()`、`.match()`、Crypto 节点），或用 JavaScript Code 节点。
- **读取另一个节点的输出**：原生 Python 没有 `_node`。先合并分支，或用 JavaScript 的 `$('Node Name')`。
- **HTTP 调用**：用 HTTP Request 节点。
