---
name: knap
description: 使用 Knap CLI 从模板和结构化数据渲染 Markdown。当用户要求应用 Knap 模板、把 JSON 或 CSV 数据转成笔记、批量生成 Markdown 文件，或将 Defuddle 输出整理成笔记时使用本 Skill。
---

> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/knap/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Knap

使用 Knap CLI 渲染带有变量、过滤器和逻辑的 Markdown 模板。

若未安装：`npm install -g knap`（需要 Node.js 20 或更高版本）。也可以使用 `npx knap`。

运行 `knap --help` 查看可用命令和选项。通过 CLI 的离线参考了解这门模板语言：

```bash
knap help syntax
knap help filters
knap help filter date
knap help tags
knap help tag for
```

先用这些列表查找名称，再针对语法、参数和示例（含预期输出）请求单项帮助。

## 用法

用 JSON 变量渲染模板：

```bash
knap render template.md --data article.json -o note.md
```

内联提供模板和数据：

```bash
knap render -t '# {{ title | trim }}' --data-json '{"title":"Hello"}'
```

覆盖变量或通过管道传入 JSON 数据：

```bash
knap render template.md --data article.json --set 'title=Custom title'
cat article.json | knap render template.md --data -
```

数据必须是 JSON 对象，其 property 会成为模板变量。`--set` 用字符串覆盖字面量顶层键。嵌套对象、数组、数字和布尔值请使用 JSON。

模板来源（文件、`-t` 或 stdin）和数据来源（`--data` 或 `--data-json`）各选其一。只能有一个输入读取 stdin。没有模板文件或 `-t` 时，Knap 从 stdin 读取模板。

输出默认到 stdout。`-o` 会创建父目录，并在渲染成功后覆盖目标文件。出错时以状态码 `1` 退出，诊断信息输出到 stderr。成功输出的同时也可能带有警告。

## 模板

用 `{{ variable }}` 表示值，`|` 表示过滤器，`{% ... %}` 表示逻辑。例如，将下面内容保存为 `template.md`：

```knap
---
{{ title | yaml_property:"title" }}
{{ tags | yaml_property:"tags" }}
---
# {{ title | trim }}
{% if author %}
By {{ author }}
{% endif %}

{{ content }}
```

对完整的 frontmatter property 使用 `yaml_property`，这样值会被正确加引号和缩进。CLI 内置标准过滤器，但不提供 Web Clipper 的浏览器变量、选择器、提示词（prompt）或依赖 DOM 的 HTML 过滤器。变量请通过 JSON 提供。

渲染前检查模板：

```bash
knap validate template.md
```

校验会检查语法、过滤器名称和静态过滤器参数，不需要数据，也不产生文件输出。它不检查变量是否存在、运行时取值或动态参数；要用真实数据渲染来检查运行时行为。诊断信息输出到 stderr，并包含相关的帮助命令。

## Defuddle 流水线

将网页提取为包含 Markdown 内容的 JSON，再渲染成笔记：

```bash
defuddle parse https://example.com/article --md --json \
  | knap render template.md --data - -o note.md
```

Defuddle 的 JSON property（如 `title` 和 `content`）会直接成为模板变量。

## 批量渲染

为每个 CSV 行、JSON 数组元素或文件夹中的 JSON 文件各创建一个文件：

```bash
knap batch template.md --data articles.csv --output-dir notes \
  --filename '{{ title | safe_name }}.md'
```

JSON 数组使用 `--data articles.json`，JSON 对象文件夹使用 `--data ./articles`。CSV 表头会成为变量名，值保持为字符串。管道传入的数据默认按 JSON 处理；管道传入 CSV 时加 `--format csv`。

使用 `--dry-run` 进行校验并列出输出路径，而不写入文件。已有文件需要 `--overwrite` 才能覆盖，dry run 期间也是如此。同一批次内输出重名属于错误，即使加了 `--overwrite` 也一样。

文件名模板必须产出单个带扩展名的文件名，不能包含目录。数据派生的名称请使用 `safe_name`。未指定 `--filename` 时，Knap 保留源 JSON 的 basename，或将 CSV 行和数组元素编号为 `1.md`、`2.md` 等。
