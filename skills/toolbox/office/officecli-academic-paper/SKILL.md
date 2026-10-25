---
name: officecli-academic-paper
description: "当需要生成学术风格的 .docx 输出时使用本 Skill：期刊 / 会议 / 学位论文章节，包含正式引用格式（APA、Chicago、IEEE、MLA）、编号公式、图表交叉引用、脚注/尾注、参考文献（bibliography）或多栏期刊排版。触发短语：'research paper'（研究论文）、'journal paper'（期刊论文）、'conference paper'（会议论文）、'manuscript'（投稿稿件）、'thesis'（学位论文）、'APA'、'MLA'、'Chicago'、'IEEE two-column'、'bibliography'（参考文献表）、'hanging indent'（悬挂缩进）、'citation style'（引用格式）、'abstract + keywords'（摘要 + 关键词）、'equation numbering'（公式编号）、'cross-reference'（交叉引用）、带脚注/尾注的论文。输出为单个 .docx 文件。"
---

> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/officecli-academic-paper/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# OfficeCLI 学术论文 Skill

**本 Skill 是 `officecli-docx` 之上的场景层。** 每条 docx 硬规则——样式架构、标题层级、shell 引号、分页规则、活动 PAGE 域、交付门（Delivery Gate）、渲染器怪癖——都是被继承的，不再重讲。本文件只补充学术论文在其之上需要的内容：引用格式、公式、SEQ / PAGEREF 交叉引用、多栏期刊排版、参考文献悬挂缩进、摘要/关键词/作者单位信息块。

当 docx 基础规则已覆盖时，这里的文字会写 `→ see docx v2 §X`。如果还没读过 docx v2，请先读它。

## 环境准备

如果 `officecli` 缺失：

- **macOS / Linux**：`curl -fsSL https://d.officecli.ai/install.sh | bash`
- **Windows (PowerShell)**：`irm https://d.officecli.ai/install.ps1 | iex`

用 `officecli --version` 验证（如果 PATH 尚未生效，新开一个终端）。若安装失败，从 https://github.com/iOfficeAI/OfficeCLI/releases 下载二进制文件。

## ⚠️ 先查帮助规则

**本 Skill 教的是学术论文需要什么，而不是每一条命令参数。** 当属性名（prop name）、枚举值或字段指令不确定时，先查 help 再猜。

```bash
officecli help docx                          # All docx elements
officecli help docx <element>                # Full schema (e.g. section, equation, field, footnote)
officecli help docx <element> --json         # Machine-readable
```

Help 与所安装的 CLI 版本绑定。**当本 Skill 与 help 冲突时，以 help 为准。** 本文件中的每一条 `--prop X=` 都已通过 `officecli help docx <element>` 逐一 grep 核验——如果后续版本的 help 新增或重命名了某属性，请相信 help。

## 心智模型与继承关系

**继承 docx v2。** 你应当已读过 `skills/officecli-docx/SKILL.md`。本 Skill 假设你已经会添加段落、设置样式、构建表格、插入图片、管理 TOC/页脚/页眉、强制分页，以及执行交付门（Delivery Gate）。如果以上任何一项不熟悉，请先另开一个会话学习 docx v2 再继续。

## Shell 与执行纪律

**shell 引号、增量执行、`$FILE` 约定** → see docx v2 §Shell & Execution Discipline。同样的规则在这里逐字适用——引用 `[N]` 路径，对任何含 `$` 的值加单引号（包括正文段落里的 `$2.8B` 或含 `@` 的 DOI），绝不在可执行示例中手写 `\$ \t \n`，一次只执行一条命令。下文的学术论文示例用 `$FILE` 作为 shell 变量（`FILE="thesis.docx"`）。

## 这里"学术"的含义（身份定位）

学术论文是在 docx 之上叠加**学术层**的文档：可核验的引用、精确的公式、保持同步的交叉引用、排版好的参考文献列表。docx 基础规则仍然全部适用；学术层在此基础上新增六条差异项：

1. **引用格式是一份契约。** APA / Chicago / IEEE / MLA 各自规定了作者写法、日期位置、参考文献列表排序、正文内标记形态。开工时选定一种；之后所有决定（悬挂缩进、脚注还是夹注、`[1]` 还是 `(Smith, 2024)`）都随之而定。
2. **公式是一等公民内容**——行内 `oMath` 嵌在行文之中，展示式 `oMathPara` 独立成块，可选编号。
3. **图和表自动编号。** `SEQ Figure` / `SEQ Table` 域负责计数；`PAGEREF` 把"见 Fig. 2"链接到其实时页码。
4. **参考文献使用悬挂缩进**（首行顶格，续行缩进）。不是首行缩进。不是单纯的左缩进。是悬挂缩进。
5. **摘要 / 关键词 / 作者单位信息块**是首页三件套，不是市场营销意义上的封面。块状摘要，无首行缩进，无装饰。
6. **多栏排版**常见于 IEEE / ACM / Nature / 许多期刊：单栏摘要 + 双栏正文。

### 反向移交——何时退回 docx

白皮书、政策简报、技术报告、HR 模板——一切没有投稿渠道 / 引用格式的文档，留在 **docx v2**。只有当文档至少满足以下两项时才用**本 Skill**：带引用格式的参考文献、公式、SEQ/PAGEREF 交叉引用、多栏、摘要 + 关键词块。

## 工作流——5 个动词

1. **读投稿规范。** APA 7 / Chicago 17 / IEEE / MLA 9 / 期刊自有规范。行距、字体、引用形态、文献排序——后续一切皆由这一个决定派生。
2. **规划章节。** 摘要 → 关键词 → 引言 → 方法 → 结果 → 讨论 → 结论 → 参考文献。估算标题数量以决定 TOC（3 个及以上标题 = 加 TOC，see docx v2 §Table of Contents）。
3. **预先建好样式。** Heading1 / Heading2 / Heading3 / Caption / AbstractTitle / Bibliography。在任何内容之前定义所有样式（→ see docx v2 §Paragraphs and styles——同一规则，跳过它的失败模式也相同）。
4. **按顺序构建正文。** 封面 / 标题块 → 摘要 → 关键词 → TOC（如需要）→ 按阅读顺序的正文各节 → 带 SEQ 题注的图 / 表 → 参考文献 → 脚注最后按段落路径添加。
5. **QA——交付门（Delivery Gate）。** 继承 docx v2 的 Gate 1-3，再加上下文的学术 Gate 4-5。

