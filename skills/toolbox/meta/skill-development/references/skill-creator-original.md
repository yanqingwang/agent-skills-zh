---
name: skill-creator
description: 创建高效 Skill 的指南。当用户想创建一个新 Skill（或更新已有 Skill），用专业知识、工作流或工具集成扩展 Claude 的能力时，应使用本 Skill。
license: Complete terms in LICENSE.txt
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/plugin-dev/skills/skill-development/references/skill-creator-original.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Skill 创建器（Skill Creator）

本 Skill 提供创建高效 Skill 的指南。

## 关于 Skill

Skill 是模块化、自包含的包，通过提供专业知识、工作流与工具来扩展 Claude 的能力。可以把它们看作特定领域或任务的"入职指南"：它们把 Claude 从通用代理改造成具备程序性知识的专用代理，这类知识没有哪个模型能完整拥有。

### Skill 提供什么

1. 专属工作流 - 特定领域的多步骤流程
2. 工具集成 - 处理特定文件格式或 API 的说明
3. 领域专长 - 公司专属知识、schema、业务逻辑
4. 捆绑资源 - 服务于复杂与重复任务的脚本、参考文档与资产

### Skill 的结构

每个 Skill 必含一个 SKILL.md 文件，另附可选的捆绑资源：

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

**元数据质量：** YAML frontmatter 中的 `name` 与 `description` 决定 Claude 何时使用该 Skill。要写清楚 Skill 做什么、何时使用。用第三人称（例如 "This skill should be used when..."，而不是 "Use this skill when..."）。

#### 捆绑资源（可选）

##### 脚本（`scripts/`）

可执行代码（Python/Bash 等），用于需要确定性可靠性或被反复重写的任务。

- **何时纳入**：同一段代码被反复重写，或需要确定性可靠性时
- **示例**：`scripts/rotate_pdf.py` 用于 PDF 旋转任务
- **收益**：节省 token、结果确定、可不加载进上下文直接执行
- **注意**：Claude 做打补丁或环境适配时，可能仍需要阅读脚本

##### 参考文档（`references/`）

按需加载进上下文的文档与参考资料，用于支撑 Claude 的流程与思考。

- **何时纳入**：Claude 工作过程中需要查阅的文档
- **示例**：`references/finance.md` 存金融 schema、`references/mnda.md` 存公司 NDA 模板、`references/policies.md` 存公司政策、`references/api_docs.md` 存 API 规格
- **用例**：数据库 schema、API 文档、领域知识、公司政策、详细工作流指南
- **收益**：SKILL.md 保持精简，仅在 Claude 判断需要时才加载
- **最佳实践**：文件较大（>10k 词）时，在 SKILL.md 中给出 grep 搜索模式
- **避免重复**：信息要么放 SKILL.md，要么放 references 文件，不要两边都放。详细信息优先放 references 文件，除非它确实是 Skill 的核心：这样 SKILL.md 保持精简，信息可被发现，又不会占据大量上下文窗口。SKILL.md 只保留核心流程指令与工作流指引；把详细参考资料、schema 与示例移到 references 文件。

##### 资产（`assets/`）

不打算加载进上下文、而是在 Claude 产出中直接使用的文件。

- **何时纳入**：Skill 需要在最终产出中使用的文件时
- **示例**：`assets/logo.png` 存品牌素材、`assets/slides.pptx` 存 PowerPoint 模板、`assets/frontend-template/` 存 HTML/React 样板代码、`assets/font.ttf` 存字体
- **用例**：模板、图片、图标、样板代码、字体、供复制或修改的示例文档
- **收益**：把产出资源与文档分开，Claude 可以不加载进上下文直接使用这些文件

### 渐进式披露设计原则

Skill 用三级加载系统高效管理上下文：

1. **元数据（name + description）** - 始终在上下文中（约 100 词）
2. **SKILL.md 正文** - Skill 触发时加载（<5k 词）
3. **捆绑资源** - 由 Claude 按需加载（无上限*）

*无上限是因为脚本可以不读入上下文窗口而直接执行。

## Skill 创建流程

创建 Skill 时，按顺序执行"Skill 创建流程"；只有明确某步骤不适用时才可跳过。

### 第 1 步：用具体示例理解 Skill

只有在已经清楚理解 Skill 的使用模式时才跳过本步。即使是在改进已有 Skill，这一步仍有价值。

要创建高效的 Skill，先清楚理解 Skill 将如何被使用的具体示例。这种理解可以来自用户直接给出的示例，也可以来自经用户反馈验证过的生成示例。

例如，构建图片编辑 Skill 时，相关问题包括：

- "image-editor skill 应支持哪些功能？编辑、旋转，还有别的吗？"
- "能举几个这个 Skill 的使用示例吗？"
- "我能想到用户会提'去掉这张图的红眼'或'旋转这张图'这类需求。你还能想到其他用法吗？"
- "用户说什么话应该触发这个 Skill？"

