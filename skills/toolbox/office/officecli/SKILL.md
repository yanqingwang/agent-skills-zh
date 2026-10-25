---
name: officecli
description: 使用 officecli CLI 工具创建、分析、校对和修改 Office 文档（.docx、.xlsx、.pptx）。当用户想要创建、检查、核对格式、发现问题、添加图表或修改 Office 文档时使用。
---

> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/officecli/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# officecli

AI 友好的 .docx、.xlsx、.pptx 命令行工具。单一二进制文件，无依赖，无需安装 Office。

## 安装

如果 `officecli` 未安装：

```bash
# macOS / Linux
curl -fsSL https://d.officecli.ai/install.sh | bash

# Windows (PowerShell)
irm https://d.officecli.ai/install.ps1 | iex
```

用 `officecli --version` 验证。安装后如果仍未找到，请打开一个新终端。

---

## 策略

**L1（读取）→ L2（DOM 编辑）→ L3（原始 XML）**。始终优先使用更高的层。需要结构化输出时加 `--json`。

**文档工作开始前，先查看「专用 Skill」部分**（本文件底部）。融资 deck、学术论文、财务模型、数据看板和 Morph 动画需要先加载各自的 Skill ， `load_skill` 一次，然后继续。

---

## 帮助系统（重要）

**对属性名、取值格式或命令语法拿不准时，始终运行 help，不要靠猜。** 一次 help 查询胜过"猜测-失败-重试"的循环。

`officecli help` ≡ `officecli --help`，且 `officecli <cmd> --help` ≡ `officecli help <cmd>` ， 内容相同。

```bash
officecli help                                  # All commands + global options + schema entry points
officecli help docx                             # List all docx elements
officecli help docx paragraph                   # Full schema: properties, aliases, examples, readbacks
officecli help docx set paragraph               # Verb-filtered: only props usable with `set`
officecli help docx paragraph --json            # Structured schema (machine-readable)
```

格式别名：`word`→`docx`、`excel`→`xlsx`、`ppt`/`powerpoint`→`pptx`。动词：`add`、`set`、`get`、`query`、`remove`。MCP 通过单一的 `command` 字符串参数暴露同一套 schema：`{"command":"help docx paragraph"}`（不是结构化的 `{"format":...,"type":...}` 对象 ， MCP 工具只有一个参数 `command`，并原样透传给 CLI）。

---

## 性能：常驻模式

**每条命令在首次访问时自动启动常驻进程**（60 秒空闲超时）， 文件锁冲突会被自动避免。更长的会话（12 分钟空闲）仍建议显式使用 `open`/`close`：
```bash
officecli open report.docx       # explicitly keep in memory
officecli set report.docx ...    # no file I/O overhead
officecli close report.docx      # save and release
```

如需禁用自动启动：`OFFICECLI_NO_AUTO_RESIDENT=1`。

**只在非 officecli 边界处刷新。** officecli 自己的读取（`get`/`query`/`view`/`dump`）总能看到你最新的编辑，因此工作流中途无需保存。只**在非 officecli 程序读取文件之前**才运行 `save`（保留常驻进程）或 `close`（刷新 + 释放）， 例如 python-docx/openpyxl、Word、渲染器、交付/上传。（空闲会话会在几秒内自动刷新；`OFFICECLI_RESIDENT_FLUSH=each` 会让每次变更在返回前先刷新。）

---

## 快速上手

**PPT：**
```bash
officecli create slides.pptx
officecli add slides.pptx / --type slide --prop title="Q4 Report" --prop background=1A1A2E
officecli add slides.pptx '/slide[1]' --type shape --prop text="Revenue grew 25%" --prop x=2cm --prop y=5cm --prop font=Arial --prop size=24 --prop color=FFFFFF
```

**Word：**
```bash
officecli create report.docx
officecli add report.docx /body --type paragraph --prop text="Executive Summary" --prop style=Heading1
officecli add report.docx /body --type paragraph --prop text="Revenue increased by 25% year-over-year."
```

**Excel：**
```bash
officecli create data.xlsx
officecli set data.xlsx /Sheet1/A1 --prop value="Name" --prop bold=true
officecli set data.xlsx /Sheet1/A2 --prop value="Alice"
```

---