## 要求（docx v2 之上的学术底线）

docx v2 §Requirements for Outputs 中的全部内容都适用。在此之上，学术论文必须满足以下附加规则：

### 排版与间距（随投稿渠道而定）

- **字体。** 正文 Times New Roman 11-12pt（默认）或按投稿渠道指定（IEEE 用 Times 10pt 双栏；APA 允许 Calibri 11pt）。全文正文统一字体；标题不使用装饰性字体。
- **标题层级。** H1 = 20pt 粗体，H2 = 14pt 粗体，H3 = 12pt 粗斜体，正文 = 11-12pt。（与 docx v2 相同的数字——重申一遍，因为学术论文绝不能依赖 Word 默认值。）
- **行距。** APA 7 = 2x（双倍）。Chicago / IEEE / 大多数期刊 = 1.5x。绝不低于 1.15x。设在正文段落和 References 上。
- **页边距。** 四周 1 inch（1440 twips），除非投稿渠道另有规定（一些期刊要求左边距 1.25in 以便装订——查规范）。

### 摘要、参考文献、题注位置

- **摘要为块状样式。** 不用 `firstLineIndent`。用 `spaceAfter=12pt` 制造段落间距。如果 `view issues` 对某个 Abstract 段落报告"正文段落缺少首行缩进"，那是误报——忽略它。
- **参考文献使用悬挂缩进。** 每条文献是一个段落，带 `indent=720 hangingIndent=720`（左缩进 0.5"，首行反向缩进等量）。首行顶格；折行缩进到作者名之下。
- **图题注置于图下方。表题注置于表上方。** 这是非学术界人士最容易搞错的一条规则——APA、Chicago、IEEE、MLA 在此完全一致。
- **引用往返闭环。** 每个正文内引用键都必须能在参考文献列表中解析到对应条目。交付门 Gate 4 负责核验。
- **SEQ 存在性。** 任何带编号图或编号表的论文都必须携带活动 `SEQ Figure` / `SEQ Table` 域（而不是硬编码的"Figure 1"文字——在文档中部插入新图时会脱节）。交付门 Gate 5 负责核验。

### 封面 / 首页信息块

学术封面不同于职业文档封面。最少元素：标题（居中，20-22pt 粗体）、作者、单位、投稿目标或期刊、日期、摘要、关键词。docx v2 §Visual delivery floor 的"60% 填充"规则仍然适用——三行封面配半页留白即失败。首页配方见下文 §摘要 / 关键词 / 作者单位信息块。

### 章节编号约定（依样式而定——切勿盲目套用）

学术章节编号是**标题文本的一部分**，不通过列表编号计算。`officecli` 的 `numId`/`listStyle` 机制在 Heading1 复用时很脆弱，所以要手写前缀。但前缀形态因样式而异——四种样式不要用同一种写法：

| 样式 | H1 格式 | H2 格式 | 示例 |
|---|---|---|---|
| **APA 7** | **不编号、居中、粗体** | 不编号、左对齐、粗体 | `Introduction` / `Methods`（居中） |
| **Chicago** | `"N. Title"` 左对齐 | `"N.M Title"` | `1. Introduction`、`2.1 Policy Formation` |
| **IEEE** | `"N. TITLE"` 全大写 + 罗马数字 | `A. Subtitle` title case | `I. INTRODUCTION`、`II. RELATED WORK`、`A. Datasets` |
| **MLA 9** | 不编号、左对齐、粗体 | 同上 | `Literature Review`（无前缀） |

APA 7 的一级标题**居中、粗体、不编号**；二级标题左对齐粗体；三级标题左对齐粗斜体；四级/五级为 run-in。不要给 APA 标题加 `1. / 2.` 前缀——那是 Chicago/IEEE 的约定。IEEE 要求全大写加罗马数字（`I. INTRODUCTION`）；每节内部用 `A./B./C.` 子标题（title case）。阿拉伯数字编号的正文章节仅属 Chicago 风格。

**四种样式共同的例外**：References / Bibliography / Works Cited / Acknowledgments 无论何种样式都不编号——省略 `N.` 前缀。

## 快速上手——最小 APA 论文

```bash
FILE="paper.docx"
officecli create "$FILE"
officecli open "$FILE"
officecli set "$FILE" / --prop defaultFont="Times New Roman"
officecli add "$FILE" /body --type paragraph --prop text="Remote Work and Team Cohesion" --prop align=center --prop size=20pt --prop bold=true --prop spaceAfter=24pt
officecli add "$FILE" /body --type paragraph --prop text="Alice Chen" --prop align=center --prop size=12pt
officecli add "$FILE" /body --type paragraph --prop text="Department of Psychology, Stanford University" --prop align=center --prop size=11pt --prop spaceAfter=24pt
officecli add "$FILE" /body --type paragraph --prop text="Abstract" --prop align=center --prop size=14pt --prop bold=true --prop spaceBefore=12pt --prop spaceAfter=6pt
officecli add "$FILE" /body --type paragraph --prop text="This study examines remote-work adoption on team cohesion across 18 months..." --prop size=12pt --prop lineSpacing=2x --prop spaceAfter=12pt
officecli add "$FILE" /body --type paragraph --prop text="Keywords: remote work, team cohesion, psychological safety" --prop italic=true --prop size=11pt --prop spaceAfter=18pt
officecli add "$FILE" /body --type paragraph --prop text="1. Introduction" --prop style=Heading1 --prop size=20pt --prop bold=true --prop spaceBefore=18pt --prop spaceAfter=12pt
officecli add "$FILE" /body --type paragraph --prop text="Remote-work research (Smith, 2024) has expanded since 2020..." --prop size=12pt --prop lineSpacing=2x --prop firstLineIndent=720
officecli add "$FILE" /body --type paragraph --prop text="References" --prop style=Heading1 --prop size=20pt --prop bold=true --prop spaceBefore=18pt --prop spaceAfter=12pt
officecli add "$FILE" /body --type paragraph --prop text="Smith, J. (2024). Remote work and cohesion. Journal of Applied Psychology, 109(3), 412-430." --prop size=12pt --prop lineSpacing=2x --prop indent=720 --prop hangingIndent=720
officecli add "$FILE" / --type footer --prop type=default --prop align=center --prop size=10pt --prop field=page
officecli close "$FILE"
officecli validate "$FILE"
```

