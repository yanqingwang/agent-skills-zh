---
name: search-first
description: "先调研后编码（research-first）工作流：在编写自定义代码之前，先在 npm/PyPI、MCP 服务器、Skills 和 GitHub 中搜索现成工具，再决定采用（adopt）、扩展（extend）还是自建（build）。对非平凡需求会启动 researcher Agent。适用于开始开发新功能、添加依赖或集成、或准备编写一个可能早已存在的工具函数时。"
metadata:
  origin: ECC
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/search-first/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# /search-first — 写代码前先调研

将"实现之前先搜索现成方案"的工作流系统化。

## 触发时机

在以下情况使用本 Skill：
- 开始一个很可能已有现成方案的新功能
- 添加依赖或集成
- 用户要求"添加 X 功能"而你正准备动手写代码
- 在创建新的工具函数、helper 或抽象之前

## 工作流

```
┌─────────────────────────────────────────────┐
│  0. TOOL AVAILABILITY PREFLIGHT             │
│     Check search channels before relying on │
│     them; report skipped channels honestly   │
├─────────────────────────────────────────────┤
│  1. NEED ANALYSIS                           │
│     Define what functionality is needed      │
│     Identify language/framework constraints  │
├─────────────────────────────────────────────┤
│  2. PARALLEL SEARCH (researcher agent)      │
│     ┌──────────┐ ┌──────────┐ ┌──────────┐  │
│     │  npm /   │ │  MCP /   │ │  GitHub / │  │
│     │  PyPI    │ │  Skills  │ │  Web      │  │
│     └──────────┘ └──────────┘ └──────────┘  │
├─────────────────────────────────────────────┤
│  3. EVALUATE                                │
│     Score candidates (functionality, maint, │
│     community, docs, license, deps)         │
├─────────────────────────────────────────────┤
│  4. DECIDE                                  │
│     ┌─────────┐  ┌──────────┐  ┌─────────┐  │
│     │  Adopt  │  │  Extend  │  │  Build   │  │
│     │ as-is   │  │  /Wrap   │  │  Custom  │  │
│     └─────────┘  └──────────┘  └─────────┘  │
├─────────────────────────────────────────────┤
│  5. IMPLEMENT                               │
│     Install package / Configure MCP /       │
│     Write minimal custom code               │
└─────────────────────────────────────────────┘
```

## 决策矩阵

| 信号 | 动作 |
|------|------|
| 完全匹配、维护良好、MIT/Apache 许可 | **采用（Adopt）** — 直接安装使用 |
| 部分匹配、基础良好 | **扩展（Extend）** — 安装 + 编写薄封装层 |
| 多个弱匹配 | **组合（Compose）** — 组合 2-3 个小型包 |
| 未找到合适方案 | **自建（Build）** — 编写自定义代码，但以调研结论为依据 |

## 使用方法

### 第 0 步：工具可用性预检

这是给 Agent 的指导，而非可执行的安装脚本。
只检查与当前任务和项目相关的渠道。

| 渠道 | 检查方式 | 缺失时的处理 |
|------|----------|--------------|
| 仓库内搜索 | `rg --files` 及有针对性的 `rg` 查询 | 说明仅检查了可见文件 |
| 包注册表 | `npm --version`、`python -m pip --version` 或项目自身的包管理器 | 改用 web/文档搜索，避免声称已覆盖注册表 |
| GitHub CLI | `gh auth status` | 仅使用公开网页或本地 git 历史 |
| MCP/文档工具 | 可用工具列表或本地 MCP 配置 | 回退到官方文档/web 搜索 |
| Skills 目录 | 适用时执行 `ls ~/.claude/skills ~/.codex/skills` | 说明没有可用的本地 Skill 目录 |

### 快速模式（内联）

在编写工具函数或添加功能之前，先在脑中过一遍：