## L1：创建、读取与检查

```bash
officecli create <file>               # Create blank .docx/.xlsx/.pptx (type from extension)
officecli view <file> <mode>          # outline | stats | issues | text | annotated | html
officecli get <file> <path> --depth N # Get a node and its children [--json]
officecli query <file> <selector>     # CSS-like query
officecli validate <file>             # Validate against OpenXML schema
```

### view 模式

| 模式 | 说明 | 实用标志 |
|------|-------------|-------------|
| `outline` | 文档结构 | |
| `stats` | 统计信息（页数、字数、形状数） | |
| `issues` | 格式/内容/结构问题 | `--type format\|content\|structure`、`--limit N` |
| `text` | 纯文本提取 | `--start N --end N`、`--max-lines N` |
| `annotated` | 带格式标注的文本 | |
| `html` | 静态 HTML 快照 ， 与 `watch` 相同的渲染器，无需服务器 | `--browser`、`--page N`（docx）、`--start N --end N`（pptx） |
| `screenshot` / `svg` / `pdf` / `forms` | 通过无头浏览器输出 PNG / SVG（pptx 幻灯片）/ 通过导出插件输出 PDF / 通过格式处理器插件输出表单字段 JSON | `-o`、`--screenshot-width/-height`、pptx `--grid N` |

`view html` 适合一次性快照（CI 产物、归档、diff 对比）；需要实时刷新或浏览器端点击选择时用 `watch`。

### get

通过元素的 localName 指定任意 XML 路径。用 `--depth N` 展开子节点。加 `--json` 可获得结构化输出。默认文本输出对 grep 友好：`path (type) "text" key=val key=val ...`

```bash
officecli get report.docx '/body/p[3]' --depth 2 --json
officecli get slides.pptx '/slide[1]' --depth 1          # list all shapes on slide 1
officecli get data.xlsx '/Sheet1/B2' --json
```

### 稳定 ID 寻址

拥有稳定 ID 的元素会返回 `@attr=value` 形式的路径而非位置索引。在多步骤工作流中优先使用它们 ， 位置索引会随插入/删除而移动，稳定 ID 不会。

```
/slide[1]/shape[@id=550950021]                    # PPT shape
/slide[1]/table[@id=1388430425]/tr[1]/tc[2]       # PPT table
/body/p[@paraId=1A2B3C4D]                         # Word paragraph
/comments/comment[@commentId=1]                    # Word comment
```

PPT 还接受 `@name=`（例如 `shape[@name=Title 1]`），并能感知 morph 的 `!!` 前缀。没有稳定 ID 的元素（slide、run、tr/tc、row）回退到位置索引。

### query

类 CSS 选择器：`[attr=value]`、`[attr!=value]`、`[attr~=text]`、`[attr>=value]`、`[attr<=value]`、`:contains("text")`、`:empty`、`:has(formula)`、`:no-alt`。在 `query`/`set`/`remove` 中支持布尔 `and`/`or` 组合：`cell[value>5000 or value<100]`、`cell[(type=Number or type=Date) and value>0]`。Excel 按列名取行：`Sheet1!row[Salary>5000]`。`set` 接受选择器和 Excel 原生路径（与 `get`/`query` 对等）。`set`/`remove` 上会拒绝裸的无作用域选择器。

```bash
officecli query report.docx 'paragraph[style=Normal] > run[font!=Arial]'
officecli query slides.pptx 'shape[fill=FF0000]'
```

---

## Watch 与交互式选择

实时 HTML 预览，每次文件变更都会自动刷新。浏览器中可以点击 / shift 点击 / 框选拖拽来选择形状；CLI 可以读取浏览器当前的选区并据此操作。

```bash
officecli watch <file> [--port N]      # Start preview server (default port 26315)
officecli unwatch <file>               # Stop
officecli goto <file> <path>           # Scroll watching browser(s) to element (docx: p / table / tr / tc)
```

打开打印出的 `http://localhost:N` URL。单击选择；shift/cmd/ctrl+单击多选；从空白处拖拽进行框选。PPT/Word 使用蓝色轮廓；Excel 使用原生风格的绿色选区（双击单元格可内联编辑；拖拽图表可重新定位）。

### `get <file> selected` ： 读取用户点击的内容

