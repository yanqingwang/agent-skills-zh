---
name: arxiv
description: 搜索、下载并总结 arXiv 学术论文。当用户说 "search arxiv"（搜索 arxiv）、"download paper"（下载论文）、"fetch arxiv"（获取 arxiv）、"arxiv search"（arxiv 搜索）、"get paper pdf"（获取论文 PDF），或想从 arXiv 查找并把论文保存到本地论文库时使用。
argument-hint: "[query-or-arxiv-id]"
allowed-tools: Bash(*), Read, Write
---

> **中文汉化版** · 上游：[wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) · 原文件：`skills/arxiv/SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# arXiv 论文搜索与下载

搜索主题或 arXiv 论文 ID：$ARGUMENTS

## 常量

- **PAPER_DIR** - 保存下载 PDF 的本地目录。默认：当前项目目录下的 `papers/`。
- **MAX_RESULTS = 10** - 默认的搜索结果数量。
- **ARXIV_FETCHER** — 规范名 `arxiv_fetch.py`，按
  [`shared-references/integration-contract.md`](../shared-references/integration-contract.md) §2
  解析（Policy D1 — 主路径 + 回退级联）。若无法解析（规范
  链已穷尽），回退到 Step 2 中记录的内联 Python 替代方案。

> 覆盖参数（附加到参数后）：
> - `/arxiv "attention mechanism" - max: 20` - 最多返回 20 条结果
> - `/arxiv "2301.07041" - download` - 按 ID 下载指定论文
> - `/arxiv "query" - dir: literature/` - 将 PDF 保存到自定义目录
> - `/arxiv "query" - download: all` - 下载全部结果的 PDF

## 工作流

### Step 1：解析参数

解析 `$ARGUMENTS` 中的指令：

- **Query or ID（查询或 ID）**：主搜索词，或裸 arXiv ID，如 `2301.07041` 或 `cs/0601001`
- **`- max: N`**：覆盖 MAX_RESULTS（如 `- max: 20`）
- **`- dir: PATH`**：覆盖 PAPER_DIR（如 `- dir: literature/`）
- **`- download`**：列出结果后下载第一条结果的 PDF
- **`- download: all`**：下载全部结果的 PDF

若参数匹配 arXiv ID 模式（`YYMM.NNNNN` 或 `category/NNNNNNN`），跳过搜索，直接进入 Step 3。

### Step 2：搜索 arXiv

按规范 strict-safe 链解析 `$ARXIV_FETCHER`（见
[`shared-references/integration-contract.md`](../shared-references/integration-contract.md) §2）：

```bash
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
if [ -z "${ARIS_REPO:-}" ] && [ -f .aris/installed-skills.txt ]; then
    ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null) || true
fi
if [ -z "${ARIS_REPO:-}" ] && [ -f "$HOME/.aris/repo" ]; then
    ARIS_REPO=$(cat "$HOME/.aris/repo" 2>/dev/null) || true
fi
ARXIV_FETCHER=".aris/tools/arxiv_fetch.py"
[ -f "$ARXIV_FETCHER" ] || ARXIV_FETCHER="tools/arxiv_fetch.py"
[ -f "$ARXIV_FETCHER" ] || { [ -n "${ARIS_REPO:-}" ] && ARXIV_FETCHER="$ARIS_REPO/tools/arxiv_fetch.py"; }
[ -f "$ARXIV_FETCHER" ] || ARXIV_FETCHER=""
```

**若 `$ARXIV_FETCHER` 非空**，运行：

```bash
python3 "$ARXIV_FETCHER" search "QUERY" --max MAX_RESULTS
```

**若 `$ARXIV_FETCHER` 为空**（Policy D1 级联），回退到内联 Python：

```bash
python3 - <<'PYEOF'
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2005/Atom"
query = urllib.parse.quote("QUERY")
url = (f"http://export.arxiv.org/api/query"
       f"?search_query={query}&start=0&max_results=MAX_RESULTS"
       f"&sortBy=relevance&sortOrder=descending")
with urllib.request.urlopen(url, timeout=30) as r:
    root = ET.fromstring(r.read())
papers = []
for entry in root.findall(f"{{{NS}}}entry"):
    aid = entry.findtext(f"{{{NS}}}id", "").split("/abs/")[-1].split("v")[0]
    title = (entry.findtext(f"{{{NS}}}title", "") or "").strip().replace("\n", " ")
    abstract = (entry.findtext(f"{{{NS}}}summary", "") or "").strip().replace("\n", " ")
    authors = [a.findtext(f"{{{NS}}}name", "") for a in entry.findall(f"{{{NS}}}author")]
    published = entry.findtext(f"{{{NS}}}published", "")[:10]
    cats = [c.get("term", "") for c in entry.findall(f"{{{NS}}}category")]
    papers.append({
        "id": aid,
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "published": published,
        "categories": cats,
        "pdf_url": f"https://arxiv.org/pdf/{aid}.pdf",
        "abs_url": f"https://arxiv.org/abs/{aid}",
    })
print(json.dumps(papers, ensure_ascii=False, indent=2))
PYEOF
```

以表格形式呈现结果：

```text
| # | arXiv ID   | Title               | Authors        | Date       | Category |
|---|------------|---------------------|----------------|------------|----------|
| 1 | 2301.07041 | Attention Is All... | Vaswani et al. | 2017-06-12 | cs.LG    |
```

### Step 3：获取指定 ID 的详情

当请求单个论文 ID 时（直接给出或来自 Step 2）：

```bash
python3 "$ARXIV_FETCHER" search "id:ARXIV_ID" --max 1
# or fallback:
python3 -c "
import urllib.request, xml.etree.ElementTree as ET
NS = 'http://www.w3.org/2005/Atom'
url = 'http://export.arxiv.org/api/query?id_list=ARXIV_ID'
with urllib.request.urlopen(url, timeout=30) as r:
    root = ET.fromstring(r.read())
