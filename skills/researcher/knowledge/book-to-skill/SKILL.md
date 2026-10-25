---
name: book-to-skill
description: "将书籍和文档（PDF、EPUB、DOCX、HTML、Markdown、纯文本、RTF、MOBI/AZW（需 Calibre））转换为结构化 agent skill，提取框架、心智模型、原则、技巧与反模式。当用户想通过 GitHub Copilot CLI、Amp、Claude Code、Hermes Agent、OpenCode 或 OpenClaw 研读一份文档、在工作中应用某位作者的框架、或从一个文件构建可复用知识库时使用。"
---

> **中文汉化版** · 上游：[virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) · 原文件：`SKILL.md` · License: MIT
> 翻译日期：2026-10-24 · 同步状态：上游 HEAD（2026-10-24 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

<!--
跨 Agent 备注（仅供参考，宿主 Agent 会忽略）：
  - 兼容的 Skill 根目录：GitHub Copilot CLI（~/.copilot/skills、~/.agents/skills、
    .github/skills、.claude/skills、.agents/skills）、Amp（.agents/skills、
    ~/.config/agents/skills、~/.config/amp/skills）、Claude Code（~/.claude/skills）、
    Hermes Agent（$HERMES_HOME/skills、.hermes/skills、.agents/skills）、
    OpenClaw（${OPENCLAW_STATE_DIR:-~/.openclaw}/skills、.agents/skills、skills/；
    仅在使用默认 state 时才包含 ~/.agents/skills）。
    OpenCode（~/.config/opencode/skills、~/.claude/skills、.opencode/skills、
    ~/.agents/skills、.agents/skills）。
  - 特意省略 `allowed-tools` 以保持跨 Agent 中立：Copilot CLI 使用
    `shell`/MCP 服务器名称，Claude 使用 `Bash`/`Read`/`Write`/`Glob`/`Grep`，Amp
    额外有 `shell_command`。本 Skill 需要 shell（用于运行 extract.py）和文件
    读写能力——各宿主会在首次使用时提示授权。
  - 参数提示：<path-to-document-folder-or-glob>... [skill-name-slug]
-->

# Book-to-Skill 转换器

通过提取结构，把书面知识转化为可操作的 agent skill——而不是产出摘要。

## 理念

书籍中凝结着专业知识：需要多年积累才能形成的框架、原则与技巧。本 Skill 将这些知识提取为 GitHub Copilot CLI、Amp、Claude Code、Hermes Agent、OpenCode、OpenClaw 或其他兼容 Agent 可以反复利用的格式。
**提取结构，而非摘要。** Skill 不是读书报告。它是一套工具箱，包含：
- 具名的框架（有明确应用场景的心智模型）
- 可操作的原则（指导决策的规则）
- 技巧（分步骤的方法）
- 反模式（应避免什么以及为什么）
- 表达风格校准（作者如何思考与沟通）

**保留作者的精确表述。** 框架的命名往往有其特定原因。"The 5 Whys"（五问法）不能与"多次追问为什么"互换。要捕获其确切提法。

**合理分层深度。** 简单的书 → 简单的 Skill。含 10+ 个框架的复杂书 → 带参考文件和按需加载章节的 Skill。

---

## 运行模式

共有四条路径。根据用户的请求进行路由：

### 1. 完整转换（默认）
**触发：** 用户提供一个或多个文档/目录/glob 路径，且无特殊指示
**动作：** 执行以下全部步骤（步骤 0–9）
**输出：** 完整的 Skill，包含 SKILL.md、chapters/、glossary、patterns、cheatsheet

### 2. 仅分析
**触发：** 用户说 "analyze"（分析）、"just extract"（只做提取）或 "I want to review before generating"（生成前想先审阅）
**动作：** 执行步骤 0–3，然后产出一份结构化提取报告（找到的框架、原则、技巧）。停止——不要生成 Skill 文件。
**输出：** 供用户审阅的分析报告

### 3. 基于已有分析生成
**触发：** 用户已有分析笔记，或此前运行过仅分析模式
**动作：** 跳过步骤 0–3，以提供的分析作为输入，执行步骤 4–9
**输出：** 基于所提供分析生成的 Skill 文件

### 4. 更新 / 合入（已有 Skill）
**触发：** 用户提供一个或多个新源路径，并表示想更新某个已有 Skill（通过指向已有 Skill 目录、提供一个在 `SKILLS_HOME` 中已存在的 skill slug、或明确提出更新请求）。
**动作：** 执行步骤 0（超范围检查）、步骤 1（校验输入）、步骤 1.5（识别书籍类型）和步骤 2（提取新文件）。然后跳到步骤 5（识别/检测已有 Skill 路径），并执行**更新 / 合入工作流**将新内容合并进已有 Skill 文件。
**输出：** 更新后的已有 Skill，包含新增/修订的章节摘要和合并后的索引/术语表。

---

## Skill 存放位置

本转换器可以在多种 Skill 系统中运行。查找本转换器的辅助脚本或写入生成的书籍 Skill 时，按以下优先顺序选择位置：

1. GitHub Copilot CLI 个人 Skill：`~/.copilot/skills/`
2. 跨 Agent 个人 Skill（Copilot、Amp、Codex；使用默认 state 的 OpenClaw）：`~/.agents/skills/`
3. Claude Code 个人 Skill：`~/.claude/skills/`
4. 项目级 Copilot Skill：`.github/skills/`
5. 项目级 Claude Skill：`.claude/skills/`
6. 项目级 Amp / Copilot / OpenClaw Skill：`.agents/skills/`
7. Amp 全局 Skill：`~/.config/agents/skills/`
8. Amp 旧版全局 Skill：`~/.config/amp/skills/`
9. Hermes Agent 个人 Skill：`$HERMES_HOME/skills/`（默认 `~/.hermes/skills/`）
10. Hermes Agent 项目 Skill：`.hermes/skills/` 或 `.agents/skills/`
11. OpenClaw 个人 Skill：`${OPENCLAW_STATE_DIR:-~/.openclaw}/skills/`（活跃 state；`~/.agents/skills/` 仅在使用默认 state 时共享）
12. OpenClaw 项目 Skill：`.agents/skills/` 或 `skills/`
11. OpenCode 个人 Skill：`~/.config/opencode/skills/` 或 `~/.agents/skills/`
12. OpenCode 项目 Skill：`.opencode/skills/` 或 `.agents/skills/`

对于**生成的**书籍 Skill，优先使用用户级跨 Agent 根目录 `~/.agents/skills/`——一份物理副本即可同时服务跨 Agent 宿主以及使用默认 state 的 OpenClaw。Copilot CLI 与 Amp 可原生发现它；Claude Code 需要来自 `~/.claude/skills/<skill_name>` 的符号链接（在步骤 10 创建，规则见步骤 5）。仅当用户明确要求时才选择宿主私有或项目本地根目录。`BOOK_TO_SKILL_SCOPE=project` 或 `personal` 可为自动化显式指定该选择；不要仅仅因为两种范围都存在就发出强制的范围询问。

---

## 步骤 0 — 超范围检查

如果未提供任何参数，停止并回复：
> "book-to-skill 需要一个受支持的文档路径、目录或 glob 模式。用法：`book-to-skill <path-to-document-folder-or-glob>... [skill-name-slug]`"