```bash
officecli get <file> selected [--json]
```

返回当前选中内容对应的 DocumentNodes。未选中任何内容时结果为空。没有正在运行的 watch 时退出码 != 0。

```bash
# User clicks shapes in the browser, then asks "make these red"
PATHS=$(officecli get deck.pptx selected --json | jq -r '.data.Results[].path')
for p in $PATHS; do officecli set deck.pptx "$p" --prop fill=FF0000; done
```

### 关键特性

- **选区在文件编辑后依然有效。** 路径使用稳定的 `@id=` 形式。
- **所有已连接的浏览器共享同一个选区。** 后写者胜。
- **同一文件只允许一个 watch。** 同一文件同一时刻只能有一个 watch 进程。
- **组合形状整体选择。** v1 不支持深入选择组合内的单个子元素。
- **覆盖范围：** `.pptx` 的形状/图片/表格/图表/连接线/组合；`.docx` 的顶层段落和表格。继承自版式/母版的装饰以及 Word 嵌套元素（表格单元格、run 级）无法寻址。**`.xlsx` 不会输出 `data-path`** ， xlsx 上的 `mark`/`selection` 总是解析为 `stale=true`（v2 候选功能）。

### Marks ： 等待审阅的编辑提案

当变更在写入文件之前需要人工审阅时使用 `mark`。Marks 只存在于 watch 进程中；被接受的 mark 由单独的 `set` 流水线应用。一次性变更直接用 `set`；永久性文件批注用 `add --type comment`（Word 原生）。

```bash
officecli mark <file> <path> [--prop find=... color=... note=... tofix=... regex=true] [--json]
officecli unmark <file> [--path <p> | --all] [--json]
officecli get-marks <file> [--json]
```

属性：`find`（字面量，`regex=true` 时为正则；原始形式 `find='r"[abc]"'`）、`color`（hex / `rgb(...)` / 22 个具名白名单色）、`note`、`tofix`（驱动应用流水线）。**Path** 必须是 watch HTML 中的 `data-path` 格式 ， 完整流水线见各子 Skill。

---

## L2：DOM 操作

### set ： 修改属性

```bash
officecli set <file> <path> --prop key=value [--prop ...]
```

通过元素路径（可用 `get --depth N` 找到）**可以设置任何 XML 属性** ， 即使是当前不存在的属性。不带 `find=` 时，`set` 会把格式应用到整个元素。

**取值格式：**

| 类型 | 格式 | 示例 |
|------|--------|---------|
| 颜色 | Hex（带/不带 `#`）、具名色、RGB、主题色 | `FF0000`、`#FF0000`、`red`、`rgb(255,0,0)`、`accent1`..`accent6` |
| 间距 | 带单位 | `12pt`、`0.5cm`、`1.5x`、`150%` |
| 尺寸 | EMU 或带后缀 | `914400`、`2.54cm`、`1in`、`72pt`、`96px` |

**点号属性别名** ， `font.<attr>` 形式可用于 shape/run/paragraph/table/row/cell/section/styles，例如 `--prop font.color=red --prop font.bold=true --prop font.size=14pt`。运行 `officecli help <fmt> <element>` 查看完整列表。

### find ： 格式化或替换匹配文本

在 `set` 上使用顶层 `--find` / `--replace`（`query` 上可用 `--find`）。旧式 `--prop find=X` 仍然有效，但会输出提示。

```bash
# Format matched text (auto-splits runs)
officecli set doc.docx '/body/p[1]' --find weather --prop bold=true --prop color=red

# Regex matching (regex= still a prop flag)
officecli set doc.docx '/body/p[1]' --find '\d+%' --prop regex=true --prop color=red

# Replace text (use `/` for whole-document scope)
officecli set doc.docx / --find draft --replace final

# docx: tracked Find&Replace
officecli set doc.docx / --find draft --replace final --prop revision.author=Alice

# PPT — same syntax, different paths
officecli set slides.pptx / --find draft --replace final
```

**路径决定搜索范围：** `/` = 整个文档，`/body/p[1]` 或 `/slide[N]/shape[M]` = 特定元素，`/header[1]` / `/footer[1]` = 页眉/页脚。

