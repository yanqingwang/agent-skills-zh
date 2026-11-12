---
name: skill-development
description: 当用户想要"创建 Skill"、"为 Plugin 添加 Skill"、"编写新 Skill"、"改进 Skill 描述"、"整理 Skill 内容"，或需要有关 Skill 结构、渐进式披露，或 Claude Code Plugin 的 Skill 开发最佳实践的指导时，应使用本 Skill。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/skill-development/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 面向 Claude Code Plugin 的 Skill 开发

本 Skill 就如何为 Claude Code Plugin 创建高效的 Skill 提供指导。

## 关于 Skill

Skill 是模块化、自包含的包，通过提供专门的知识、工作流和工具来扩展 Claude 的能力。
可以把它们看作针对特定领域或任务的「入门指南」，
把 Claude 从通用 Agent 转变为配备程序性知识的专用 Agent，
而这类知识是任何模型都无法完全具备的。

### Skill 提供什么

1. 专门的工作流 - 针对特定领域的多步骤流程
2. 工具集成 - 处理特定文件格式或 API 的说明
3. 领域专业知识 - 公司特有的知识、schema、业务逻辑
4. 随附资源 - 面向复杂且重复性任务的脚本、references 和 assets

### Skill 的构成

每个 Skill 由一个必需的 SKILL.md 文件和可选的随附资源组成：

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

#### SKILL.md（必需）

**元数据质量：** YAML frontmatter 中的 `name` 和 `description` 决定 Claude 何时会使用该 Skill。要具体说明该 Skill 做什么、何时使用。使用第三人称（例如用"当用户……时应使用本 Skill"而非"在需要……时使用本 Skill"）。

#### 随附资源（可选）

##### 脚本（`scripts/`）

用于需要确定性可靠性、或会被反复重写的任务的可执行代码（Python/Bash/etc.）。

- **何时纳入**：当同一段代码需要反复重写，或需要确定性可靠性时
- **示例**：用于 PDF 旋转任务的 `scripts/rotate_pdf.py`
- **好处**：节省 token、结果确定、可不加载到上下文中直接执行
- **注意**：为打补丁或做环境相关的调整，Claude 仍可能需要读取脚本

##### 参考文件（`references/`）

按需加载到上下文中、用于为 Claude 的流程与思考提供依据的文档和参考资料。

- **何时纳入**：用于 Claude 工作时需要参考的文档
- **示例**：金融 schema 用 `references/finance.md`、公司 NDA 模板用 `references/mnda.md`、公司政策用 `references/policies.md`、API 规格用 `references/api_docs.md`
- **用例**：数据库 schema、API 文档、领域知识、公司政策、详细的工作流指南
- **好处**：让 SKILL.md 保持精简，只在 Claude 判定需要时才加载
- **最佳实践**：如果文件很大（>10k 词），就在 SKILL.md 中加入 grep 搜索模式
- **避免重复**：信息应只放在 SKILL.md 或 references 文件中的一处，不要两处都放。除确实属于该 Skill 核心的内容外，详细信息优先放入 references 文件，这样既让 SKILL.md 保持精简，又能让信息可被找到而不挤占 context window。SKILL.md 中只保留必要的程序性指令和工作流指导；把详细的参考资料、schema 和示例移到 references 文件。

##### 素材（`assets/`）

不打算加载到上下文中，而是用于 Claude 所生成输出里的文件。

- **何时纳入**：当该 Skill 需要用于最终输出的文件时
- **示例**：品牌素材用 `assets/logo.png`、PowerPoint 模板用 `assets/slides.pptx`、HTML/React 样板代码用 `assets/frontend-template/`、字体排印用 `assets/font.ttf`
- **用例**：模板、图片、图标、样板代码、字体，以及供复制或改动的示例文档
- **好处**：把输出资源与文档分开，让 Claude 无需把文件加载到上下文中也能使用它们

### 渐进式披露设计原则

Skill 采用三级加载系统来高效管理上下文：

1. **元数据（name + description）** - 始终在上下文中（~100 词）
2. **SKILL.md 正文** - Skill 触发时加载（<5k 词）
3. **随附资源** - 由 Claude 按需加载（不限*）

*不限，因为脚本可在不读入 context window 的情况下执行。

## Skill 创建流程

创建 Skill 时，请按顺序遵循「Skill 创建流程」，只有在有明确理由认定某步骤不适用时才跳过。

