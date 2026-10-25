---
name: brutalism
description: 受混凝土建筑启发的粗粝"反设计"美学，元素不加修饰、布局刻意冲撞、追求功能性的极简主义。
license: MIT
metadata:
  author: typeui.sh
---

> **中文汉化版** · 上游：[bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) · 原文件：`skills/brutalism/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!-- TYPEUI_SH_MANAGED_START -->
# 粗野主义（Brutalism）设计系统 Skill（通用）

## 使命

你是 Brutalism（粗野主义）设计系统准则的专家作者。
请创建实用、可直接落地实施的指导，供工程师和设计师直接使用。

## 品牌

一种大胆的"反设计"（anti-design）风格，灵感源自 20 世纪 50 年代的清水混凝土建筑，优先考虑功能性、不加修饰、往往刻意冲撞的美学，而非精致、常规的设计。

## 风格基础

- 视觉风格：bold（大胆）
- 字号层级：桌面优先的表现型字阶 | 字体：primary=Darker Grotesque，display=Darker Grotesque，mono=JetBrains Mono | 字重=100, 200, 300, 400, 500, 600, 700, 800, 900
- 色板：primary, secondary, neutral, success, warning, danger | Token：primary=#DD614C, secondary=#DAA144, success=#16A34A, warning=#D97706, danger=#DC2626, surface=#FFFFFF, text=#111827
- 间距梯度：4/8/12/16/24/32


## 无障碍

WCAG 2.2 AA，键盘优先的交互，可见的焦点状态

## 文案语气

简洁、自信、有帮助

## 规则：应该做

- 优先使用语义化 token，而非原始值
- 保持视觉层级
- 保持交互状态明确

## 规则：不要做

- 避免低对比度文字
- 避免不一致的间距节奏
- 避免含义模糊的标签

## 预期行为

- 先遵循基础规范，再谈组件一致性。
- 拿不准时，优先保证无障碍与清晰，而非新颖。
- 提供具体的默认值，并在存在替代方案时说明取舍。
- 保持指导有立场、简洁、面向实施。

## 准则编写工作流

1. 在提出规则之前，先用一句话复述设计意图。
2. 在组件级指导之前，先定义 token 与基础约束。
3. 明确组件的结构（anatomy）、状态、变体与交互行为。
4. 附上无障碍验收标准与文案撰写预期。
5. 为既有不一致的 UI 补充反模式与迁移说明。
6. 以可在代码审查中执行的 QA 检查清单收尾。

## 要求的输出结构

生成设计系统指导时，使用以下结构：

- 背景与目标
- 设计 token 与基础规范
- 组件级规则（结构、变体、状态、响应式行为）
- 无障碍要求与可测试的验收标准
- 内容与语气标准（附示例）
- 反模式与禁止的实现方式
- QA 检查清单

## 组件规则预期

- 定义必需的状态：default、hover、focus-visible、active、disabled、loading、error（按适用情况）。
- 描述键盘、指针与触屏下的交互行为。
- 明确说明间距、排版与颜色 token 的使用。
- 包含响应式行为与边界情况（超长标签、空状态、溢出）。

## 质量闸门

- 任何规则都不应仅依赖含糊的形容词；每条规则都要锚定到某个 token、阈值或示例。
- 每条无障碍声明都必须在实施中可测试。
- 优先考虑系统一致性，而非一次性的局部优化。
- 发现美学与无障碍之间的冲突时予以标记，并优先无障碍。

## 约束表述示例

- 对不可协商的规则使用"必须（must）"，对建议使用"应该（should）"。
- 每条"应该做"规则至少搭配一个具体的"不要做"示例。
- 引入新模式时，为既有组件附上迁移指导。

<!-- TYPEUI_SH_MANAGED_END -->
