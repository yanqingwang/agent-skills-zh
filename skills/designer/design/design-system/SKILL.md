---
name: design-system
description: Token 架构、组件规格与幻灯片生成。三层 token（primitive→semantic→component）、CSS 变量、间距/字体排印刻度、组件规格、策略化幻灯片创建。适用于设计 token、系统化设计、符合品牌规范的演示文稿。
argument-hint: "[component or token]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---

> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design-system/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 设计系统（Design System）

Token 架构、组件规格、系统化设计与幻灯片生成。

## 何时应用

- 设计 token 创建
- 组件状态定义
- CSS 变量体系
- 间距/字体排印刻度
- 设计到代码的交接
- Tailwind 主题配置
- **幻灯片/演示文稿生成**

## Token 架构

加载：`references/token-architecture.md`

### 三层结构

```
Primitive (raw values)
       ↓
Semantic (purpose aliases)
       ↓
Component (component-specific)
```

**示例：**
```css
/* Primitive */
--color-blue-600: #2563EB;

/* Semantic */
--color-primary: var(--color-blue-600);

/* Component */
--button-bg: var(--color-primary);
```

## 脚本路径

本 Skill 及其 `references/` 中的脚本路径相对于包含本 SKILL.md 的目录，而非项目目录：`scripts/<file>` 指本 Skill 自身的 `scripts/` 文件夹，`../<skill>/scripts/<file>` 指随之一并安装的同级子 Skill。请基于该目录构建完整路径（Skill 加载时 Claude Code 会将其报告为该 Skill 的基准目录），并把工作目录保持在项目根目录——脚本会相对于项目根目录读写 `docs/brand-guidelines.md`、`assets/design-tokens.json`、`src/` 等项目文件。

## 快速上手

**生成 token：**
```bash
node scripts/generate-tokens.cjs --config tokens.json -o tokens.css
```

**校验使用情况：**
```bash
node scripts/validate-tokens.cjs --dir src/
```

## 参考资料

| 主题 | 文件 |
|-------|------|
| Token 架构 | `references/token-architecture.md` |
| Primitive token | `references/primitive-tokens.md` |
| Semantic token | `references/semantic-tokens.md` |
| Component token | `references/component-tokens.md` |
| 组件规格 | `references/component-specs.md` |
| 状态与变体 | `references/states-and-variants.md` |
| Tailwind 集成 | `references/tailwind-integration.md` |

## 组件规格模式

| 属性 | 默认 | 悬停 | 激活 | 禁用 |
|----------|---------|-------|--------|----------|
| 背景 | primary | primary-dark | primary-darker | muted |
| 文本 | white | white | white | muted-fg |
| 边框 | none | none | none | muted-border |
| 阴影 | sm | md | none | none |

## 脚本

| 脚本 | 用途 |
|--------|---------|
| `generate-tokens.cjs` | 从 JSON token 配置生成 CSS |
| `validate-tokens.cjs` | 检查代码中的硬编码值 |
| `search-slides.py` | BM25 检索 + 上下文推荐 |
| `slide-token-validator.py` | 校验幻灯片 HTML 的 token 合规性 |
| `fetch-background.py` | 从 Pexels/Unsplash 抓取图片 |

## 模板

| 模板 | 用途 |
|----------|---------|
| `design-tokens-starter.json` | 含三层结构的入门 JSON |

## 集成

**与 brand 配合：**从品牌色彩/字体排印中提取 primitive token
**与 ui-styling 配合：**组件 token → Tailwind 配置

**Skill 依赖：**brand、ui-styling
**主要 Agent：**ui-ux-designer、frontend-developer

## 幻灯片系统

基于设计 token + Chart.js + 上下文决策系统的符合品牌规范的演示文稿。

### 事实来源（Source of Truth）

| 文件 | 用途 |
|------|---------|
| `docs/brand-guidelines.md` | 品牌识别、语气、色彩 |
| `assets/design-tokens.json` | Token 定义（primitive→semantic→component） |
| `assets/design-tokens.css` | CSS 变量（在幻灯片中导入） |
| `assets/css/slide-animations.css` | CSS 动画库 |