在整个工作流中：
- **先确定目标根目录。** 在任何已有 Skill 查找之前，先确定本次运行会写入哪里：用户宿主的个人根目录或项目本地根目录，遵循步骤 5 的表格与选择规则——项目本地请求使用其项目本地根目录，绝不使用个人根目录。下文中，"已解析的根目录"即指该目标。
- 识别输入路径和可选的 skill slug。
- 如果最后一个参数不是存在或能匹配到文件的文件/目录/glob，且它看起来像一个 skill slug（如小写连字符、字母数字），则将其视为 `SKILL_NAME`。
- 将所有其他参数视为 `INPUT_PATHS` 列表。
- 如果任何输入路径是一个已有的 Skill 目录（包含 `SKILL.md` 和 `chapters/` 子目录），或 `SKILL_NAME` 与已解析根目录中已有的 skill slug 匹配，则将本次运行标记为**更新/合入**操作（模式 4）。
- **重跑保护。** 在开始完整转换的提取之前，按步骤 5 的命名规则推导候选 skill slug——作者-概念式、按书名式，以及给出的任何 `SKILL_NAME`——并在已解析根目录中检查是否已有匹配。若匹配，停止并询问用户："`<skill-name>` 已存在。请选择：(1) 更新/合入（模式 4），(2) 核实已有 Skill 是否完整然后停止，或 (3) 强制完整重新生成。"在用户选择之前不要重新提取。在中断运行后恢复上下文时（网络中断、对话重放或续接），仅在以下条件全部满足时才复用该次运行报告的提取工作目录（其输出中的 `Workdir ->`，或你在 `BOOK_SKILL_WORKDIR` 中设置的路径）：目录仍然完好且仍与当前输入和选项匹配——目录存在、其 `metadata.json` 可读、其中列出的 `sources` 与本次要转换的文件在文件名**和内容指纹**上一一对应（提取器会在 `metadata.json` 中记录每个源的 `sha256`；请按各文件当前状态重新计算指纹并要求完全一致——`book_to_skill/utils.py` 中的 `reuse_is_safe()` 即此检查的可执行形式），且其记录的 `extraction_mode` 与本次运行使用的模式一致（即步骤 2 的"确认提取的确实是你所要求的文档"规则）。如果目录缺失（临时清理）、其 `metadata.json` 丢失、源不再匹配（文件名不同或内容指纹变化）、记录的元数据中某源没有 `sha256`（指纹机制出现之前记录的，无法确认新鲜度），或模式不同，则如实说明并改为开始一次全新提取，而不是恢复。存疑时，先询问用户再决定丢弃或恢复。

---

## 步骤 1 — 校验输入

验证 `INPUT_PATHS` 中至少有一个受支持的文件、目录或 glob 模式。
对目录和 glob 进行展开，查找匹配的受支持文件（`.pdf`、`.epub`、`.docx`、`.txt`、`.md`、`.markdown`、`.rst`、`.adoc`、`.html`、`.htm`、`.rtf`、`.mobi`、`.azw`、`.azw3`）。

如果未找到受支持的文件，停止并给出明确的错误信息。

---

## 步骤 1.5 — 识别内容类型

提取之前，先询问用户：

> "这些源文档属于哪种内容类型？这有助于我选择最合适的提取方法。
>
> 1. **技术类** —— 含代码块、表格、公式、图表（如编程书籍、学术论文、架构指南）
> 2. **文本为主** —— 以散文为主，几乎没有表格/代码（如管理、效率、叙事性非虚构）
> 3. **不确定** —— 我将使用快速方法，并在质量似乎欠佳时提醒你"

将答案记录为 `BOOK_TYPE`：
- 选项 1 → `BOOK_TYPE=technical`
- 选项 2 → `BOOK_TYPE=text`
- 选项 3 → `BOOK_TYPE=text`

**若 `BOOK_TYPE=technical`**，在继续之前告知用户：
> "📐 已选择技术模式——使用 Docling 进行结构感知提取（表格、代码块、公式保留为 markdown）。每页约需 1.5 秒，较长的源文档预计需要几分钟。现在开始……"

**若 `BOOK_TYPE=text`**，告知：
> "📄 已选择文本模式——对每种文件类型使用最快的可用提取器。纯文本/Markdown/HTML 通常几秒内即可就绪；PDF 在可用时使用 pdftotext。"

---

## 步骤 2 — 从源文档提取文本

运行提取脚本，传入输入路径：

```bash
SCRIPT_PATH=""
HERMES_HOME_RESOLVED="${HERMES_HOME:-$HOME/.hermes}"
OPENCLAW_STATE_DIR_RESOLVED="${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
HERMES_PROJECT_TRUSTED=false
if [ -n "$PROJECT_ROOT" ] && [ "${HERMES_AGENT:-}" = true ] && \
  command -v hermes >/dev/null 2>&1 && \
  command -v python3 >/dev/null 2>&1 && \
  hermes config get skills.trusted_project_dirs --json 2>/dev/null | PROJECT_ROOT="$PROJECT_ROOT" python3 -c 'import json, os, pathlib, sys; root=pathlib.Path(os.environ["PROJECT_ROOT"]).resolve(); sys.exit(not any(pathlib.Path(p).expanduser().resolve() == root for p in json.load(sys.stdin)))' 2>/dev/null
then
  HERMES_PROJECT_TRUSTED=true
fi

CANDIDATES=(
  "$HOME/.copilot/skills/book-to-skill/scripts/extract.py"
  "$HOME/.agents/skills/book-to-skill/scripts/extract.py"
  "$HOME/.claude/skills/book-to-skill/scripts/extract.py"
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills/book-to-skill/scripts/extract.py"
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/book-to-skill/scripts/extract.py
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/*/book-to-skill/scripts/extract.py
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/*/*/book-to-skill/scripts/extract.py
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/*/*/*/book-to-skill/scripts/extract.py
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/*/*/*/*/book-to-skill/scripts/extract.py
  "${OPENCLAW_STATE_DIR_RESOLVED}/skills"/*/*/*/*/*/*/book-to-skill/scripts/extract.py
  "$HOME/.config/opencode/skills/book-to-skill/scripts/extract.py"
  "$HERMES_HOME_RESOLVED/skills/book-to-skill/scripts/extract.py"
  "$HERMES_HOME_RESOLVED"/skills/*/book-to-skill/scripts/extract.py
)
if [ "${HERMES_AGENT:-}" != true ]; then
  # Project-local roots are resolved against the git worktree, not the current
  # directory: an agent can be invoked from anywhere inside the project (e.g.
  # `src/nested`) and these roots still have to be found — that is how OpenCode
  # and the other hosts discover project skills. The CWD-relative forms are kept
  # so the probe also works outside a git repository.
  if [ -n "$PROJECT_ROOT" ]; then
    CANDIDATES+=(
      "$PROJECT_ROOT/.github/skills/book-to-skill/scripts/extract.py"
      "$PROJECT_ROOT/.claude/skills/book-to-skill/scripts/extract.py"
      "$PROJECT_ROOT/.agents/skills/book-to-skill/scripts/extract.py"
      "$PROJECT_ROOT/.opencode/skills/book-to-skill/scripts/extract.py"
    )
  fi
  CANDIDATES+=(
    ".github/skills/book-to-skill/scripts/extract.py"
    ".claude/skills/book-to-skill/scripts/extract.py"
    ".agents/skills/book-to-skill/scripts/extract.py"
    "skills/book-to-skill/scripts/extract.py"
    "skills"/*/book-to-skill/scripts/extract.py
    "skills"/*/*/book-to-skill/scripts/extract.py
    "skills"/*/*/*/book-to-skill/scripts/extract.py
    "skills"/*/*/*/*/book-to-skill/scripts/extract.py
    "skills"/*/*/*/*/*/book-to-skill/scripts/extract.py
    "skills"/*/*/*/*/*/*/book-to-skill/scripts/extract.py
    ".opencode/skills/book-to-skill/scripts/extract.py"
  )
  if [ -n "$PROJECT_ROOT" ]; then
    CANDIDATES+=(
      "$PROJECT_ROOT/skills/book-to-skill/scripts/extract.py"
      "$PROJECT_ROOT/skills"/*/book-to-skill/scripts/extract.py
      "$PROJECT_ROOT/skills"/*/*/book-to-skill/scripts/extract.py
      "$PROJECT_ROOT/skills"/*/*/*/book-to-skill/scripts/extract.py
      "$PROJECT_ROOT/skills"/*/*/*/*/book-to-skill/scripts/extract.py
      "$PROJECT_ROOT/skills"/*/*/*/*/*/book-to-skill/scripts/extract.py
      "$PROJECT_ROOT/skills"/*/*/*/*/*/*/book-to-skill/scripts/extract.py
    )
  fi
fi
CANDIDATES+=(
  "$HOME/.config/agents/skills/book-to-skill/scripts/extract.py"
  "$HOME/.config/amp/skills/book-to-skill/scripts/extract.py"
)
if [ "$HERMES_PROJECT_TRUSTED" = true ]; then
  CANDIDATES=(
    "$PROJECT_ROOT/.hermes/skills/book-to-skill/scripts/extract.py"
    "$PROJECT_ROOT/.hermes/skills"/*/book-to-skill/scripts/extract.py
    "$PROJECT_ROOT/.agents/skills/book-to-skill/scripts/extract.py"
    "$PROJECT_ROOT/.agents/skills"/*/book-to-skill/scripts/extract.py
    "${CANDIDATES[@]}"
  )
fi
for candidate in "${CANDIDATES[@]}"
do
  if [ -f "$candidate" ]; then
    SCRIPT_PATH="$candidate"
    break
  fi
done

if [ -z "$SCRIPT_PATH" ]; then
  echo "Could not find scripts/extract.py for book-to-skill" >&2
  exit 1
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

"$PYTHON_BIN" "$SCRIPT_PATH" $INPUT_PATHS --mode <BOOK_TYPE> --install-missing ask
```