**注意：**
- 默认区分大小写。不区分大小写：`--prop 'find=(?i)error' --prop regex=true`
- 匹配可跨越 run 边界
- 无匹配 = 静默成功。`--json` 中包含 `"matched": N`
- **Excel：** 只支持 `find` + `replace`（不支持 find + 格式属性）

### add ： 添加元素或克隆

```bash
officecli add <file> <parent> --type <type> [--prop ...]
officecli add <file> <parent> --type <type> --after <path> [--prop ...]   # insert after anchor
officecli add <file> <parent> --type <type> --before <path> [--prop ...]  # insert before anchor
officecli add <file> <parent> --type <type> --index N [--prop ...]        # 0-based position (legacy)
officecli add <file> <parent> --from <path>                               # clone existing element
```

`--after`、`--before`、`--index` 互斥。不带位置标志 = 追加到末尾。

**元素类型（含别名）：**

| 格式 | 类型 |
|--------|-------|
| **pptx** | slide（含隐藏页），shape（font.latin/ea/cs、direction=rtl、underline.color、highlight=COLOR（Add/Set/Get/HTML 预览）、effective.X+effective.X.src；arrow 是 rightArrow 的别名；slideMaster/slideLayout 支持带类型的 add/set/remove），picture（SVG、brightness/contrast/glow/shadow、rotation、link、tooltip），chart（direction=rtl、pieOfPie、barOfPie、axisLine/gridline 逐属性 setter、animation+chartBuild=byCategory\|bySeries、line 的 dropLines/hiLowLines/upDownBars、anchor=x,y,w,h 简写），table（cell 的 direction=rtl、fill/background、内置 PowerPoint 样式目录、/col[C] get + swap/copyFrom、row/col 的 Move/CopyFrom），row（tr），connector（from/to 接受完整路径的 `@name=`/`@id=` 形式 ， 裸 `@name=Foo` 会被拒绝，必须写成 `/slide[N]/shape[@name=Foo]` ， startshape/endshape 支持按路径设置（SetByPath）；默认端到端（edge-to-edge）锚定，fromSide/toSide 可强制指定边，fromIdx/toIdx 用于原始 cxn 索引），group（link、tooltip、可通过 get/query/add/remove 深度遍历，ungroup=true 会解散回 slide 绝对坐标），align/distribute（targets= 接受 shape[@id=N] 路径，不限于位置索引），video/audio（loop、autoStart 别名），equation，notes（direction=rtl、lang），comment（传统版 + 现代 p188 串联回复的往返读写），animation（15 个强调 + 16 个退出预设、多效果链、motion-path 预设、repeat/restart/autoReverse、图表动画），transition（12 个 p15 预设 + morph/p14），paragraph（para），run，zoom，ole（preview=，通过 add-part+raw-set 实现完整 dump 往返），placeholder（phType=...），model3d（rotation=ax,ay,az；完整 dump 往返），smartart（通过 add-part 实现 dump 往返），diagram（仅添加：mermaid → 原生形状或渲染图片，`--type diagram`/`flowchart`）。 |
| **docx** | paragraph（direction/font.latin/ea/cs、bold.cs/italic.cs/size.cs、lang.latin/ea/cs、wordWrap、framePr.\*、tabs 简写），run（lang 槽位、direction、underline.color、position 半磅单位、**revision.type=ins\|del\|format\|moveFrom\|moveTo + revision.action=accept\|reject**（带 .author/.date）， 在 `set /revision[...]` 上可用裸 `@author=`/`@type=` 选择器做按条件 accept/reject，但 `query 'revision[...]'` 需要用点号形式 `revision.author=`/`revision.type=`；move+revision 仅支持 run 级路径，不支持段落级；段落/shape 路径上的 **range=START:END** 可按显式 0 基半开偏移量格式化字符区间，而不是定位到某个 run ， 它是 find= 的偏移量版对应功能），table（direction=rtl、hMerge、row 上的 cantSplit / cell 上的 nowrap（add 与 set 均支持）、**虚拟列操作**：在 /body/tbl[N]/col 上执行 add/remove/move/copyfrom），row（tr），cell（td），image，header/footer（direction），section（pageNumFmt 全枚举、direction=rtl、rtlGutter、pgBorders=box），bookmark，comment，footnote，endnote，formfield，sdt，chart，equation，field（28 种类型），hyperlink，style（Add/Set 支持 direction、indents、pbdr、lineSpacing），toc，watermark，break，ole，**num/abstractNum/lvl**，**tab**，**textbox/shape**（以 add 为主 ， Get 仅返回原始 XML 预览，无结构化回读；Set 仅限 width/height/geometry/fill/line.\*；位置用 `anchor.x`/`anchor.y` 而非裸 x/y；`textDirection`/rotation/gradient/shadow **仅 textbox 支持** ， docx shape 本身既无 rotation 也无 gradient），内嵌 **OLE 在 dump→batch 上支持往返**，**diagram**（仅添加：mermaid → 原生形状或渲染图片，`--type diagram`/`flowchart`，添加时不支持 x/y ， 请通过 `set /body/group[N]` 重新定位）。docDefaults.rtl、autoHyphenation，`get /` 会暴露 locale + /comments /footnotes /endnotes。`create --minimal` 用于生成原始 OOXML 脚手架。 |
| **xlsx** | sheet（visible/hidden/veryHidden、打印边距、printTitleRows/Cols、rightToLeft sheetView、级联感知的重命名），row（c{N}= 单元格内容简写；add 接受 --from /Sheet/col[L]；插入时重写公式引用），col（重写公式引用、移动时命名区域跟随），cell（type=richtext+runs、merge=range/sweep、direction=rtl、phonetic；remove 时 **--shift left\|up**，add 时 shift=right\|down ， 与 Excel UI 对话框行为对齐；公式自动检测；calc 中的 OFFSET/INDIRECT），chart（逐轴 RTL/标题、anchor=x,y,w,h、pareto），image（SVG），comment（direction=rtl），table（listobject），namedrange（definedname、volatile、`[@name=X]`；解析时公式体被内联展开），pivottable（缓存 CoW + 跨透视表共享、labelFilter=field:type:value 仅添加时可用、topN=integer 仅添加时可用、fillDownLabels 是 repeatLabels 的别名而非独立功能、calculatedField），sparkline，validation，autofilter，shape，textbox，CF（databar/colorscale/iconset/formulacf/cellIs/topN/aboveAverage），ole，csv。Query 支持 `merge`/`mergedrange`。Workbook：password。Shape 选择器可枚举 grpSp 内的叶子节点。 |