十行骨架。真实论文通过添加更多正文段落、更多参考文献条目（每条都带同样的 `indent=720 hangingIndent=720` 组合）、带题注的图 / 表，以及在 Heading1 达到 3 个以上时加 TOC 而长大。快速上手示例可通过校验；下面各小节逐一展开每个维度。

## 引用格式配方

四大主流家族。项目开工时选定一种；之后所有决定随之而定。**各样式决策表：**

| 样式 | 正文内标记形态 | 参考文献列表排序 | 正文行距 | 用脚注？ |
|---|---|---|---|---|
| APA 7 | `(Smith, 2024)` 或 `Smith (2024)` | 按作者字母序 | 2x（双倍） | 少见（仅内容注） |
| Chicago 17 (Notes-Bib) | 上标脚注编号 | 按作者字母序 | 1.5x-2x | **主要方式**（完整引文写入脚注） |
| IEEE | `[1]`、`[2]`、...、`[N]` | 按首次引用顺序 | 1.15x-1.5x，双栏 | 少见 |
| MLA 9 | `(Smith 412)` 页码式 | 按作者字母序，标题"Works Cited" | 2x | 少见 |

四种样式共通的默认值：参考文献列表段落用 `indent=720 hangingIndent=720`（悬挂缩进 0.5"）；Heading1 达 3 个以上时加活动 TOC（→ see docx v2 §Table of Contents）；设置 `updateFields=true`，并在 Word 兼容的域引擎更新之前把 TOC 页码报告为"未计算"。

### APA 7（社会科学——心理学、教育学、管理学）

- 正文内：`(Author, Year)`，叙事式用 `Author (Year)`。直接引语必须带页码：`(Smith, 2024, p. 15)`。三位及以上作者：首次引用之后用 `(Smith et al., 2024)`。
- 参考文献列表排序：**按第一作者姓氏字母序**。标题大小写：论文标题用 sentence case，期刊名用 title case（斜体）。
- 文献条目形态：`Author, A. A., & Co-Author, B. B. (Year). Title of article. Journal Name, Volume(Issue), pages.` 优先用 DOI 而非 URL；以 https URL 形式呈现，不用 `doi:` 前缀。
- 全部双倍行距（`lineSpacing=2x`），包括摘要和参考文献。正文首行缩进 0.5"（`firstLineIndent=720`）。

```bash
# Body paragraph with parenthetical citation
officecli add "$FILE" /body --type paragraph --prop text="Remote work adoption accelerated during the pandemic (Kramer & Kramer, 2020)." --prop size=12pt --prop lineSpacing=2x --prop firstLineIndent=720
# Reference entry with hanging indent
officecli add "$FILE" /body --type paragraph --prop text="Kramer, A., & Kramer, K. Z. (2020). The potential impact of the Covid-19 pandemic on occupational status. Journal of Vocational Behavior, 119, 103442." --prop size=12pt --prop lineSpacing=2x --prop indent=720 --prop hangingIndent=720
# DOI hyperlink appended to the reference paragraph
officecli add "$FILE" "/body/p[last()]" --type hyperlink --prop url="https://doi.org/10.1016/j.jvb.2020.103442" --prop text="https://doi.org/10.1016/j.jvb.2020.103442"
```

QA：`officecli query "$FILE" 'paragraph[hangingIndent]'` 应返回每一条参考文献条目；出现首行缩进而非悬挂缩进的文献条目数为零。

### Chicago 17 — Notes-Bibliography（人文学科——历史、哲学、宗教学）

- 正文内：上标脚注编号；完整引文写入首个脚注（`Timothy Brook, The Troubled Empire (Cambridge, MA: Harvard UP, 2010), 142.`）；其后一律用**简化形式**（`Brook, Troubled Empire, 150.`）。
- **重复引用规则（Chicago 17，op. cit. 已弃用）：**
  - **紧邻连续**引用**同一来源、同一页** → `Ibid.`
  - **紧邻连续**引用同一来源但**不同页** → `Ibid., 22.`
  - 非连续的重复引用 → **简化形式**（`Brook, Troubled Empire, 150.`），不用 `op. cit.`。Chicago 17 取消了 `op. cit.`——除紧邻重复外一律用简化形式。
- 文末设 Bibliography，**按第一作者姓氏字母序**（"Brook, Timothy."），悬挂缩进。脚注正文按查看器的脚注默认值渲染（通常 10pt）；bibliography 条目 12pt。（`footnote` 元素只暴露 `text`——字号不能按脚注单独设置；相信渲染器默认值。）
- 以一手史料为主的论文的典型拆分：单个 `Bibliography` Heading1 之下设 `Primary Sources` 和 `Secondary Sources` 两个 Heading2。书名在脚注和 bibliography 中都用斜体。
- Chicago 还有一个自然科学使用的 Author-Date 变体——如果投稿渠道指定 Chicago Author-Date，退回 APA 配方，只改标点（作者与年份之间无逗号：`(Smith 2024)`）。

```bash
# Body paragraph that will anchor a footnote, then the footnote itself
officecli add "$FILE" /body --type paragraph --prop text="The Ming dynasty's 海禁 policy shaped coastal trade for two centuries." --prop size=12pt --prop lineSpacing=1.5x --prop firstLineIndent=720
officecli add "$FILE" "/body/p[last()]" --type footnote --prop text="Timothy Brook, The Troubled Empire: China in the Yuan and Ming Dynasties (Cambridge, MA: Harvard University Press, 2010), 142."
# Next footnote — shortened form
officecli add "$FILE" "/body/p[last()]" --type footnote --prop text="Brook, Troubled Empire, 150."
# Bibliography section split — primary sources first
officecli add "$FILE" /body --type paragraph --prop text="Bibliography" --prop style=Heading1 --prop size=20pt --prop bold=true --prop spaceBefore=18pt
officecli add "$FILE" /body --type paragraph --prop text="Primary Sources" --prop style=Heading2 --prop size=14pt --prop bold=true --prop spaceBefore=12pt
officecli add "$FILE" /body --type paragraph --prop text="Ming Shilu 明實錄. Taipei: Academia Sinica, 1966." --prop size=12pt --prop indent=720 --prop hangingIndent=720
officecli add "$FILE" /body --type paragraph --prop text="Secondary Sources" --prop style=Heading2 --prop size=14pt --prop bold=true --prop spaceBefore=12pt
officecli add "$FILE" /body --type paragraph --prop text="Brook, Timothy. The Troubled Empire: China in the Yuan and Ming Dynasties. Cambridge, MA: Harvard University Press, 2010." --prop size=12pt --prop indent=720 --prop hangingIndent=720
```