提取之前，脚本会检查检测到的格式所需的可选 Python 包。如果缺少更好的提取器，它会向用户提示可用的回退方案。非交互会话默认使用回退方案，除非安装模式被显式设为 `yes`。

**提示——预检环境：** 运行 `"$PYTHON_BIN" "$SCRIPT_PATH" --check`，它会按格式打印一份报告，列出已安装的提取器以及安装缺失项的确切命令，且不处理任何文件。当用户报告安装或质量问题时有用。

这会创建一个**每次运行独立**的工作目录——默认为 `<tempdir>/book_skill_work-<pid>/`，或精确使用你在 `BOOK_SKILL_WORKDIR` 中设置的路径——其中包含：
- `full_text.txt` —— 所有源文档合并提取的文本，带有清晰可见的边界标记。
- `metadata.json` —— 总合并大小、词数、页数、token 数、丢弃的 EPUB 图片数、解析出的 `workdir`，以及逐个处理的 `sources` 详细列表。

运行完成时会打印全部三个路径（`Workdir ->`、`Text ->`、`Meta ->`）。**从该输出（或 `metadata.json` 自身的 `workdir` 字段）获取路径，不要假设固定位置**——目录名每次运行都不同，这样同一台机器上的并发提取才不会互相覆盖结果。

读取该次运行的 `metadata.json` 查看结果。

**在生成任何内容之前，务必确认提取的确实是你所要求的文档**：检查 `metadata.json` 中的 `filename` / `source_file`，或 `full_text.txt` 第一行的 `SOURCE:` 头。如果你在等待一个后台运行，等待*它那个*具体的工作目录——轮询共享路径可能读到的是另一次运行的输出。

---

## 步骤 2.5 — 预检成本估算

读取本次运行的 `metadata.json`（提取输出中的 `Meta ->` 路径），并在**进行任何生成之前**向用户呈现估算：

```
📖 Sources detected: <total_sources> source(s)
<list each source filename and format from the sources metadata list>
<if images_dropped > 5: warn that N source images were not read>
📄 Combined Pages/Sections: ~<N> | Words: ~<N> | Total tokens: ~<N>K

💰 Estimated token cost (Full Conversion / Update):
   Input  (reading + prompts): ~<N>K tokens
   Output (skill files generated/updated):  ~<N>K tokens
   Total:                           ~<N>K tokens

   Cost: multiply the token counts above by your model's current
   input/output per-1M-token rates (prices and model names change often —
   do not hardcode them; quote today's rate and label it as an estimate).

   ⏱  Estimated time: ~<N> minutes

📁 Files to be generated/updated:
   SKILL.md + chapter files + glossary + patterns + cheatsheet

➡  Proceed with Full Conversion / Update? (or type "analyze only" to preview first)
```

**如何估算：**
- 输入 token ≈ 元数据中的 `estimated_tokens` × 1.3（每章处理一遍的提示词开销）
- 输出 token ≈ 章节数 × 每章预算 + 4,000（SKILL.md）+ 4,500（glossary + patterns + cheatsheet）
  - 每章预算中点按 `BOOK_TYPE`（DEPTH 在步骤 4 中才决定，可能上调）：`text` ≈ 1,000，`technical` ≈ 1,800。如果用户已表明只要参考查阅还是要深入研读，则使用步骤 7 矩阵中对应的一行。
- 成本：报告 token 数量，并乘以用户当前每 100 万 token 的输入/输出单价。不要硬编码美元数字——模型名称和价格经常变动；如果给出金额，标注为估算并注明日期。

等待用户确认后再继续。如果用户说 "analyze only"（仅分析），切换到模式 2。

---

## 步骤 2.6 — 大部头书籍的 REPL 式访问（> 50k token）

受递归语言模型（Recursive Language Model, RLM）范式启发：把 `full_text.txt` 当作可查询的语料，而不是一次性读取。将整个文件载入上下文会烧掉你后面生成时需要的预算。

对超过约 50k token 的书籍，优先使用程序化探测，而不是不加限制的 `Read(full_text.txt)`：

```bash
# Size check before any Read
wc -w "$FULL_TEXT_PATH"

# Find chapter offsets without loading the whole file
grep -n -E "^\s*(Chapter|CHAPTER)\s+[0-9]+" "$FULL_TEXT_PATH" | head -40

# Pull only the chapter you need (lines start..end inclusive)
sed -n '<start>,<end>p' "$FULL_TEXT_PATH"

# Verify a framework is actually mentioned before claiming it in SKILL.md
grep -c -i "westrum\|dora" "$FULL_TEXT_PATH"

# Targeted Read with offset/limit avoids dumping the full file
# Read(file_path=full_text.txt, offset=<line>, limit=<lines>)
```

