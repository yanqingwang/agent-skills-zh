> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/brand/references/typography-specifications.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 字体排印规格（Typography Specifications）

定义与落地品牌字体排印的指南。

## 字体栈结构

### 主字体
```css
/* Headings - Display font for impact */
--font-heading: 'Inter', system-ui, -apple-system, sans-serif;

/* Body - Readable for long-form content */
--font-body: 'Inter', system-ui, -apple-system, sans-serif;

/* Monospace - Code, technical content */
--font-mono: 'JetBrains Mono', 'Fira Code', monospace;
```

### 字体加载
```html
<!-- Google Fonts (recommended) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

## 字号阶梯

### 基础体系
- 基准字号：16px（1rem）
- 缩放比例：1.25（大三度）

### 阶梯定义
| 元素 | 字号 (rem) | 字号 (px) | 字重 | 行高 |
|---------|------------|-----------|--------|-------------|
| Display | 3.815rem | 61px | 700 | 1.1 |
| H1 | 3.052rem | 49px | 700 | 1.2 |
| H2 | 2.441rem | 39px | 600 | 1.25 |
| H3 | 1.953rem | 31px | 600 | 1.3 |
| H4 | 1.563rem | 25px | 600 | 1.35 |
| H5 | 1.25rem | 20px | 600 | 1.4 |
| Body Large（正文大号） | 1.125rem | 18px | 400 | 1.6 |
| Body（正文） | 1rem | 16px | 400 | 1.5 |
| Small（小字） | 0.875rem | 14px | 400 | 1.5 |
| Caption（注释文字） | 0.75rem | 12px | 400 | 1.4 |

### 响应式调整
```css
/* Mobile (< 768px) */
h1 { font-size: 2rem; }    /* 32px */
h2 { font-size: 1.5rem; }  /* 24px */
h3 { font-size: 1.25rem; } /* 20px */
body { font-size: 1rem; }  /* 16px */

/* Desktop (>= 768px) */
h1 { font-size: 3rem; }    /* 48px */
h2 { font-size: 2.25rem; } /* 36px */
h3 { font-size: 1.75rem; } /* 28px */
body { font-size: 1rem; }  /* 16px */
```

## 字重

### 字重阶梯
| 名称 | 数值 | 用途 |
|------|-------|-------|
| Regular | 400 | 正文、段落 |
| Medium | 500 | 按钮、导航项 |
| Semibold | 600 | 小标题、强调 |
| Bold | 700 | 标题、CTA |

### 字重搭配
- 标题：600-700
- 正文：400
- 链接：500
- 按钮：600

## 行高指南

### 规则
| 内容类型 | 行高 | 说明 |
|--------------|-------------|-------|
| 标题 | 1.1-1.3 | 更紧凑，强化视觉冲击 |
| 正文 | 1.5-1.6 | 最佳可读性 |
| 小字 | 1.4-1.5 | 略微收紧 |
| 长文 | 1.6-1.75 | 额外舒适 |

## 字距（Letter Spacing）

### 指南
| 元素 | 字距 | 数值 |
|---------|----------|-------|
| Display | 收紧 | -0.02em |
| 标题 | 正常 | 0 |
| 正文 | 正常 | 0 |
| 全大写 | 加宽 | 0.05em |
| 小型大写字母 | 加宽 | 0.1em |

## 段落间距

### 外边距
```css
/* Heading spacing */
h1, h2 { margin-top: 2rem; margin-bottom: 1rem; }
h3, h4 { margin-top: 1.5rem; margin-bottom: 0.75rem; }

/* Paragraph spacing */
p { margin-bottom: 1rem; }
p + p { margin-top: 0; }
```

### 最大行宽
- 正文：65-75 字符（最佳）
- 标题：可以更宽
- 代码块：80-100 字符

```css
.prose {
  max-width: 65ch;
}
```

## CSS 实现

### 完整变量
```css
:root {
  /* Font Families */
  --font-heading: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Font Sizes */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;

  /* Font Weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-snug: 1.375;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
}
```

### Tailwind 配置
```javascript
theme: {
  fontFamily: {
    heading: ['Inter', 'system-ui', 'sans-serif'],
    body: ['Inter', 'system-ui', 'sans-serif'],
    mono: ['JetBrains Mono', 'monospace'],
  },
  fontSize: {
    xs: ['0.75rem', { lineHeight: '1rem' }],
    sm: ['0.875rem', { lineHeight: '1.25rem' }],
    base: ['1rem', { lineHeight: '1.5rem' }],
    lg: ['1.125rem', { lineHeight: '1.75rem' }],
    xl: ['1.25rem', { lineHeight: '1.75rem' }],
    '2xl': ['1.5rem', { lineHeight: '2rem' }],
    '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
    '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
    '5xl': ['3rem', { lineHeight: '1.1' }],
  }
}
```

## 常见字体搭配

### 简洁现代
- 标题：Inter
- 正文：Inter

### 专业
- 标题：Playfair Display
- 正文：Source Sans Pro

### 创业/科技
- 标题：Poppins
- 正文：Open Sans

### 编辑风
- 标题：Merriweather
- 正文：Lato

## 无障碍

### 最小字号
- 正文：最小 16px
- 小字：最小 14px，不要用于长内容
- 注释文字：最小 12px，尽量少用

### 对比度要求
- 文字与背景：最低 4.5:1（AA 级）
- 大号文字（18px 以上）：最低 3:1

### 最佳实践
- 不要对长文本使用全大写
- 避免两端对齐（用左对齐）
- 确保行间距充足
- 小字号下不要使用过细字重（<400）
