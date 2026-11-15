> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/export-formats.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 导出格式

当存在 `design.md` 且其 `## Exports` 需要刷新，或用户要求以其他格式提供 token 时加载本文件。`tokens.css` 是唯一事实来源，由 `theme.mjs scaffold` 写出；其他一切格式都只是对它的翻译，仅在有人要求时才写出。

## Token 清单

| 族 | Token |
| --- | --- |
| 颜色 | `--color-paper`, `-paper-2`, `-paper-3`, `-ink`, `-ink-2`, `-muted`, `-rule`（主题设有 `-rule-2` 时一并保留）, `-accent`, `-accent-ink`, `-focus`, `-error`, `-success`；Committed 姿态下另有 `-field`，主题命名了第二种墨色时有 `-accent-2` |
| 字体 | `--font-display`, `--font-body`, `--font-outlier`；`--text-xs` 到 `--text-3xl`，以 16px 为基准的 1.25 比例，`--text-display-s`, `--text-display`，以及角色 token `--text-section`（`h2`）、`--text-title`（`h3`）、`--text-lead`（应用屏幕：固定 1.2 比例，角色 token 取小的固定档位）；`--tracking-display` |
| 空间 | `--space-3xs` (2px) 到 `--space-4xl` (144px)，共十档；`--container`, `--gutter`, `--gap-columns`, `--section-gap-s`, `--section-gap`, `--section-gap-l` |
| 形状 | `--radius-card`, `--radius-pill`, `--rule-hair`, `--shadow-card` |
| 动效 | `--ease-out`, `--ease-in`, `--ease-in-out`；`--dur-micro` 120ms, `--dur-short` 220ms, `--dur-long` 420ms |
| 层级 | `--z-base` 1, `-raised` 10, `-dropdown` 100, `-sticky` 200, `-sticky-nav` 300, `-modal` 400, `-toast` 500, `-tooltip` 600 |

页面需要别的 token 时，按角色命名并在 `tokens.css` 中声明；下游不使用任何 `tokens.css` 未声明的名字。

## 项目中的 `tokens.css`

脚手架把 `tokens.css` 和 `base.css` 写在项目入口样式表旁边（`src/index.css`、`app/globals.css`；`--dir` 可指定另一文件夹），并打印适配它的两条 import。它们紧跟文件的最后一个 `@import`，绝不放在任何规则之后：CSS 会丢弃位于规则之后的 `@import`，token 就会无声消失。项目已有自己的 token 命名（`--background`、Tailwind 的 `@theme`）时，把 Hallmark 的角色映射到那些名字上，而不是另起一套平行体系。只有用户要求完全接管时才替换文件。

## Tailwind v4

入口样式表导入 Tailwind 4 时，脚手架分两块写出 `tokens.css`，import 跟在 `@import "tailwindcss"` 之后：

```css
@import "tailwindcss";
@import "./tokens.css";
@import "./base.css" layer(base);
```

```css
@theme static { --color-paper: oklch(96.5% 0.008 50); --font-display: "Fraunces", serif; --text-lg: 1.25rem; --radius-card: 4px; }
:root { --space-lg: 24px; --dur-short: 220ms; --z-modal: 400; --section-gap: 144px; }
```

- **`@theme static`** 收纳所有 `--color-*`、`--font-*`、`--text-*`、`--tracking-*`、`--radius-*`、`--shadow-*` 与 `--ease-*` token，使每个都成为工具类（`bg-paper`、`text-ink`、`font-display`、`rounded-card`），且因为 static，在手写 CSS 里仍是变量。其余都留在 `:root`。
- **绝不使用 `--spacing-<name>`。** Tailwind 由这个命名空间推导 `w-`、`max-w-`、`p-`、`gap-` 的尺寸，`--spacing-xl: 40px` 会把 `max-w-xl` 变成 40px。空间刻度不需要映射：除 2px 外每一档都是 Tailwind 4px 单位的倍数（`--space-lg` 是 `p-6`，`--space-xl` 是 `p-10`，`--space-2xl` 是 `p-16`）。
- **九个名字属于 Tailwind 本身：** `--text-xs`, `-sm`, `-lg`, `-xl`, `-2xl`, `-3xl`，以及三个 `--ease-*`。脚手架的取值会替换 Tailwind 的，所以项目里凡是用到 `text-lg` 与 `ease-out` 的地方都会改变。在新项目上、在改款或整体重设计上，这就是系统到位。在一个其他页面不能动的项目里新增单个页面时，把这九个从 `@theme` 中取出，声明在该页面的根元素上。
- **`base.css` 放进 base layer。** 不分层时，它的元素规则（`a { color: inherit }`、`h1 { max-width: 20ch }`）会压过所有工具类，因为 Tailwind 的工具类位于 layer 内。
- **印记（stamp）从源文件读取。** Tailwind 会丢弃输出中的注释；sloplint 读的是你写的那份样式表。

Tailwind v3（`@tailwind` 指令）：`tokens.css` 保持单个 `:root` 块，stamp 与两条 import 放在指令之上（放在指令之下会被丢弃），`base.css` 带 `layer(base)`，使其落在 Preflight 之后、工具类之前。工具类按需生成：`tailwind.config` 的 `theme.extend` 下使用相同名字，每个取值都是对应 token 的 `var()`。

## DTCG `tokens.json`

面向 Style Dictionary 或 Tokens Studio 流水线。按路径组织，每个 token 带 `$type`，OKLCH 以字符串导出（只有流水线读不了时才转 hex，并注明该转换有损）。流式字号导出其最大值；`clamp()` 留在 CSS 里。

```json
{
  "color": {
    "paper": { "$value": "oklch(96.5% 0.008 50)", "$type": "color" },
    "accent": { "$value": "oklch(62% 0.17 28)", "$type": "color" }
  },
  "font": { "display": { "$value": "General Sans, ui-sans-serif, sans-serif", "$type": "fontFamily" } },
  "space": { "lg": { "$value": "24px", "$type": "dimension" } },
  "duration": { "short": { "$value": "220ms", "$type": "duration" } }
}
```

## shadcn/ui

shadcn 把完整颜色值存进自己的变量，并在 `@theme inline` 中映射。把它的变量指向 Hallmark 的 token：

```css
:root {
  --background: var(--color-paper); --foreground: var(--color-ink);
  --card: var(--color-paper-2); --card-foreground: var(--color-ink);
  --popover: var(--color-paper-2); --popover-foreground: var(--color-ink);
  --primary: var(--color-accent); --primary-foreground: var(--color-accent-ink);
  --secondary: var(--color-paper-3); --secondary-foreground: var(--color-ink-2);
  --muted: var(--color-paper-2); --muted-foreground: var(--color-muted);
  --accent: var(--color-paper-3); --accent-foreground: var(--color-ink);
  --destructive: var(--color-error);
  --border: var(--color-rule); --input: var(--color-rule); --ring: var(--color-focus);
  --radius: var(--radius-card);
}
```

shadcn 的 `accent` 是 hover 表面、`muted` 是安静的背景，所以它的 `@theme inline` 块定义的 `--color-accent` 与 `--color-muted` 在含义上与 Hallmark 的冲突。在 shadcn 项目中，把 Hallmark 的这两个 token 留在 `@theme` 之外，让页面 CSS 通过 `var()` 取用，或在 `@theme` 里改名（`--color-signal`、`--color-ink-3`）并在交接说明中注明。