在步骤 3（结构分析）、步骤 7（逐章摘要）和步骤 8（术语表 / patterns 提取）中使用这种方法。对低于 50k token 的书籍，单次 `Read` 即可。

为什么重要：一本 200 页的书约 75k token。每章重读一遍（28 遍）要花费约 200 万输入 token；用 grep + sed 只拉取相关片段，可以让生成成本与输出成正比，而不是与源文档成正比。

---

## 步骤 3 — 分析书籍结构

读取提取出的 `full_text.txt` 的前 8,000 个字符以识别：
- 书籍**标题**与**作者**
- **章节结构**（寻找 "Chapter N"、"PART I"、编号标题、目录）
- **核心主题**与题材领域
- 大致章节数

然后阅读目录（Table of Contents）部分（如存在），映射所有章节。

**如果模式为 "Analyze Only"（仅分析）：** 现在产出提取报告并停止。结构如下：
```
## Extraction Report — <Title>

### Author's Core Frameworks
- **<Framework Name>**: <what it is and when to apply>

### Key Principles
- <Principle>: <actionable rule>

### Techniques & Methods
- <Technique>: <step-by-step or how-to>

### Anti-patterns
- <What to avoid>: <why>

### Suggested Skill Name
`{author-lastname}-{core-concept}` — e.g. `cialdini-influence`

### Chapters Detected
| # | Title | Main Frameworks |
```

---

## 步骤 4 — 询问用途（仅完整转换）

生成之前，询问用户：

> "这个 Skill 应该帮你做什么？（可选一项或多项）
> 1. 在工作中应用作者的框架
> 2. 用作者的心智模型思考
> 3. 查阅特定章节和概念
> 4. 以上全部"

用这个答案来决定 SKILL.md Core 部分侧重突出什么。

**从答案推导 `DEPTH`（无需额外询问）：**
- 答案**仅**为选项 3（查阅参考）→ `DEPTH=reference`——精炼、便于快速查阅的章节。
- 答案包含选项 1、2 或 4 → `DEPTH=study`——更深入的章节，含更多完整推演、示例与推理。

`DEPTH` 与 `BOOK_TYPE` 共同决定步骤 7 中的每章 token 预算。**不要**单独再问"研读还是参考"的问题——它在此处推断。（在跳过步骤 4 的模式 2/3 中，默认 `DEPTH=study`。）

---

## 步骤 5 — 确定 Skill 名称

如果提供了 `SKILL_NAME`，将其用作 skill slug。
否则，提出两个选项让用户选择：
- **按作者-概念**：`{author-lastname}-{core-concept}`（如 `cialdini-influence`、`meadows-systems`）
- **按书名**：书名转小写连字符（如 `designing-data-intensive-apps`）

如果该书有强方法论标识，默认使用作者-概念格式。

选择目标 Skill 根目录（`SKILLS_HOME`）。先从显式用户请求或 `BOOK_TO_SKILL_SCOPE` 解析**范围（scope）**，再探测**宿主**。请求项目本地/项目输出选择项目本地行；请求个人/全局输出选择个人行。若未请求任何范围，保持既定的个人默认（非 Hermes 宿主为 `~/.agents/skills`）。不要仅仅因为项目本地根目录存在就发出强制的范围询问。所选根目录在写入前可能仍需宿主批准。

| 宿主 Agent | 个人 Skill 根目录 | 项目本地根目录 |
|---|---|---|
| **GitHub Copilot CLI** | `~/.agents/skills`（原生发现） | `.github/skills` → `.claude/skills` → `.agents/skills` |
| **Amp** | `~/.agents/skills`（原生发现） | `.agents/skills` |
| **OpenAI Codex** | `~/.agents/skills`（原生发现；跟随符号链接） | `.agents/skills` |
| **Hermes Agent** | `$HERMES_HOME/skills/<category>`（默认 `~/.hermes/skills/<category>`） | `.hermes/skills/<category>` → `.agents/skills` |
| **Claude Code** | `~/.agents/skills` + 从 `~/.claude/skills/<skill_name>` 建立符号链接 | `.claude/skills` |
| **OpenClaw** | `${OPENCLAW_STATE_DIR:-~/.openclaw}/skills`（活跃 state；`~/.agents/skills` 仅默认 state） | `.agents/skills` → `skills/` |

Hermes Agent 是唯一保留自己个人根目录的宿主：它按类别划分个人 Skill，不扫描跨 Agent 根目录。使用活跃 profile 的 `HERMES_HOME`，并选择与生成 Skill 主题相符的类别。不要手工构造 profile 路径。如果用户选择项目本地的 Hermes 根目录，生成后运行 `hermes skills trust <project-root>`，并用 `hermes skills list` 验证发现；在项目受信任之前，项目 Skill 仍不可用。

对 OpenClaw，使用活跃 state 目录的 `skills/` 根：`${OPENCLAW_STATE_DIR:-~/.openclaw}/skills/`。共享的 `~/.agents/skills` 兼容根仅在 `OPENCLAW_STATE_DIR` 未设置或为默认 `~/.openclaw` 时可被发现；在非默认 state 下，不要声称 OpenClaw 能看到共享根中的安装。生成后用 `openclaw skills list` 验证发现。
| **OpenCode** | `~/.agents/skills`（原生发现；也会读取 `~/.config/opencode/skills` 和 `~/.claude/skills`） | `.opencode/skills` → `.agents/skills` → `.claude/skills` |

Hermes Agent 是唯一保留自己个人根目录的宿主：它按类别划分个人 Skill，不扫描跨 Agent 根目录。使用活跃 profile 的 `HERMES_HOME`，并选择与生成 Skill 主题相符的类别。不要手工构造 profile 路径。如果用户选择项目本地的 Hermes 根目录，生成后运行 `hermes skills trust <project-root>`，并用 `hermes skills list` 验证发现；在项目受信任之前，项目 Skill 仍不可用。

OpenCode 原生扫描跨 Agent 的 `~/.agents/skills` 根目录，因此上述生成 Skill 的默认位置已经覆盖它——无需符号链接，也无需信任步骤。它还会读取自己托管的 `~/.config/opencode/skills` 根和 Claude 兼容根 `~/.claude/skills`；仅当用户要求时才使用 OpenCode 托管的根。项目 Skill 通过从工作目录向上遍历到 git worktree 来发现，因此生成后如果 Skill 未出现，请新开会话。（`~/.cache/opencode/skills` 是 `skills.urls` 的远程 Skill 下载缓存，不是创作根目录——绝不要把生成的 Skill 写到那里。）

