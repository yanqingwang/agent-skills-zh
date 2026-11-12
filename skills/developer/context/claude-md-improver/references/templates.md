> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/claude-md-management/skills/claude-md-improver/references/templates.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CLAUDE.md 模板

## 关键原则

- **简洁**：内容密集、人类可读；每个概念尽量一行
- **可执行**：命令应可直接复制粘贴使用
- **项目专属**：记录本项目独有的模式，而非泛泛的建议
- **时效**：所有信息都应反映代码库的实际状态

---

## 推荐章节

只保留与项目相关的章节，并非所有章节都需要。

### Commands

记录使用该项目的核心命令。

```markdown
## Commands

| Command | Description |
|---------|-------------|
| `<install command>` | Install dependencies |
| `<dev command>` | Start development server |
| `<build command>` | Production build |
| `<test command>` | Run tests |
| `<lint command>` | Lint/format code |
```

### Architecture

描述项目结构，让 Claude 知道各类内容放在哪里。

```markdown
## Architecture

```
<root>/
  <dir>/    # <purpose>
  <dir>/    # <purpose>
  <dir>/    # <purpose>
```
```

### Key Files

列出 Claude 应当了解的重要文件。

```markdown
## Key Files

- `<path>` - <purpose>
- `<path>` - <purpose>
```

### Code Style

记录项目专属的编码约定。

```markdown
## Code Style

- <convention>
- <convention>
- <preference over alternative>
```

### Environment

记录必需的环境变量与环境搭建步骤。

```markdown
## Environment

Required:
- `<VAR_NAME>` - <purpose>
- `<VAR_NAME>` - <purpose>

Setup:
- <setup step>
```

### Testing

记录测试方法与命令。

```markdown
## Testing

- `<test command>` - <what it tests>
- <testing convention or pattern>
```

### Gotchas

记录非显而易见的模式、怪癖与警告。

```markdown
## Gotchas

- <non-obvious thing that causes issues>
- <ordering dependency or prerequisite>
- <common mistake to avoid>
```

### Workflow

记录开发工作流模式。

```markdown
## Workflow

- <when to do X>
- <preferred approach for Y>
```

---

## 模板：项目根目录（精简版）

```markdown
# <Project Name>

<One-line description>

## Commands

| Command | Description |
|---------|-------------|
| `<command>` | <description> |

## Architecture

```
<structure>
```

## Gotchas

- <gotcha>
```

---

## 模板：项目根目录（完整版）

```markdown
# <Project Name>

<One-line description>

## Commands

| Command | Description |
|---------|-------------|
| `<command>` | <description> |

## Architecture

```
<structure with descriptions>
```

## Key Files

- `<path>` - <purpose>

## Code Style

- <convention>

## Environment

- `<VAR>` - <purpose>

## Testing

- `<command>` - <scope>

## Gotchas

- <gotcha>
```

---

## 模板：包/模块

适用于 monorepo 内的包或独立模块。

```markdown
# <Package Name>

<Purpose of this package>

## Usage

```
<import/usage example>
```

## Key Exports

- `<export>` - <purpose>

## Dependencies

- `<dependency>` - <why needed>

## Notes

- <important note>
```

---

## 模板：Monorepo 根目录

```markdown
# <Monorepo Name>

<Description>

## Packages

| Package | Description | Path |
|---------|-------------|------|
| `<name>` | <purpose> | `<path>` |

## Commands

| Command | Description |
|---------|-------------|
| `<command>` | <description> |

## Cross-Package Patterns

- <shared pattern>
- <generation/sync pattern>
```

---

## 更新原则

更新任何 CLAUDE.md 时：

1. **具体**：使用真实的文件路径与本项目实际使用的命令
2. **时效**：对照实际代码库核实信息
3. **简短**：每个概念尽量一行
4. **有用**：它能否帮助新的 Claude 会话理解项目？
