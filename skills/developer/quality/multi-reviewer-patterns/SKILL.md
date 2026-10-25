---
name: multi-reviewer-patterns
description: 跨多个质量维度协调并行代码审查，包括发现项去重、严重性校准与整合报告。在组织多审查者代码审查、校准发现项严重性或整合审查结果时使用本 Skill。
version: 1.0.2
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/multi-reviewer-patterns/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 多审查者模式（Multi-Reviewer Patterns）

用于协调跨多个质量维度的并行代码审查、发现项去重、严重性校准以及产出整合报告的模式。

## 何时使用本 Skill

- 组织一次多维度代码审查
- 决定分配哪些审查维度
- 对来自多个审查者的发现项去重
- 一致地校准严重性评级
- 产出整合的审查报告

## 审查维度分配

### 可用维度

| 维度             | 侧重点                                   | 何时纳入                                       |
| ---------------- | --------------------------------------- | ------------------------------------------- |
| **安全（Security）**      | 漏洞、认证、输入验证 | 凡是处理用户输入或认证的代码一律纳入 |
| **性能（Performance）**   | 查询效率、内存、缓存       | 更改数据访问或热点路径时                     |
| **架构（Architecture）**  | SOLID、耦合、模式               | 结构性变更或新模块                           |
| **测试（Testing）**       | 覆盖率、质量、边界情况           | 新增功能时                                  |
| **无障碍（Accessibility）** | WCAG、ARIA、键盘导航                | UI/前端变更                                 |

### 推荐组合

| 场景                   | 维度                                         |
| ---------------------- | -------------------------------------------- |
| API 端点变更           | 安全、性能、架构                             |
| 前端组件               | 架构、测试、无障碍                           |
| 数据库迁移             | 性能、架构                                   |
| 认证变更               | 安全、测试                                   |
| 完整功能审查           | 安全、性能、架构、测试                       |

## 发现项去重

当多个审查者在同一位置报告问题时：

### 合并规则

1. **同文件：行号，同一问题** — 合并为一个发现项，署名所有审查者
2. **同文件：行号，不同问题** — 保留为独立发现项
3. **同一问题，不同位置** — 保留为独立发现项，但相互交叉引用
4. **严重性冲突** — 采用较高的严重性评级
5. **修复建议冲突** — 两者都保留，并标注审查者归属

### 去重流程

```
For each finding in all reviewer reports:
  1. Check if another finding references the same file:line
  2. If yes, check if they describe the same issue
  3. If same issue: merge, keeping the more detailed description
  4. If different issue: keep both, tag as "co-located"
  5. Use highest severity among merged findings
```

## 严重性校准

### 严重性标准

| 严重性         | 影响                                           | 可能性                   | 示例                                         |
| ------------ | --------------------------------------------- | ---------------------- | -------------------------------------------- |
| **Critical（严重）** | 数据丢失、安全入侵、彻底失败   | 必然或极有可能 | SQL 注入、认证绕过、数据损坏  |
| **High（高）**     | 显著的功能影响、性能退化 | 很可能                 | 内存泄漏、缺失校验、流程中断 |
| **Medium（中）**   | 部分影响、存在变通方案             | 有可能               | N+1 查询、遗漏边界情况、错误信息不清  |
| **Low（低）**      | 影响极小、外观问题                       | 不太可能               | 风格问题、次要优化、命名      |

### 校准规则

- 外部用户可利用的安全漏洞：一律 Critical 或 High
- 热点路径中的性能问题：至少 Medium
- 关键路径缺失测试：至少 Medium
- 核心功能的无障碍违规：至少 Medium
- 无功能影响的代码风格问题：Low

## 整合报告模板

```markdown
## Code Review Report

**Target**: {files/PR/directory}
**Reviewers**: {dimension-1}, {dimension-2}, {dimension-3}
**Date**: {date}
**Files Reviewed**: {count}

### Critical Findings ({count})

#### [CR-001] {Title}

**Location**: `{file}:{line}`
**Dimension**: {Security/Performance/etc.}
**Description**: {what was found}
**Impact**: {what could happen}
**Fix**: {recommended remediation}

### High Findings ({count})

...

### Medium Findings ({count})

...

### Low Findings ({count})

...

### Summary

| Dimension    | Critical | High  | Medium | Low   | Total  |
| ------------ | -------- | ----- | ------ | ----- | ------ |
| Security     | 1        | 2     | 3      | 0     | 6      |
| Performance  | 0        | 1     | 4      | 2     | 7      |
| Architecture | 0        | 0     | 2      | 3     | 5      |
| **Total**    | **1**    | **3** | **9**  | **5** | **18** |

### Recommendation

{Overall assessment and prioritized action items}
```
