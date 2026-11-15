---
# gstack: design-md-format=spec
name: gstack
typography:
  display:
    fontFamily: Satoshi
  body:
    fontFamily: DM Sans
  label:
    fontFamily: DM Sans
  mono:
    fontFamily: JetBrains Mono
    fontFeature: tnum
colors:
  primary-dark-mode: "#F59E0B"
  primary-light-mode: "#D97706"
  primary-text-accent-dark-mode: "#FBBF24"
  primary-text-accent-light-mode: "#B45309"
  zinc-50: "#FAFAFA"
  zinc-400: "#A1A1AA"
  zinc-600: "#52525B"
  zinc-800: "#27272A"
  surface-dark: "#141414"
  base-dark: "#0C0C0C"
  surface-light: "#FFFFFF"
  base-light: "#FAFAF9"
  border-dark: "#262626"
  border-light: "#E7E5E4"
  success: "#22C55E"
  warning: "#F59E0B"
  error: "#EF4444"
  info: "#3B82F6"
spacing:
  2xs: 2px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
---

> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/DESIGN.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 设计系统 — gstack

## Overview

- **这是什么：** gstack 的社区网站。gstack 是一个把 Claude Code 变成虚拟工程团队的 CLI 工具
- **给谁用：** 发现 gstack 的开发者，以及现有社区成员
- **领域/行业：** 开发者工具（同侪：Linear、Raycast、Warp、Zed）
- **项目类型：** 社区 dashboard + 营销站点

- **方向：** Industrial/Utilitarian（工业/实用主义），功能优先、数据密集，等宽字体作为个性字体
- **装饰程度：** Intentional（有意图的），表面叠加细微噪点/颗粒纹理以增加质感
- **氛围：** 一个在乎工艺的人打造的严肃工具。温暖，不冰冷。CLI 出身就是品牌本身。
- **参考站点：** formulae.brew.sh（竞品，但我们的版本在线且可交互）、Linear（深色 + 克制）、Warp（暖色点缀）

## Colors

- **方法：** Restrained（克制），amber 强调色稀少而有意义。颜色给 dashboard 数据；界面框架保持中性。
- **Primary（深色模式）：** amber-500 #F59E0B，温暖、有能量，读作"终端光标"
- **Primary（浅色模式）：** amber-600 #D97706，更深以便在白色背景上形成对比
- **Primary 文本强调（深色模式）：** amber-400 #FBBF24
- **Primary 文本强调（浅色模式）：** amber-700 #B45309
- **中性色：** 冷调 zinc 灰
  - zinc-50: #FAFAFA（最浅）
  - zinc-400: #A1A1AA
  - zinc-600: #52525B
  - zinc-800: #27272A
  - Surface（深色）：#141414
  - Base（深色）：#0C0C0C
  - Surface（浅色）：#FFFFFF
  - Base（浅色）：#FAFAF9
- **语义色：** success #22C55E、warning #F59E0B、error #EF4444、info #3B82F6
- **深色模式：** 默认。近黑基底（#0C0C0C），surface 卡片 #141414，边框 #262626。
- **浅色模式：** 暖石色基底（#FAFAF9），白色 surface 卡片，石色边框（#E7E5E4）。amber 强调色切换为 amber-600 以保证对比度。

## Typography

- **Display/Hero：** Satoshi（Black 900 / Bold 700），几何形带温度，字形独特（小写 'a' 与 'g'）。不是 Inter，不是 Geist。从 Fontshare CDN 加载。
- **Body：** DM Sans（Regular 400 / Medium 500 / Semibold 600），干净、易读，比几何形 display 略亲切。从 Google Fonts 加载。
- **UI/Labels：** DM Sans（与 body 相同）
- **Data/Tables：** JetBrains Mono（Regular 400 / Medium 500），个性字体。支持 tabular-nums。等宽字体应突出使用，而不是藏在代码块里。从 Google Fonts 加载。
- **Code：** JetBrains Mono
- **加载：** DM Sans + JetBrains Mono 用 Google Fonts，Satoshi 用 Fontshare。使用 `display=swap`。
- **字号阶梯：**
  - Hero: 72px / clamp(40px, 6vw, 72px)
  - H1: 48px
  - H2: 32px
  - H3: 24px
  - H4: 18px
  - Body: 16px
  - Small: 14px
  - Caption: 13px
  - Micro: 12px
  - Nano: 11px（JetBrains Mono 标签）

## Layout

- **方法：** dashboard 用严格网格，landing page 用杂志式 hero
- **网格：** lg+ 为 12 列，移动端为 1 列
- **最大内容宽度：** 1200px（6xl）
- **圆角：** sm:4px、md:8px、lg:12px、full:9999px
  - 卡片/面板：lg（12px）
  - 按钮/输入框：md（8px）
  - 徽章/胶囊：full（9999px）
  - Skill 条：sm（4px）

### Spacing
- **基础单位：** 4px
- **密度：** Comfortable（舒适），不拥挤（不是 Bloomberg Terminal），不空旷（不是营销站点）
- **阶梯：** 2xs(2px) xs(4px) sm(8px) md(16px) lg(24px) xl(32px) 2xl(48px) 3xl(64px)

## Motion

- **方法：** Minimal-functional（最小功能主义），只保留帮助理解的过渡。dashboard 的 live feed 本身就是动效。
- **缓动：** enter(ease-out / cubic-bezier(0.16,1,0.3,1)) exit(ease-out) move(ease-in-out)
- **时长：** micro(50-100ms) short(150ms) medium(250ms) long(400ms)
- **动画元素：** live feed 圆点脉冲（2s infinite）、skill 条填充（600ms ease-out）、hover 状态（150ms）

## Grain Texture

给整页叠加细微噪点以增加质感：
- 深色模式：opacity 0.03
- 浅色模式：opacity 0.02
- 用 SVG feTurbulence 滤镜作为 body::after 的 CSS background-image
- pointer-events: none、position: fixed、z-index: 9999

## Decisions Log

| 日期 | 决定 | 理由 |
|------|----------|-----------|
| 2026-03-21 | 初始设计系统 | 由 /design-consultation 创建。工业美学、暖 amber 强调色、Satoshi + DM Sans + JetBrains Mono。 |
| 2026-03-21 | 浅色模式用 amber-600 | amber-500 在白色上太亮/发灰；amber-700 太棕/发褐。amber-600 是最佳点。 |
| 2026-03-21 | 颗粒纹理 | 给平坦深色表面增加质感。避免"通用 SaaS 模板"式的千篇一律。 |
| 2026-09-08 | 开放 DESIGN.md 格式 | 用 `gstack-design-md convert` 转换：token 放入 frontmatter，使用标准小节，Motion 与 Decisions Log 保留为附加项。DM Sans 仍是正文字体：它在"过度用作 display"名单上，而在 Operate 表面上作 body/UI 用途属于 role-scoped 规则允许的例外。 |
| 2026-09-08 | Live feed 脉冲是唯一的 authored 动效时刻 | live-feed 圆点上的 2s 脉冲是唯一的 authored 动效时刻，是对 pulsing-dot 目录规则的有意例外。skill 条填充与 150ms hover 过渡是功能性状态过渡，不是 authored 时刻。 |
| 2026-09-08 | JetBrains Mono 数据标签用 11px | Nano（11px）数据标签使用 JetBrains Mono，低于 12px 的 UI 文本下限；UI 标签保持 DM Sans（`typography.label` token）。记录在案，使检测器的 undersized-ui-text 与 monospace-costume 行读作"已决定"，而非"未决"。 |
