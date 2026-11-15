> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/slides/references/layout-patterns.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 布局模式

25 种幻灯片布局，带 CSS 结构与动画 class。

## 按用例选择布局

| 布局 | 用例 | 动画 |
|--------|----------|-----------|
| 标题页 | 开场/第一印象 | `animate-fade-up` |
| 问题陈述 | 确立痛点 | `animate-stagger` |
| 方案概览 | 引出方案 | `animate-scale` |
| 功能网格 | 展示能力（3-6 张卡） | `animate-stagger` |
| 指标仪表盘 | 展示 KPI（3-4 个指标） | `animate-stagger-scale` |
| 对比表 | 比较选项 | `animate-fade-up` |
| 时间线 | 展示进程 | `animate-stagger` |
| 团队网格 | 介绍成员 | `animate-stagger` |
| 引言背书 | 客户背书 | `animate-fade-up` |
| 双栏分列 | 对比/对照 | `animate-fade-up` |
| 大数字主视觉 | 单个有力指标 | `animate-count` |
| 产品截图 | 展示产品 UI | `animate-scale` |
| 定价卡 | 呈现档位 | `animate-stagger` |
| CTA 收尾 | 驱动行动 | `animate-pulse` |

## CSS 结构

### 标题页
```css
.slide-title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
```

### 双栏分列
```css
.slide-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 48px;
    align-items: center;
}
@media (max-width: 768px) {
    .slide-split { grid-template-columns: 1fr; gap: 24px; }
}
```

### 功能网格（3 列）
```css
.slide-features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
@media (max-width: 768px) {
    .slide-features { grid-template-columns: repeat(2, 1fr); gap: 16px; }
}
@media (max-width: 480px) {
    .slide-features { grid-template-columns: 1fr; }
}
```

### 指标仪表盘（4 列）
```css
.slide-metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
}
@media (max-width: 768px) {
    .slide-metrics { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 480px) {
    .slide-metrics { grid-template-columns: 1fr; }
}
```

## 组件变体

### 卡片样式
| 样式 | CSS Class | 用途 |
|-------|-----------|---------|
| 图标居左 | `.card-icon-left` | 带图标的功能 |
| 强调条 | `.card-accent-bar` | 突出的功能 |
| 指标卡 | `.card-metric` | 数字/统计 |
| 头像卡 | `.card-avatar` | 团队成员 |
| 定价卡 | `.card-pricing` | 价格档位 |

### 指标样式
| 样式 | 效果 |
|-------|--------|
| `gradient-number` | 数字上的渐变文字 |
| `oversized` | 超大（120px+） |
| `sparkline` | 小型行内图 |
| `funnel-numbers` | 转化漏斗各阶段 |

## 视觉处理

| 处理 | 何时使用 |
|-----------|-------------|
| `gradient-glow` | 标题页、CTA |
| `subtle-border` | 问题陈述 |
| `icon-top` | 功能网格 |
| `screenshot-shadow` | 产品截图 |
| `popular-highlight` | 定价（scale 1.05） |
| `bg-overlay` | 背景图 |
| `contrast-pair` | 前后对比 |
| `logo-grayscale` | 客户 Logo |

## 搜索命令

```bash
# Find layout for specific use
python ../design-system/scripts/search-slides.py "metrics dashboard" -d layout

# Contextual recommendation
python ../design-system/scripts/search-slides.py "traction slide" \
  --context --position 4 --total 10
```

## 布局决策流程

```
1. What's the slide goal?
   └─> Search layout-logic.csv

2. What emotion should it trigger?
   └─> Search color-logic.csv

3. What's the content type?
   └─> Search typography.csv

4. Should it break pattern?
   └─> Check position (1/3, 2/3) → Use full-bleed
```