为避免让用户应接不暇，不要在一条消息里问太多问题。先问最重要的，再按需追问，效果更好。

当对 Skill 应支持的功能有了清晰认识，即可结束本步。

### 第 2 步：规划 Skill 的可复用内容

要把具体示例转化为高效的 Skill，按以下方式分析每个示例：

1. 考虑如何从零开始完成该示例
2. 找出反复执行这些工作流时，哪些脚本、参考文档与资产会有帮助

示例：构建 `pdf-editor` Skill 处理"帮我旋转这个 PDF"这类请求时，分析结论如下：

1. 旋转 PDF 每次都要重写同样的代码
2. 在 Skill 中保存 `scripts/rotate_pdf.py` 脚本会很有用

示例：设计 `frontend-webapp-builder` Skill 处理"给我做个 todo 应用"或"给我做个记录步数的仪表盘"这类请求时，分析结论如下：

1. 写前端 web 应用每次都要同样的 HTML/React 样板代码
2. 在 Skill 中保存 `assets/hello-world/` 模板（内含 HTML/React 样板项目文件）会很有用

示例：构建 `big-query` Skill 处理"今天有多少用户登录过？"这类请求时，分析结论如下：

1. 查询 BigQuery 每次都要重新摸索表 schema 与表间关系
2. 在 Skill 中保存记录表 schema 的 `references/schema.md` 文件会很有用

要确定 Skill 内容，逐个分析具体示例，列出要纳入的可复用资源清单：脚本、参考文档与资产。

### 第 3 步：初始化 Skill

到这一步，就该真正动手创建 Skill 了。

只有当要开发的 Skill 已存在、只需迭代或打包时才跳过本步。这种情况下直接进入下一步。

从零创建新 Skill 时，务必运行 `init_skill.py` 脚本。该脚本会便捷地生成一个新的模板 Skill 目录，自动包含 Skill 所需的全部内容，让创建过程高效且可靠得多。

用法：

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

该脚本会：

- 在指定路径创建 Skill 目录
- 生成带正确 frontmatter 与 TODO 占位符的 SKILL.md 模板
- 创建示例资源目录：`scripts/`、`references/`、`assets/`
- 在每个目录中放入可自定义或删除的示例文件

初始化后，按需定制或删除生成的 SKILL.md 与示例文件。

### 第 4 步：编辑 Skill

编辑（新生成或已有）Skill 时记住：Skill 是为另一个 Claude 实例使用而创建的。重点写入对 Claude 有益且不显然的信息。想想哪些程序性知识、领域细节或可复用资产，能帮助另一个 Claude 实例更高效地完成这些任务。

#### 从可复用内容入手

实现时先从上面确定的可复用资源入手：`scripts/`、`references/` 与 `assets/` 文件。注意这一步可能需要用户提供输入。例如实现 `brand-guidelines` Skill 时，用户可能需要提供品牌素材或模板放入 `assets/`，或提供文档放入 `references/`。

同时，删除 Skill 用不到的示例文件与目录。初始化脚本会在 `scripts/`、`references/`、`assets/` 中创建示例文件以演示结构，但多数 Skill 用不到全部。

#### 更新 SKILL.md

**写作风格：** 整个 Skill 用**祈使/不定式形式**（动词开头的指令）书写，不用第二人称。用客观的指令性语言（例如 "To accomplish X, do Y"，而不是 "You should do X" 或 "If you need to do X"）。这能保证 AI 阅读时的一致性与清晰度。

完成 SKILL.md 前回答以下问题：

1. Skill 的目的是什么，用几句话说清？
2. Skill 应在何时使用？
3. 实践中 Claude 应如何使用这个 Skill？要引用上面开发的全部可复用内容，让 Claude 知道怎么用它们。

### 第 5 步：打包 Skill

Skill 就绪后，打包成可分发的 zip 文件交给用户。打包流程会先自动校验 Skill，确保满足全部要求：

```bash
scripts/package_skill.py <path/to/skill-folder>
```

可选指定输出目录：

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

打包脚本会：

1. **校验** Skill，检查：
   - YAML frontmatter 格式与必填字段
   - Skill 命名规范与目录结构
   - description 完整性与质量
   - 文件组织与资源引用

2. 校验通过后**打包** Skill，生成以 Skill 命名的 zip 文件（如 `my-skill.zip`），包含全部文件并保持正确的分发目录结构。

校验失败时，脚本会报告错误并退出，不生成包。修复所有校验错误后重新运行打包命令。

### 第 6 步：迭代

测试过 Skill 之后，用户可能要求改进。这通常发生在刚用完 Skill 之时，对它的表现记得最清楚。

**迭代流程：**
1. 在真实任务中使用 Skill
2. 留意吃力或低效之处
3. 确定 SKILL.md 或捆绑资源应如何更新
4. 实施修改并再次测试
