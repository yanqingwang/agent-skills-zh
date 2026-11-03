> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/runtime.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 运行时与配置

在任何引擎命令之前阅读本文件。运行这些片段前，把 `SKILL_DIR` 绑定到已加载的根 SKILL.md。参考目录永远不是安装根。

# 第 0 步：陈旧克隆自检 — 阅读下文之前先运行

在阅读本文件的其他任何内容之前，先检查你是否从唯一已知的陈旧克隆位置加载了 SKILL.md：Claude Code 的 marketplaces 目录。

**运行这项检查：**

```bash
CLAUDE_CACHE_LATEST=$(find "$HOME/.claude/plugins/cache/last30days-skill/last30days" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | sort -V | tail -1)
# Two cache layouts ship in the wild — nested ({version}/skills/last30days/SKILL.md)
# and flat ({version}/SKILL.md). Resolve to whichever shape actually exists.
CLAUDE_CACHE_SKILL_MD=""
if [ -n "$CLAUDE_CACHE_LATEST" ]; then
  if [ -f "$CLAUDE_CACHE_LATEST/skills/last30days/SKILL.md" ]; then
    CLAUDE_CACHE_SKILL_MD="$CLAUDE_CACHE_LATEST/skills/last30days/SKILL.md"
  elif [ -f "$CLAUDE_CACHE_LATEST/SKILL.md" ]; then
    CLAUDE_CACHE_SKILL_MD="$CLAUDE_CACHE_LATEST/SKILL.md"
  fi
fi
echo "CLAUDE_CACHE_SKILL_MD=$CLAUDE_CACHE_SKILL_MD"
```

如果已加载的根 SKILL.md 路径包含 `/.claude/plugins/marketplaces/`，且 `$CLAUDE_CACHE_SKILL_MD` 非空，就停止并重新阅读 `$CLAUDE_CACHE_SKILL_MD` 再继续。否则你手上的 SKILL.md 没问题，继续即可。

**其他安装路径都没问题：** `~/.codex/skills/`、`~/.agents/skills/`、`npx skills add` 的安装目录或仓库检出都是有效的加载点，根 `SKILL_DIR` 绑定会自动识别它们。在这些路径上不要中止或跳转。

---


## 运行时预检

在本 Skill 中运行任何 `last30days.py` 命令之前，一次性解析出 Python 3.12+ 解释器并把它保存在 `LAST30DAYS_PYTHON` 中：

