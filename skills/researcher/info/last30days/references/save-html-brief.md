> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/save-html-brief.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 保存可分享的 HTML 简报

用户要 HTML 简报时，主 `SKILL.md` 会加载本参考文件（或通过形似 HTML 的命令参数如 `--emit=html` / `--emit:html` / `--html`，或用自然语言："给我一份可分享的 HTML 简报"、"给我 HTML 版"、"发 Slack 用"、"发 Notion 用"、"导出成 HTML"等）。检测在 `SKILL.md` 完成，让常见的无 HTML 路径保持简短；实现放在这里。这些命令参数是给 skill 的用户意图信号，不是完整的 Python CLI 契约。

契约有两种模式：

- **HTML 是要求的交付物**（`--emit=html`、`--emit:html`、`--html`，或"给我 HTML 版"之类表述）：HTML 产物是主输出。把综述写入临时文件，渲染 HTML，然后在聊天中做一次简短的产物交接，而不是重新粘贴整份 Markdown 报告。
- **普通报告外加 HTML 副本**（用户要普通报告，同时也想要 HTML 副本）：综述仍以聊天为主输出。HTML 是另存到磁盘供分享的附加产物。两者在同一轮完成。

## 何时触发本流程

- 普通报告加 HTML 模式：在你已完整发出聊天响应之后：徽章、"What I learned:"（或对比标题）、带引用的加粗引导段、KEY PATTERNS 列表、引擎页脚透传、结尾引导块。
- HTML 交付物模式：在你起草完将进入 HTML 的综述之后、发出最终聊天响应之前。
- 在结尾引导之前，并等待用户响应。
- 仅在用户要求时。用户没要求就不要存 HTML。

## 如何触发

```bash
# 1. Write your synthesis prose VERBATIM to a temp file. The synthesis is the
#    "What I learned:" prose label, the bold-lead-in paragraphs with their
#    inline citations, and the "KEY PATTERNS from the research:" numbered list.
#    Do NOT include the badge or the engine footer in the temp file - the engine
#    adds those when it renders the HTML.
#    - HTML-as-deliverable mode: use the exact synthesis draft you prepared for
#      the artifact. Do not paste it to chat first.
#    - Normal-report-plus-HTML mode: use the exact synthesis text you already
#      wrote in chat.
#    In both modes, do not paraphrase, summarize, or reorder. The HTML must read
#    identically to the intended report in voice and citations.
SYNTHESIS_FILE="/tmp/last30days-synthesis-${CLAUDE_SESSION_ID}.md"
# >| not >: fixed path may already exist on a same-session re-run; a plain >
# is refused under `set -o noclobber`.
cat >| "${SYNTHESIS_FILE}" << 'SYNTHESIS_EOF'
What I learned:

**{First headline}** - {body with [name](url) inline citations}

**{Second headline}** - {body}

**{Third headline}** - {body}

KEY PATTERNS from the research:
1. {pattern} - per [@handle](url)
2. {pattern} - per [r/sub](url)
3. {pattern} - per [@handle](url)
SYNTHESIS_EOF

# 2. Convert the synthesis to a self-contained HTML file via the engine.
#    Use --cached-report with the same topic as your original run. The engine
#    reuses the original scope and per-entity reports in the structured cache at
#    ~/.config/last30days/last-report.json to build badge metadata and footer
#    without re-running source fetchers. That cache is intentionally short-lived
#    (default: one hour; tune with LAST30DAYS_REPORT_CACHE_TTL_SECONDS, or set
#    it to 0 to disable reuse). Do not replay --plan, --competitors-plan, or
#    --x-posts: their temporary files can already be removed. If the cache is
#    stale, missing, or for a different topic, stderr says
#    "No matching cached report data" and the command exits without research. Recreate the original
#    research plans, rerun research with the original scope, and update the
#    synthesis before retrying this export.
SLUG=$(printf '%s\n' "${TOPIC}" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed 's/^-//;s/-$//')
# Render beside the destination, then create a new name atomically. The hard
# link refuses existing paths even when another exporter wins the same name.
HTML_PATH=$(
  HTML_TMP=$(mktemp "${LAST30DAYS_MEMORY_DIR}/.last30days-html.XXXXXXXX") || exit "$?"
  trap 'rm -f -- "${HTML_TMP}"' EXIT
  "${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" "${TOPIC}" \
    --emit=html \
    --cached-report \
    --synthesis-file "${SYNTHESIS_FILE}" \
    >| "${HTML_TMP}" || exit "$?"
  "${LAST30DAYS_PYTHON}" - "${HTML_TMP}" "${LAST30DAYS_MEMORY_DIR}" "${SLUG}" << 'HTML_PATH_PY'
from datetime import date
import os
from pathlib import Path
import sys

temporary, directory, slug = sys.argv[1:]
base = Path(directory) / f"{slug}-brief"
dated = f"{base}-{date.today().isoformat()}"
candidate = Path(f"{base}.html")
suffix = 1
while True:
    try:
        os.link(temporary, candidate)
    except FileExistsError:
        candidate = Path(f"{dated}.html" if suffix == 1 else f"{dated}-{suffix}.html")
        suffix += 1
    else:
        print(candidate)
        break
HTML_PATH_PY
) || exit "$?"
#    The cached report preserves hiring scope and comparison targeting.

# 3. Finish with the artifact handoff described below. Do not print the saved
#    path from the shell block; the chat handoff is the single user-visible
#    completion message.
```

