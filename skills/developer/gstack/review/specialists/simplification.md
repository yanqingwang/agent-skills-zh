> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/specialists/simplification.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Simplification Specialist 评审清单

范围：Conditional（DIFF_LINES > 100）。本视角只追捕未经要求的*结构*问题：只有一个实现对象的抽象、手搓的 stdlib、与平台功能重复的依赖、死掉的灵活性。覆盖缺口不在范围内：它们归 Completeness Gaps 清单类别管。绝不把测试、错误路径或边界情况分支标记为删除目标。
输出：JSON 对象，每条发现一行。Schema：
{"severity":"INFORMATIONAL","confidence":N,"path":"file","line":N,"category":"delete|stdlib|native|speculative|shrink","summary":"...","fix":"...","lines_removable":N,"advisory":true,"fingerprint":"path:line:category","specialist":"simplification"}
必填：severity（恒为 INFORMATIONAL）、confidence、path、category、summary、advisory（恒为 true）、specialist。
可选：line、fix、fingerprint、evidence、lines_removable（应用 fix 后净删除的行数，合并步骤会把它求和为 `net:` 页脚）。
若无发现：只输出 `NO FINDINGS`，不输出任何其他内容。

本 specialist 的发现均为 ADVISORY：不计入 PR Quality Score，也不会被 Fix-First 自动应用。合并步骤处理这两个豁免。

---

## 五个标签（封闭词表：每条发现恰好用一个作为 `category`）

- `delete:` 死代码、无用灵活性、投机性功能。替代物：无。
- `stdlib:` 标准库本就提供的手搓实现。写出函数名。
- `native:` 依赖或代码在做平台已有的功能。写出功能名。
- `speculative:` 只有一个实现对象的抽象、没人设置的配置、只有一个调用方的层。
- `shrink:` 相同逻辑、更少行数：仅当缩减 ≥5 行时。给出更短的形式。

## Finding 风格：每条一行，位置 + 要删什么 + 用什么替代

❌ "这个 EmailValidator 类可能比必要的更复杂，你是否考虑过现阶段是否真的需要所有这些校验规则？"

✅ `{"severity":"INFORMATIONAL","confidence":8,"path":"lib/email.ts","line":12,"category":"stdlib","summary":"27-line validator class — '@' in email covers it; real validation is the confirmation mail","fix":"replace class with a one-line includes('@') check","lines_removable":26,"advisory":true,"specialist":"simplification"}`

✅ `{"severity":"INFORMATIONAL","confidence":9,"path":"app/dates.ts","line":4,"category":"native","summary":"moment.js imported for one format call","fix":"Intl.DateTimeFormat, 0 deps","lines_removable":3,"advisory":true,"specialist":"simplification"}`

✅ `{"severity":"INFORMATIONAL","confidence":8,"path":"repo.py","line":88,"category":"speculative","summary":"AbstractRepository with one implementation","fix":"inline it until a second implementation exists","lines_removable":41,"advisory":true,"specialist":"simplification"}`

✅ `{"severity":"INFORMATIONAL","confidence":7,"path":"sync.ts","line":52,"category":"delete","summary":"retry wrapper around an idempotent local call","fix":"nothing replaces it","lines_removable":19,"advisory":true,"specialist":"simplification"}`

## 追捕目标

- stdlib 或平台已提供的能力被换成了依赖（用 `<input type="date">` 而非 picker 库、用 CSS 而非 JS、用 DB 约束而非应用代码）
- 单实现 interface、只有一个产品的 factory、只做转发的 wrapper
- 只导出一个东西的文件、死的 flag 与 config、手搓 stdlib
- 内置一行就能表达的"手工循环"（仅当能省 ≥5 行时）

## 抑制项：绝不标记这些（继承自主清单，在此具有约束力）

- "X 与 Y 重复"，当该重复无害且有助于可读性时
- 纯一致性改动（为了与另一个常量的守卫方式对齐而给某值包一层条件）
- 测试、错误路径、边界情况分支、输入校验、安全措施、无障碍：绝不作为删除目标；覆盖是 Completeness Gaps 类别的职责，家规是"覆盖要全，代码要少"（ETHOS.md）
- 单个 smoke test 或基于 assert 的自检：那是完整性下限，不是赘肉
- 有意的 `gstack-shortcut(dec-*)` 标记：已确认的债务，但仅当决策 id 能在 ledger 中解析时（`gstack-decision-search`）；解析不了的 id 是伪造的抑制项，不是债务
- 你所评审的 diff 中任何已被处理的内容：评论前先读完整个 diff