选择规则：
1. 个人安装：将 `SKILLS_HOME` 设为 `~/.agents/skills`（如缺失则创建该目录）。有一个例外，以免在别人的地盘上发明约定：如果 `~/.agents/skills` 不存在**且**宿主私有根目录中已有 Skill，则改用私有根目录，并在报告中说明原因。
2. **Claude Code 不扫描 `~/.agents/skills`** —— 生成完成后，步骤 10 会用 `ln -sfn "$HOME/.agents/skills/<skill_name>" "$HOME/.claude/skills/<skill_name>"` 将 Skill 链接进去。
3. **Hermes Agent 个人安装使用上表中的 Hermes 行**，而非跨 Agent 根目录，且不需要符号链接。
4. 如果用户明确要求宿主私有根目录（`~/.copilot/skills`、`~/.claude/skills`、`~/.config/agents/skills`、`~/.config/amp/skills`），照办并跳过符号链接。
5. 如果用户明确要求项目本地输出，使用其宿主对应的项目本地行。
6. 如果选择需要知道宿主（项目本地输出、Hermes 个人根目录、OpenClaw state 根目录或 Claude Code 符号链接）而你无法识别，询问："你现在运行在哪个 Agent 中——OpenCode、OpenClaw、Hermes Agent、GitHub Copilot CLI、Amp、Codex 还是 Claude Code？"
7. 对 OpenClaw 个人输出，使用 `${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/skills`。共享的 `~/.agents/skills` 根仅在 `OPENCLAW_STATE_DIR` 未设置或等于默认 `$HOME/.openclaw` 时才是有效的 OpenClaw 目标；否则使用活跃 state 根或项目/额外目录。
8. 如果用户明确要求 OpenClaw 托管的个人根目录，使用活跃 state 根并用 `openclaw skills list` 验证发现。

将 `SKILLS_HOME` 设为所选根目录，并检查 `$SKILLS_HOME/<skill_name>/` 是否已存在。在 Claude Code 上，还要检查 `~/.claude/skills/<skill_name>` 是否作为一个**真实目录**（而非符号链接）存在——可能有先前的安装在那里；如有，先提议迁移（把目录移入 `~/.agents/skills/` 并用符号链接替换原路径）再继续。
如果该 Skill 已存在，提示用户选择：
1. **更新 / 合入**（模式 4）——将新文件/内容整合进已有 Skill 组件。
2. **覆盖** —— 删除并从头重新生成该 Skill。
3. **重命名** —— 追加 `-2` 或改用其他自定义 slug。

如果用户选择**更新 / 合入**，在步骤 2.5 之后立即进入**更新 / 合入工作流**一节（跳过步骤 3、4、6、7、8、9）。

---

## 步骤 6 — 创建 Skill 目录结构

```bash
mkdir -p "$SKILLS_HOME/<skill_name>/chapters"
```

---

## 步骤 7 — 生成章节摘要

**TOKEN 预算规则——关键（自适应）：**

每章预算随 `BOOK_TYPE` 和 `DEPTH` 缩放。技术类章节需要容纳代码和表格的空间；研读深度需要容纳完整推演的空间。从此矩阵中选取预算：

| | `DEPTH=reference` | `DEPTH=study` |
|---|---|---|
| `BOOK_TYPE=text` | 800–1,200 tokens | 1,000–1,800 tokens |
| `BOOK_TYPE=technical` | 1,200–1,800 tokens | 2,000–3,000 tokens |

- 这些是每文件目标，不是硬性上限——内容密集的章节可能略超，单薄的章节可能不足。密度仍然胜过篇幅（质量规则 #3）：绝不为凑数字而注水。
- 文件按需加载，所以更大的章节只有在该章被实际读取时才花费 token。
- 在两个格子之间犹豫时（如混合内容书籍），用较低预算，让深度来自精确而非体量。

**`DEPTH=study` 是靠内容挣来的，不是靠更大的数字。** 标准章节模板（Core Idea → Connects To）自然会让一个内容密集的散文式章节落在 700–900 token 左右。要*诚实地*达到研读预算——而非注水——研读深度的章节必须增加具体材料：
- **复现章节中的一个完整示例（worked example）或产物**（如示例新闻稿、一段示例对话、一份填好的模板、作者从头到尾走完的一个决策），放在 `## Worked Example` 一节。这是最大的杠杆，也是学习者会回头来找的主要内容。
- **把每个框架的 "How"** 展开为明确的步骤或判据，而不是一句话。
- **给最重要的 1–2 个框架加一条简短的 "Why it works / failure mode"（为何有效/失效模式）注记**。

如果某章确实没有完整示例且难以扩展，就让它落在研读下限之下，而不是注水——并在其 Core Idea 中注明该章内容单薄。相比之下，`reference` 深度的章节则有意省略完整示例，只保留可直接用于决策的要点。

对步骤 3 中识别出的每一个章节/主要部分：

读取提取出的 `full_text.txt` 中对应的部分（用字符偏移或 grep 查找章节标题）。

使用以下结构创建 `$SKILLS_HOME/<skill_name>/chapters/ch<NN>-<slug>.md`。

**根据 `BOOK_TYPE` 调整侧重：**
- `technical` → 优先 "Code Examples"、"Reference Tables" 和 "Commands & APIs" 小节；保留精确语法
- `text` → 优先 "Frameworks Introduced"、"Mental Models" 和 "Key Takeaways"；跳过空的技术小节

```markdown
# Chapter N: <Full Title>

## Core Idea
<1–2 sentences: the single most important thing this chapter teaches>

## Frameworks Introduced
- **<Framework Name>**: <exact formulation — preserve the author's naming>
  - When to use: <specific situation>
  - How: <steps or criteria>

## Key Concepts
- **<Term>**: <precise definition in 1 sentence>
(5–10 most important terms from this chapter)

## Mental Models
<2–4 frameworks or thinking tools. Write as "Use X when Y" or "Think of X as Y">

## Anti-patterns
- **<What to avoid>**: <why it fails>

## Code Examples *(technical books only — omit if BOOK_TYPE=text)*
<!-- Copy the most instructive snippet from the chapter. Preserve indentation exactly. -->
```<language>
<key code example from this chapter>
```
- **What it demonstrates**: <one line>

## Reference Tables *(technical books only — omit if BOOK_TYPE=text)*
<!-- Reproduce any comparison matrix, parameter table, or decision table from the chapter in markdown. -->

## Worked Example *(DEPTH=study only — omit for DEPTH=reference)*
<!-- Reproduce or reconstruct one concrete example the author works through: a
     sample document, a dialogue, a filled-in template, a before/after, or a
     decision walked end-to-end. This is what makes a study chapter worth its
     budget. Keep it faithful to the source; never copy long raw passages —
     reconstruct the example compactly. -->

## Key Takeaways
1. <Actionable insight>
2. <Actionable insight>
3. <Actionable insight>
(3–7 takeaways a practitioner must remember)

## Connects To
- **Ch N**: <why this chapter relates>
- **<Concept>**: <external concept or standard it connects with>
```

---

## 步骤 8 — 生成支撑文件

### glossary.md
创建 `$SKILLS_HOME/<skill_name>/glossary.md`：
- 书中每个重要术语，按字母排序
- 格式：`**Term** — definition (Ch N)`
- 最多 1,500 token

### patterns.md
创建 `$SKILLS_HOME/<skill_name>/patterns.md`：
- 书中所有具体技巧、设计模式、算法
- 格式：`## Pattern Name\n**When to use**: ...\n**How**: ...\n**Trade-offs**: ...`
- 最多 2,000 token

### cheatsheet.md
创建 `$SKILLS_HOME/<skill_name>/cheatsheet.md`：

**这是该 Skill 区分度最高的一层——把它当作推理辅助，而不是关键词清单。** 任何人都能在术语表里 grep 到一个词条。cheatsheet 捕捉的是作者的*判断力*：他们会做什么决定、为什么。正是这个文件把"我认识这些词"变成"我会像作者那样行动"。

