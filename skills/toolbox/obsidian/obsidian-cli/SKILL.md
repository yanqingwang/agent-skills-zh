---
name: obsidian-cli
description: 使用 Obsidian CLI 与 Obsidian vault（仓库）交互，读取、创建、搜索和管理笔记、任务、property（属性）等。还支持插件与主题开发，提供重载插件、运行 JavaScript、捕获错误、截图和检查 DOM 等命令。当用户要求与 Obsidian vault 交互、管理笔记、搜索 vault 内容、从命令行执行 vault 操作，或开发和调试 Obsidian 插件与主题时使用本 Skill。
---

> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/obsidian-cli/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Obsidian CLI

使用 `obsidian` CLI 与正在运行的 Obsidian 实例交互。需要 Obsidian 处于打开状态。

## 命令参考

运行 `obsidian help` 可查看所有可用命令，该列表始终是最新的。完整文档：https://help.obsidian.md/cli

## 语法

**参数（Parameters）**用 `=` 接收值。含空格的值需要加引号：

```bash
obsidian create name="My Note" content="Hello world"
```

**标志（Flags）**是不带值的布尔开关：

```bash
obsidian create name="My Note" silent overwrite
```

多行内容中用 `\n` 表示换行、`\t` 表示制表符。

## 文件定位

许多命令接受 `file` 或 `path` 来定位文件。两者都不提供时，将使用当前活动文件。

- `file=<name>` — 像 wikilink 一样解析（只需名称，无需路径或扩展名）
- `path=<path>` — 从 vault 根目录起的精确路径，例如 `folder/note.md`

## Vault 定位

命令默认作用于最近聚焦的 vault。将 `vault=<name>` 作为第一个参数可指定特定 vault：

```bash
obsidian vault="My Vault" search query="test"
```

## 常见用法

```bash
obsidian read file="My Note"
obsidian create name="New Note" content="# Hello" template="Template" silent
obsidian append file="My Note" content="New line"
obsidian search query="search term" limit=10
obsidian daily:read
obsidian daily:append content="- [ ] New task"
obsidian property:set name="status" value="done" file="My Note"
obsidian tasks daily todo
obsidian tags sort=count counts
obsidian backlinks file="My Note"
```

在任意命令上加 `--copy` 可将输出复制到剪贴板。使用 `silent` 可阻止文件被打开。在列表命令上加 `total` 可获取数量。

## 插件开发

### 开发/测试循环

修改插件或主题代码后，请遵循以下工作流：

1. **重载（Reload）**插件以应用更改：
   ```bash
   obsidian plugin:reload id=my-plugin
   ```
2. **检查错误** —— 如出现错误，修复后从第 1 步重新开始：
   ```bash
   obsidian dev:errors
   ```
3. **可视化验证**：通过截图或 DOM 检查：
   ```bash
   obsidian dev:screenshot path=screenshot.png
   obsidian dev:dom selector=".workspace-leaf" text
   ```
4. **检查控制台输出**中是否有警告或意外日志：
   ```bash
   obsidian dev:console level=error
   ```

### 其他开发者命令

在应用上下文中运行 JavaScript：

```bash
obsidian eval code="app.vault.getFiles().length"
```

检查 CSS 值：

```bash
obsidian dev:css selector=".workspace-leaf" prop=background-color
```

切换移动端模拟：

```bash
obsidian dev:mobile on
```

运行 `obsidian help` 可查看更多开发者命令，包括 CDP 和调试器控制。