### 数据透视表（xlsx）

```bash
officecli add data.xlsx /Sheet1 --type pivottable \
  --prop source="Sheet1!A1:E100" --prop rows=Region,Category \
  --prop cols=Year --prop values="Sales:sum,Qty:count" \
  --prop grandTotals=rows --prop subtotals=off --prop sort=asc
```

关键属性：`rows`、`cols`、`values`（Field:func[:showDataAs]）、`filters`、`source`、`position`、`layout`（compact/outline/tabular）、`repeatLabels`、`blankRows`、`aggregate`、`showDataAs`（percent_of_total/row/col、running_total）、`grandTotals`、`subtotals`、`sort`。聚合函数：sum、count、average、max、min、product、stdDev、stdDevp、var、varp、countNums。日期列自动分组。运行 `officecli help xlsx pivottable` 查看完整 schema。

### 文档级属性（所有格式）

```bash
officecli set doc.docx / --prop docDefaults.font=Arial --prop docDefaults.fontSize=11pt
officecli set doc.docx / --prop protection=forms --prop evenAndOddHeaders=true
officecli set data.xlsx / --prop calc.mode=manual --prop calc.refMode=r1c1
officecli set slides.pptx / --prop defaultFont=Arial --prop show.loop=true --prop print.what=handouts
```

运行 `officecli help <format> /` 查看所有文档级属性（docDefaults、docGrid、CJK 间距、calc、print、show、theme、extended）。

### 排序（xlsx）

```bash
officecli set data.xlsx /Sheet1 --prop sort="C desc" --prop sortHeader=true
officecli set data.xlsx '/Sheet1/A1:D100' --prop sort="A asc" --prop sortHeader=true
```

格式：`COL DIR[, COL DIR ...]`。会拒绝包含合并单元格或公式的范围。随行元数据（超链接、批注、条件格式、图形）会自动跟随行移动。

