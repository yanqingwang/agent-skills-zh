> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/agent-mode.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 代理模式

当技能参数中出现 `--agent`，或用户明确要求机器可读的 JSON 时阅读本文件。此模式绝不代表用户授予浏览器 Cookie 授权。只有在跳过交互式提问与根文档的授权要求不冲突时才可跳过；没有授权时走无 Cookie 路径。

## 代理模式（--agent 标志）

若 ARGUMENTS 中出现 `--agent`（例如 `/last30days plaud granola --agent`）：

1. **跳过**开场展示块（"I'll research X across Reddit..."）
2. **跳过**所有 `AskUserQuestion` 调用——未指定时使用 `TARGET_TOOL = "unknown"`
3. **照常运行**研究脚本与 WebSearch
4. **跳过**"WAIT FOR USER RESPONSE" 停顿
5. **跳过**追问邀请（"I'm now an expert on X..."）
6. **输出**完整研究报告后结束——不要等待进一步输入

当解析出的目录非空时，代理模式会通过 `--save-dir` 自动把原始研究数据保存到 `LAST30DAYS_MEMORY_DIR`（默认为 `~/Documents/Last30Days`）（由脚本处理，无需额外工具调用）。目录为空则禁用这些保存及其页脚指针。仅当调用方需要把渲染后的 stdout 产物落到指定路径时才使用 `--output <file>`，输出格式由 `--emit` 控制。

**机器可读 JSON 例外：** 如果用户明确要求为代理、脚本或工作流输出结构化 JSON，请把常规的 `--emit=compact` 引擎调用换成 `--emit=json`，并原样透传引擎的 stdout，而不是按下面的报告格式自行拼装。默认的 `--json-profile=agent` 是稳定且带版本的扁平契约；只有在用户明确要求完整的内部 `Report` 转储时才使用 `--json-profile=raw`。`--preflight --emit=json` 是另一套权限预检契约，不受 `--json-profile` 影响。完整字段文档与版本策略见仓库内的 `docs/reference/json-export.md`。

代理模式报告格式：

```
## Research Report: {TOPIC}
Generated: {date} | Sources: Reddit, X, Bluesky, YouTube, TikTok, HN, Polymarket, Web

### Key Findings
[3-5 bullet points, highest-signal insights with citations]

### What I learned
{The full "What I learned" synthesis from normal output}

### Stats
{The standard stats block}
```

---
