> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/design-md.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# design.md：被锁定的系统

当用户要求把当前构建的系统锁定为一个可携带文件，或一次重设计跨越多个页面（`redesign.md`）时，在脚手架运行之后加载：该文件从 `tokens.css` 写出，绝不从主题文件写出。单页构建从不自己写 `design.md`；`tokens.css` 已经让每次构建都可携带，而 Picks 块会用一行话提供锁定选项。

## 触发条件

*lock the system*, *lock the design system*, *give me a design.md*, *export this as a design.md*, *extract the tokens*, *make this portable*, *I want to use this in another project*。其他任何说法，包括对同一提示词的进一步迭代，都不加载本文件。

- **页面构建，以及跨越多页的重设计。** 单个组件太小，成不了系统。
- **绝不覆写。** 根目录已有 `design.md` 或 `DESIGN.md` 时，刷新其 `## Exports` 并用一行话说明：*design.md found; Exports refreshed, system unchanged.*

## 格式

写在项目根目录，采用项目的大小写惯例，约 45 行：足以给另一个页面当种子，又短到可维护。先用大白话说出选择（*Genre: editorial. Shape: Long Document. Theme: Newsprint. Locking this as the project's system.*），然后写出：

````markdown
# Design: <project name>

The locked system. Every Hallmark run reads this first and pages share it. Change it on purpose; the file is the rule.

## System
- Genre: <editorial | modern-minimal | atmospheric | playful>
- Shape of the first page: <macrostructure, or app screen>
- Theme: <catalog name, or custom (vibe: "<4 to 8 words>")>
- Axes: <paper band>/<display class>/<accent band> · posture: <posture>

## Tokens
`tokens.css` is the source of truth. The roles:
```css
:root {
  --color-paper: oklch(<L> <C> <H>);  --color-paper-2: oklch(…);  --color-paper-3: oklch(…);
  --color-ink: oklch(…);  --color-ink-2: oklch(…);  --color-muted: oklch(…);  --color-rule: oklch(…);
  --color-accent: oklch(…);  --color-accent-ink: oklch(…);  --color-focus: oklch(…);
  --font-display: "<face>", <fallbacks>;  --font-body: "<face>", <fallbacks>;  --font-outlier: <…>;
  --radius-card: <px>;  --radius-pill: <px>;  --rule-hair: <px>;  --shadow-card: <value or none>;
}
```
The spacing scale, the type scale, the easings and the durations are the scaffold's and live in `tokens.css`.

## Controls
- Primary: <fill> · <radius> · <height>
- Secondary: <outline or text> · same radius and height

## Motion
- Character: <still | severe | brisk | calm>; one reveal at most; under reduced motion everything ends at once.

## Exports
`tokens.css` in this project. Tailwind, DTCG or shadcn blocks are added here on request, per `export-formats.md`.
````

## 文件存在之后

预检（pre-flight）在此后的每次运行中都会找到它（SKILL.md Step 0）。从那时起每个选择都服从它，多样性规则反转（页面共享系统而不是彼此不同），而一个确实需要别的什么东西的页面，会用 `## Variants` 章节修订 `design.md`，而不是在本地覆盖它。
