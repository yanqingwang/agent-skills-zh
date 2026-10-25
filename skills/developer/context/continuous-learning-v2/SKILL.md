---
name: continuous-learning-v2
description: 基于 instinct（本能规则）的学习系统：通过 Hook 观察会话，创建带置信度评分的原子 instinct，并将其演化为 Skill/命令/Agent。v2.1 新增项目级（project-scoped）instinct，防止跨项目污染。适用于从会话中沉淀经验、管理 instinct，或将其晋升为 Skill、命令或 Agent。
metadata:
  version: 2.1.0
  origin: ECC
---

> **中文汉化版** · 上游：[affaan-m/ECC](https://github.com/affaan-m/ECC) · 原文件：`skills/continuous-learning-v2/SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 持续学习 v2.1 - 基于 Instinct（本能规则）的架构

一套先进的学习系统，通过原子的 "instinct"（本能规则）——带有置信度评分的小型习得行为——把你的 Claude Code 会话转化为可复用的知识。

**v2.1** 新增 **项目级（project-scoped）instinct**——React 模式留在你的 React 项目里，Python 约定留在你的 Python 项目里，而通用模式（如"始终校验输入"）则全局共享。

## 何时激活

- 设置从 Claude Code 会话中自动学习
- 通过 Hook 配置基于 instinct 的行为提取
- 调整习得行为的置信度阈值
- 审查、导出或导入 instinct 库
- 将 instinct 演化为完整的 Skill、命令或 Agent
- 管理项目级与全局 instinct
- 将 instinct 从项目范围晋升到全局范围

## v2.1 有什么新变化

| 特性 | v2.0 | v2.1 |
|---------|------|------|
| 存储位置 | 全局（`~/.claude/homunculus/`） | 项目级（`${XDG_DATA_HOME:-~/.local/share}/ecc-homunculus/projects/<hash>/`） |
| 作用范围 | 所有 instinct 在任何地方生效 | 项目级 + 全局 |
| 项目识别 | 无 | git remote URL / 仓库路径 |
| 晋升 | 不适用 | 在 2 个及以上项目中出现后：项目 → 全局 |
| 命令 | 4 个（status/evolve/export/import） | 6 个（+promote/projects） |
| 跨项目 | 有污染风险 | 默认隔离 |

## v2 有什么新变化（对比 v1）

| 特性 | v1 | v2 |
|---------|----|----|
| 观察方式 | Stop hook（会话结束时） | PreToolUse/PostToolUse（100% 可靠） |
| 分析位置 | 主上下文 | 后台 Agent（Haiku） |
| 粒度 | 完整 Skill | 原子 "instinct" |
| 置信度 | 无 | 0.3-0.9 加权 |
| 演化路径 | 直接生成 Skill | instinct -> 聚类 -> Skill/命令/Agent |
| 分享 | 无 | 导出/导入 instinct |

## Instinct 模型

一个 instinct 是一小段习得的行为：

```yaml
---
id: prefer-functional-style
trigger: "when writing new functions"
confidence: 0.7
domain: "code-style"
source: "session-observation"
scope: project
project_id: "a1b2c3d4e5f6"
project_name: "my-react-app"
---

# Prefer Functional Style

## Action
Use functional patterns over classes when appropriate.

## Evidence
- Observed 5 instances of functional pattern preference
- User corrected class-based approach to functional on 2025-01-15
```

**特性：**
- **原子性** —— 一个触发条件，一个动作
- **置信度加权** —— 0.3 = 试探性，0.9 = 近乎确定
- **领域标签** —— code-style、testing、git、debugging、workflow 等
- **有证据支撑** —— 记录是哪些观察产生了它
- **作用域感知** —— `project`（默认）或 `global`

## 工作原理

```
Session Activity (in a git repo)
      |
      | Hooks capture prompts + tool use (100% reliable)
      | + detect project context (git remote / repo path)
      v
+---------------------------------------------+
|  projects/<project-hash>/observations.jsonl  |
|   (prompts, tool calls, outcomes, project)   |
+---------------------------------------------+
      |
      | Observer agent reads (background, Haiku)
      v
+---------------------------------------------+
|          PATTERN DETECTION                   |
|   * User corrections -> instinct             |
|   * Error resolutions -> instinct            |
|   * Repeated workflows -> instinct           |
|   * Scope decision: project or global?       |
+---------------------------------------------+
      |
      | Creates/updates
      v
+---------------------------------------------+
|  projects/<project-hash>/instincts/personal/ |
|   * prefer-functional.yaml (0.7) [project]   |
|   * use-react-hooks.yaml (0.9) [project]     |
+---------------------------------------------+
|  instincts/personal/  (GLOBAL)               |
|   * always-validate-input.yaml (0.85) [global]|
|   * grep-before-edit.yaml (0.6) [global]     |
+---------------------------------------------+
      |
      | /evolve clusters + /promote
      v
+---------------------------------------------+
|  projects/<hash>/evolved/ (project-scoped)   |
|  evolved/ (global)                           |
|   * commands/new-feature.md                  |
|   * skills/testing-workflow.md               |
|   * agents/refactor-specialist.md            |
+---------------------------------------------+
```

## 项目识别

系统会自动检测你当前所在的项目：

1. **`CLAUDE_PROJECT_DIR` 环境变量**（最高优先级）——即使该目录不是 git 仓库，也会被视为显式覆盖（按其绝对路径哈希）
2. **`git remote get-url origin`**——哈希后生成可移植的项目 ID（不同机器上的同一仓库得到相同 ID）
3. **`git rev-parse --show-toplevel`**——使用仓库路径作为回退（机器特定）
4. **全局回退**——如果未检测到任何项目，instinct 归入全局作用域

每个项目会得到一个 12 字符的哈希 ID（例如 `a1b2c3d4e5f6`）。`${XDG_DATA_HOME:-~/.local/share}/ecc-homunculus/projects.json` 处有一个注册表文件，把 ID 映射到人类可读的名称。

### 数据目录

continuous-learning-v2 将 Observer 数据存储在 `~/.claude` 之外，这样 Claude Code 的敏感路径防护就不会阻止后台 instinct 写入：

1. `CLV2_HOMUNCULUS_DIR`（当其被设置为绝对路径时）
2. `$XDG_DATA_HOME/ecc-homunculus`
3. `$HOME/.local/share/ecc-homunculus`

已有数据存放在 `~/.claude/homunculus` 的用户可以一次性迁移：

```bash
bash skills/continuous-learning-v2/scripts/migrate-homunculus.sh
```

## 快速开始

### 1. 启用观察 Hook

**如果以插件方式安装**（推荐）：

无需额外的 `settings.json` hook 配置块。Claude Code v2.1+ 会自动加载插件的 `hooks/hooks.json`，`observe.sh` 已经在其中注册。

如果你之前把 `observe.sh` 复制进了 `~/.claude/settings.json`，请删除那段重复的 `PreToolUse` / `PostToolUse` 配置块。重复插件 Hook 会导致双重执行，以及 `${CLAUDE_PLUGIN_ROOT}` 解析错误——因为该变量只在插件托管的 `hooks/hooks.json` 条目中可用。

**如果手动安装**到 `~/.claude/skills`，请将以下内容加入你的 `~/.claude/settings.json`：

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning-v2/hooks/observe.sh"
      }]
    }],
    "PostToolUse": [{
      "matcher": "*",
      "hooks": [{
        "type": "command",
        "command": "~/.claude/skills/continuous-learning-v2/hooks/observe.sh"
      }]
    }]
  }
}
```

### 2. 初始化目录结构

系统会在首次使用时自动创建目录，但你也可以手动创建：

```bash
# Global directories
mkdir -p "${XDG_DATA_HOME:-$HOME/.local/share}/ecc-homunculus"/{instincts/{personal,inherited},evolved/{agents,skills,commands},projects}

