> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/obsidian-markdown/references/CALLOUTS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Callout（标注块）参考

## 基本 Callout

```markdown
> [!note]
> This is a note callout.

> [!info] Custom Title
> This callout has a custom title.

> [!tip] Title Only
```

## 可折叠 Callout

```markdown
> [!faq]- Collapsed by default
> This content is hidden until expanded.

> [!faq]+ Expanded by default
> This content is visible but can be collapsed.
```

## 嵌套 Callout

```markdown
> [!question] Outer callout
> > [!note] Inner callout
> > Nested content
```

## 支持的 Callout 类型

| 类型 | 别名 | 颜色 / 图标 |
|------|---------|-------------|
| `note` | - | 蓝色，铅笔 |
| `abstract` | `summary`、`tldr` | 青绿色，剪贴板 |
| `info` | - | 蓝色，信息 |
| `todo` | - | 蓝色，复选框 |
| `tip` | `hint`、`important` | 青色，火焰 |
| `success` | `check`、`done` | 绿色，对勾 |
| `question` | `help`、`faq` | 黄色，问号 |
| `warning` | `caution`、`attention` | 橙色，警告 |
| `failure` | `fail`、`missing` | 红色，X |
| `danger` | `error` | 红色，闪电 |
| `bug` | - | 红色，虫子 |
| `example` | - | 紫色，列表 |
| `quote` | `cite` | 灰色，引号 |

## 自定义 Callout（CSS）

```css
.callout[data-callout="custom-type"] {
  --callout-color: 255, 0, 0;
  --callout-icon: lucide-alert-circle;
}
```
