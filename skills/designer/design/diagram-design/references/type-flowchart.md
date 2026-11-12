> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/type-flowchart.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 流程图

**适用场景：** 决策逻辑、算法、面向用户的分支流程（"我该不该……？"）、新手引导路由、支持分诊树。

## 布局约定
- 形状承载类型，不靠颜色：
  - **椭圆**（`rx=20`）：起点 / 终点
  - **矩形**（`rx=6`）：步骤 / 动作
  - **菱形**：判断（≤3 个出口）
  - **小的实心 ink 圆点**（`r=4`）：分支重新汇合的合流点
- 流程自上而下。菱形的惯例出口：Yes 向右，No 向下：但无论如何每条出向箭头都要有标签。
- coral 用在 happy path *或*唯一一个后果最重的判断上：绝不用在每个判断上。
- 如果两条箭头必须交叉，在其中一条上做一个小弧形跳线，让交叉可读。

## 反模式
- 用填充颜色区分节点类型（形状已经做了）。
- 判断菱形有 4 个以上出口：重构成嵌套菱形。
- 判断分支无标签。

## 示例
- `assets/example-flowchart.html` — 极简浅色
- `assets/example-flowchart-dark.html` — 极简深色
- `assets/example-flowchart-full.html` — 完整编辑排版