```bash
try_last30days_python() {
  candidate="${1}"
  [ -n "$candidate" ] || return 1
  if [ -x "$candidate" ]; then
    :
  elif command -v "$candidate" >/dev/null 2>&1; then
    :
  else
    return 1
  fi
  "$candidate" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)' || return 1
  LAST30DAYS_PYTHON="$candidate"
  return 0
}

windows_path_to_unix() {
  path="${1}"
  [ -n "$path" ] || return 1
  if command -v cygpath >/dev/null 2>&1; then
    cygpath -u "$path"
  else
    printf '%s\n' "$path"
  fi
}

if [ -z "${LAST30DAYS_PYTHON:-}" ]; then
  while IFS= read -r windows_python_root; do
    [ -n "$windows_python_root" ] && [ -d "$windows_python_root" ] || continue
    while IFS= read -r py; do
      try_last30days_python "$py" && break 2
    done <<EOF_PYTHON_CANDIDATES
$(find "$windows_python_root" -maxdepth 2 -type f -iname python.exe 2>/dev/null | sort -r)
EOF_PYTHON_CANDIDATES
  done <<EOF_WINDOWS_PYTHON_ROOTS
$([ -n "${LOCALAPPDATA:-}" ] && printf '%s\n' "$(windows_path_to_unix "$LOCALAPPDATA")/Programs/Python")
$([ -n "${ProgramFiles:-}" ] && windows_path_to_unix "$ProgramFiles")
$([ -n "${PROGRAMFILES:-}" ] && windows_path_to_unix "$PROGRAMFILES")
$(program_files_x86="$(printenv 'ProgramFiles(x86)' 2>/dev/null || true)"; [ -n "$program_files_x86" ] && windows_path_to_unix "$program_files_x86")
EOF_WINDOWS_PYTHON_ROOTS
fi

if [ -z "${LAST30DAYS_PYTHON:-}" ]; then
  for py in python3.14 python3.13 python3.12 python3 python; do
    try_last30days_python "$py" && break
  done
fi

# uv fallback: on hosts without a system 3.12 but with `uv` on PATH (most agent
# sandboxes: Cowork, Codex, etc.), provision a managed 3.12 automatically instead
# of hard-failing. No-op when uv is absent — those hosts still hit the error below.
if [ -z "${LAST30DAYS_PYTHON:-}" ] && command -v uv >/dev/null 2>&1; then
  uv_py="$(uv python find '>=3.12' 2>/dev/null)"
  if [ -z "$uv_py" ] || [ ! -x "$uv_py" ]; then
    echo "NOTE: no Python 3.12+ found; installing a managed CPython 3.12 via uv (~28MB, one-time)." >&2
    if UV_HTTP_TIMEOUT=30 uv python install 3.12 >/dev/null 2>&1; then
      uv_py="$(uv python find '>=3.12' 2>/dev/null)"
    else
      echo "WARN: 'uv python install 3.12' failed (network, disk space, or proxy?); falling through to the version-gate error below." >&2
    fi
  fi
  try_last30days_python "$uv_py"
fi

if [ -z "${LAST30DAYS_PYTHON:-}" ]; then
  echo "ERROR: last30days v3 requires Python 3.12+. Install Python 3.12+ or set LAST30DAYS_PYTHON to a supported interpreter." >&2
  exit 1
fi

"${LAST30DAYS_PYTHON}" -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 12) else 1)' || {
  echo "ERROR: LAST30DAYS_PYTHON must point to Python 3.12+." >&2
  exit 1
}

last30days_python_path="$(command -v "$LAST30DAYS_PYTHON")" || exit 1
case "$last30days_python_path" in
  /*) LAST30DAYS_PYTHON="$last30days_python_path" ;;
  */*) last30days_python_dir="$(cd -P -- "${last30days_python_path%/*}" && pwd -P)" || exit 1
       LAST30DAYS_PYTHON="$last30days_python_dir/${last30days_python_path##*/}" ;;
  *) echo "ERROR: selected Python must resolve to an executable path." >&2; exit 1 ;;
esac
export LAST30DAYS_PYTHON
"${LAST30DAYS_PYTHON}" -c 'import os, shlex; print("LAST30DAYS_PYTHON=" + shlex.quote(os.environ["LAST30DAYS_PYTHON"]))'

```

**PYTHON 版本门槛 — 当上面的运行时预检 Bash 块因 Python 版本错误而退出时：**

如果预检脚本（包括上面的 uv 回退）输出 `ERROR: last30days v3 requires Python 3.12+`（或 `LAST30DAYS_PYTHON must point to Python 3.12+`）并退出，你必须：

1. 向用户显示这条消息：
   > "The last30days engine needs Python 3.12+. Your system has an older version. Install it with one command:
   > - **Mac:** `brew install python@3.12`
   > - **Windows:** `winget install Python.Python.3.12`
   > - **Linux:** `sudo apt install python3.12` (or `pyenv install 3.12`)
   >
   > Then re-run `/last30days <your topic>` and the setup wizard will configure everything automatically."
2. **停止。** 不要尝试研究。不要退回到只用 WebSearch 的综合。

只用 WebSearch 的综合并不等同于运行引擎 — 它会漏掉 Reddit 社区数据、X/Twitter 时间线、YouTube 转录、TikTok 与 Polymarket。不加说明就呈现它，会误导用户以为实际检索过的东西就是这些。这与不带引擎页脚的纯 WebSearch 运行属于同一类失败。

**原生搜索信号（web 覆盖面）。** 如果你（承载模型）自带 web 搜索工具，在调用引擎前先在同一个 shell 中导出 `LAST30DAYS_NATIVE_SEARCH=1`：

```bash
export LAST30DAYS_NATIVE_SEARCH=1   # ONLY when you have a native web-search tool
```

你所在的宿主搜索强于引擎的免密 web 回退，所以这会告诉引擎跳过那个回退，把通用 web 检索留给你（你本来就在第 2 步跑 web 搜索补充）。如果 Agent 会话里没有任何 web 搜索工具，就**不要**设置它：引擎的免密 web 下限会自动提供通用 web 覆盖面。这条规则基于能力，而不是宿主名称，只有在你确实有更好的搜索时才设置，绝不要在什么都没有的宿主上为了压掉这个下限而设置。

