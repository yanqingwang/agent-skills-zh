---
name: slides
description: 借助 Chart.js、设计 token、响应式布局、文案写作公式与情境化的幻灯片策略，创建策略导向的 HTML 演示文稿。
argument-hint: "[topic] [slide-count]"
metadata:
  author: claudekit
  version: "1.0.0"
---

> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/slides/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Slides（幻灯片）

策略导向的 HTML 演示文稿设计，融合数据可视化。

## 何时应用

- 营销演示与商业路演（pitch deck）幻灯片
- 基于 Chart.js 的数据驱动幻灯片
- 结合布局模式的策略导向幻灯片设计
- 经过文案写作优化的演示内容

## 子命令

| 子命令 | 说明 | 参考文件 |
|--------|------|----------|
| `create` | 创建策略导向的演示幻灯片 | `references/create.md` |

## 脚本路径

本 Skill 及其 `references/` 中的脚本路径均相对于包含本 SKILL.md 的目录，而非相对于项目：`scripts/<file>` 指本 Skill 自己的 `scripts/` 文件夹，`../<skill>/scripts/<file>` 指与之并列安装的同级子 Skill。请从该目录构建完整路径（Skill 加载时 Claude Code 会将其报告为该 Skill 的基准目录），并将工作目录保持在项目根目录——脚本会以项目根为基准读写 `docs/brand-guidelines.md`、`assets/design-tokens.json`、`src/` 等项目文件。

## 参考文件（知识库）

| 主题 | 文件 |
|------|------|
| 布局模式 | `references/layout-patterns.md` |
| HTML 模板 | `references/html-template.md` |
| 文案写作公式 | `references/copywriting-formulas.md` |
| 幻灯片策略 | `references/slide-strategies.md` |

## 路由

1. 从 `$ARGUMENTS` 中解析子命令（第一个词）
2. 加载对应的 `references/{subcommand}.md`
3. 用其余参数执行
