---
name: claude-md-improver
description: 审计并改进仓库中的 CLAUDE.md 文件。当用户要求检查、审计、更新、改进或修复 CLAUDE.md 文件时使用。扫描所有 CLAUDE.md 文件，依据模板评估质量，输出质量报告，然后进行针对性更新。当用户提到 "CLAUDE.md maintenance"（CLAUDE.md 维护）或 "project memory optimization"（项目记忆优化）时也应使用。
tools: Read, Glob, Grep, Bash, Edit
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/claude-md-management/skills/claude-md-improver/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CLAUDE.md Improver

审计、评估并改进整个代码库中的 CLAUDE.md 文件，确保 Claude Code 获得最优的项目上下文。

**本 Skill 会写入 CLAUDE.md 文件。** 在呈现质量报告并获得用户批准后，它会对 CLAUDE.md 文件进行针对性的更新。

## 工作流

### 阶段 1：发现

找出仓库中所有 CLAUDE.md 文件：

```bash
find . -name "CLAUDE.md" -o -name ".claude.md" -o -name ".claude.local.md" 2>/dev/null | head -50
```

**文件类型与位置：**

| 类型 | 位置 | 用途 |
|------|----------|---------|
| 项目根目录 | `./CLAUDE.md` | 主要项目上下文（提交进 git，与团队共享） |
| 本地覆盖 | `./.claude.local.md` | 个人/本地设置（被 gitignore，不共享） |
| 全局默认 | `~/.claude/CLAUDE.md` | 跨所有项目的用户级默认设置 |
| 包级专属 | `./packages/*/CLAUDE.md` | monorepo 中的模块级上下文 |
| 子目录 | 任意嵌套位置 | 特性/领域专属上下文 |

**注意：** Claude 会自动发现父目录中的 CLAUDE.md 文件，因此 monorepo 结构可以自动生效。

### 阶段 2：质量评估

对每个 CLAUDE.md 文件，依据质量标准进行评估。详细的评分细则见 [references/quality-criteria.md](references/quality-criteria.md)。

**快速评估清单：**

| 标准 | 权重 | 检查项 |
|-----------|--------|-------|
| 命令/工作流已记录 | 高 | 是否包含构建/测试/部署命令？ |
| 架构清晰度 | 高 | Claude 能否理解代码库结构？ |
| 非显而易见的模式 | 中 | 是否记录了坑点与怪癖？ |
| 简洁性 | 中 | 是否没有冗长的解释或显而易见的信息？ |
| 时效性 | 高 | 是否反映了代码库的当前状态？ |
| 可执行性 | 高 | 指令是否可直接执行，而非含糊其辞？ |

**质量评分：**
- **A (90-100)**：全面、时效、可执行
- **B (70-89)**：覆盖良好，存在小缺口
- **C (50-69)**：仅有基础信息，缺少关键章节
- **D (30-49)**：内容稀疏或已过时
- **F (0-29)**：缺失或严重过时

### 阶段 3：质量报告输出

**在进行任何更新之前，务必先输出质量报告。**

格式：

```
## CLAUDE.md Quality Report

### Summary
- Files found: X
- Average score: X/100
- Files needing update: X

### File-by-File Assessment

#### 1. ./CLAUDE.md (Project Root)
**Score: XX/100 (Grade: X)**

| Criterion | Score | Notes |
|-----------|-------|-------|
| Commands/workflows | X/20 | ... |
| Architecture clarity | X/20 | ... |
| Non-obvious patterns | X/15 | ... |
| Conciseness | X/15 | ... |
| Currency | X/15 | ... |
| Actionability | X/15 | ... |

**Issues:**
- [List specific problems]

**Recommended additions:**
- [List what should be added]

#### 2. ./packages/api/CLAUDE.md (Package-specific)
...
```

### 阶段 4：针对性更新

输出质量报告后，先请求用户确认，再进行更新。

**更新准则（关键）：**

1. **只提出针对性的增补** - 聚焦真正有用的信息：
   - 分析过程中发现的命令或工作流
   - 在代码中发现的坑点或非显而易见的模式
   - 此前不清晰的包之间的关系
   - 行之有效的测试方法
   - 配置上的怪癖

2. **保持精简** - 避免：
   - 复述从代码中一眼可见的内容
   - 已被覆盖的通用最佳实践
   - 不太可能复现的一次性修复
   - 一行话足够时却写冗长解释

3. **展示 diff** - 对每处修改，展示：
   - 要更新哪个 CLAUDE.md 文件
   - 具体的增补内容（以 diff 或引用块形式）
   - 简要说明这为什么有助于未来的会话

**Diff 格式：**

```markdown
### Update: ./CLAUDE.md

**Why:** Build command was missing, causing confusion about how to run the project.

```diff
+ ## Quick Start

+ ```bash
+ npm install
+ npm run dev  # Start development server on port 3000
+ ```
```
```

### 阶段 5：应用更新

获得用户批准后，使用 Edit 工具应用修改。保留现有内容的结构。

## 模板

各项目类型的 CLAUDE.md 模板见 [references/templates.md](references/templates.md)。

## 需要标记的常见问题

1. **失效的命令**：已无法运行的构建命令
2. **缺失的依赖**：未提及的必需工具
3. **过时的架构**：已发生变化的文件结构
4. **缺失的环境配置**：必需的环境变量或配置
5. **失效的测试命令**：已发生变化的测试脚本
6. **未记录的坑点**：未被记录的非显而易见的模式

## 应分享给用户的提示

在给出建议时，提醒用户：

- **`#` 快捷键**：在 Claude 会话中按 `#`，可让 Claude 自动把学到的东西纳入 CLAUDE.md
- **保持简洁**：CLAUDE.md 应当人类可读；密集优于冗长
- **可执行的命令**：所有被记录的命令都应可直接复制粘贴使用
- **使用 `.claude.local.md`**：存放不与团队共享的个人偏好（并将其加入 `.gitignore`）
- **全局默认**：把用户级偏好放在 `~/.claude/CLAUDE.md`

## 什么样的 CLAUDE.md 才是优秀的

**关键原则：**
- 简洁且人类可读
- 命令可直接复制粘贴执行
- 项目专属的模式，而非泛泛的建议
- 非显而易见的坑点与警告

**推荐章节**（只保留相关项）：
- Commands（构建、测试、开发、lint）
- Architecture（目录结构）
- Key Files（入口文件、配置）
- Code Style（项目约定）
- Environment（必需变量、环境搭建）
- Testing（命令、模式）
- Gotchas（怪癖、常见错误）
- Workflow（何时做什么）