QA：`officecli query "$FILE" 'footnote'` 的数量 ≥ 带引用的正文段落数。

### IEEE（工程领域——汇刊、会议论文集）

- 正文内：`[1]`、`[2]`。按**首次出现顺序**编号，不按字母序。重复引用复用同一编号。页码引用用 `[1, p. 15]`，区间用 `[1]-[3]`。
- 文献条目以方括号编号开头：`[1] A. Smith and B. Jones, "Title," IEEE Trans. X, vol. 5, no. 3, pp. 1-10, 2024, doi: ...`。作者名缩写在前、姓在后；期刊名按 IEEE 缩写表缩写（`IEEE Trans. Neural Netw.`，不用全名）。
- 正文为**双栏**（see §多栏排版）。摘要是版面上方（above the fold）的单栏，10pt，1.15x 行距，通常 200-250 词。
- 正文段落首行缩进 = 0.2"（`firstLineIndent=288` twips ≈ 14pt）。比 APA 的 0.5" 小，因为双栏栏宽更窄。
- **章节标题：全大写 + 罗马数字**——`I. INTRODUCTION`、`II. RELATED WORK`、`III. METHOD`。子节 `A. Datasets`、`B. Baselines` 用 title case。IEEE 不要用 `1. Introduction`（阿拉伯数字）——那是 Chicago 风格。
- **表格编号用罗马数字**：`Table I`、`Table II`、`Table III`。图保持阿拉伯数字（`Fig. 1`、`Fig. 2`）。`recalcFields=seq` 对两者都写入阿拉伯数字缓存值——IEEE 罗马数字表格要么在 recalc 后手动把缓存的 `<w:t>` 改成罗马数字，要么接受阿拉伯数字并在投稿信中说明。

```bash
# Body citing reference 1
officecli add "$FILE" /body --type paragraph --prop text="Attention-based anomaly detection has been applied to industrial sensor data [1], [2]." --prop size=10pt --prop lineSpacing=1.15x
# Reference list entry — number in the text
officecli add "$FILE" /body --type paragraph --prop text="[1] A. Smith and B. Jones, \"Attention for anomaly detection,\" IEEE Trans. Neural Netw., vol. 35, no. 2, pp. 412-430, 2024." --prop size=10pt --prop indent=720 --prop hangingIndent=720
officecli add "$FILE" /body --type paragraph --prop text="[2] C. Lee, \"Time-series anomaly survey,\" in Proc. ICML, 2023, pp. 1200-1215." --prop size=10pt --prop indent=720 --prop hangingIndent=720
```

QA：正文中最高的 `[N]` 必须等于参考文献列表条目数。Grep：`officecli view "$FILE" text | grep -oE '\[[0-9]+\]' | sort -u | tail -5`。

### MLA 9（文学、语言学、文化研究）

与 APA 的差异：正文内为 `(Author Page)`，**无逗号**（如 `(Smith 412)`）；直接引语必须带页码。文献节标题为 **Works Cited**（不叫 References / Bibliography）。条目按姓氏字母序排列，悬挂缩进，2x 行距，九个"核心元素"以句点分隔：`Author. Title. Container, Other Contributors, Version, Number, Publisher, Date, Location.`——不适用的元素直接跳过。书名斜体；论文标题加引号。其余段落设置与 APA 相同。

## 公式（OMML——行内 vs 展示式）

`--type equation` 把类 LaTeX 公式解析为 OMML。两种模式，由 `--prop mode=` 选择：

| 模式 | XML | 视觉 | 用途 |
|---|---|---|---|
| `display`（默认） | `/body` 处的 `<m:oMathPara>` | 独立居中成块 | 编号公式、定理陈述 |
| `inline` | 追加到段内某个 run 的 `<m:oMath>` | 随文字连排 | 行文中的 `if $x > 0$` 之类 |

```bash
# Display equation (own paragraph, centered) — explicitly set mode=display for clarity
officecli add "$FILE" /body --type equation --prop mode=display --prop formula="x^2 + y^2 = z^2"
# Display equation with Greek / subscript / integral — verify rendering below
officecli add "$FILE" /body --type equation --prop mode=display --prop formula="\\lambda_1 + \\alpha"
officecli add "$FILE" /body --type equation --prop mode=display --prop formula="\\frac{1}{2\\pi} \\int_0^{\\infty} e^{-x^2} dx"
# Inline equation INSIDE prose — required whenever variables like x_{t+1}, \lambda, etc. appear in a body paragraph:
officecli add "$FILE" /body --type paragraph --prop text="Given the weight " --prop size=11pt
officecli add "$FILE" "/body/p[last()]" --type equation --prop mode=inline --prop formula="W_t"
officecli add "$FILE" "/body/p[last()]" --type run --prop text=" we define the loss..."
```

**验证公式渲染为 OMML 数学**，而不是纯文本 LaTeX 记号。`close` 之后执行：

```bash
officecli view "$FILE" text | head -20       # λ₁ + α, ∫₀∞, x² must appear as unicode math (verified renders)
officecli raw "$FILE" /document | grep -c '<m:oMathPara'   # ≥ 1 per display equation
```

如果正文行文里出现原始的 `lambda_1`、`x_{t+1}`、`\alpha` 之类纯文本记号（也就是说你把它们敲进了 `paragraph --prop text=`，而没有用 `--type equation --prop mode=inline` 包裹），下游查看器会把它们渲染成字面 ASCII。**规则：行文中的每个数学变量 / 希腊字母 / 下标都必须走 `--type equation mode=inline`，绝不走 `paragraph --prop text=`。**

