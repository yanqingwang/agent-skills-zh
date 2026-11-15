> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/brand/references/color-palette-management.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 配色管理（Color Palette Management）

定义、提取与执行品牌配色的指南。

## 颜色体系结构

### 层级
```
Primary Colors (1-2)
├── Main brand color - Used for CTAs, headers, key elements
└── Supporting primary - Secondary emphasis

Secondary Colors (2-3)
├── Accent colors - Highlights, interactive states
└── Supporting visuals - Icons, illustrations

Neutral Palette (3-5)
├── Background colors - Page, card, modal backgrounds
├── Text colors - Headings, body, muted text
└── UI elements - Borders, dividers, shadows

Semantic Colors (4)
├── Success - #22C55E (green)
├── Warning - #F59E0B (amber)
├── Error - #EF4444 (red)
└── Info - #3B82F6 (blue)
```

## 颜色文档格式

### Markdown 表格
```markdown
| Name | Hex | RGB | HSL | Usage |
|------|-----|-----|-----|-------|
| Primary Blue | #2563EB | rgb(37,99,235) | hsl(217,91%,53%) | CTAs, links |
```

### CSS 变量
```css
:root {
  /* Primary */
  --color-primary: #2563EB;
  --color-primary-light: #3B82F6;
  --color-primary-dark: #1D4ED8;

  /* Secondary */
  --color-secondary: #8B5CF6;
  --color-accent: #F59E0B;

  /* Neutral */
  --color-background: #FFFFFF;
  --color-surface: #F9FAFB;
  --color-text-primary: #111827;
  --color-text-secondary: #6B7280;
  --color-border: #E5E7EB;
}
```

### Tailwind 配置
```javascript
colors: {
  primary: {
    DEFAULT: '#2563EB',
    50: '#EFF6FF',
    100: '#DBEAFE',
    500: '#3B82F6',
    600: '#2563EB',
    700: '#1D4ED8',
  }
}
```

## 无障碍要求

### 对比度要求（WCAG 2.1）
| 级别 | 普通文本 | 大号文本 | UI 组件 |
|-------|-------------|------------|---------------|
| AA | 4.5:1 | 3:1 | 3:1 |
| AAA | 7:1 | 4.5:1 | 4.5:1 |

### 检查对比度
```javascript
// Formula for relative luminance
function luminance(r, g, b) {
  const [rs, gs, bs] = [r, g, b].map(v => {
    v /= 255;
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function contrastRatio(l1, l2) {
  const lighter = Math.max(l1, l2);
  const darker = Math.min(l1, l2);
  return (lighter + 0.05) / (darker + 0.05);
}
```

## 颜色提取

### 从图片提取
用 `extract-colors.cjs` 脚本来：
1. 加载图片文件
2. 用 k-means 聚类提取主色
3. 映射到最接近的品牌色
4. 报告合规百分比

### 从品牌指南提取
解析 markdown 以提取：
- 表格中的 Hex 值
- CSS 变量定义
- 颜色名称与用途描述

## 品牌合规校验

### 规则
1. **主色占比**：设计的 60-70%
2. **辅色占比**：设计的 20-30%
3. **强调色占比**：设计的 5-10%
4. **脱离品牌容忍度**：非调色板颜色最多 20%

### 校验输出
```json
{
  "compliance": 85,
  "colors": {
    "brand": ["#2563EB", "#8B5CF6", "#FFFFFF"],
    "offBrand": ["#FF5500"],
    "dominant": "#2563EB"
  },
  "issues": [
    "Off-brand color #FF5500 detected (15% coverage)",
    "Primary color underused (45% vs 60% target)"
  ]
}
```

## 颜色使用指南

### 该做的
- 主色用于主要 CTA 与关键元素
- 保持一致的 hover/active 状态
- 对所有组合做无障碍测试
- 把颜色决定写成文档

### 不该做的
- 单个组件里用超过 2-3 种颜色
- 无意图地混用暖冷色调
- 文字用纯黑 (#000)（应改用 #111 或近似值）
- 只靠颜色传达含义（还要配图标/文字）

## 配色方案示例

### 科技/SaaS
```
Primary: #2563EB (Blue)
Secondary: #8B5CF6 (Purple)
Accent: #10B981 (Emerald)
Background: #F9FAFB
Text: #111827
```

### 营销/创意
```
Primary: #F97316 (Orange)
Secondary: #EC4899 (Pink)
Accent: #14B8A6 (Teal)
Background: #FFFFFF
Text: #1F2937
```

### 专业/企业
```
Primary: #1E40AF (Navy)
Secondary: #475569 (Slate)
Accent: #0EA5E9 (Sky)
Background: #F8FAFC
Text: #0F172A
```

## 工具与资源

- [Coolors](https://coolors.co) - 生成配色
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Tailwind Color Reference](https://tailwindcss.com/docs/customizing-colors)
- [Color Hunt](https://colorhunt.co) - 精选配色
