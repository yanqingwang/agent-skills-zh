---
name: wcag-audit-patterns
description: 开展 WCAG 2.2 无障碍审计，涵盖自动化测试、人工验证与修复指导。在审计网站无障碍性、修复 WCAG 违规或实现无障碍设计模式时使用。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/accessibility-compliance/skills/wcag-audit-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# WCAG 审计模式

对照 WCAG 2.2 指南审计 Web 内容的全面指南，附可落地的修复策略。

## 何时使用本 Skill

- 开展无障碍审计
- 修复 WCAG 违规
- 实现无障碍组件
- 为无障碍诉讼做准备
- 满足 ADA/Section 508 要求
- 达成 VPAT 合规

## 核心概念

### 1. WCAG 符合性级别

| 级别    | 说明           | 适用场景     |
| ------- | -------------- | ------------ |
| **A**   | 最低无障碍要求 | 法律基线     |
| **AA**  | 标准符合性     | 大多数法规   |
| **AAA** | 增强无障碍     | 特殊需求     |

### 2. POUR 原则

```
Perceivable:  Can users perceive the content?
Operable:     Can users operate the interface?
Understandable: Can users understand the content?
Robust:       Does it work with assistive tech?
```

### 3. 按影响程度分类的常见违规

```
Critical (Blockers):
├── Missing alt text for functional images
├── No keyboard access to interactive elements
├── Missing form labels
└── Auto-playing media without controls

Serious:
├── Insufficient color contrast
├── Missing skip links
├── Inaccessible custom widgets
└── Missing page titles

Moderate:
├── Missing language attribute
├── Unclear link text
├── Missing landmarks
└── Improper heading hierarchy
```

## 详细模式与完整示例

详细模式文档位于 `references/details.md`。当上述导航层级不够用时，请阅读该文件。

## 最佳实践

### 应该做的

- **尽早开始** - 从设计阶段就考虑无障碍
- **与真实用户一起测试** - 残障用户提供最好的反馈
- **能自动化的尽量自动化** - 30-50% 的问题可被检测
- **使用语义化 HTML** - 减少 ARIA 需求
- **文档化模式** - 构建无障碍组件库

### 不该做的

- **不要只依赖自动化测试** - 人工测试必不可少
- **不要把 ARIA 当作首选方案** - 原生 HTML 优先
- **不要隐藏焦点轮廓** - 键盘用户需要它们
- **不要禁用缩放** - 用户需要调整大小
- **不要只靠颜色** - 需要多种指示方式