## 可选的托管发布

只有在本地 HTML 文件已保存且用户选择了发布选项之后才发布。本地 HTML 保存永远在前，任何发布/上传步骤之前都必须先展示绝对路径。

先尊重既有的用户、项目或宿主 HTML 发布偏好。用户已有首选发布器或内部分享流程时，把该选项也列上。有多个发布选项时逐个展示，并把 `ht-ml.app` 列为其中之一；标注 `ht-ml.app` 支持可选密码保护。没有偏好时，用 `ht-ml.app` 作为兜底发布选项。

按此决策流程：

- 保存本地 HTML 文件。
- 展示保存的绝对路径。
- 然后主动给出下一步选项：
  1. 打开 HTML 文件
  2. 发布到 `<首选/已配置服务>`；展示 `ht-ml.app` 时说明可选密码保护
  3. 暂告一段落
- 用户选择发布选项之前不要上传。

发布到 `ht-ml.app` 时再问一个问题：

- **公开链接**：不带密码发布。
- **密码保护链接**：让用户自由输入共享密码，然后用该密码发布。

在给出 `ht-ml.app` 选项之前，告诉用户公开页面可能被爬取或收录，且可选密码保护。用户选密码保护时，使用他们为本报告专门提供的共享密码；不要用他们自己的账号密码。

代理应在需要时自行了解所选服务当前的发布机制，包括访问其官网，而不是在聊天里硬编码服务专属的详细说明。内置 `ht-ml.app` 路径上，引擎支持 `--publish-html`；密码保护分支经 `LAST30DAYS_PUBLISH_PASSWORD` 传共享密码，不走命令行参数。

用户选内置 `ht-ml.app` 路径时，在同一条 `--emit=html` 命令上加 `--publish-html`。用 `--output "$HTML_PATH"` 而非 shell 重定向，让引擎能把 `.publish.json` 伴随元数据写在本地 HTML 旁。密码保护分支在子进程环境里设 `LAST30DAYS_PUBLISH_PASSWORD`，不在 shell 命令里传 `--publish-password`。

```bash
LAST30DAYS_PUBLISH_PASSWORD="${PUBLISH_PASSWORD:-}" \
"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" "${TOPIC}" \
  --emit=html \
  --cached-report \
  --synthesis-file "$SYNTHESIS_FILE" \
  --output "$HTML_PATH" \
  --publish-html \
  >/dev/null
```

托管 URL 以 `[last30days] Published HTML to https://...` 形式出现在 stderr。用托管 URL 确认结果。用户选了密码保护时，把他们选的共享密码再复述一次，方便把 URL 和密码一起发出去。引擎把 URL 元数据写到 `<HTML_PATH>.publish.json`。服务商可能返回 `update_key`；按机密对待。引擎刻意不把 update key 写进 stdout、HTML 产物或 `.publish.json` 伴随元数据。

## 保存后的聊天交接

按请求匹配模式。

### HTML 是要求的交付物

HTML 是交付物时（无论经 `--emit=html`、`--emit:html`、`--html` 还是自然语言表述），保存产物后**不要**把整份 Markdown 报告再粘回聊天。用户要的是 HTML 交付物；重复 Markdown 会让这次运行像是普通报告硬加了附件。

用包含下一步选项的简短交接回应：

```text
{the engine's first line, copied verbatim}

📎 Shareable brief saved to <absolute HTML path>

What do you want to do next?
1. Open HTML file
2. Publish to <available HTML publishing service> (<service-specific note, e.g. ht-ml.app supports optional password protection>)
3. Done for now
```

用户选打开时，宿主能安全打开本地文件就打开 HTML，聊天里保留保存路径行，并加一句 `Opened locally.`。由宿主选择正确的 OS 专属机制；不要打印一份 shell 命令菜单。打开失败或宿主无界面（headless）时不视为报告失败：展示路径，说明文件已就绪、可在浏览器打开。

### 普通报告外加 HTML 副本

用户要普通 `/last30days` 报告同时也要 HTML 副本时，保留完整聊天综述，并在结尾引导后追加这个产物块：