# Project directories are auto-created when the hook first runs in a git repo
```

### 3. 使用 instinct 命令

```bash
/instinct-status     # Show learned instincts (project + global)
/evolve              # Cluster related instincts into skills/commands
/instinct-export     # Export instincts to file
/instinct-import     # Import instincts from others
/promote             # Promote project instincts to global scope
/projects            # List all known projects and their instinct counts
```

## 命令

| 命令 | 说明 |
|---------|-------------|
| `/instinct-status` | 显示所有 instinct（项目级 + 全局）及其置信度 |
| `/evolve` | 将相关 instinct 聚类为 Skill/命令，并给出晋升建议 |
| `/instinct-export` | 导出 instinct（可按作用域/领域过滤） |
| `/instinct-import <file>` | 导入 instinct，带作用域控制 |
| `/promote [id]` | 将项目级 instinct 晋升到全局作用域 |
| `/projects` | 列出所有已知项目及其 instinct 数量 |

## 配置

编辑 `config.json` 来控制后台 Observer：

```json
{
  "version": "2.1",
  "observer": {
    "enabled": false,
    "run_interval_minutes": 5,
    "min_observations_to_analyze": 20
  }
}
```

| 键 | 默认值 | 说明 |
|-----|---------|-------------|
| `observer.enabled` | `false` | 启用后台 Observer Agent |
| `observer.run_interval_minutes` | `5` | Observer 每隔多久分析一次观察数据 |
| `observer.min_observations_to_analyze` | `20` | 触发分析所需的最少观察条数 |

其他行为（观察捕获、instinct 阈值、项目作用域、晋升标准）通过 `instinct-cli.py` 和 `observe.sh` 中的代码默认值配置。

### Observer 平台支持

后台 Observer 需要 WSL2、Linux 或 macOS。在原生 Windows
（Git Bash / MSYS2）上，它会启动并报告成功，但当生成它的 Hook 退出、
其 Job Object 关闭时，该进程会被杀死，因此分析永远不会运行——
在这种环境下设置 `observer.enabled: true` 实际上等于无效操作
（见 issue #2489）。

`observe.sh` 会在下一次 Hook 调用时检测到这种情况，并
在 Observer 连续多次未能存活后，向 `observer-start.log`
写入一次说明性的警告。

| 环境变量 | 默认值 | 说明 |
|---------|---------|-------------|
| `ECC_OBSERVER_NOSURVIVE_WARN_AFTER` | `3` | 写入警告前允许的连续未存活次数 |

## 文件结构

```
${XDG_DATA_HOME:-~/.local/share}/ecc-homunculus/
+-- identity.json           # Your profile, technical level
+-- projects.json           # Registry: project hash -> name/path/remote
+-- observations.jsonl      # Global observations (fallback)
+-- instincts/
|   +-- personal/           # Global auto-learned instincts
|   +-- inherited/          # Global imported instincts
+-- evolved/
|   +-- agents/             # Global generated agents
|   +-- skills/             # Global generated skills
|   +-- commands/           # Global generated commands
+-- projects/
    +-- a1b2c3d4e5f6/       # Project hash (from git remote URL)
    |   +-- project.json    # Per-project metadata mirror (id/name/root/remote)
    |   +-- observations.jsonl
    |   +-- observations.archive/
    |   +-- instincts/
    |   |   +-- personal/   # Project-specific auto-learned
    |   |   +-- inherited/  # Project-specific imported
    |   +-- evolved/
    |       +-- skills/
    |       +-- commands/
    |       +-- agents/
    +-- f6e5d4c3b2a1/       # Another project
        +-- ...