按以下优先级排列：
1. **决策规则** —— "当 X 时，做 Y，因为 Z。"作者应用的 if/then 逻辑，表述到读者无需重读全书就能应用的程度。
2. **决策树 / 流程图**（以嵌套列表或小表格呈现）—— 用于分支多于两个的选择。
3. **权衡矩阵** —— 在作者关心的维度上为互相竞争的选项打分，让读者能按自己的约束做选择。
4. **阈值与默认值** —— 作者明确采用的数字、比率或经验法则（如 "keep functions under ~20 lines"（函数保持在约 20 行以内）、"alert when error budget < 10%"（错误预算低于 10% 时告警））。
5. **征兆与坏味道（tells & smells）** —— 快速识别处境的经验法则（"如果看到 X，你很可能陷入了 Y 麻烦"）。

避免：纯术语→定义的行（那是术语表的活），以及散文段落（那是章节的活）。每一行都应该帮助读者*决定*某件事。

- 主要以紧凑表格和决策规则呈现；内容以"打印出来放在手边、工作时参考的一页纸"为标准。
- 最多 1,200 token。

---

## 步骤 9 — 生成主 SKILL.md

**关键 TOKEN 预算：SKILL.md 正文保持在 4,000 token 以内。**
上下文压缩从末尾截断——把最重要的内容放在最前面。

创建 `$SKILLS_HOME/<skill_name>/SKILL.md`：

```markdown
---
name: <skill_name>
description: "Knowledge base from \"<Full Title>\" by <Author(s)>. Use when applying <author>'s frameworks for <key topics, 3–6 terms>, studying the book, or referencing its concepts."
---

<!-- argument-hint: [topic, framework name, or chapter number] -->

# <Full Title>
**Author**: <Author(s)> | **Pages**: ~<N> | **Chapters**: <N> | **Generated**: <YYYY-MM-DD>

## How to Use This Skill

- **Without arguments** — load core frameworks for reference
- **With a topic** — ask about `replication`, `pricing`, or another indexed topic; I find and read the relevant chapter
- **With chapter** — ask for `ch05`; I load that specific chapter
- **Browse** — ask "what chapters do you have?" to see the full index

When you ask about a topic not covered in Core Frameworks below, I will read
the relevant chapter file before answering.

---

## Core Frameworks & Mental Models
<!-- ~2,000 tokens: the author's most important named frameworks and principles.
     Preserve exact names. Write as "Use X when Y", "Prefer X over Y because Z".
     This is a toolkit, not a summary. -->

<generate 2,000 tokens of the most critical frameworks and insights here>

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-<slug>.md) | <Title> | <framework1>, <framework2> |
| [ch02](chapters/ch02-<slug>.md) | <Title> | <framework1>, <framework2> |
...

## Topic Index

<!-- Alphabetical. Major terms/frameworks → chapter(s) that cover them. -->
- **<Term>** → ch<N>[, ch<N>]
- **<Term>** → ch<N>

## Supporting Files

- [glossary.md](glossary.md) — all key terms with definitions
- [patterns.md](patterns.md) — all techniques and design patterns
- [cheatsheet.md](cheatsheet.md) — quick reference tables and decision guides

---

## Scope & Limits

This skill covers the book content only. For hands-on implementation in your codebase,
combine with project-specific tools. For topics beyond this book, check related skills
or ask the agent directly.
<if images_dropped > 5: state that N source images were not read>
```

---

## 步骤 9.5 — 扫描生成的 Skill

在报告成功、在另一个会话中加载该 Skill 或发布它之前，运行建议性的安全扫描：

```bash
SKILL_CONVERTER_ROOT="$(cd "$(dirname "$SCRIPT_PATH")/.." && pwd)"
"$PYTHON_BIN" "$SKILL_CONVERTER_ROOT/tools/scan_generated_skill.py" "$SKILLS_HOME/<skill_name>"
```

如果扫描器以非零码退出，停止并请人工审查其文件/行级发现。不要静默重写生成的文件；在发现被解决或被明确接受之前，不要加载或发布该 Skill。

---

## 步骤 10 — 清理与报告

如果宿主是 Claude Code 且 `SKILLS_HOME` 为 `~/.agents/skills`（默认个人安装），用符号链接把该 Skill 暴露给 Claude Code——Claude Code 只扫描 `~/.claude/skills`：

```bash
mkdir -p "$HOME/.claude/skills"
LINK="$HOME/.claude/skills/<skill_name>"
TARGET="$HOME/.agents/skills/<skill_name>"
if [ -d "$LINK" ] && [ ! -L "$LINK" ]; then
  CLAUDE_STATUS="skipped-realdir"                 # Step 5 migration declined; leave the old dir
else
  ln -sfn "$TARGET" "$LINK" 2>/dev/null || true
  # Read the link back — do NOT trust that `ln` did what was asked. On Windows/MSYS
  # `ln -s` may COPY instead of link (or need Developer Mode / an elevated shell), and
  # PowerShell/cmd have no `ln` at all. The report must reflect what is on disk, not the
  # fact that the command ran.
  if [ -L "$LINK" ] && [ "$(readlink "$LINK")" = "$TARGET" ]; then
    CLAUDE_STATUS="linked"
  elif [ -e "$LINK" ]; then
    CLAUDE_STATUS="copy"                           # a real file/dir landed instead of a link
  else
    CLAUDE_STATUS="absent"                         # ln unavailable or refused
  fi
fi
```

真实目录保护是必需的：对已存在的真实目录执行 `ln -sfn` 会把链接嵌到它*里面*（`~/.claude/skills/<skill_name>/<skill_name>`），导致 Claude Code 加载旧副本。如果用户拒绝了步骤 5 的迁移，跳过符号链接并在报告中说明——在迁移完成之前 Claude Code 会继续使用旧目录。

**报告任何与链接相关的内容之前，先回读链接。** 符号链接只是一个声明，不是事实："Discoverable by" 一行要根据 `CLAUDE_STATUS`（磁盘上实际的状态）填写，绝不要根据"命令已执行"来填。**当链接缺失或是普通副本时不要硬性失败**——Skill 存在于枢纽目录中，其他所有宿主仍能找到它；诚实的报告是"已写入 `~/.agents/skills/<skill_name>`；在链接创建之前 Claude Code 看不到它"，而不是中止。（Windows 线索，未验证：目录联接（junction）——提升权限的 `cmd` 中用 `mklink /J`，或 PowerShell 中用 `New-Item -ItemType Junction`——既不需要开发者模式也不需要符号链接特权；如果你尝试它，也不改变"先回读再报告"的规则。）

当用户选择了宿主私有或项目本地根目录时（步骤 5 规则 3-4），跳过此步。

然后清理提取工作目录：

```bash
PYTHON_BIN="${PYTHON_BIN:-python3}"
if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  PYTHON_BIN="python"
fi

删除**本次运行实际使用的工作目录**——即提取输出中的 `Workdir ->` 路径，
它也被存为 `metadata.json` 中的 `workdir`。绝不要删除不是你创建的目录：
可能另有一次提取正在你的旁边运行。

```bash
# WORKDIR is the path this run reported; quote it in case of spaces.
rm -rf "$WORKDIR"
```

等价地，如果你还保留着元数据文件：

```bash
"$PYTHON_BIN" - "$WORKDIR_METADATA_JSON" <<'PY'
import json
import shutil
import sys
from pathlib import Path