### 文本锚定插入（`--after find:X` / `--before find:X`）

通过段落内的文本匹配来定位插入点。行内类型（run、picture、hyperlink）插入在段落内；块级类型（table、paragraph）会自动拆分该段落。PPT 仅支持行内插入。

```bash
# Word: inline run after matched text
officecli add doc.docx '/body/p[1]' --type run --after find:weather --prop text=" (sunny)"

# Word: block table after matched text (auto-splits paragraph)
officecli add doc.docx '/body/p[1]' --type table --after "find:First sentence." --prop rows=2 --prop cols=2
```

### 克隆

`officecli add <file> / --from '/slide[1]'` ， 连同所有跨部件关系一起复制。

### move、swap、remove

```bash
officecli move <file> <path> [--to <parent>] [--index N] [--after <path>] [--before <path>]
officecli swap <file> <path1> <path2>
officecli remove <file> '/body/p[4]'
```

使用 `--after` 或 `--before` 时可省略 `--to` ， 目标容器会从锚点推断。

### batch ： 一次保存周期内的多个操作

**默认原子化（v1.0.137+）：** 每一项仍然会执行并被逐项报告（因此 `N succeeded, M failed` 的统计依然有意义，每个失败都会显现），但只要*有任何一项*失败，整个 batch 就会回滚 ， 磁盘上的文件与 batch 运行前逐字节一致（已在独立模式和常驻模式下实测确认）。用 `--best-effort` 可恢复旧的"成功多少应用多少"行为（适用于有损的 `dump→batch` 重放场景：为一个不支持的项目丢掉全部结果，还不如保留部分结果）。`--stop-on-error` 只改变运行停止得有多早（剩余项标记为 `skipped`），不改变已执行部分是否保留 ， 如果想要"遇错即停但保留已成功部分"，请将它与 `--best-effort` 组合使用。`--force` 与此无关 ， 它只是 docx 保护绕过。失败项带有机器可读的 `code` 字段（清单与 `error.code` 相同）；被回滚的 batch 其 JSON 摘要会带有 `"atomicRolledBack": true`。

`officecli dump <file> [<path>]` 会生成可重放的 batch JSON 用于往返读写 ， `.docx`（全覆盖）、`.pptx`（文本/表格/图片/图表/备注/主题 + 通过 raw-set 直通支持 OLE/3D/视频/音频/SmartArt/morph/p15 切换效果）、`.xlsx`（单元格/公式/样式 + 表格、条件格式、数据验证、批注、图表、迷你图、图片、形状、数据透视表；切片器/chartEx/OLE 通过原样载体支持）。路径默认为 `/`（整个文档）；传入子树路径（docx：`/body`、`/body/p[N]`、`/body/tbl[N]`、`/theme`、`/settings`、`/numbering`、`/styles`；xlsx：`/SheetName`、`/sheet[N]`）可限定 dump 范围。`officecli refresh <file.docx>` 在重放后重新计算目录页码 / PAGE / 交叉引用（Windows 上使用 Word 后端；其他平台回退到无头 HTML）。`officecli plugins list` 可将对 `.doc`、`.hwpx`、`.pdf` 导出的支持扩展进来。

```bash
echo '[
  {"command":"set","path":"/Sheet1/A1","props":{"value":"Name","bold":"true"}},
  {"command":"set","path":"/Sheet1/B1","props":{"value":"Score","bold":"true"}}
]' | officecli batch data.xlsx --json

officecli batch data.xlsx --commands '[{"op":"set","path":"/Sheet1/A1","props":{"value":"Done"}}]' --json
officecli batch data.xlsx --input updates.json --best-effort --json   # keep whatever succeeds even if some items fail
```

支持：`add`、`set`、`get`、`query`、`remove`、`move`、`swap`、`view`、`raw`、`raw-set`、`validate`。字段：`command`（或 `op`）、`path`、`parent`、`type`、`from`、`to`、`index`、`after`、`before`、`props`、`selector`、`mode`、`depth`、`part`、`xpath`、`action`、`xml`。

---

## L3：原始 XML

当 L2 无法表达你的需求时使用。无需 xmlns 声明 ， 前缀会自动注册。