### 第 1 步：结合具体示例理解 Skill

仅当已清楚理解该 Skill 的使用模式时才跳过此步。即便处理的是现有 Skill，这一步仍有价值。

要创建高效的 Skill，需清楚理解该 Skill 将如何被使用的具体示例。这种理解既可以来自用户直接给出的示例，也可以来自经用户反馈确认后生成的示例。

例如，在构建图像编辑器 Skill 时，相关的问题包括：

- "图像编辑器 Skill 应支持哪些功能？编辑、旋转，还有其他吗？"
- "能否举一些该 Skill 会被如何使用的例子？"
- "我能想到用户会提出诸如「去除这张图里的红眼」或「旋转这张图」之类的请求。你还能想到该 Skill 的其他使用方式吗？"
- "用户会说什么样的话来触发该 Skill？"

为避免让用户不堪其扰，不要在单条消息里提太多问题。先从最重要的问题开始，再按需追问以提升效果。

当对该 Skill 应支持的功能有了清晰认识时，即可结束此步。

### 第 2 步：规划可复用的 Skill 内容

要把具体示例转化为高效的 Skill，请按以下方式分析每个示例：

1. 思考如何从零开始完成该示例
2. 找出在反复执行这些工作流时，哪些 scripts、references 和 assets 会有帮助

示例：在构建用于处理"帮我旋转这个 PDF"这类请求的 `pdf-editor` Skill 时，分析表明：

1. 旋转 PDF 每次都要重写相同的代码
2. 把一个 `scripts/rotate_pdf.py` 脚本存入该 Skill 会很有帮助

示例：在设计用于处理"给我做一个待办应用"或"给我做一个记录步数的仪表盘"这类请求的 `frontend-webapp-builder` Skill 时，分析表明：

1. 编写前端 Web 应用每次都需要相同的 HTML/React 样板代码
2. 把一个包含 HTML/React 项目样板代码的 `assets/hello-world/` 模板存入该 Skill 会很有帮助

示例：在构建用于处理"今天有多少用户登录了？"这类请求的 `big-query` Skill 时，分析表明：

1. 查询 BigQuery 每次都要重新弄清表的 schema 和表间关系
2. 把记录表 schema 的 `references/schema.md` 文件存入该 Skill 会很有帮助

**针对 Claude Code Plugin：** 在构建 hooks Skill 时，分析表明：
1. 开发者反复需要校验 hooks.json 并测试 hook 脚本
2. `scripts/validate-hook-schema.sh` 和 `scripts/test-hook.sh` 这类工具会很有帮助
3. 用 `references/patterns.md` 收纳详细的 hook 模式，避免让 SKILL.md 臃肿

为确定该 Skill 的内容，请分析每个具体示例，列出要纳入的可复用资源：scripts、references 和 assets。

### 第 3 步：创建 Skill 结构

针对 Claude Code Plugin，创建如下 Skill 目录结构：

```bash
mkdir -p plugin-name/skills/skill-name/{references,examples,scripts}
touch plugin-name/skills/skill-name/SKILL.md
```

**注意：** 通用 skill-creator 使用 `init_skill.py`，而 Plugin 的 Skill 则直接以更简单的手工结构创建在 Plugin 的 `skills/` 目录下。

### 第 4 步：编辑 Skill

编辑（新建或现有的）Skill 时，请记住该 Skill 是供另一个 Claude 实例使用的。重点纳入对 Claude 有益且并非显而易见的信息。思考哪些程序性知识、领域专属细节或可复用 assets 能帮助另一个 Claude 实例更高效地执行这些任务。

#### 从可复用的 Skill 内容入手

开始实现时，先处理上面确定的可复用资源：`scripts/`、`references/` 和 `assets/` 文件。注意此步可能需要用户输入。例如，在实现 `brand-guidelines` Skill 时，用户可能需要提供品牌素材或模板存入 `assets/`，或提供文档存入 `references/`。

另外，删除该 Skill 不需要的示例文件和目录。只创建真正需要的目录（references/、examples/、scripts/）。

#### 更新 SKILL.md

**写作风格：** 通篇使用**祈使式/不定式**（以动词开头的指令）撰写 Skill，不要用第二人称。使用客观、指令式的语言（例如用"要完成 X，执行 Y"，而非"你应当执行 X"或"如果你需要执行 X"）。这能保持面向 AI 消费的一致性与清晰度。