0. 仓库里是否已有现成实现？→ 先用 `rg` 检索相关模块/测试
1. 这是不是一个常见问题？→ 搜索 npm/PyPI
2. 是否有对应的 MCP？→ 检查 `~/.claude/settings.json` 并搜索
3. 是否有对应的 Skill？→ 检查 `~/.claude/skills/`
4. 是否有 GitHub 上的实现/模板？→ 在编写全新代码之前，先运行 GitHub 代码搜索寻找有人维护的 OSS

### 完整模式（Agent）

对于非平凡的功能需求，启动 researcher Agent：

```
Agent(subagent_type="general-purpose", prompt="
  Research existing tools for: [DESCRIPTION]
  Language/framework: [LANG]
  Constraints: [ANY]

  Search: npm/PyPI, MCP servers, Claude Code skills, GitHub
  Return: Structured comparison with recommendation
")
```

较旧版本的 Claude Code 文档可能将其称为 `Task(...)`；
请使用当前 Harness 所暴露的 agent/subagent 工具名。

## 按类别划分的搜索捷径

### 开发工具链
- Lint → `eslint`、`ruff`、`textlint`、`markdownlint`
- 格式化 → `prettier`、`black`、`gofmt`
- 测试 → `jest`、`pytest`、`go test`
- Pre-commit → `husky`、`lint-staged`、`pre-commit`

### AI/LLM 集成
- Claude SDK → 用 Context7 获取最新文档
- 提示词管理 → 检查 MCP 服务器
- 文档处理 → `unstructured`、`pdfplumber`、`mammoth`

### 数据与 API
- HTTP 客户端 → `httpx`（Python）、`ky`/`undici`（Node）
- 校验 → `zod`（TS）、`pydantic`（Python）
- 数据库 → 优先检查是否有 MCP 服务器

### 内容与发布
- Markdown 处理 → `remark`、`unified`、`markdown-it`
- 图片优化 → `sharp`、`imagemin`

## 集成点

### 与 planner Agent 协作
planner 应在阶段 1（架构评审）之前调用 researcher：
- researcher 识别可用工具
- planner 将其纳入实施计划
- 避免在计划中"重新发明轮子"

### 与 architect Agent 协作
architect 应就以下事项咨询 researcher：
- 技术栈决策
- 集成模式发现
- 现有参考架构

### 与 iterative-retrieval Skill 协作
两者结合可实现渐进式发现：
- 第 1 轮：宽泛搜索（npm、PyPI、MCP）
- 第 2 轮：详细评估头部候选方案
- 第 3 轮：测试与项目约束的兼容性

## 示例

### 示例 1："添加死链检查"
```
Need: Check markdown files for broken links
Search: npm "markdown dead link checker"
Found: textlint-rule-no-dead-link (score: 9/10)
Action: ADOPT — npm install textlint-rule-no-dead-link
Result: Zero custom code, battle-tested solution
```

### 示例 2："添加 HTTP 客户端封装"
```
Need: Resilient HTTP client with retries and timeout handling
Search: npm "http client retry", PyPI "httpx retry"
Found: got (Node) with retry plugin, httpx (Python) with built-in retry
Action: ADOPT — use got/httpx directly with retry config
Result: Zero custom code, production-proven libraries
```

### 示例 3："添加配置文件 linter"
```
Need: Validate project config files against a schema
Search: npm "config linter schema", "json schema validator cli"
Found: ajv-cli (score: 8/10)
Action: ADOPT + EXTEND — install ajv-cli, write project-specific schema
Result: 1 package + 1 schema file, no custom validation logic
```

## 反模式

- **直接跳去写代码**：不检查是否已有现成实现就编写工具函数
- **无视 MCP**：不检查是否已有 MCP 服务器提供该能力
- **静默跳过**：在某个搜索渠道不可用时仍报告"未找到任何结果"
- **过度定制**：对库的封装过重，使其丧失原有优势
- **依赖膨胀**：为一个小功能安装庞大的包
