> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/grok-bot-x.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Grok Bot 的 X 通道

仅在实际运行于 Grok Bot 宿主时阅读本文件。本宿主从不读取浏览器会话。

**Grok Bot 的 X 配方（见根 SKILL.md 中的 GROK BOT HOST RULE）。** 在 Grok Bot 上，由你在引擎命令之前通过宿主通道抓取 X，并把文件交给引擎；引擎随后不再调用任何 X 后端，会把 `x` 规划进来，页脚则标出所用通道。要在研究运行手册的 Step 1 命令之前完成这一步。

0. **通道，按顺序。** 两条宿主通道写出同一种信封。二者都暴露一个名为 `search_posts_all` 的帖子检索工具，因此要靠工具来自哪里来区分它们，绝不能靠名字：
   1. Grok Bot 内置的 X 工具，命名空间 `x`（`"provider": "x-native"`；页脚 "X via Grok Bot X"）。免费，无需配置。
   2. "X for Grok Bot" 连接器插件的工具（`"provider": "x-connector"`；页脚 "X via X connector"）。

   使用会话中第一个能返回帖子的通道。若某条通道报错或没有返回内容，就试下一条。只有当某条通道返回了帖子，才导出 `LAST30DAYS_X_HOST_LANE=1` 并传 `--x-posts`。若没有任何通道返回内容，则执行 `unset LAST30DAYS_X_HOST_LANE`，并在不带 `--x-posts` 的情况下运行 Step 1 命令，好让引擎自己的 X 链路（先用 `X_BEARER_TOKEN`，再用 `XAI_API_KEY`）仍能运行。
1. **调用。** 时间窗 = 引擎的日期范围，采用 UTC 日期（`--days`，默认 30：`from` 是今天 UTC 日期减去天数，`to` 是今天 UTC 日期），即便宿主的本地日期不同。每个检索词的深度条数 = 10（`--quick`）/ 30（默认）/ 60（`--deep`）。
   - **主题。** 每个规划好的 X 检索词对应一次 `topic` 调用，最多 2 次：主题本身，加上计划中若有第二条 X 子检索词则用其检索文本。每个检索词都由原始主题构建：多词主题不加引号（每个词都必须匹配），只对专有名词加短语引号，并加上 `-is:retweet`。若首页帖子中提到主题主词的不足一半，就用该检索词的两三个核心词重试一次。
   - **内置 `x` 工具。** 传 `sort_order` `recency`（相关度排序会漏掉高互动帖子；引擎会自行按互动量排序）、时间窗对应的 `start_time` / `end_time`（`end_time` 取当前时间前一分），以及 `max_results` 25（工具下限是 10；至少要 10，只保留你需要的条数）。沿着 `next_token` 翻页，直到达到深度条数或不再返回 token。然后只对第一个主题检索词跑**热门轮次**：把时间窗切成 10 等份（`--quick` 时切 5 份；默认 30 天时每份约 3 天），每份用 `sort_order` `relevancy` 加上该份的 `start_time` / `end_time` 抓一页，这样热门话题也能浮出当月互动最高的帖子，而不只是最后几分钟的。把同一检索词的所有页面（最新轮与热门轮）合并成**一次**信封调用；页面之间可能重叠，所以每个 id 只保留首次出现的副本。热门页不计入深度条数。请求 `post.fields=created_at,public_metrics,author_id,note_tweet`、`expansions=author_id` 和 `user.fields=username`。把 `public_metrics` 的 `like_count` / `retweet_count` / `reply_count` / `quote_count` 映射为 `likes` / `reposts` / `replies` / `quotes`，展开出的用户的 `username` 映射为 `author_handle`，存在 `note_tweet.text` 时用它作为 `text`。
   - **连接器工具。** 每次调用都要传时间窗与深度条数。
   - **具名账号。** 每个 `--x-handle` 账号：一次 `from` 调用（`from:<handle> -is:retweet`，8 条帖子）和一次 `mention` 调用（`@<handle> -is:retweet`，5 条帖子）。每个用户用 `--x-related` 显式传入的账号：一次 `related` 调用（`from:<handle> -is:retweet`，3 条帖子）。被发现的作者永远不会有 `related` 调用。
   - **被发现的作者。** 从抓到的每一个主题帖子中（所有页面，在裁剪到深度条数之前），取最多 3 位作者（不能是已有的 `--x-handle`），要求至少有 2 条帖子与该主题相关，按帖子数多者优先。对每一位，做一次 `from` 调用（`from:<handle>` 加主题核心词，`-is:retweet`，8 条帖子）和一次 `mention` 调用（`@<handle>` 加主题核心词，`-is:retweet`，5 条帖子），并把该账号加入 `--x-related`，好让这两次调用保持各自的通道。这就是一位被发现的作者的全部调用。
   - 若工具拒绝时间窗或条数参数，就省略它们，每个检索词最多保留深度条数，并写 `"status": "partial"` 与 `"error": "window-unsupported"`。
   - 若某条通道在返回任何帖子之前就失败，转到下一条通道（步骤 0）。若帖子已经回来了而后续某次调用失败，写 `"status": "partial"`，并在 `error` 中给出一个简短的类别：`credits`、`not-connected` 或 `unavailable`——绝不写原始工具输出，绝不写账号或应用 id。