## 保存目录解析

解释器引导之后，在第一次需要保存目录的引擎操作之前，一次性解析出保存目录。如果用户提供了一次性目录，在运行下面的解析命令之前，先加上 `--save-dir="<requested directory>"`。从后面的研究参数中去掉重复的保存目录参数。绝不 source `.env` 文件。

```bash
LAST30DAYS_MEMORY_DIR="$("${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" --resolve-save-dir)" || exit
printf 'Resolved save directory: <%s>\n' "$LAST30DAYS_MEMORY_DIR" >&2
```

捕获那个确切值，包括空字符串。后续的 library、discovery 与 research 配方都使用这个捕获值，不再重新解析。当各次 shell 调用之间不共享变量时，显式恢复捕获到的值。所有 discovery 阶段都使用同一个值，即使配置或工作目录发生变化。

## 配置

在进程环境、可信项目配置或全局 `~/.config/last30days/.env` 中设置 `LAST30DAYS_MEMORY_DIR`，以决定原始研究文件保存在哪里。在显式的 `--save-dir` 之后，解析顺序遵循该优先级。只有完全未设置时才让 Skill 默认为 `~/Documents/Last30Days`；显式留空则禁用研究文件保存。引擎在首次保存时创建非空目录。

引擎从进程环境或 `~/.config/last30days/.env` 读取 `LAST30DAYS_MEMORY_DIR`，因此在环境变量已设置时，不带 `--save-dir` 的直接 CLI 调用（`python3 scripts/last30days.py ...`）同样会保存。这与 `LAST30DAYS_STORE` 的环境变量或参数约定一致。显式的 `--save-dir` 始终优先。

当 `LAST30DAYS_API_KEY` 与 `LAST30DAYS_API_BASE` 同时设置时，引擎会通过该配置的远程 API 而不是本地来源来运行研究（除非传入 `--mock`）；`LAST30DAYS_API_BASE` 是端点，没有内置默认值，因此任一变量未设置都会照常运行本地来源。配置了 `--corpus` / `LAST30DAYS_CORPUS_DIRS` 属于隐私例外：引擎绕过托管后端、改为本地运行，这样任何源自文件的输入都不会被转发。显式的 `--perplexity-search-type` 参数在存在直连 `PERPLEXITY_API_KEY` 时也会本地运行，因为托管后端无法应用它；引擎会打印一条 stderr 提示。没有直连密钥时，运行仍走托管路径，并打印一条说明该参数未被应用的提示。仅在环境变量中设置的 `LAST30DAYS_PERPLEXITY_SEARCH_TYPE` 值仍会保持托管路由，并打印一条说明它未被应用的提示。除此之外调用方式不变：参数相同，`--quick`/`--deep` 映射到搜索深度，非默认的 `--register` 会转发给服务端做综合，进度行仍流式输出到 stderr（`[narrate] step=...` 加一行紧凑的耗时/剩余时间），报告照常打印到 stdout 并保存到记忆目录，因此第 1-4 步在输出上照常进行。例外是研究 JSON：远程端点不返回版本化 Agent 画像所需的本地 `Report`，因此请用 `--emit=json --json-profile=raw` 以获取其既有的服务端响应 JSON 契约。在此模式下，搜索本身不需要任何按来源的密钥或设置向导凭证。有两种引擎退出需要特别处理：退出码 3 表示 API 先提出了一个澄清问题，引擎会把问题和选项打印到 stderr；把它们呈现给用户，并把选定的角度折进话题后重新运行。额度不足的失败（HTTP 402）会打印账户余额、所需金额与账单链接，原样把这些行转达给用户；不要退回到只用 WebSearch 的综合。

**仅开发者用的评测采集：** `--record-fixtures <dir>` 是维护确定性研究质量测试套件用的隐藏直连引擎参数。它把脱敏后的 HTTP 与 CLI 适配器响应记录到 `<dir>/http.json`；它绝不属于面向用户的斜杠命令调用。夹具评审、回放与基线规则见 `docs/reference/eval.md`。
