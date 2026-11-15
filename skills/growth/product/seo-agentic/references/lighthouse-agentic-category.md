> **中文汉化版** · 上游：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) · 原文件：`skills/seo-agentic/references/lighthouse-agentic-category.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Lighthouse Agentic Browsing 分类（源码核验，Lighthouse 13.5.0）

2026-09-23 对照 Lighthouse 13.5.0 npm 包核验（`core/config/default-config.js`、`core/audits/agentic/*`、`core/audits/webmcp-*`、`core/gather/gatherers/agentic/*`、`report/renderer/report-utils.js`），以及 PSI v5 实跑。该分类标注为"仍在开发中、可能变化"，所以 Lighthouse 版本升级时要重读源码。

## 在哪里运行

| 路径 | 说明 |
|---|---|
| PSI API v5 | `category=AGENTIC_BROWSING`（v5 discovery 文档中的枚举；`agentic-browsing` 也可以）。2026-09-23 时 PSI 在 HeadlessChrome 153 上运行 Lighthouse 13.5.0，并暴露了 WebMCP 工具。 |
| Lighthouse CLI | `npx lighthouse@latest <url> --only-categories=agentic-browsing --output=json`（Node 22.19+）。 |
| DevTools | Lighthouse 面板，Chrome 150+。WebMCP 审计需要开启了 WebMCP 的浏览器（origin trial 或 flag）。 |

CrUX 永远不提供这些审计：它们只在实验室环境（lab）运行。

## 分类定义

分类 id `agentic-browsing`，`categoryScoreDisplayMode: "fraction"`，支持 navigation 和 snapshot 两种模式。七个 audit ref，权重全为 1：

| 审计 id | 分组 | 评分 |
|---|---|---|
| `agent-accessibility-tree` | agent-accessibility | 二值。仅当 33 条 axe 规则（见下）全部通过时通过。 |
| `webmcp-form-coverage` | webmcp | 只要还有表单同时缺 `toolname` 和 `tooldescription`，就是 informative；每个表单都齐了才算**二值通过**；无表单或不支持 WebMCP 时为 N/A。永不失败。 |
| `webmcp-registered-tools` | webmcp | 始终 informative；不支持 WebMCP 时为 N/A。列出 imperative 和 declarative 工具。 |
| `webmcp-schema-validity` | webmcp | 有 error 得 0，有 warning 得 0.5（两者都算失败），干净则得 1；不支持 WebMCP、或既无工具也无问题时为 N/A。 |
| `cumulative-layout-shift` | （无，CLS） | 数值型实验室 CLS；得分 0.9 或以上即通过。 |
| `llms-txt` | agent-discoverability | 抓取 `/llms.txt`。4xx：N/A。5xx 或抓取失败：0。否则要求有 H1（`^\s*#\s+.+`）、至少一个 Markdown 链接（`[..](..)`）和 50 个以上字符。 |
| `ard-schema` | agent-discoverability | 校验 `ai-catalog.json`。除非有 catalog 被声明、或 `/.well-known/ai-catalog.json` 返回 200，否则 N/A。有 error：0；仅 warning：0.9（仍算通过）。 |

`webmcp-schema-validity` 的 error：缺工具名、缺工具描述、必填参数缺名字。warning：参数缺 title 或 description、可选参数缺名字。它们会以 Chrome DevTools issues（`FormModelContext*`）的形式浮出。

### `agent-accessibility-tree` 背后的 33 条 axe 规则

`button-name`、`input-button-name`、`input-image-alt`、`label`、`link-name`、
`select-name`、`document-title`、`aria-allowed-attr`、`aria-allowed-role`、
`aria-command-name`、`aria-conditional-attr`、`aria-dialog-name`、
`aria-hidden-body`、`aria-hidden-focus`、`aria-input-field-name`、
`aria-prohibited-attr`、`aria-required-attr`、`aria-required-children`、
`aria-required-parent`、`aria-roles`、`aria-text`、`aria-toggle-field-name`、
`aria-tooltip-name`、`aria-treeitem-name`、`aria-valid-attr`、
`aria-valid-attr-value`、`duplicate-id-aria`、`definition-list`、
`table-duplicate-name`、`tabindex`、`autocomplete-valid`、
`presentation-role-conflict`、`svg-img-alt`。

颜色对比、标题顺序和 landmark **不在**集合内，所以一个页面可能让 Accessibility 分类失败，却仍能通过这个审计。

### ARD catalog 的发现顺序（gatherer `agentic/ard.js`）

1. robots.txt 的 `Agentmap: <url>`（首个匹配，不区分大小写）
2. DOM 中的 `<link rel="ai-catalog" href="...">`
3. 主文档上的 HTTP `Link: <...>; rel="ai-catalog"`
4. `/.well-known/ai-catalog.json`

ARD 检查（specVersion `1.0`、`entries` 数组、`urn:air:` 标识符、`displayName`、`type`、`url`/`data` 二选一、2 到 5 个 `representativeQueries`、`trustManifest.identity`、不允许顶层 `collections`）已移植进 `agentic_check.py`（`validate_ai_catalog`）。规范：agenticresourcediscovery.org/spec；上游仓库 ards-project/ard-spec。

## 分数是怎么算出来的

依据 `ReportUtils.calculateCategoryFraction`：

- 跳过 `hidden` 组的审计，以及模式为 `manual` 或 `notApplicable` 的审计。
- informative 审计永远不计入 N（只会抬高一个单独的 informative 计数）。
- 其余每个审计给 N 加 1，并在 `score >= 0.9` 时算通过。`error` 审计计入 N 且算失败。

JSON 字段 `categories["agentic-browsing"].score` 是加权平均，不是这个 fraction。报告时写"X/N"，永远不要写百分比。

### N 的最大值与什么会推动它

`webmcp-registered-tools` 永不计数，所以 N 最多为 6。典型取值：

| 站点状态 | 计入的审计 |
|---|---|
| 无 WebMCP、无 llms.txt、无 catalog | tree + CLS = **2** |
| + 有效的 llms.txt | **3** |
| + imperative WebMCP 工具 | + schema validity = **4** |
| + 每个表单都有标注（`toolname`/`tooldescription`） | + form coverage = **5**（见注） |
| + 有效的 `ai-catalog.json` | **6** |

注意：被标注的表单会注册 declarative 工具。在一个没有 imperative 工具的页面上，这会把 `webmcp-schema-validity` 从 N/A 变成一个计入的审计；只要有一个参数缺 description，它就得 0.5（失败）。要么标注完整，要么完全不标。

实测示例，claude-seo.md 在 2026-09-23（PSI，mobile 和 desktop）：注册了 4 个 imperative 工具，一个表单没有标注，无 catalog。结果 **4/4**，另有 2 个 informative 审计。当某次运行显示 5/5，说明 form coverage 被计入了，即该页每个表单都带标注（或被标注的表单是唯一表单）。读 `lighthouse_agentic.py` 的输出，不要猜：它会列出每个审计的状态，以及哪些"paths"增加了一个计入的审计。

## 负责任地解读结果

- 更高的 N 不是更好的站点。加 catalog 或给表单加标注只会增加审计；只有当资源或表单真实存在、且对 agent 安全时才去做。
- WebMCP 审计取决于测试用的浏览器。PSI 今天支持 WebMCP；本地 Chrome 没有 origin trial 或 flag 时会标 N/A。
- imperative 工具的注册时机可能每次运行不同。报告 WebMCP 回归前先跑两次。
- `llms-txt` 通过与否与 Google 搜索无关：Google 忽略 llms.txt（见 `seo-geo`）。

## 重新核验的触发条件

- Lighthouse 出了新的 minor 版本（对比该分类的 `auditRefs`）。
- WebMCP 离开 origin trial（该 trial 覆盖 M149 到 M156；未宣布 ship 里程碑）。
- ARD schema pin 变更（Lighthouse 中的 `third-party/ard/README.md`）。