```bash
officecli raw <file> <part>                          # view raw XML
officecli raw-set <file> <part> --xpath "..." --action replace --xml '<w:p>...</w:p>'
officecli add-part <file> <parent>                   # create new document part (returns rId)
```

`raw-set` 动作：`append`、`prepend`、`insertbefore`、`insertafter`、`replace`、`remove`、`setattr`。运行 `officecli help <format> raw` 查看可用的部件。

---

## 常见陷阱

| 陷阱 | 正确做法 |
|---------|-----------------|
| `--name "foo"` | 请用 `--prop name="foo"` ， 所有属性都要通过 `--prop` 传递 |
| 在 zsh/bash 中不加引号的 `[N]` 路径 | 始终加引号：`'/slide[1]'` 或 `"/slide[1]"`（shell 会对括号做 glob 展开） |
| 用 PPT 的 `shape[1]` 放内容 | `shape[1]` 通常是标题占位符。内容形状请用 `shape[2]+` |
| `/shape[myname]` | 不支持按名称索引。请用数字索引或 `@name=`（仅 PPT） |
| 猜测属性名 | 运行 `officecli help <format> <element>` 查看确切名称 |
| 修改已被打开的文件 | 先在 PowerPoint/WPS 中关闭该文件 |
| shell 字符串中的 `\n` | 在 `--prop text="..."` 中换行请用 `\\n` |
| shell 文本中的 `$` | `--prop text="$15M"` 会把 `$15` 剥掉。请用单引号：`--prop text='$15M'`，或改用 heredoc batch |

---

## 专用 Skill

`officecli load_skill <name>` ， 输出是一份 SKILL.md，遵循其中的规则。

**加载规则**：
- 在"何时使用"中选最具体的匹配；都不匹配时加载格式默认项（`word` / `pptx` / `excel`）。
- 场景 Skill 中已包含格式默认项的规则 ， 每个产物只加载 **一个** Skill，绝不叠加。
- 已加载的规则跨轮次持续有效；不要每次回复都重新加载。
- 两个不同产物 → 两次独立加载。

### Word (.docx)

| 名称 | 何时使用 |
|------|-------------|
| `word` | 报告、信函、备忘录、提案、通用文档 |
| `academic-paper` | 期刊 / 会议 / 学位论文：APA / Chicago / IEEE / MLA 引用、公式、SEQ + PAGEREF 交叉引用、多栏期刊排版、参考文献。不适用于商业报告或信函（请路由到 `word`） |

### PowerPoint (.pptx)

| 名称 | 何时使用 |
|------|-------------|
| `pptx` | 通用 deck：董事会评审、销售 deck、全员大会、产品发布 |
| `pitch-deck` | **仅限融资** ， 种子轮 / A-C 轮 / SAFE / 可转换票据 / 战略融资。不适用于销售 / 产品 / 董事会 deck（请路由到 `pptx`） |
| `morph-ppt` | 电影级 Morph 动画演示。不适用于静态 deck（请路由到 `pptx`） |
| `morph-ppt-3d` | 3D Morph：GLB 模型、镜头运动、景深。不适用于纯 2D Morph（请路由到 `morph-ppt`） |

### Excel (.xlsx)

| 名称 | 何时使用 |
|------|-------------|
| `excel` | 通用工作簿、公式、数据透视表、跟踪表 |
| `financial-model` | 财务模型、情景分析、预测。不适用于一般数据分析（请路由到 `excel`） |
| `data-dashboard` | CSV/表格数据 → 带图表和迷你图的 KPI / 分析 / 高管看板。不适用于原始数据记录（请路由到 `excel`） |

示例：融资 deck 任务 → `officecli load_skill pitch-deck` → 按输出的规则执行。

---

## 注意事项

- 路径是 **1 基**（XPath 约定）：`'/body/p[3]'` = 第三个段落
- `--index` 是 **0 基**（数组约定）：`--index 0` = 第一个位置
- **Excel 例外**：对 `add --type row` 和 `add --type col`，`--index N` 是 **1 基**（与 OOXML RowIndex / 列字母索引一致）。`--index 5` 插入到第 5 行 / 第 5 列。
- 修改完成后，用 `validate` 和/或 `view issues` 验证
- **拿不准时**，运行 `officecli help <format> <element>`，不要靠猜