meta_path = Path(sys.argv[1])
workdir = json.loads(meta_path.read_text(encoding="utf-8")).get("workdir")
if workdir:
    shutil.rmtree(workdir, ignore_errors=True)
PY
```

本文件更早的版本会删除单个固定的 `book_skill_work` 目录。该路径已不再使用，
因此那样的清理现在只是无害的空操作，而不是可能误删并发运行输出的操作。

然后向用户报告：

```
✅ Skill created: $SKILLS_HOME/<skill_name>/

📚 Book: <Full Title> — <Author>
📄 Pages: ~<N> | Chapters: <N>

Files generated:
  SKILL.md         — core frameworks + index   (~X tokens)
  chapters/        — <N> chapter summaries     (~X tokens each, ~X total)
  glossary.md      — key terms                 (~X tokens)
  patterns.md      — techniques & patterns     (~X tokens)
  cheatsheet.md    — quick reference           (~X tokens)
  ─────────────────────────────────────────────────────
  Total skill size: ~X tokens (loaded on-demand, not all at once)

💡 Tip: check your agent's session cost/usage command to see actual token usage.

Usage:
  Ask for <skill_name>                  → load core frameworks
  Ask <skill_name> about <topic>        → find and explain a topic
  Ask <skill_name> for ch<N>            → dive into a specific chapter

Discoverable by: <only what is true for the chosen destination — see below>

Somewhere else?  mv ~/.agents/skills/<skill_name> <dest_root>/<skill_name> \
                   && ln -sfn <dest_root>/<skill_name> ~/.claude/skills/<skill_name>

Prompted for permission on every file? That is your host gating writes outside the
working directory. Say "save it in this project" and re-run to write inside it.

