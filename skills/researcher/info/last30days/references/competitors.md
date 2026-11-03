> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/competitors.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 竞品研究

选择竞品模式时阅读本文件。根文档还要求配合 `comparison.md`；各实体自身的定向与计划要保留。

### 竞品模式（`--competitors`）

`--competitors` 是 SKILL.md 级别的快捷方式，等同于带自动发现的 vs 模式。当宿主提供 web 搜索时，由你（承载本次运行的推理模型）完成发现与 Step 0.55，然后调用 `comparison.md` 中的 web 搜索 vs 主题路径。

**有宿主 web 搜索时，使用四步协议：**
1. 通过 WebSearch **发现同类对象**，在研究运行手册规定的引擎前隔离式 web 搜索派发中进行：`"{topic} competitors"` / `"{topic} alternatives"`。默认取 N=2（与该标志的默认值一致）；若用户传入 `--competitors=N`，则 N 取参数值。
2. **对主主题和每个同类对象都执行 Step 0.55**：与单个实体主题用的是同一套协议，只是要跑 N 次。X 账号、子版块、GitHub、新闻背景，逐实体处理。
3. **构造 vs 主题字符串**：`"{main} vs {peer1} vs {peer2}"`。
4. **调用引擎**，传入 vs 主题和一份覆盖两个同类对象的 JSON 编码 `--competitors-plan` 文件，外加为捕获主主题而定向的 `--x-handle`/`--subreddits`/`--github-*` 值，并以带引号的 shell 数据形式传入。主主题的计划条目不会覆盖这些外层定向标志。逐实体的 `x_posts` 信封条目是唯一的例外，主实体同样适用。

**没有宿主 web 搜索时：** 若用户点名了同类对象，使用 `comparison.md` 中的无 web 搜索比较命令。对于只写 `--competitors` 的请求，使用研究运行手册中带引号的 `RESEARCH_TOPIC` heredoc，并在其引擎命令后追加 `--competitors=N --auto-resolve`，让引擎通过已配置的搜索后端发现同类对象。用户未指定数量时用 `N=2`。若引擎报告同类对象发现不可用，请让用户点名同类对象；不要凭空编造，也不要声称是无密钥的通用 web 兜底发现了竞品。适用根文档的无 web 搜索规则：跳过宿主 Step 0.55 与 0.75，且不要传宿主的 `--plan`。

**标志接口（引擎）：**
- `--competitors`（裸标志）：告知宿主模型去发现 2 个同类对象（共 3 方）。
- `--competitors=N`：N 个同类对象（1..6；超出范围会被收敛并向 stderr 输出警告）。
- `--competitors-list="A,B,C"`：最小逃生口；只给名称，没有逐实体定向。同类对象的子运行回退到规划器默认值（数据肉眼可见地更稀薄）。
- `--competitors-plan <JSON file path>`：完整的逐实体定向；隐含 vs 模式；宿主有 web 搜索时优先使用。请套用 `comparison.md` 里的带引号 heredoc 文件配方。
- `--polymarket-keywords "kw1,kw2"`：为含义模糊的单 token 主题消歧（"Warriors" → `nba,gsw,golden-state`）。
- `--hiring-signals`：深挖公开职位/招聘页证据，寻找公司的战略重心信号。只用信号式表述：正在倾斜、加码投入、关注度提升、优先级转移。不要根据职位发布信息断言确切的路线图预测。

**在有 web 搜索的宿主上为何优先 --competitors-plan 而不是 --competitors-list：** 没有逐实体的账号/子版块时，同类对象的子运行可能产出肉眼可见地比主主题更稀薄的证据。stdout 中的 Resolved Entities 块会把这个差距暴露出来。在有 web 搜索的宿主上出现短横线，说明 Step 0.55 还需要再跑一轮；在没有 web 搜索的宿主上出现短横线，则可能是没有配置解析器。

**引擎内置的 auto-resolve：** 若引擎检测到 BRAVE_API_KEY / EXA_API_KEY / SERPER_API_KEY / PARALLEL_API_KEY，它会在每次子运行前自行执行逐实体的 `resolve.auto_resolve()`。有 web 搜索的宿主模型为自己的 Step 0.55 并不需要这些密钥；没有 web 搜索的宿主以及无头 cron/CI 运行则依赖这一引擎兜底。

OpenRouter 与 Perplexity 的凭据不会启用引擎的 auto-resolve 或同类对象发现。它们付费的 Perplexity 源仍是单独的选项。没有受支持的搜索 API 密钥时，请使用宿主 web 搜索或提供点名的同类对象；引擎的无密钥通用 web 兜底不支持自动发现同类对象。

**输出：** 对 Markdown/compact 运行，在 `--save-dir` 中为每个实体生成一个 `{slug}-raw.md`，并在 stdout 上输出合并后的比较结果。对 HTML 运行，主保存产物是合并比较 HTML，同类对象产物仍按实体分开。始终以 `[last30days] Comparison artifact set: main=...; peers=...` 这行日志为事实来源。综合规范与 `comparison.md` 中的 vs 模式协议一致。
