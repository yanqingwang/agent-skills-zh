> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/review/TODOS-format.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# TODOS.md 格式参考

TODOS.md 规范格式的共享参考。由 `/ship`（Step 14）与 `/plan-ceo-review`（TODOS.md updates 小节）引用，以保证 TODO 条目结构一致。

---

## 文件结构

```markdown
# TODOS

## <Skill/Component>     ← e.g., ## Browse, ## Ship, ## Review, ## Infrastructure
<items sorted P0 first, then P1, P2, P3, P4>

## Completed
<finished items with completion annotation>
```

**小节：** 按 skill 或 component 组织（`## Browse`、`## Ship`、`## Review`、`## QA`、`## Retro`、`## Infrastructure`）。每个小节内按优先级排序（P0 在最上）。

---

## TODO 条目格式

每个条目是其所属小节下的一个 H3：

```markdown
### <Title>

**What:** One-line description of the work.

**Why:** The concrete problem it solves or value it unlocks.

**Context:** Enough detail that someone picking this up in 3 months understands the motivation, the current state, and where to start.

**Effort:** S / M / L / XL
**Priority:** P0 / P1 / P2 / P3 / P4
**Depends on:** <prerequisites, or "None">
```

**必填字段：** What、Why、Context、Effort、Priority
**可选字段：** Depends on、Blocked by

---

## 优先级定义

- **P0**（Blocking）：必须在下一个 release 之前完成
- **P1**（Critical）：应在本周期内完成
- **P2**（Important）：P0/P1 清空后处理
- **P3**（Nice-to-have）：拿到采用/使用数据后再评估
- **P4**（Someday）：好想法，无紧迫性

---

## Completed 条目格式

条目完成后，把它移入 `## Completed` 小节，保留原内容并追加：

```markdown
**Completed:** vX.Y.Z (YYYY-MM-DD)