**LaTeX 子集陷阱**（不可协商）：

1. `\left(...\right)` / `\left[...\right]` 且定界符**内部**带上下标 → 解析错误（`Error: cast object … Subscript`）。外层上标（`\left(x+y\right)^2`）没问题；普通 `(`、`)`、`[`、`]` 始终可用，且 OMML 在 display 模式下会自动调整其大小。
2. 对 `/body/oMathPara[N]` 执行 `move` 会重排展示式公式（它移动的是包裹段落）。`--before <path>` 可能留下一个游离的空段落；干净的排序请优先 `--index` 或 `--after`。

**公式编号**——没有原生的 `\eqno`。期刊标准版式是**一行**：公式居中，编号右齐到栏边缘（`Y = A(X) ⊗ X      (1)`）。用两个段落**制表位**构建——栏中点设一个 `center` 制表位、栏右缘设一个 `right` 制表位——然后在单个段落里排 `[tab] equation(inline) [tab] (1)`。不要用居中展示式公式再跟一行单独右对齐的 `(1)`——那会把编号拆到独立一行，这是 agent 复现不出预期版式最常见的原因。

```bash
# Tab positions depend on the COLUMN width (twips). Default blank doc = A4, 3.18cm margins
#   → text width = 8300 twips.
#   single column: center tab = 4150, right tab = 8300
#   two columns (default 720-twip gutter): col = (8300-720)/2 = 3790 → center 1895, right 3790
# (other page size / margins: text width = pageWidth - marginLeft - marginRight; recompute.)
officecli add "$FILE" /body --type paragraph                                   # the equation paragraph (say it lands at p[N])
officecli add "$FILE" "/body/p[N]" --type tab --prop pos=4150 --prop val=center
officecli add "$FILE" "/body/p[N]" --type tab --prop pos=8300 --prop val=right
officecli add "$FILE" "/body/p[N]" --type run --prop text=$'\t'                 # tab → jump to center
officecli add "$FILE" "/body/p[N]" --type equation --prop mode=inline --prop formula='Y = A(X) \otimes X'
officecli add "$FILE" "/body/p[N]" --type run --prop text=$'\t(1)'             # tab → jump to right edge, then the number
```

双栏节直接用双栏制表位（1895 / 3790）；同一段落于是把公式在栏内居中，`(1)` 落在栏右缘。Schema：`officecli help docx tab`。

**不要把 `--type equation` 直接放在表格单元格 `tc[N]` 路径上**——会被守卫错误拒绝（`table cells only accept paragraphs, tables, or SDTs`），因此不会写入坏 XML。若需在单元格内放公式，对 `tc[N]/p[1]` 用 `mode=inline`。

完整公式 schema：`officecli help docx equation`。

## 图、表与交叉引用（SEQ + PAGEREF）

两个原语，都是**原生 fieldTypes**（枚举见 `officecli help docx field`）：`seq` 用于自动编号题注计数器，`pageref` 用于"见 Fig. 2 于第 7 页"式反向引用。原生域插入时带未求值的缓存结果；一条 `set "$FILE" / --prop recalcFields=seq`（see §SEQ 编号）即按文档顺序填入真实编号——无需逐域手工修补。

### SEQ 自动编号——图和表

SEQ 域是一个带名字（`identifier`）的计数器。每次 `SEQ Figure` 在 **recalc** 时使 Figure 计数器加一；每次 `SEQ Table` 使 Table 计数器加一。

**SEQ 缓存值——一条命令，且在所有题注添加完毕之后。** 新加的 SEQ 域没有已求值的缓存编号；recalc 之前 `view text` 显示 `#OCLI_NOTEVAL!{SEQ Figure}` 哨兵（且 `Format["evaluated"]=false`）。**不要逐域手工修补。** 所有图/表题注就位后，执行一次：

```bash
officecli set "$FILE" / --prop recalcFields=seq
```

它按文档顺序对正文中的 `SEQ Figure` / `SEQ Table` 域计数并写入真实缓存值（`Figure 1 / Figure 2 / Figure 3`），把 `evaluated` 翻为 true。在文档中部插入题注后重跑一次，编号即可保持同步。（标题相对的 `\s` 与页眉/页脚内的 SEQ 交由 Word 自行重算——see `help docx document`。）验证：`officecli view "$FILE" text` 显示互不相同且递增的编号。

```bash
# Figure with caption BELOW the image. Caption = "Figure <seq>: title" + optional bookmark for cross-ref.
officecli add "$FILE" /body --type picture --prop src=arch.png --prop width=5in
officecli set "$FILE" "/body/p[last()]/r[last()]" --prop alt="Model architecture: attention over time-series sensors"
# Caption paragraph (below the figure, per academic convention)
officecli add "$FILE" /body --type paragraph --prop text="Figure " --prop style=Caption --prop size=10pt --prop italic=true --prop align=center
officecli add "$FILE" "/body/p[last()]" --type field --prop fieldType=seq --prop identifier=Figure
officecli add "$FILE" "/body/p[last()]" --type run --prop text=": Attention-based anomaly detection model."
# Bookmark the caption so other paragraphs can PAGEREF it
officecli add "$FILE" /body --type bookmark --prop name=fig_arch
# (Numbers are filled later by a single `set / --prop recalcFields=seq`, after all captions exist.)
```

### PAGEREF——按书签交叉引用

```bash
# Cross-ref paragraph: "see Figure 1 on page X"
officecli add "$FILE" /body --type paragraph --prop text="As shown in Figure 1 (see page " --prop size=11pt --prop lineSpacing=1.5x
officecli add "$FILE" "/body/p[last()]" --type field --prop fieldType=pageref --prop name=fig_arch
officecli add "$FILE" "/body/p[last()]" --type run --prop text=")."
```

### 表格——题注在上方

```bash
# Caption first (ABOVE the table), THEN the table
officecli add "$FILE" /body --type paragraph --prop text="Table " --prop style=Caption --prop size=10pt --prop italic=true --prop spaceAfter=6pt
officecli add "$FILE" "/body/p[last()]" --type field --prop fieldType=seq --prop identifier=Table
officecli add "$FILE" "/body/p[last()]" --type run --prop text=": Participant demographics (N=47)."
officecli add "$FILE" /body --type table --prop rows=5 --prop cols=4 --prop width=100%
# ... fill header + rows per docx v2 §Tables
```

