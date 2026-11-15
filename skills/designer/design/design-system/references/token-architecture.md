> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/design-system/references/token-architecture.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Token 架构

面向可扩展、可换主题设计系统的三层 token 体系。

## 层级总览

```
┌─────────────────────────────────────────┐
│  Component Tokens                       │  Per-component overrides
│  --button-bg, --card-padding            │
├─────────────────────────────────────────┤
│  Semantic Tokens                        │  Purpose-based aliases
│  --color-primary, --spacing-section     │
├─────────────────────────────────────────┤
│  Primitive Tokens                       │  Raw design values
│  --color-blue-600, --space-4            │
└─────────────────────────────────────────┘
```

## 为什么三层？

| 层 | 用途 | 何时变更 |
|-------|---------|----------------|
| Primitive | 基础值（颜色、尺寸） | 极少变更，属于地基 |
| Semantic | 赋予含义 | 切换主题时 |
| Component | 组件定制 | 按组件需要 |

## 第 1 层：Primitive Token

不带语义的原始设计值。

```css
:root {
  /* Colors */
  --color-gray-50: #F9FAFB;
  --color-gray-900: #111827;
  --color-blue-500: #3B82F6;
  --color-blue-600: #2563EB;

  /* Spacing (4px base) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */

  /* Typography */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;

  /* Radius */
  --radius-sm: 0.25rem;
  --radius-default: 0.5rem;
  --radius-lg: 0.75rem;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
  --shadow-default: 0 1px 3px rgb(0 0 0 / 0.1);
}
```

## 第 2 层：Semantic Token

基于用途的别名，引用 primitive。

```css
:root {
  /* Background */
  --color-background: var(--color-gray-50);
  --color-foreground: var(--color-gray-900);

  /* Primary */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-700);

  /* Secondary */
  --color-secondary: var(--color-gray-100);
  --color-secondary-foreground: var(--color-gray-900);

  /* Muted */
  --color-muted: var(--color-gray-100);
  --color-muted-foreground: var(--color-gray-500);

  /* Destructive */
  --color-destructive: var(--color-red-600);
  --color-destructive-foreground: white;

  /* Spacing */
  --spacing-component: var(--space-4);
  --spacing-section: var(--space-6);
}
```

## 第 3 层：Component Token

引用语义层的组件专属 token。

```css
:root {
  /* Button */
  --button-bg: var(--color-primary);
  --button-fg: white;
  --button-hover-bg: var(--color-primary-hover);
  --button-padding-x: var(--space-4);
  --button-padding-y: var(--space-2);
  --button-radius: var(--radius-default);

  /* Input */
  --input-bg: var(--color-background);
  --input-border: var(--color-gray-300);
  --input-focus-ring: var(--color-primary);
  --input-padding: var(--space-2) var(--space-3);

  /* Card */
  --card-bg: var(--color-background);
  --card-border: var(--color-gray-200);
  --card-padding: var(--space-4);
  --card-radius: var(--radius-lg);
  --card-shadow: var(--shadow-default);
}
```

## 暗色模式

暗色主题下覆盖语义 token：

```css
.dark {
  --color-background: var(--color-gray-900);
  --color-foreground: var(--color-gray-50);
  --color-muted: var(--color-gray-800);
  --color-muted-foreground: var(--color-gray-400);
  --color-secondary: var(--color-gray-800);
}
```

## 命名约定

```
--{category}-{item}-{variant}-{state}

Examples:
--color-primary           # category-item
--color-primary-hover     # category-item-state
--button-bg-hover         # component-property-state
--space-section-sm        # category-semantic-variant
```

## 类别

| 类别 | 示例 |
|----------|----------|
| color | primary, secondary, muted, destructive |
| space | 1, 2, 4, 8, section, component |
| font-size | xs, sm, base, lg, xl |
| radius | sm, default, lg, full |
| shadow | sm, default, lg |
| duration | fast, normal, slow |

## 文件组织

```
tokens/
├── primitives.css     # Raw values
├── semantic.css       # Purpose aliases
├── components.css     # Component tokens
└── index.css          # Imports all
```

或用单文件加层级注释：

```css
/* === PRIMITIVES === */
:root { ... }

/* === SEMANTIC === */
:root { ... }

/* === COMPONENTS === */
:root { ... }

/* === DARK MODE === */
.dark { ... }
```

## 从扁平 token 迁移

迁移前（扁平）：
```css
--button-primary-bg: #2563EB;
--button-secondary-bg: #F3F4F6;
```

迁移后（三层）：
```css
/* Primitive */
--color-blue-600: #2563EB;
--color-gray-100: #F3F4F6;

/* Semantic */
--color-primary: var(--color-blue-600);
--color-secondary: var(--color-gray-100);

/* Component */
--button-bg: var(--color-primary);
--button-secondary-bg: var(--color-secondary);
```

## 对齐 W3C DTCG

token 的 JSON 格式（W3C Design Tokens Community Group）：

```json
{
  "color": {
    "blue": {
      "600": {
        "$value": "#2563EB",
        "$type": "color"
      }
    }
  }
}
```
