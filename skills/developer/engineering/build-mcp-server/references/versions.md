> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-server/references/versions.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 版本锁定清单

本 skill 中所有版本敏感的声明集中在这里。更新 skill 时，先核对这张表。

| 声明 | 出处 | 最近核实 |
|---|---|---|
| `@modelcontextprotocol/ext-apps@1.2.2` CDN 锁定 | `build-mcp-app/SKILL.md`、`build-mcp-app/references/widget-templates.md`（4 处） | 2026-03 |
| elicitation 需要 Claude Code ≥2.1.76 | `elicitation.md:15`、`build-mcp-server/SKILL.md:43,76` | 2026-03 |
| MCP 规范 2025-11-25 的 CIMD/DCR 状态 | `auth.md:20,24,41` | 2026-03 |
| MCPB manifest schema v0.4 | `build-mcpb/references/manifest-schema.md` | 2026-03 |
| CF `agents` SDK / `McpAgent` API | `deploy-cloudflare-workers.md` | 2026-03 |
| CF 模板路径 `cloudflare/ai/demos/remote-mcp-authless` | `deploy-cloudflare-workers.md` | 2026-03 |

## 如何核实

```bash
# ext-apps latest
npm view @modelcontextprotocol/ext-apps version

# CF template still exists
gh api repos/cloudflare/ai/contents/demos/remote-mcp-authless/src/index.ts --jq '.sha'

# MCPB schema
curl -sI https://raw.githubusercontent.com/anthropics/mcpb/main/schemas/mcpb-manifest-v0.4.schema.json | head -1
```
