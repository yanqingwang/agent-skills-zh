> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/library-queue.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 资料库、订阅源与话题队列

在设置或全新研究之前，遇到 library/feed/queue 意图就阅读本文件。运行时解释器引导仍然先执行。这些快速路径跳过话题/后端预检、设置与来源研究。

**LIBRARY 搜索快速路径 — 它覆盖下面每一个研究/设置步骤。** 如果用户说“在我的资料库里搜 X”“我以前研究过 X 吗”，或以其他方式要求查询此前保存的研究，不要运行 WebSearch、设置、话题/后端预检或全新来源研究。运行：

```bash
"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" library search "${LIBRARY_QUERY}" --save-dir="${LAST30DAYS_MEMORY_DIR}"
```

转达带日期、按话题分组的匹配结果。这是在既有已保存简报扫描器加上每次运行的 SQLite 存储记录之上的确定性离线 FTS；它不调用模型，也不访问网络。如果 SQLite 缺少 FTS5，转达引擎给出的能力错误，不要落到全新研究。

**LIBRARY 订阅源快速路径 — 它覆盖下面每一个研究/设置步骤。** 如果用户要求构建、查看、刷新或订阅其已保存的研究资料库/订阅源，不要运行宿主 WebSearch 解析、首次运行设置闸门、话题预检或来源研究。运行：

```bash
"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" library feed --save-dir="${LAST30DAYS_MEMORY_DIR}"
```

转达生成的本地 `index.html` 与 `feed.xml` 路径。如果用户明确要求发布/分享整个资料库，先说明 `ht-ml.app` 页面默认公开，可能被抓取或索引，然后按既有的公开或密码保护发布选项执行。获得同意后加上 `--publish`；需要密码保护时，通过 `LAST30DAYS_PUBLISH_PASSWORD` 提供其唯一的共享密码，绝不作为可见的命令行参数传入。转达打印出的资料库 URL 与本地 Atom 路径，并说明当输出目录托管在 GitHub Pages 这类静态主机上时，`feed.xml` 就变得可订阅。绝不把 `ht-ml.app` 资料库 URL 描述为 Atom 订阅地址，也绝不因为用户要求生成或打开本地订阅源就加上 `--publish`。

**话题队列快速路径 — 它覆盖下面每一个研究/设置步骤。** 如果用户问“我的话题队列里有什么”“我接下来该聊什么”“哪些话题我还没覆盖”“展示我的内容管线”“把 <topic> 标记为已覆盖”“我在播客里讲了 X”“我们发布了那篇文章”，或类似说法 — 即使是冷启动、本会话此前没有任何研究运行 — 不要运行 WebSearch、设置、话题/后端预检或全新来源研究。运行只读形式：

```bash
"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" queue list --save-dir="${LAST30DAYS_MEMORY_DIR}"
```

或用于“把 X 标记为已覆盖”这类说法的标记形式：

```bash
"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" queue cover "<topic name>" --save-dir="${LAST30DAYS_MEMORY_DIR}"
```

转达渲染出的列表（未覆盖的浮现话题，附领域、浮现次数与最后浮现日期），或标记完成的确认。这是在该保存目录的 `research.db` 之上做的确定性离线 SQLite 操作；它不调用模型，也不访问网络。标记覆盖需要精确的队列话题名；名称未知时引擎以退出码 2 退出并指向 `queue list`，转达该信息，运行 `queue list`，然后给出队列中的名称，而不是用猜测重试。空队列是合法答案，建议运行 `/last30days trending` 或领域发现来填充它。不要把话题名或短语当作全新研究话题，也不要落到根文件的“已提供话题”分支。