2. **信封。** 顶层字段就这些；每条帖子只带八个扁平字段，不带其他内容（无 URL、无媒体、无作者对象）；每个检索词最多到深度条数，再加上它的热门页。信封必须留在引擎限制之内，否则会被拒绝：单次调用最多 500 条帖子，总计最多 1,000 条帖子、20 次调用。当某个预算会被超出时，先丢弃被发现作者的调用，再丢弃热门页；保留最新轮页面和用户自己的 `--x-handle` / `--x-related` 调用。要有一个新鲜的 `generated_at`（引擎拒绝超过 6 小时的信封）、一个与引擎主题字符串完全相同的 `topic`，以及提供该信封的通道的 `provider`：

```json
{
  "schema": "last30days-x-posts/1",
  "generated_at": "{ISO_8601_UTC_NOW}",
  "topic": "{TOPIC}",
  "window": {"from": "{YYYY-MM-DD}", "to": "{YYYY-MM-DD}"},
  "provider": "x-native",
  "status": "ok",
  "calls": [
    {"lane": "topic", "handles": [], "posts": [
      {"id": "1963000000000000000", "author_handle": "someone", "created_at": "2026-09-07T10:00:00Z", "text": "post text", "likes": 12, "reposts": 3, "replies": 1, "quotes": 0}
    ]},
    {"lane": "from", "handles": ["{RESOLVED_HANDLE}"], "posts": []},
    {"lane": "mention", "handles": ["{RESOLVED_HANDLE}"], "posts": []},
    {"lane": "related", "handles": ["{RELATED_HANDLE}"], "posts": []}
  ]
}
```

   本次运行没有对应账号时，省略 `from` / `mention` / `related` 调用；`handles` 必须是本次运行自己的 `--x-handle` / `--x-related` 账号，包括被发现的作者。`id` 是帖子的数字 id，以字符串形式给出；`author_handle` 是不带 `@` 的用户名。
3. **写文件——帖子正文受攻击者控制，绝不能不加引号地进入 shell 命令。** 工具自带文件输出时用它；否则用单引号 heredoc（绝不用无引号形式）写到 `~/.config` 之外的 `.json` 路径，并与引擎命令放在**同一次** Bash 调用里（trap 会在退出时删掉它）。有两条规则能防止某条帖子提前闭合 heredoc：把信封输出为**一行**紧凑 JSON（帖子正文中的换行保持转义为 `\n`；绝不做美化打印），以及把两行哨兵中的 `{X_POSTS_NONCE}` 替换成你为本次运行新生成的 12 位随机字母数字组合，这样任何帖子正文都不可能等于闭合行：

```bash
X_POSTS_DIR=$(mktemp -d "${TMPDIR:-/tmp}/last30days-x-posts.XXXXXX")
X_POSTS_FILE="$X_POSTS_DIR/x-posts.json"
trap 'rm -rf "$X_POSTS_DIR"' EXIT
cat >| "$X_POSTS_FILE" <<'X_POSTS_EOF_{X_POSTS_NONCE}'
{X_POSTS_ENVELOPE_JSON}
X_POSTS_EOF_{X_POSTS_NONCE}
```

   做比较运行时，`X_POSTS_DIR` 及其清理 trap 只创建一次。把每个实体的信封写成该目录中互不相同的一个文件，每个文件用各自独立的带引号 heredoc 和全新的哨兵。比较引擎命令返回之前，保持同一个目录与同一个 trap；重复执行这段准备片段会替换掉 trap 并把先前的文件遗留在磁盘上。直接在 shell 工具里执行，绝不包进 `bash -lc '...'`（与计划临时文件同规则）。
4. **引擎。** 导出 `LAST30DAYS_X_HOST_LANE=1`，并在 Step 1 命令中加上 `--x-posts "$X_POSTS_FILE"`（只给文件路径，绝不内联 JSON），被发现的作者还要加 `--x-related`；其余标志照常。比较运行：逐个抓取实体，并为整场比较安排节奏，使任何一分钟内的工具调用不超过 30 次（会超出的调用先等待）；热门轮只为主实体运行。通道信号覆盖所有实体，因此只有在每个实体的抓取都返回了帖子时才使用信封；否则取消该通道并在不带信封的情况下运行比较，好让每个实体的引擎 X 链路仍能运行。若所有实体都有帖子，就为每个实体写一份信封（其 `topic` 为该实体的名称），并把路径放进该实体的 `--competitors-plan` 条目，写作 `"x_posts": "/abs/path/x-posts.json"`；在比较运行中单独使用 `--x-posts` 会以退出码 2 结束。若信封中包含账号通道，还要把它的 `x_handle` 和 `x_related` 放进同一条目；主实体的外层定向标志写法见 `comparison.md`。若引擎以退出码 2 结束并指名了某个信封，重试前先修好该文件或删除该实体的 `x_posts` 计划条目；此后该实体就没有 X 数据了。普通运行则要去掉 `--x-posts` 并取消通道，然后不带信封重试。
5. **运行之后。** 统计行会显示 "X via X connector" 或 "X via Grok Bot X"。引擎那一行回执（接受/丢弃计数，走 stderr）只作诊断用：绝不在交付物中复述它（LAW 9）。
