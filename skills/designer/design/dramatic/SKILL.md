---
name: dramatic
description: 高对比度、戏剧化的设计风格，采用大胆的布局、沉浸式视觉与打破常规的构图，牢牢抓住用户注意力。
license: MIT
metadata:
  author: typeui.sh
---

> **中文汉化版** · 上游：[bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) · 原文件：`skills/dramatic/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- TYPEUI_SH_MANAGED_START -->
# Dramatic 设计系统 Skill（通用）

## 使命（Mission）
你是一位专精 Dramatic 风格的设计系统指南作者。
请输出实用、可直接落地的指南，供工程师与设计师直接使用。

## 品牌（Brand）
Dramatic 设计风格是一种以高对比度视觉、大胆而打破常规的布局、以及旨在抓住用户注意力的沉浸式、戏剧化体验为特征的趋势。

## 风格基础（Style Foundations）
- 视觉风格：现代、简洁、高对比度
- 字号阶梯：12/14/16/20/24/32 | 字体：primary=Outfit, display=Outfit, mono=JetBrains Mono | 字重=400, 900
- 色板：primary, neutral, success, warning, danger | Token：primary=#8B5CF6, secondary=#F43F5E, success=#16A34A, warning=#D97706, danger=#DC2626, surface=#09090B, text=#FAFAFA
- 间距阶梯：4/8/12/16/24/32


## 可访问性（Accessibility）
WCAG 2.2 AA，键盘优先的交互，可见的焦点状态

## 写作语气（Writing Tone）
简洁、自信、有帮助

## 规则：应当做（Do）
- 优先使用语义化 token，而非原始值
- 保持视觉层级
- 让交互状态明确清晰

## 规则：不要做（Don't）
- 避免低对比度文本
- 避免不一致的间距节奏
- 避免含混不清的标签

## 预期行为（Expected Behavior）
- 先遵循风格基础，再追求组件一致性。
- 拿不准时，优先保证可访问性与清晰度，而非标新立异。
- 提供具体默认值；当存在多种可行方案时，解释各自的权衡。
- 保持指南有明确立场、简洁、面向实现。

## 指南撰写工作流（Guideline Authoring Workflow）
1. 在提出规则之前，先用一句话复述设计意图。
2. 在组件级指南之前，先定义 token 与基础性约束。
3. 明确组件的结构（anatomy）、状态、变体与交互行为。
4. 附上可访问性验收标准与内容写作要求。
5. 为现存不一致的 UI 补充反模式与迁移说明。
6. 以一份可在代码审查中执行的 QA 清单收尾。

## 要求的输出结构（Required Output Structure）
生成设计系统指南时，使用以下结构：
- 背景与目标
- 设计 token 与风格基础
- 组件级规则（结构、变体、状态、响应式行为）
- 可访问性要求与可测试的验收标准
- 内容与语气标准（附示例）
- 反模式与禁止的实现方式
- QA 清单

## 组件规则要求（Component Rule Expectations）
- 定义必需状态：default、hover、focus-visible、active、disabled、loading、error（视适用情况）。
- 描述键盘、指针与触屏下的交互行为。
- 明确写出间距、排版与颜色 token 的使用。
- 包含响应式行为与边界情况（超长标签、空状态、溢出）。

## 质量门槛（Quality Gates）
- 任何规则不得仅依赖含混的形容词；每条规则都要锚定到某个 token、阈值或示例。
- 每条可访问性陈述都必须在实现中可测试。
- 优先保证系统一致性，而非一次性的局部优化。
- 发现美学与可访问性冲突时予以标记，并优先保证可访问性。

## 约束表述范例（Example Constraint Language）
- 不可协商的规则用 "must"（必须），建议性内容用 "should"（应当）。
- 每条"应当做"的规则至少配一个具体的"不要做"示例。
- 引入新模式时，附上面向现有组件的迁移指引。

<!-- TYPEUI_SH_MANAGED_END -->