**描述（frontmatter）：** 使用第三人称格式，并带上具体的触发短语：

```yaml
---
name: Skill Name
description: This skill should be used when the user asks to "specific phrase 1", "specific phrase 2", "specific phrase 3". Include exact phrases users would say that should trigger this skill. Be concrete and specific.
version: 0.1.0
---
```

**好的描述示例：**
```yaml
description: This skill should be used when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", "implement prompt-based hooks", or mentions hook events (PreToolUse, PostToolUse, Stop).
```

**差的描述示例：**
```yaml
description: Use this skill when working with hooks.  # Wrong person, vague
description: Load when user needs hook help.  # Not third person
description: Provides hook guidance.  # No trigger phrases
```

要完成 SKILL.md 正文，请回答以下问题：

1. 用几句话说明该 Skill 的用途是什么？
2. 该 Skill 应在何时使用？（把这一点连同具体的触发词写进 frontmatter 的 description）
3. 在实践中，Claude 应如何使用该 Skill？上面开发的所有可复用 Skill 内容都应加以引用，以便 Claude 知道如何使用它们。

**保持 SKILL.md 精简：** 正文目标为 1,500-2,000 词。把详细内容移到 references/：
- 详细模式 → `references/patterns.md`
- 高阶技巧 → `references/advanced.md`
- 迁移指南 → `references/migration.md`
- API 参考资料 → `references/api-reference.md`

**在 SKILL.md 中引用资源：**
```markdown
## Additional Resources

### Reference Files

For detailed patterns and techniques, consult:
- **`references/patterns.md`** - Common patterns
- **`references/advanced.md`** - Advanced use cases

### Example Files

Working examples in `examples/`:
- **`example-script.sh`** - Working example
```

### 第 5 步：验证与测试

**对 Plugin 的 Skill，验证方式不同于通用 Skill：**

1. **检查结构**：Skill 目录位于 `plugin-name/skills/skill-name/`
2. **校验 SKILL.md**：具有含 name 和 description 的 frontmatter
3. **检查触发短语**：description 包含具体的用户请求
4. **核查写作风格**：正文使用祈使式/不定式，不用第二人称
5. **检验渐进式披露**：SKILL.md 精简（~1,500-2,000 词），详细内容放在 references/
6. **检查引用**：所有被引用的文件都存在
7. **校验示例**：示例完整且正确
8. **测试脚本**：脚本可执行且运行正确

**使用 skill-reviewer Agent：**
```
Ask: "Review my skill and check if it follows best practices"
```

skill-reviewer Agent 会检查描述质量、内容组织和渐进式披露。

### 第 6 步：迭代

测试 Skill 之后，用户可能会要求改进。这种情况往往出现在刚用过该 Skill、对其表现记忆犹新的时候。

**迭代工作流：**
1. 在真实任务中使用该 Skill
2. 留意卡点或低效之处
3. 确定 SKILL.md 或随附资源应如何更新
4. 实施改动并再次测试

**常见的改进：**
- 强化 description 中的触发短语
- 把冗长章节从 SKILL.md 移到 references/
- 补充缺失的示例或脚本
- 澄清含糊的指令
- 增加边界情况处理

## 针对 Plugin 的注意事项

### Skill 在 Plugin 中的位置

Plugin 的 Skill 位于该 Plugin 的 `skills/` 目录下：

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
├── agents/
└── skills/
    └── my-skill/
        ├── SKILL.md
        ├── references/
        ├── examples/
        └── scripts/
```

### 自动发现

Claude Code 会自动发现 Skill：
- 扫描 `skills/` 目录
- 找到包含 `SKILL.md` 的子目录
- 始终加载 Skill 元数据（name + description）
- Skill 触发时加载 SKILL.md 正文
- 按需加载 references/examples

### 无需打包

Plugin 的 Skill 随 Plugin 一起分发，而不是作为单独的 ZIP 文件。用户安装 Plugin 时即获得这些 Skill。

### 在 Plugin 中测试

通过本地安装 Plugin 来测试 Skill：

```bash
# Test with --plugin-dir
cc --plugin-dir /path/to/plugin