```text
📎 Shareable brief saved to <absolute HTML path>

What do you want to do next?
1. Open HTML file
2. Publish to <available HTML publishing service> (<service-specific note, e.g. ht-ml.app supports optional password protection>)
3. Done for now
```

用户选打开时，宿主能安全打开本地文件就打开；否则保存路径行就够了。用户不选发布选项就不要上传。

## HTML 文件里最终有什么

引擎的 `--emit=html` 渲染器组合了：

- 顶部的引擎徽章行
- 徽章下方一行内联元数据（`{date range} · {active sources}`）
- 你的综述原样，散文标签升为 `<h2>`，加粗引导保留
- 所有 `[name](url)` 引用渲染为 `<a>` 标签
- 引擎页脚（`✅ All agents reported back!` 树）以等宽字体原样保留
- 含主题和重跑提示的尾注（colophon）

渲染器会剥掉不属于可分享产物的引擎内部噪音：`# last30days vX.Y.Z: TOPIC` 调试文件头、面向模型的 `> Safety note:` 引用块，以及 `I'm now an expert on X` 结尾引导块。数据质量警告（降级运行、证据薄弱等）留在引擎 stderr 日志里，绝不泄漏进待分享文件。

## 对比模式

主题是 `X vs Y`（或 `X vs Y vs Z`）时流程相同。用 `--cached-report`，不带已删除的 `--competitors-plan` 和 `--plan` 文件。引擎把存储的实体报告送入 `render_for_html_comparison`。综述临时文件仍应包含你在聊天里写的对比形态综述（`## Quick Verdict`、每个实体的 `## {Entity}`、`## Head-to-Head` 表、`## The Bottom Line`、`## The emerging stack`，依 LAW 4 对比例外）。

## 后续轮次

用户正常跑 `/last30days OpenClaw`，在聊天里看到综述，然后明确回指那份可见综述（"存成 HTML"、"做成可分享的"、"把上面转成 HTML"）时，对上一轮写的综述执行同样的保存流程。把综述写入临时文件，用 `--cached-report --emit=html --synthesis-file` 调引擎，用普通报告加 HTML 的产物块。

后续请求是要新的 HTML 交付物（"给我 HTML 版"、`--emit=html`、`--html`）而不是回指已可见的报告时，按 HTML 交付物模式处理。

引擎在 `LAST30DAYS_REPORT_CACHE_TTL_SECONDS`（默认一小时）之内会复用 `~/.config/last30days/last-report.json`。stderr 说在复用缓存报告数据时正常继续。没有匹配缓存时命令在研究前停止。先重建原计划、重跑原研究范围、更新综述，再重新导出。

## 不要做的事

- 用户没要求就不要存 HTML。稀疏模式（无综述）产出的文件很单薄，不适合分享。
- 临时文件里除综述正文外不要加内容。徽章/页脚/尾注由引擎生成。
- 不要改文件路径约定。`${LAST30DAYS_MEMORY_DIR}/${SLUG}-brief.html` 是规范位置。
- 不要覆盖已有文件。第 2 步先渲染到私有临时文件，再把完成的输出链接到一个新名字。`{slug}-brief.html` 已存在时，先试 `{slug}-brief-YYYY-MM-DD.html`，再试 `{slug}-brief-YYYY-MM-DD-2.html`，递增直到有可用名字。这也天然处理并发导出，不替换文件、目录或符号链接。临时文件无论成败都会删除。渲染或链接失败时报告错误，而不是谎报保存成功。聊天交接中始终报告 `HTML_PATH` 里存的路径。
- 临时文件和最终聊天行里都不要放数据质量警告文本。警告是引擎 stderr 的事，不是产物的事。
- 本地保存流程中不要把 HTML 发布、上传或发送到第三方服务。
- 不要因为用户要了 HTML 就发布到某个服务。先展示保存路径和下一步选项；发布必须由用户选择发布选项。
- 除非用户明确要托管 URL，否则不要让本地 HTML 导出阻塞在托管决定上。
- 不要把 `update_key` 粘贴或存进聊天、Markdown、HTML、原始输出或伴随元数据。

## 边界情况

- **主题含 shell 特殊字符**（引号、与号）：临时文件名用 slug 化版本，引擎收到的是原始主题。`cat <<'SYNTHESIS_EOF'` 带引号 heredoc 形式可处理任意内容而不展开。综述文本可以含任何字符。
- **超长综述**：没有上限。引擎能处理长 Markdown 正文。原样粘贴即可。
- **综述含图片或非 ASCII**：emoji 和 Unicode 原样通过。图片标签按原始 HTML 通过；渲染器不转换它们。聊天里没放图片，这里也不要加。
- **未设置 `${LAST30DAYS_MEMORY_DIR}` 时**：按 `references/runtime.md` 的 `Configuration` 节，默认 `~/Documents/Last30Days/`。