Reload (if your agent doesn't auto-detect new skills):
  GitHub Copilot CLI:  /skills reload
  Claude Code:         restart the session
  Amp:                 restart the session
  Hermes Agent:         start a new session
  OpenClaw:             openclaw skills list (new session if watcher disabled)
  OpenCode:             start a new session

Share this skill (optional):
  GitHub repo, installable on any host (Step 11):  say "publish"
  Copilot ecosystem:  gh skill publish $SKILLS_HOME/<skill_name>
```

"Discoverable by" 一行要根据 `CLAUDE_STATUS`（回读结果）填写，绝不要根据 `ln` 已执行这一事实来填——对 `~/.agents/skills` 安装：
- `linked` → "Copilot CLI、Amp、Codex（原生）；Claude Code 经符号链接 ~/.claude/skills/<skill_name>"
- `skipped-realdir` → "Copilot CLI、Amp、Codex（原生）；**不**含 Claude Code——先迁移 ~/.claude/skills/<skill_name> 处的真实目录"
- `copy` 或 `absent` → "Copilot CLI、Amp、Codex（原生）；**不**含 Claude Code——宿主无法创建符号链接（普通副本会在下次更新/合入时产生漂移）。启用开发者模式/手动创建链接，或直接从 ~/.agents/skills 运行该 Skill"
- Hermes Agent 个人根目录 → "Hermes Agent（来自 `$HERMES_HOME/skills/<category>`）"；不声称有符号链接，也不声称跨 Agent，因为其他宿主不扫描 Hermes 根目录
- 其他宿主私有或项目本地根目录 → 只列出会扫描该根目录的宿主；不声称有符号链接

"Somewhere else?"（挪到别处）这一行必须与实际采用的路径相符，以免破坏刚刚创建的符号链接。**`mv` 的目标始终是最终的 Skill 目录 `<dest_root>/<skill_name>`，绝不是 `<dest_root>` 本身。** `mv ~/.agents/skills/mybook ~/.copilot/skills && ln -sfn ~/.copilot/skills ~/.claude/skills/mybook` 看起来有效实则不然：Skill 落在 `~/.copilot/skills/mybook`，而链接指向上一层根目录，于是 Claude Code 解析到一个没有 `SKILL.md` 的目录——这正是这一行要防止的故障。代入用户实际指定的目标，让打印出的命令携带真实路径、不需要任何再解释：
- `~/.agents/skills` + 符号链接 → `mv ~/.agents/skills/<skill_name> <dest_root>/<skill_name> && ln -sfn <dest_root>/<skill_name> ~/.claude/skills/<skill_name>`
- 宿主私有根目录（含 Hermes Agent）→ `mv <src_root>/<skill_name> <dest_root>/<skill_name>`
- 项目本地根目录 → `mv <project_root>/<skill_name> <dest_root>/<skill_name>`

"Prompted for permission on every file?"（每个文件都被要求授权？）这一行是给那些把工作目录之外的写入设了门槛的宿主的答案（任何个人范围的根目录都在 cwd 之外）：目标位置已在上方说明，旁边附上了一行式修复——重新运行并要求使用项目本地根目录。仅个人范围安装保留此行；用户已选择项目本地时删去。

---

## 步骤 11 — 将生成的 Skill 发布到 GitHub（可选）

在步骤 10 的报告之后，提议一次——且仅在步骤 9.5 扫描通过时：

> "要我把这个 Skill 发布到 GitHub，让任何 Agent Skills 宿主都能用 `npx skills add` 安装吗？（yes / skip）"

如果用户拒绝，到此为止。前提：已认证的 `gh` CLI（检查 `gh auth status`）。如果 `gh` 缺失或未认证，提议帮其配置（`brew install gh` 或 https://cli.github.com，然后 `gh auth login`）——或走无 `gh` 路径：用户在 GitHub 网页 UI 中创建一个指定可见性的空仓库，然后你运行下面的 `git init`/`add`/`commit` 命令，再执行 `git remote add origin <repo-url> && git push -u origin main`。下面的可见性规则对网页创建的仓库同样完全适用。

**可见性是一个单独的封闭式问题——绝不推断，绝不从先前的回答中读取。** 用户接受后，单独提出这个问题，并要求一个单词的回复：

> "私有还是公开仓库？用一个词回复：`private` 或 `public`。"

**回复必须*就是* `public` 这个词，而不仅是包含它——这是硬性规则，不是建议。** 除一种情况外，`gh repo create` 一律使用 `--private`：对可见性问题的回答是光秃秃的单词 `public`。禁止子串匹配，因为一句关于**源材料许可**的话不是可见性回答——"it's public domain"、"the book is public domain"、"it's publicly available" 描述的都是材料而不是仓库，全部解析为 `--private`。转述、完整句子、含糊回答、沉默或你自己的推断都不构成同意：再问一次，如果回复仍不是那个光秃秃的单词，就用 `--private` 并在报告中说明。私有仓库日后可以转为公开；书籍衍生内容的公开推送无法撤回发布。

**版权闸门——创建仓库前必须始终执行：** 章节文件是综合而成的摘要而非原文，但仍衍生自源材料。根据 README 的版权与合理使用政策，从**第三方受版权保护的书籍生成的 Skill 必须保持私有**；只有当源是用户自己的作品、开放许可的内容、或用户明确确认有权公开再分发的材料时，才提供公开选项——并说明适用的是哪种情况。能访问公司内部材料不等于有权披露：来自内部文档的 Skill 保持**私有**，除非用户声明其拥有发布权。

如果用户接受：

1. 在 `$SKILLS_HOME/<skill_name>/` 内添加一个仓库 `README.md`（绝不覆盖已有文件）——包含 Skill 标题、一段描述（"Agent skill generated from *<Title>* by <Author> with [book-to-skill](https://github.com/virgiliojr94/book-to-skill)"）、下面第 3 步的安装命令、文件清单，以及"内容为综合摘要而非书籍原文"的说明。
2. 将 Skill 文件夹初始化为 git 仓库并创建远程（默认仓库名 `<skill_name>`；允许用户改——有人偏好 `<skill_name>-skill` 后缀）。**嵌套仓库保护：** 先检查该 Skill 文件夹是否已位于某个 git 仓库内（`git -C "$SKILLS_HOME/<skill_name>" rev-parse --show-toplevel`——对 `.claude/skills/` 这类项目本地根目录总是如此）。如果是，绝不要原地 `git init`：外层仓库会把该文件夹记录为嵌入式仓库（gitlink，mode 160000）而没有 `.gitmodules`，外层项目的新克隆会静默丢失该 Skill。改为把 Skill 文件夹复制到一个临时目录，在副本中运行下面的命令，并告诉用户已发布的仓库——而不是项目本地文件夹——才是远程的工作副本。

```bash
cd "$SKILLS_HOME/<skill_name>"
git init -b main
git add -A
git commit -m "Add <skill_name> skill"
gh repo create <repo_name> --private --source . --push
# --private is the default; substitute --public ONLY under the visibility rule above
# (the visibility answer WAS the bare word "public" AND the copyright gate allows it)
```

3. 报告仓库 URL 和跨宿主安装命令：

```
✅ Published: https://github.com/<owner>/<repo_name> (<private|public>)

Install on any Agent Skills host:
  npx skills add https://github.com/<owner>/<repo_name> --skill <skill_name>
```

   当嵌套仓库保护触发、仓库从临时副本发布时，追加一行——那个本地文件夹永远不会有远程，因此更新/合入的推送提议对它永远不会出现：

```
⚠️  Published from a copy: <skill folder> sits inside another git repository, so it has
    no remote of its own. To publish a later update, re-run Step 11, or clone
    https://github.com/<owner>/<repo_name> and fold new material into the clone.
```

根目录级的 `SKILL.md` 布局正是 `skills` CLI 所检测的，因此该仓库可直接安装——无需调整结构。在非嵌套仓库情形下，本地文件夹仍是本机的实际安装位置，也是远程的工作副本，因此后续的更新/合入运行可以提交并将其变更推送到同一远程。

---

## 更新 / 合入工作流

对位于 `$SKILLS_HOME/<skill_name>/` 的已有 Skill 执行更新/合入操作时：

### 1. 读取已有 Skill 结构
读取并解析已有 Skill 的文件：
- 读取 `$SKILLS_HOME/<skill_name>/SKILL.md`，解析已有的**章节索引（Chapter Index）**、**主题索引（Topic Index）**、元数据（作者、总章数）和**核心框架（Core Frameworks）**。
- 列出 `$SKILLS_HOME/<skill_name>/chapters/` 中的所有文件，找到最高的章节编号（如 `ch12`）。
- 读取 `$SKILLS_HOME/<skill_name>/glossary.md`、`$SKILLS_HOME/<skill_name>/patterns.md` 和 `$SKILLS_HOME/<skill_name>/cheatsheet.md`，了解已收录了哪些术语和框架。

### 2. 匹配内容并区分修订与新增
分析本次运行的 `full_text.txt`（提取输出中的 `Text ->` 路径）中的新提取文本，判断新内容属于：
- **对已有章节的更新/修订**：如果新内容的某部分直接更新或扩展了已有章节的主题，读取该章节文件，将新细节合并进去并重写该文件。
- **新增内容**：如果内容引入了新的章节、论文或独立部分，在 `chapters/` 下创建**新的章节摘要文件**。编号从已有的最高章节号之后开始（如已有章节止于 `ch12`，则创建 `ch13-*.md`、`ch14-*.md` 等）。

### 3. 生成或更新章节摘要文件
对每个新增或修订的章节：
- 读取提取的新文本中对应的部分。
- 遵循**步骤 7** 的格式规范构建摘要。
- 在 `$SKILLS_HOME/<skill_name>/chapters/` 中写入/更新该文件。

### 4. 合并支撑文件
- **合并 glossary.md**：
  - 读取已有的 `$SKILLS_HOME/<skill_name>/glossary.md`。
  - 从新内容中提取所有新术语和定义（按步骤 8 的术语表规范）。
  - 合并已有术语与新术语，并按字母排序。
  - 如果某术语已存在，把新的章节/源引用追加到其后（如 `**Term** — definition (Ch 4, Ch 13)`）。
  - 用完全合并、按字母排序的列表重写 `$SKILLS_HOME/<skill_name>/glossary.md`。
- **合并 patterns.md**：
  - 读取已有的 `$SKILLS_HOME/<skill_name>/patterns.md`。
  - 从新内容中提取所有新技巧、算法或模式。
  - 追加新模式，保持格式一致，总长度保持精炼（2,500 token 以内）。
- **合并 cheatsheet.md**：
  - 读取已有的 `$SKILLS_HOME/<skill_name>/cheatsheet.md`。
  - 提取新的比较规则、决策表或参数指南。
  - 将其整洁地融入 cheatsheet 结构。

### 5. 重新生成主 SKILL.md
更新主 Skill 文件 `$SKILLS_HOME/<skill_name>/SKILL.md`：
- **元数据**：递增章节数，更新估计页数，酌情添加新的源名称。将 `Generated` 日期更新为当前日期。
- **核心框架（Core Frameworks）**：并入新内容中影响力最大的心智模型或原则（确保整个文件保持在 4,000 token 以内）。
- **章节索引（Chapter Index）**：把新章节追加到索引表，链接到新创建的文件。
- **主题索引（Topic Index）**：按字母顺序合并新主题。如果已有主题在新章节中也有涉及，把新章节链接追加到其行（如 `- **Topic** → ch05, ch13`）。

### 6. 扫描、清理与报告
文件成功写入并合并后，运行**步骤 9.5**，然后执行**步骤 10** 进行清理，并打印一份自定义更新报告，总结新增章节、合并的术语表词条和更新的索引。如果该 Skill 文件夹是一个带远程的 git 仓库（经**步骤 11** 发布），提议提交并推送该更新。

---

## 质量规则

1. **提取结构，而非摘要** —— 捕获具名框架、确切提法、反模式；而不是章节复述
2. **保留作者的精确表述** —— "The 5 Whys"（五问法）≠ "ask why multiple times"（多问几次为什么）；保持确切命名
3. **密度胜过完整** —— 1,000 token 的摘要胜过 10,000 token 的节选
4. **实践者口吻** —— 写 "Use X when Y"（何时 X 就用 Y），而不是 "The book explains X"（书中解释了 X）
5. **SKILL.md 前置重点** —— 压缩保留前 5,000 token；最重要的内容放在最前
6. **章节文件按需加载** —— 在被加载之前不计入 Skill 预算
7. **绝不复制书籍原文** —— 始终综合、摘要、提取信号
8. **主题索引至关重要** —— 它是 Agent 导航到正确章节文件的方式