### 幻灯片检索（BM25）

```bash
# Basic search (auto-detect domain)
python scripts/search-slides.py "investor pitch"

# Domain-specific search
python scripts/search-slides.py "problem agitation" -d copy
python scripts/search-slides.py "revenue growth" -d chart

# Contextual search (Premium System)
python scripts/search-slides.py "problem slide" --context --position 2 --total 9
python scripts/search-slides.py "cta" --context --position 9 --prev-emotion frustration
```

### 决策系统 CSV

| 文件 | 用途 |
|------|---------|
| `data/slide-strategies.csv` | 15 套演示文稿结构 + 情绪弧线 + sparkline 节拍 |
| `data/slide-layouts.csv` | 25 种布局 + 组件变体 + 动画 |
| `data/slide-layout-logic.csv` | 目标 → 布局 + break_pattern 标志 |
| `data/slide-typography.csv` | 内容类型 → 字体排印刻度 |
| `data/slide-color-logic.csv` | 情绪 → 色彩处理 |
| `data/slide-backgrounds.csv` | 幻灯片类型 → 图片类别（Pexels/Unsplash） |
| `data/slide-copy.csv` | 25 个文案公式（PAS、AIDA、FAB） |
| `data/slide-charts.csv` | 25 种图表类型及 Chart.js 配置 |

### 上下文决策流程

```
1. Parse goal/context
        ↓
2. Search slide-strategies.csv → Get strategy + emotion beats
        ↓
3. For each slide:
   a. Query slide-layout-logic.csv → layout + break_pattern
   b. Query slide-typography.csv → type scale
   c. Query slide-color-logic.csv → color treatment
   d. Query slide-backgrounds.csv → image if needed
   e. Apply animation class from slide-animations.css
        ↓
4. Generate HTML with design tokens
        ↓
5. Validate with slide-token-validator.py
```

### 模式打破（Duarte Sparkline）

高端演示文稿会在情绪之间交替切换以增强感染力：
```
"What Is" (frustration) ↔ "What Could Be" (hope)
```

系统会在 1/3 与 2/3 位置计算模式打破点。

### 幻灯片要求

**所有幻灯片必须：**
1. 导入 `assets/design-tokens.css` —— 唯一事实来源
2. 使用 CSS 变量：`var(--color-primary)`、`var(--slide-bg)` 等
3. 图表使用 Chart.js（不要只用 CSS 条形）
4. 包含导航（键盘方向键、点击、进度条）
5. 内容居中对齐
6. 聚焦说服/转化

### Chart.js 集成

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

<canvas id="revenueChart"></canvas>
<script>
new Chart(document.getElementById('revenueChart'), {
    type: 'line',
    data: {
        labels: ['Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            data: [5, 12, 28, 45],
            borderColor: '#FF6B6B',  // Use brand coral
            backgroundColor: 'rgba(255, 107, 107, 0.1)',
            fill: true,
            tension: 0.4
        }]
    }
});
</script>
```

### Token 合规性

```css
/* CORRECT - uses token */
background: var(--slide-bg);
color: var(--color-primary);
font-family: var(--typography-font-heading);

/* WRONG - hardcoded */
background: #0D0D0D;
color: #FF6B6B;
font-family: 'Space Grotesk';
```

### 参考实现

包含全部功能的可运行示例：
```
assets/designs/slides/claudekit-pitch-251223.html
```

### 命令

```bash
/slides:create "10-slide investor pitch for ClaudeKit Marketing"
```

## 最佳实践

1. 组件中绝不使用原始十六进制色值——始终引用 token
2. 语义层支持主题切换（浅色/深色）
3. 组件 token 支持逐组件定制
4. 使用 HSL 格式控制透明度
5. 为每个 token 记录用途
6. **幻灯片必须导入 design-tokens.css 并只使用 var()**