```

## 作用域决策指南

| 模式类型 | 作用范围 | 示例 |
|-------------|-------|---------|
| 语言/框架约定 | **project** | "使用 React hooks"、"遵循 Django REST 模式" |
| 文件结构偏好 | **project** | "测试放在 `__tests__`/"、"组件放在 src/components/" |
| 代码风格 | **project** | "使用函数式风格"、"优先使用 dataclass" |
| 错误处理策略 | **project** | "错误用 Result 类型表示" |
| 安全实践 | **global** | "校验用户输入"、"净化 SQL" |
| 通用最佳实践 | **global** | "先写测试"、"始终处理错误" |
| 工具工作流偏好 | **global** | "先 Grep 再 Edit"、"先 Read 再 Write" |
| Git 实践 | **global** | "约定式提交（Conventional commits）"、"小而专注的 commit" |

## Instinct 晋升（项目 -> 全局）

当同一个 instinct 在多个项目中以较高置信度出现时，它就是晋升到全局作用域的候选。

**自动晋升条件：**
- 同一 instinct ID 出现在 2 个及以上项目中
- 平均置信度 >= 0.8

**如何晋升：**

```bash
# Promote a specific instinct
python3 instinct-cli.py promote prefer-explicit-errors

# Auto-promote all qualifying instincts
python3 instinct-cli.py promote

# Preview without changes
python3 instinct-cli.py promote --dry-run
```

`/evolve` 命令也会给出晋升候选建议。

## 置信度评分

置信度随时间演化：

| 分值 | 含义 | 行为 |
|-------|---------|----------|
| 0.3 | 试探性 | 仅建议，不强制 |
| 0.5 | 中等 | 在相关时应用 |
| 0.7 | 较强 | 自动批准应用 |
| 0.9 | 近乎确定 | 核心行为 |

**置信度提高**的条件：
- 模式被反复观察到
- 用户没有纠正建议的行为
- 来自其他来源的相似 instinct 相互印证

**置信度降低**的条件：
- 用户明确纠正了该行为
- 长时间未观察到该模式
- 出现相矛盾的证据

## 为什么观察用 Hook 而不是 Skill？

> "v1 依赖 Skill 来做观察。Skill 是概率性的——它们大约只有 50-80% 的概率触发，取决于 Claude 的判断。"

Hook 则以**100%** 的概率、确定性地触发。这意味着：
- 每次工具调用都会被观察到
- 不会漏掉任何模式
- 学习是全面的

## 向后兼容

v2.1 与 v2.0 和 v1 完全兼容：
- 既有全局 instinct 可通过 `scripts/migrate-homunculus.sh` 从 `~/.claude/homunculus/instincts/` 迁移过来
- v1 中既有的 `~/.claude/skills/learned/` Skill 仍然可用
- Stop hook 仍在运行（但现在也会馈入 v2）
- 渐进式迁移：两者并行运行

## 隐私

- 观察数据**留在你本机**
- 项目级 instinct 按项目相互隔离
- 只有 **instinct**（模式）可以被导出——原始观察数据不能
- 不共享任何实际代码或对话内容
- 由你控制导出与晋升什么

## 相关资源

- [ECC-Tools GitHub App](https://github.com/apps/ecc-tools) - 从仓库历史生成 instinct
- Homunculus - 启发了 v2 基于 instinct 架构（原子观察、置信度评分、instinct 演化流水线）的社区项目
- [The Longform Guide](https://x.com/affaanmustafa/status/2014040193557471352) - 持续学习章节

---

*基于 Instinct 的学习：把你的模式教给 Claude，一次一个项目。*