# print full details ...
"
```

展示：标题、全部作者、分类、完整摘要、发表日期、PDF URL、摘要页 URL。

### Step 4：下载 PDF

当请求下载时，对每个待下载的论文 ID：

```bash
# Using fetch script:
python3 "$ARXIV_FETCHER" download ARXIV_ID --dir PAPER_DIR

# Fallback:
mkdir -p PAPER_DIR && python3 -c "
import pathlib
import sys
import urllib.request

out = pathlib.Path('PAPER_DIR/ARXIV_ID.pdf')
if out.exists():
    print(f'Already exists: {out}')
    sys.exit(0)
req = urllib.request.Request(
    'https://arxiv.org/pdf/ARXIV_ID.pdf',
    headers={'User-Agent': 'arxiv-skill/1.0'},
)
with urllib.request.urlopen(req, timeout=60) as r:
    out.write_bytes(r.read())
print(f'Downloaded: {out} ({out.stat().st_size // 1024} KB)')
"
```

每次下载之后：

- 确认文件大小 > 10 KB（拒绝更小的文件，很可能是错误 HTML 页面）
- 连续下载之间加 1 秒延迟，以避免触发速率限制
- 报告：`Downloaded: papers/2301.07041.pdf (842 KB)`

### Step 5：总结

对每篇论文（已下载或已通过 API 获取的）：

```markdown
## [Title]

- **arXiv**: [ID] - [abs_url]
- **Authors**: [full author list]
- **Date**: [published]
- **Categories**: [cs.LG, cs.AI, ...]
- **Abstract**: [full abstract]
- **Key contributions** (extracted from abstract):
  - [contribution 1]
  - [contribution 2]
  - [contribution 3]
- **Local PDF**: papers/[ID].pdf (if downloaded)
```

### Step 6：更新 Research Wiki（若已启用）

**当项目中存在 `research-wiki/` 时必须执行**；否则静默跳过。
当 wiki 目录存在时，按
[`shared-references/wiki-helper-resolution.md`](../shared-references/wiki-helper-resolution.md)
的规范链（Variant B — 警告后跳过）解析 `$WIKI_SCRIPT`，
然后将本次调用返回的每一篇论文都纳入：

```bash
if [ -d research-wiki/ ]; then
  cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
  ARIS_REPO="${ARIS_REPO:-$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null)}"
  if [ -z "${ARIS_REPO:-}" ] && [ -f "$HOME/.aris/repo" ]; then
    ARIS_REPO=$(cat "$HOME/.aris/repo" 2>/dev/null) || true
  fi
  WIKI_SCRIPT=".aris/tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || WIKI_SCRIPT="tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || { [ -n "${ARIS_REPO:-}" ] && WIKI_SCRIPT="$ARIS_REPO/tools/research_wiki.py"; }
  [ -f "$WIKI_SCRIPT" ] || {
    echo "WARN: research_wiki.py not found; arxiv results delivered, wiki ingest skipped. Fix: bash tools/install_aris.sh or smart_update.sh (refreshes ~/.aris/repo), export ARIS_REPO, or cp <ARIS-repo>/tools/research_wiki.py tools/." >&2
    WIKI_SCRIPT=""
  }
  if [ -n "$WIKI_SCRIPT" ]; then
    for each arxiv_id in results:
        python3 "$WIKI_SCRIPT" ingest_paper research-wiki/ \
            --arxiv-id "<arxiv_id>"
  fi
fi
```

该辅助脚本会在一次调用中完成元数据获取、slug、去重、页面创建、
索引重建和日志追加，**不要手写
`papers/<slug>.md`**。规范辅助脚本规则见
[`shared-references/integration-contract.md`](../shared-references/integration-contract.md)。
遗漏的纳入可稍后用
`python3 "$WIKI_SCRIPT" sync research-wiki/ --arxiv-ids <id1>,<id2>,...`
补录（先按上文方式解析 `$WIKI_SCRIPT`）。

### Step 7：最终输出

总结所做的事情：

- `Found N papers for "query"`
- `Downloaded: papers/2301.07041.pdf (842 KB)`（每次下载一条）
- `Wiki-ingested N papers`（若存在 `research-wiki/`）
- 任何警告（触发速率限制、文件过小、已存在）

建议后续使用的 skill：

```text
/research-lit "topic"     - multi-source review: Zotero + Obsidian + local PDFs + web
/novelty-check "idea"     - verify your idea is novel against these papers
```

## 关键规则

- 始终醒目地展示 arXiv ID，用户做引用和复现都需要它
- 校验下载的 PDF：文件必须 > 10 KB；更小则警告并删除
- 速率限制：连续下载 PDF 之间等待 1 秒；遇到 HTTP 429 时等 5 秒后重试一次
- 绝不覆盖同路径下已存在的 PDF，跳过并报告 "already exists"（已存在）
- 兼容两种 arXiv ID 格式：新格式（`2301.07041`）和旧格式（`cs/0601001`）
- PAPER_DIR 不存在时自动创建
- 若 arXiv API 不可达，清晰报告错误，并建议改用 `/research-lit` 加 `- sources: web` 作为回退