### 验证 SEQ + PAGEREF 域已落位

```bash
# At least one SEQ Figure or SEQ Table in the body document part
officecli raw "$FILE" /document | grep -c 'w:instrText[^>]*>[^<]*SEQ'   # expect ≥ 1
officecli raw "$FILE" /document | grep -c 'w:instrText[^>]*>[^<]*PAGEREF' # 0 ok if no cross-refs
```

活动域携带**缓存值**，在有人于 Word 中按 F9 之前渲染的是旧值。recalc 之后应立即看到"Figure 1"显示为 `1`、`2`、…；recalc 之前，某些查看器渲染 `0` 或空白。判断域存在与否要看 `fldChar` 是否存在，而不是看可见数字（→ see docx v2 §Field / cached-value spot-check）。

## 脚注 vs 尾注

**脚注（Footnote）**——位于锚定段落所在页的页底。用于 Chicago Notes-Bib 的文献引注，或任何样式下的内容旁注。

**尾注（Endnote）**——位于文档末尾（或参考文献之前）。某些投稿渠道用它替代脚注，或用于会弄乱页面的长上下文注释。

```bash
# Footnote anchored to paragraph N
officecli add "$FILE" "/body/p[3]" --type footnote --prop text="Smith et al. reported similar findings in their 2023 review."
# Endnote — anchored to paragraph N (like footnote); lands at /endnote[@endnoteId=N]
officecli add "$FILE" "/body/p[3]" --type endnote --prop text="Extended derivation of equation (4) is available at the project repository."
```

两者在 `view annotated` 输出中都显示为空字符串 run（`r[N] ""`）——run 携带的是 `<w:footnoteReference>` XML 元素，而非可见文本。用 `officecli query "$FILE" 'footnote'` 或 `officecli get "$FILE" "/footnotes/footnote[N]"` 确认插入。脚注不会移动段落索引；正文内容就位之后可按任意顺序添加。完整 schema：`officecli help docx footnote` / `officecli help docx endnote`。

## Bibliography 节

每篇学术论文以参考文献列表收尾。节名取决于样式（**References** 用于 APA / IEEE / Chicago Author-Date；**Bibliography** 用于 Chicago Notes-Bib；**Works Cited** 用于 MLA）。每条文献是一个独立段落，带**悬挂缩进**。

```bash
# Section heading — same as body Heading1 (excluded from body numbering by convention)
officecli add "$FILE" /body --type paragraph --prop text="References" --prop style=Heading1 --prop size=20pt --prop bold=true --prop spaceBefore=18pt --prop spaceAfter=12pt
# Each entry: hanging indent 720 twips (0.5"), with indent=720 as the partner (first line flush, wraps indented)
officecli add "$FILE" /body --type paragraph --prop text="Smith, J. (2024). Remote work and cohesion. Journal of Applied Psychology, 109(3), 412-430." --prop size=12pt --prop lineSpacing=2x --prop indent=720 --prop hangingIndent=720
# DOI hyperlink on its own run appended to the entry paragraph
officecli add "$FILE" "/body/p[last()]" --type hyperlink --prop url="https://doi.org/10.1037/apl0001123" --prop text="https://doi.org/10.1037/apl0001123"
```

已验证：`--prop indent=720 --prop hangingIndent=720` 是 `officecli help docx paragraph` 认定的规范悬挂缩进组合。旧的 `ind.firstLine=-720` 形式（负首行缩进）不是规范形式，emit 时会挂 schema——→ see docx v2 §Schema-invalid-on-emit。

**往返闭环 QA。** 对比正文内引用标记数（APA `(Author, Year)`、IEEE `[N]`、MLA `(Author N)`）与参考文献列表条目数。见下文交付门 Gate 4。每个被引键必须可解析；每条被列条目应至少被引用一次。

## 多栏排版（IEEE 期刊双栏配方）

IEEE 与许多工程 / 物理期刊把正文排成双栏，摘要在其上方保持单栏。机制：一个 `type=continuous` 且 `columns=2` 的节分隔符，然后在结尾再加一个节分隔符**还原**为单栏。

**还原这一步不是可选的。** 缺了它，文档其余部分——包括参考文献——都会渲染成双栏。这是多栏排版最常见的单一失败点。

```bash
FILE="ieee.docx"
officecli create "$FILE"
officecli open "$FILE"

# 1. Title, authors, affiliation — single-column (the default first section)
officecli add "$FILE" /body --type paragraph --prop text="Attention-Based Anomaly Detection for Industrial Time Series" --prop align=center --prop size=18pt --prop bold=true --prop spaceAfter=12pt
officecli add "$FILE" /body --type paragraph --prop text="Alice Chen, Bob Martinez" --prop align=center --prop size=11pt
officecli add "$FILE" /body --type paragraph --prop text="Department of CS, Stanford University" --prop align=center --prop size=10pt --prop spaceAfter=18pt

# 2. Abstract — still single-column, block-style
officecli add "$FILE" /body --type paragraph --prop text="Abstract" --prop align=center --prop size=12pt --prop bold=true --prop spaceAfter=6pt
officecli add "$FILE" /body --type paragraph --prop text="We present an attention-based model for detecting anomalies in industrial sensor time series..." --prop size=10pt --prop lineSpacing=1.15x --prop spaceAfter=12pt

# 3. Section break + two-column from here on
#    `/section[last()]` resolves to the final section (like p[last()]); an explicit /section[N] also works.
officecli add "$FILE" /body --type section --prop type=continuous
SECTION_COUNT=$(officecli query "$FILE" section --json | jq '.data.results | length')
# After the add, SECTION_COUNT should be 2 — [1] is pre-break, [2] is post-break (2-col body area).
officecli set "$FILE" "/section[2]" --prop columns=2 --prop columnSpace=1cm

# 4. Body — IEEE wants Roman numerals + ALL CAPS section titles (P1.2).
officecli add "$FILE" /body --type paragraph --prop text="I. INTRODUCTION" --prop style=Heading1 --prop size=10pt --prop bold=true
officecli add "$FILE" /body --type paragraph --prop text="Industrial anomaly detection has been studied since [1]..." --prop size=10pt --prop lineSpacing=1.15x --prop firstLineIndent=360

# 5. At the end of 2-column body, ANOTHER section break + revert to single column for references / appendices
# (If you want references in 2-col too, skip step 5 — but most IEEE papers use 2-col for references as well.)
# officecli add "$FILE" /body --type section --prop type=continuous
# Use /section[last()] for the final section, or re-count for an explicit /section[N]:
# officecli set "$FILE" "/section[3]" --prop columns=1

# 6. Footer, close, validate
officecli add "$FILE" / --type footer --prop type=default --prop align=center --prop size=9pt --prop field=page
officecli close "$FILE"
officecli validate "$FILE"
```

