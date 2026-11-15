> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/routing.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 命令指引

## 工作流问题

给建议，不执行命令；下面的菜单只用于裸调用。按需查阅相关命令的参考文件了解前置条件与范围。更完整的工作流指引链接到 [docs](https://impeccable.style/docs/)。用户同时要求执行时，照办那个请求。

## 无参数路由：情境感知菜单

用户不带参数调用 `/impeccable` 时读本节。他们在问"我该做什么？"。让菜单感知情境，而不是静态列表。

安装阶段已经运行过 `impeccable context`。如果它报告 `NO_PRODUCT_MD`，说明项目还没有抓取过上下文：菜单以 `/impeccable init` 作为首位推荐（附一行原因），下方仍列出其余项；不要悄悄直接进 init。否则运行一次 `.claude/skills/impeccable/scripts/impeccable signals` 并读取其 JSON，然后以 **2-3 个价值最高的下一步命令**领头，每个附一条从信号里取来的一行理由，其后是完整菜单（SKILL.md 的 Commands 表，按类别分组）。**绝不自动运行命令；推荐只是等用户确认的建议。**

对信号做推理；没有要服从的分数：

- `setup.hasDesign` 为 false 而 `setup.hasCode` 为 true → `document`（抓取视觉体系）。
- `critique.latest` 为 `null` → 项目从未被批评过；对一个已完成安装且有真实界面的项目，主动提供 `/impeccable critique <surface>` 是强默认。
- `critique.latest` 的 `score` 偏低或 `p0` / `p1` 非零 → `polish`（它把那份快照当作待办清单，过期或清零后关闭）。
- `git.changedFiles` 指向单一界面 → 把 `audit` 或 `polish` 明确限定到那些文件，并点名它们。
- `devServer.running` 为 true → `live` 可用于浏览器内迭代，`generate` 可对指定元素做一次性变体运行；为 false 时两者都不作为推荐。**`live`、`generate` 和随包的 `impeccable detect` 仅限 web。**`setup.platform` 是 `ios`、`android` 或 `adaptive` 时，任何一项都不作为推荐；浏览器叠加层与 HTML 规则引擎不适用于原生应用代码。
- 其余情况按意图分组（构建新东西 / 改进已有 / 视觉迭代），结合当前界面与 `setup.platform` 调整。

**`scan.targets` 非空且 `setup.platform` 不是 `ios`/`android`/`adaptive` 时，运行一次 `.claude/skills/impeccable/scripts/impeccable detect --json <scan.targets joined by spaces>`**（随包检测器扫本地文件：无网络、无 npx；它读 HTML/CSS，原生项目跳过）。`scan.via` 说明这些文件是什么：`git-changes`（脏工作区里的标记/样式文件，最相关的一组）、`source-dir`（如 `src`、`app`）、`html` 或 `root`。把命中并进你的推荐：大量质量/对比度命中 → `audit` 或 `polish`；某个具体的 AI 腔家族 → 对应命令（渐变文字或 eyebrow → `quieter` / `typeset`，扁平或灰色色板 → `colorize`，依此类推）。这是真实、当下的信号，胜过猜测。detect 报错或文件树又大又慢时跳过它，让用户自己运行 `audit`；绝不让推荐阻塞在这上面。

控制在 2-3 条有锋芒的推荐，附上要敲的确切命令。菜单仍是兜底；推荐才是主角。
