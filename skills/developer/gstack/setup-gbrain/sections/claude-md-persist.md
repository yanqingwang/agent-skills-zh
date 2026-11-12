<!-- AUTO-GENERATED from claude-md-persist.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`setup-gbrain/sections/claude-md-persist.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

查找替换（或追加）该节。块格式取决于模式：

### Path 4（远程 MCP）

```markdown
## GBrain Configuration (configured by /setup-gbrain)
- Mode: remote-http
- MCP URL: {MCP_URL}
- Server version: gbrain v{SERVER_VERSION}  (from Step 4c verify)
- Setup date: {today}
- MCP registered: yes (user scope)
- Token: stored in ~/.claude.json (do not commit; never written to CLAUDE.md)
- Artifacts repo: {gstack_artifacts_remote URL or "none"}
- Artifacts sync: {off|artifacts-only|full}
- Current repo policy: {read-write|read-only|deny|unset}
```

bearer token **绝不**写入 CLAUDE.md（很多项目的 CLAUDE.md 会提交进
git）。它只存在于 `claude mcp add` 放置它的 `~/.claude.json`。

### Paths 1、2a、2b、3（本地 stdio）

```markdown
## GBrain Configuration (configured by /setup-gbrain)
- Mode: local-stdio
- Engine: {pglite|postgres}
- Config file: ~/.gbrain/config.json (mode 0600)
- Setup date: {today}
- MCP registered: {yes/no}
- Artifacts sync: {off|artifacts-only|full}
- Current repo policy: {read-write|read-only|deny|unset}
```

这里不要写 `## GBrain Search Guidance` 块。`/sync-gbrain` 是它唯一的
写入者：只有当其读取检查确认本仓库的代码索引能应答之后它才写该块，
并替换同一标题下的旧块。Step 10 会提议运行 `/sync-gbrain`。
