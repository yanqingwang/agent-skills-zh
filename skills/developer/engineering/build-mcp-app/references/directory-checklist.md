> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/directory-checklist.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Connector 目录提交清单

把远程 MCP 应用提交到 Claude connector 目录前，先做一遍预检。每一项都是硬性审查标准。

| 领域 | 要求 |
|---|---|
| **Auth** | OAuth（DCR 或 CIMD）或 **`none`**（无鉴权）。静态 bearer token 仅限私有部署，会阻塞上架。公共数据服务器可用无鉴权模式：上游 API key 由服务器持有。 |
| **Tool annotations** | 每个工具都要设 `annotations.title` 加相关提示：fetch/search 类工具设 `readOnlyHint: true`，写操作设 `destructiveHint` / `idempotentHint`，会触达外部系统的工具设 `openWorldHint: true`。 |
| **Tool names** | ≤ 64 字符，snake/kebab 命名。 |
| **Widget layout** | 内联高度 ≤ 500px，无嵌套滚动容器，触控目标最小 44pt，两种主题下均达 WCAG-AA 对比度。 |
| **Theming** | `html, body { background: transparent }`、`<meta name="color-scheme" content="light dark">`，通过 `applyHostStyleVariables` 采用宿主 CSS token。 |
| **External links** | 用 `app.openLink`。在 connector 的 *Allowed link URIs* 里声明每个来源（如 `https://api.example.com`），链接就能跳过确认弹窗。 |
| **Helper tools** | 仅 widget 使用的工具（几何/图片抓取）标注 `_meta.ui.visibility: ["app"]`，不出现在 Claude 的工具列表里。 |
| **Screenshots** | 3–5 张 PNG，宽度 ≥ 1000px，只裁应用响应部分：画面里不要有提示词文本。 |

无鉴权端点公开后，限流与 IP 分层指引参见 `abuse-protection.md`。