# Ask questions that should trigger the skill
# Verify skill loads correctly
```

## 来自 Plugin-Dev 的示例

把本 Plugin 中的 Skill 当作最佳实践范例来研究：

**hook-development Skill：**
- 出色的触发短语："创建 Hook"、"添加 PreToolUse Hook" 等
- 精简的 SKILL.md（1,651 词）
- 3 个 references/ 文件收纳详细内容
- 3 个可运行 Hook 的 examples/
- 3 个 scripts/ 实用工具

**agent-development Skill：**
- 有力的触发词："创建 Agent"、"Agent frontmatter" 等
- 聚焦的 SKILL.md（1,438 词）
- references 包含来自 Claude Code 的 AI 生成提示词
- 完整的 Agent 示例

**plugin-settings Skill：**
- 具体的触发词："Plugin 设置"、".local.md 文件"、"YAML frontmatter"
- references 展示了真实实现（multi-agent-swarm、ralph-loop）
- 可运行的解析脚本

每个都体现了渐进式披露和有力的触发设计。

## 渐进式披露实践

### SKILL.md 中放什么

**纳入（Skill 触发时始终加载）：**
- 核心概念与概览
- 必要的流程与工作流
- 快速参考表
- 指向 references/examples/scripts 的指引
- 最常见的用例

**控制在 3,000 词以内，理想为 1,500-2,000 词**

### references/ 中放什么

**移到 references/（按需加载）：**
- 详细模式与高阶技巧
- 全面的 API 文档
- 迁移指南
- 边界情况与问题排查
- 大量示例与逐步讲解

**每个参考文件可以很长（2,000-5,000+ 词）**

### examples/ 中放什么

**可运行的代码示例：**
- 完整、可运行的脚本
- 配置文件
- 模板文件
- 真实场景的使用示例

**用户可以直接复制并改造它们**

### scripts/ 中放什么

**实用脚本：**
- 校验工具
- 测试辅助
- 解析工具
- 自动化脚本

**应可执行且有文档**

## 写作风格要求

### 祈使式/不定式

用以动词开头的指令撰写，不要用第二人称：

**正确（祈使式）：**
```
To create a hook, define the event type.
Configure the MCP server with authentication.
Validate settings before use.
```

**错误（第二人称）：**
```
You should create a hook by defining the event type.
You need to configure the MCP server.
You must validate settings before use.
```

### 描述中使用第三人称

frontmatter 的 description 必须使用第三人称：

**正确：**
```yaml
description: This skill should be used when the user asks to "create X", "configure Y"...
```

**错误：**
```yaml
description: Use this skill when you want to create X...
description: Load this skill when user asks...
```

### 客观、指令式语言

聚焦要做什么，而非谁该去做：

**正确：**
```
Parse the frontmatter using sed.
Extract fields with grep.
Validate values before use.
```

**错误：**
```
You can parse the frontmatter...
Claude should extract fields...
The user might validate values...
```

## 验证清单

在定稿一个 Skill 之前：

**结构：**
- [ ] SKILL.md 文件存在，且带有合法的 YAML frontmatter
- [ ] frontmatter 有 `name` 和 `description` 字段
- [ ] Markdown 正文存在且内容充实
- [ ] 所引用的文件确实存在

**描述质量：**
- [ ] 使用第三人称（"当用户……时应使用本 Skill"）
- [ ] 包含用户会说的具体触发短语
- [ ] 列出具体场景（"创建 X"、"配置 Y"）
- [ ] 不含糊、不笼统

**内容质量：**
- [ ] SKILL.md 正文使用祈使式/不定式
- [ ] 正文聚焦且精简（理想 1,500-2,000 词，上限 <5k）
- [ ] 详细内容已移到 references/
- [ ] 示例完整且可运行
- [ ] 脚本可执行且有文档

**渐进式披露：**
- [ ] 核心概念在 SKILL.md
- [ ] 详细文档在 references/
- [ ] 可运行代码在 examples/
- [ ] 实用工具在 scripts/
- [ ] SKILL.md 引用了这些资源

**测试：**
- [ ] Skill 在预期的用户请求上触发
- [ ] 内容对目标任务有帮助
- [ ] 各文件之间没有重复信息
- [ ] references 在需要时加载

## 需要避免的常见错误

### 误区 1：触发描述薄弱

❌ **错误：**
```yaml
description: Provides guidance for working with hooks.
```

**为何错误：** 含糊、没有具体触发短语、不是第三人称

✅ **正确：**
```yaml
description: This skill should be used when the user asks to "create a hook", "add a PreToolUse hook", "validate tool use", or mentions hook events. Provides comprehensive hooks API guidance.
```

**为何正确：** 第三人称、具体短语、具体场景

### 误区 2：SKILL.md 塞得太多

❌ **错误：**
```
skill-name/
└── SKILL.md  (8,000 words - everything in one file)
```

**为何错误：** Skill 加载时使上下文膨胀，详细内容始终都要加载

✅ **正确：**
```
skill-name/
├── SKILL.md  (1,800 words - core essentials)
└── references/
    ├── patterns.md (2,500 words)
    └── advanced.md (3,700 words)