**视觉核验。** 运行 `officecli view "$FILE" html` 并 Read 返回的 HTML 来审查渲染输出。摘要必须渲染为通栏，从引言起为双栏。如果摘要折成了两个窄栏，说明第一个节分隔符落在了摘要之前——把它移走。

**节索引记账。** 每次 `add /body --type section` 都会向 `/body` 插入一个空段落（节分隔符标记）。其后所有 `p[N]` 索引按每个节分隔符 +1 偏移。提前规划节分隔符；加完一个分隔符后，用 `officecli get "$FILE" /body --depth 1` 重新索引再继续。

完整节 schema（`columns`、`columnSpace`、`orientation`、`pageNumFmt`、`titlePage`、`lineNumbers`）：`officecli help docx section`。

## 摘要 / 关键词 / 作者单位信息块

首页元数据栈：标题（居中 20-22pt 粗体）→ 作者（居中 12pt，多单位时上标 `^1 ^2`）→ 单位（居中 11pt，与上标对应）→ 投稿目标 / 日期 → **Abstract** 标题（14pt 粗体）→ 摘要正文（块状样式，**不用 `firstLineIndent`**，150-300 词）→ 关键词行（斜体 11pt）。与 docx v2 相同的"封面 ≥ 60% 填充"规则。

```bash
# Superscript affiliation markers (multi-institution paper)
officecli add "$FILE" /body --type paragraph --prop text="Alice Chen" --prop align=center --prop size=12pt
officecli add "$FILE" "/body/p[last()]" --type run --prop text="1" --prop superscript=true
officecli add "$FILE" "/body/p[last()]" --type run --prop text=", Bob Martinez"
officecli add "$FILE" "/body/p[last()]" --type run --prop text="2" --prop superscript=true
# Running header (skip on cover via type=first empty header — see docx v2 §headers)
officecli add "$FILE" / --type header --prop type=default --prop align=right --prop size=9pt --prop text="Short Running Title"
```

**Nature 系双栏摘要**很少见——若确有要求，在摘要标题**之前**开一个 `section type=continuous columns=2`；短摘要（<100 词）会造成参差不齐的栏。**奇偶页镜像页眉**已由高层 API 暴露：`officecli set "$FILE" /settings --prop evenAndOddHeaders=true`，然后用 `--type header --prop type=even` 添加偶数页页眉。完整页眉 schema：`officecli help docx header`。

## QA——交付门（Delivery Gate，可执行）

**假设一定存在问题。你的任务是把它们找出来。** 首次渲染几乎从不正确。在宣布完成之前运行这一整块。

### Gate 1-3——继承自 docx v2

→ see docx v2 §Delivery Gate。schema 校验、token 泄漏 grep、活动 PAGE 域结构。先把 docx v2 的 gate 代码块原样复制过来。每项检查都必须打印其成功消息。

### Gate 4——引用往返闭环

每个正文内引用键都应能解析到 bibliography 条目。计数不匹配 = REJECT。

```bash
# IEEE example (bracketed numerics). Adjust regex for APA (Author, Year) or MLA (Author Page).
CITATIONS=$(officecli view "$FILE" text | grep -oE '\[[0-9]+\]' | sort -u | wc -l)
ENTRIES=$(officecli query "$FILE" 'paragraph[hangingIndent]' --json | jq '.data.results | length')
echo "In-text citation markers: $CITATIONS | Bibliography entries: $ENTRIES"
# REJECT when citations exceed entries (cites without references). Entries > citations is allowed by some venues.
[ "$CITATIONS" -le "$ENTRIES" ] && echo "Gate 4 OK" || { echo "REJECT Gate 4: $CITATIONS in-text markers but only $ENTRIES bibliography entries"; exit 1; }
```

### Gate 5a——SEQ 存在性 + 缓存编号互异

如果论文含任何编号图或编号表，正文必须携带活动 `SEQ` 域，且其缓存值必须显示为互不相同、递增的编号（否则 `view text` 和不重算缓存域的下游查看器会把所有图都显示成"Figure 1"）。

```bash
# Count SEQ fields via query (raw-grep collapses multi-matches on one XML line → undercounts).
SEQ_COUNT=$(officecli query "$FILE" 'field[fieldType=seq]' --json | jq '.data.results | length')
VISIBLE_FIG=$(officecli view "$FILE" text | grep -cE '(Figure|Table) [0-9]+')
if [ "$VISIBLE_FIG" -gt 0 ] && [ "$SEQ_COUNT" -eq 0 ]; then
  echo "REJECT Gate 5a: $VISIBLE_FIG visible Figure/Table labels but 0 SEQ fields."
  exit 1
fi
# Cached values must be distinct. Run `set / --prop recalcFields=seq` once after all captions exist;
# before recalc the fields render the #OCLI_NOTEVAL! sentinel, after recalc Figure 1 / Figure 2 / Figure 3:
DISTINCT=$(officecli view "$FILE" text | grep -oE '(Figure|Table) [0-9]+' | sort -u | wc -l)
[ "$SEQ_COUNT" -le "$DISTINCT" ] && echo "Gate 5a OK (SEQ=$SEQ_COUNT, distinct=$DISTINCT)" || { echo "REJECT Gate 5a: $SEQ_COUNT SEQ fields but only $DISTINCT distinct rendered labels — run 'set \"$FILE\" / --prop recalcFields=seq'"; exit 1; }
```

### Gate 5b——经 HTML 预览做视觉审查（强制，不可省）

