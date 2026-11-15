> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/improve-animations/PLAN-TEMPLATE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 计划模板（Plan Template）

由 `improve-animations` 写出的每份计划都遵循这一结构。执行者可能是一个上下文为零、品味为零、能力较弱的模型，所以计划必须把一切内容精确包含在内。不要出现"上文审计"或"我们讨论过的缓动"这类指代。

```markdown
# NNN — <Short imperative title>

- **Status**: TODO
- **Commit**: <output of `git rev-parse --short HEAD` when this plan was written>
- **Severity**: HIGH | MEDIUM | LOW
- **Category**: <audit category>
- **Estimated scope**: <n files, rough size>

## Problem

What is wrong, where, and why it matters to how the product feels. Cite every
location as `path/to/file.tsx:123` and include the current code verbatim:

​```css
/* src/components/dropdown.css:14 — current */
.dropdown { transition: all 400ms ease-in; }
​```

## Target

The exact end state. Every value spelled out — curves, durations, spring
configs, media queries. Never "use a nicer easing":

​```css
/* target */
.dropdown {
  transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out);
  transform-origin: var(--transform-origin);
}
​```

## Repo conventions to follow

How this codebase already does it, with one exemplar the executor should
imitate (token names, file placement, prop patterns):

- Easing tokens live in `src/styles/tokens.css`; add new curves there, e.g. `--ease-out: cubic-bezier(0.23, 1, 0.32, 1);`
- <exemplar file:line that already does this correctly>

## Steps

1. <One concrete edit per step: file, what changes, resulting code.>
2. …

## Boundaries

- Do NOT touch <files/components out of scope>.
- Do NOT change markup/structure — motion properties only (unless a step says otherwise).
- Do NOT add new dependencies.
- If a step doesn't match the code you find (drift since the commit stamp), STOP and report instead of improvising.

## Verification

- **Mechanical**: <exact commands — typecheck, lint, build — with expected outcome>.
- **Feel check**: run the UI, trigger <interaction>, and confirm:
  - <observable check, e.g. "the dropdown scales from its trigger, not from center">
  - <e.g. "spamming the toggle never restarts the animation from zero">
  - In DevTools, set playback to 10% (Animations panel) and confirm <detail>.
  - Toggle `prefers-reduced-motion` (Rendering panel) and confirm movement is dropped but opacity feedback remains.
- **Done when**: <machine- or eye-checkable completion criteria>.
```

## 给计划作者的备注

- 一份计划对应一个发现。若两个发现涉及完全相同的文件集合和相同的修复模式（例如在多个组件间替换同一个缓动 token），可以合并为一份计划。
- 每个取值都从 [AUDIT.md](AUDIT.md) 拉取，绝不要凭记忆近似。
- Feel check 不可省略。动效可以在机械上正确，但感觉仍然不对；要给执行者（或审查执行者 diff 的人）在慢放时应当盯住的具体观察点。
- 写完计划后，创建或更新 `plans/README.md`，内容包括：计划一览表（编号、标题、严重度、状态）、建议的执行顺序，以及计划之间的依赖关系。