```

**为何正确：** 渐进式披露，详细内容仅在需要时加载

### 误区 3：第二人称写作

❌ **错误：**
```markdown
You should start by reading the configuration file.
You need to validate the input.
You can use the grep tool to search.
```

**为何错误：** 第二人称，不是祈使式

✅ **正确：**
```markdown
Start by reading the configuration file.
Validate the input before processing.
Use the grep tool to search for patterns.
```

**为何正确：** 祈使式，指令直接

### 误区 4：缺少资源引用

❌ **错误：**
```markdown
# SKILL.md

[Core content]

[No mention of references/ or examples/]
```

**为何错误：** Claude 不知道 references 的存在

✅ **正确：**
```markdown
# SKILL.md

[Core content]

## Additional Resources

### Reference Files
- **`references/patterns.md`** - Detailed patterns
- **`references/advanced.md`** - Advanced techniques

### Examples
- **`examples/script.sh`** - Working example
```

**为何正确：** Claude 知道去哪里找额外信息

## 快速参考

### 最小 Skill

```
skill-name/
└── SKILL.md
```

适用于：简单知识，无需复杂资源

### 标准 Skill（推荐）

```
skill-name/
├── SKILL.md
├── references/
│   └── detailed-guide.md
└── examples/
    └── working-example.sh
```

适用于：多数带有详细文档的 Plugin Skill

### 完整 Skill

```
skill-name/
├── SKILL.md
├── references/
│   ├── patterns.md
│   └── advanced.md
├── examples/
│   ├── example1.sh
│   └── example2.json
└── scripts/
    └── validate.sh
```

适用于：带有校验工具的复杂领域

## 最佳实践总结

✅ **应当：**
- 在 description 中使用第三人称（"当用户……时应使用本 Skill"）
- 纳入具体的触发短语（"创建 X"、"配置 Y"）
- 保持 SKILL.md 精简（1,500-2,000 词）
- 采用渐进式披露（把细节移到 references/）
- 使用祈使式/不定式撰写
- 清晰地引用支持文件
- 提供可运行的示例
- 为常见操作创建实用脚本
- 把 plugin-dev 的 Skill 当作模板来研究

❌ **不要：**
- 在任何地方使用第二人称
- 设置含糊的触发条件
- 把所有内容都塞进 SKILL.md（>3,000 词却没有 references/）
- 使用第二人称写作（"你应当……"）
- 让资源没有被引用
- 放入损坏或不完整的示例
- 跳过验证

## 其他资源

### 研究这些 Skill

plugin-dev 的 Skill 体现了最佳实践：
- `../hook-development/` - 渐进式披露、实用工具
- `../agent-development/` - AI 辅助创建、references
- `../mcp-integration/` - 全面的 references
- `../plugin-settings/` - 真实场景示例
- `../command-development/` - 清晰的关键概念
- `../plugin-structure/` - 良好的组织

### 参考文件

如需完整的 skill-creator 方法论：
- **`references/skill-creator-original.md`** - skill-creator 的完整原始内容

## 实施工作流

为你的 Plugin 创建一个 Skill：

1. **理解用例**：找出 Skill 使用的具体示例
2. **规划资源**：确定需要哪些 scripts/references/examples
3. **创建结构**：`mkdir -p skills/skill-name/{references,examples,scripts}`
4. **编写 SKILL.md**：
   - 带第三人称 description 和触发短语的 frontmatter
   - 采用祈使式的精简正文（1,500-2,000 词）
   - 引用支持文件
5. **添加资源**：按需创建 references/、examples/、scripts/
6. **验证**：检查 description、写作风格、组织结构
7. **测试**：核实 Skill 在预期触发词上加载
8. **迭代**：根据使用情况改进

着力打磨有力的触发描述、渐进式披露和祈使式写作风格，让 Skill 在需要时加载并提供有针对性的指导。