Gate 1–5a 能抓 schema 错误、token 泄漏、活动域存在性、引用计数。**它们抓不到物理装配缺陷**——页序错乱、文档中部出现重复的 Abstract、三个图全都标着"Fig. 1"（尽管 SEQ 域存在）、公式变量渲染成纯文本 LaTeX（`lambda_1`、`x_{t+1}`）而非数学。不要跳过——Gate 1–5a 通过 ≠ 视觉合格。

运行 `officecli view "$FILE" html` 并 Read 返回的 HTML 路径。对论文的每一页回答：

> (a) 各页是否按学术逻辑顺序排列？（Title → Abstract → Keywords → Introduction → 正文 → References——不许向前跳页，不许向后泄漏。）
> (b) Abstract 是否恰好出现一次，未在文档中部重复？
> (c) Figure N / Table N 标签是否互异且递增？（Fig. 1、Fig. 2、Fig. 3——而不是全是"Fig. 1"。表同理。）
> (d) 公式是否渲染为数学？（斜体变量、希腊字母如 λ / α、正规的积分 / 分式——而不是纯文本 `lambda_1`、`x_{t+1}`、`\int`。）
> (e) IEEE 论文：节标题是否全大写加罗马数字（`I. INTRODUCTION`）？表格是否用罗马数字（`Table I`、`Table II`）？
> (f) APA 论文：一级标题是否居中粗体且不编号（而不是 `1. Introduction`）？
> (g) 每处正文内的"see Fig. N" / "see Table N"是否都能解析到实际带有该编号的图/表？
> (h) H1 / H2 / H3 的标题层级在视觉上是否可区分（字号 + 字重）？

逐一报告所有缺陷。只要存在一处缺陷 → REJECT；修复前不得交付。

**人工预览（可选）。** 若想让用户视觉预览论文，运行 `officecli watch "$FILE"` 提供一个实时预览，由用户自行决定是否打开；或让用户直接在 Word / WPS / Pages 中打开该 `.docx`。最终视觉核验请在目标查看器中打开文件。

### 诚实的边界

`validate` 抓的是 schema 错误，不是学术样式错误。一份文档可以在 IEEE 论文里用 APA 引用、在不允许脚注的样式里用脚注、带硬编码编号的图（插入新图后编号脱节），照样通过 `validate`。上面这些 gate——尤其是 Gate 4（往返闭环）和 Gate 5（SEQ 存在性）——才是抓出 validate 抓不到的问题的手段。

## 已知问题与陷阱（学术特有）

→ 基础陷阱（shell 转义、`\$ \t \n` 字面量、表格单元格格式化顺序、分页边界、`shd.fill` / `ind.firstLine` 这类 schema 非法形式、TOC 缓存值、水印两步法）：see docx v2 §Known Issues & Pitfalls。

学术特有：

- **`\left(...\right)` / `\left[...\right]` 且定界符内部带上下标 → 解析错误**（`cast object … Subscript`）。外层上标（`\left(x+y\right)^2`）没问题。用普通 `(`、`)`、`[`、`]`——OMML 在 display 模式下会自动调整大小。
- **对 `/body/oMathPara[N]` 执行 `move` 会重排公式**（包裹段落被移动）。`--before <path>` 可能留下游离空段落；优先 `--index` / `--after`。
- **节分隔符 +1 段落偏移。** 每次 `add /body --type section` 都向 `/body` 插入一个空段落。分隔符之后所有 `p[N]` 索引 +1。提前规划；任何 `add section` 之后，用 `officecli get "$FILE" /body --depth 1` 重新索引。
- **`/section[last()]` 解析为最后一节**（与 `p[last()]` 同理），get 和 set 均适用。显式 `/section[N]` 也可：
  ```bash
  SECTION_COUNT=$(officecli query "$FILE" section --json | jq '.data.results | length')
  # use /section[last()] for the final section, or an explicit /section[2], /section[3], ...
  ```
  每次 `add /body --type section` 都使计数加一。每个分隔符之后都重新查询。
- **多栏不会自动还原。** 在 `columns=2` 的节之后，必须再加一个节分隔符并在新的 `/section[N]` 上显式设置 `columns=1`（N = 还原后的计数）——否则文档其余部分（包括参考文献）渲染为双栏。用 `officecli get "$FILE" "/section[N]"` 逐一验证。
- **`--type equation` 放在 `tc[N]` 单元格路径上会被守卫错误拒绝**（`table cells only accept paragraphs, tables, or SDTs`）——不会写入坏 XML。单元格内改对 `tc[N]/p[1]` 用 `--prop mode=inline`。
- **SEQ 题注编号由 `set / --prop recalcFields=seq` 填入**（所有题注存在后执行一次），而不是逐域 raw-set 修补。recalc 之前 SEQ 域在 `view text` 中显示 `#OCLI_NOTEVAL!` 哨兵。
- **悬挂缩进的规范形式是 `indent=720 hangingIndent=720`。** 不是 `ind.firstLine=-720`。点分形式 emit 时把 `<w:ind>` 排在 `<w:jc>` 之后，会挂 schema。
- **脚注引用 run 在 `view annotated` 中显示为空字符串。** `<w:footnoteReference>` XML 元素在引用侧没有可见文本；注释正文在 `/footnotes/footnote[N]`。用 `officecli query "$FILE" 'footnote'` 确认，不要靠肉眼盯 `view text`。
- **题注位置：** 表题注在表上方；图题注在图下方。各主要样式（APA、Chicago、IEEE、MLA）一致。把表题注放表下方是学术样式错误，不是渲染问题——`validate` 抓不到它。
- **TOC 缓存渲染 / shell 转义：** → see docx v2 §Table of Contents, §Shell escape。

## 渲染器怪癖（跨查看器）

→ see docx v2 §Renderer quirks。PAGE / TOC 缓存值、OMML 基线偏移、scheme 颜色——所有同样的怪癖同样适用于学术论文。在断定某个公式或引用标记坏了之前，先在用户的目标查看器（Word、WPS、Pages）中打开文件——如果在那里渲染正确，那就是查看器怪癖，不是 Skill 缺陷。

## Help 指引

拿不准时：`officecli help docx`、`officecli help docx <element>`、`officecli help docx <element> --json`。Help 是权威 schema；本 Skill 是 docx v2 之上学术差异项的决策指南。
