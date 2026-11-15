> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/setup-wizard.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 首次运行设置与来源修复

根级设置门禁或修复门禁任一适用时阅读。首次运行设置按下方 Step 0 执行。初始引导完成后，恢复原本请求的路径，包括发现（discovery）；不要用普通主题研究替换它。

**修复入口（包括 `SETUP_COMPLETE=true` 时）：** 用户请求修复或医生给出宿主专属处方时，直接进入下方适用的 **Manual Setup Guide** 子节。跳过 Step 0 及其欢迎语、各项提议、来源档位提示和主题选择器。Manual Setup Guide 的完成尾段只适用于初始引导：修复期间不写 `SETUP_COMPLETE=true`，除非研究本身被请求，也不启动研究。完成获准的修复或修复指引后，回到原始请求。

只执行获准的修复。阅读本指南或医生处方不授权安装、启动浏览器、读取 cookie 或写配置。浏览器访问需要明确的浏览器 cookie 同意。既有授权仍然有效；拒绝、跳过或不回答都不是同意。`LAST30DAYS_HOST=grok-bot` 宿主上，X 只用 **X on a Grok Bot (repair)**；绝不读取浏览器会话，也不用 Linux / Mac mini 修复。保留适用子节中的 MacBook 例外、人工登录交接和封锁/验证挑战/限流停止规则。

## Step 0: 首次运行设置向导

**关键：始终在 Step 1（研究运行手册中的主题研究）之前执行 Step 0，即使用户已给出主题。** 用户输入 `/last30days Mercer Island` 时，处理首次运行选择的同时保留该主题。向导可能询问浏览器 cookie 同意，但拒绝或跳过 X 绝不能阻断被请求的研究。

**研究继续覆盖规则（优先于下方所有可选引导步骤）：** 调用已包含主题、且用户在 Auto setup 中拒绝 X/浏览器 cookie 访问时，走无 cookie 设置路径，然后用可用来源立即研究该主题。用户选择 Skip for now 时，标记设置完成并立即研究，不运行设置。两种情况下，都在完成有用的研究响应之后才处理 ScrapeCreators 提议、来源档位提示、重试提示和首主题选择器。同一次运行不要再问任何 X 问题。发现输出之后，把 X 作为可选缺失来源报告一次，不做解锁推销，**然后在同一次运行中恢复被推迟的引导：呈现 Step 4 的 ScrapeCreators 提议，若保存了 key 再呈现 Step 5 的来源开启。** 推迟不等于放弃：`SETUP_COMPLETE=true` 已写入，后续调用会完全跳过 Step 0，本次运行是发出提议的唯一机会。首主题选择器保持跳过（已提供主题），恢复过程绝不重新询问 X/浏览器 cookie 同意。浏览器 cookie 读取仍需明确同意；跳过或不回答绝不是同意。

**你是对话驱动者。** Python 设置脚本只做机械工作（读 cookie、装工具、GitHub 设备授权流程），它无法向用户提问，因为它以非交互子进程运行。所以同意发生在聊天里：你问，用户答，你按答案决定是否调用每个子进程。不要只跑 `setup` 然后报告结果：那是本节要防止的静默引导回归。

**首次运行检测（静默，不跑命令，不向用户输出）：**
- 进程环境、项目配置（`.claude/last30days.env`）、全局配置（`~/.config/last30days/.env`）中有 `SETUP_COMPLETE=true`，或设置检查报告已有配置凭证时，完全跳过 Step 0，回到根分发处理原始请求（主题研究对应研究运行手册的 Parse User Intent）。不要宣告"设置已完成"。用户不需要每次运行都收到状态消息。
- 不要仅凭 `~/.config/last30days/.env` 不存在就判定为首次运行。凭证可能存在于进程环境、项目配置、macOS 钥匙串（`last30days-<KEY>`）、pass(1) 或宿主提供的认证。
- 凭 key 是否存在和设置状态判断首次运行，不要靠转储文件。不要打印 `.env` 内容或凭证值。
- `--preflight` 是自愿开启的检查器（展示本次运行会读什么写什么，忽略项目配置）。不要把它作为必需的首次运行步骤。
- 没有设置标记也没有凭证来源时，这就是首次运行。

**模态框要求：** 保留引导式流程：欢迎 → Auto/Manual/Skip → cookie 同意 → ScrapeCreators 提议 → 来源开启 → 首主题选择器。不要用静默设置或纯散文引导替换模态框流程。

**平台分派：只运行其中一个分支：**
- **有 WebSearch 和 AskUserQuestion（Claude Code）时：** 运行紧随其后的 **Claude Code 模态框流程**。
- **没有时（OpenClaw、Codex、Cursor、Gemini CLI、raw CLI）：** 运行下方的 **非模态散文流程**。它以对话方式完成同样的工作，不用模态框。
- **以 Grok Bot 运行时**（根 SKILL.md 的 GROK BOT HOST RULE）：运行第三个分支 **Grok Bot 散文流程**，位于非模态流程之后。Bot 自带的 X 工具优先，任何备用 key 只经引擎写入，不读取浏览器会话。Cursor 留在非模态散文流程。

---

### Claude Code 模态框流程

**除非研究继续覆盖规则把待研主题直接送入研究，否则严格按序执行。** 正常序列：(1) 欢迎（内置于设置模态框）→ (2) 设置模态框 → (3) 如选择则运行设置 → (4) ScrapeCreators 提议模态框 → (5) 来源开启模态框 → (6) 首主题选择器。从第 1 步开始。

**Step 1 - 欢迎。** 欢迎语放在 Step 2 设置模态框内部，不作为单独消息。Claude Code 会把 Bash/工具输出折叠在 "ctrl+o to expand" 之后，单独的欢迎消息或单独的 `--welcome` 命令运行会被埋没，用户根本看不到。AskUserQuestion 模态框是唯一始终完全可见的界面，所以欢迎语放进它的问题文本。本模态框流程中不要单独运行 `--welcome` 命令，也不要在模态框之前把欢迎语打印成聊天消息；直接进 Step 2。（`--welcome` 仍为下方非模态散文流程保留，那里没有模态框。）

**Step 2 - 欢迎 + 设置选择（一个模态框）。** 用一字不差的这个问题和这些选项调用 AskUserQuestion。逐字复现问题，包括开头几行的欢迎语：

问题：
"欢迎来到 /last30days！我会跨 Reddit、X、YouTube、TikTok、Digg、arXiv、Techmeme、HN、Polymarket 等平台研究任何主题，提取人们最近 30 天的真实发言。

你想如何设置？"

选项：
- "Auto setup（约 30 秒）" - 描述："扫描浏览器 cookie 获取 X，并安装 yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance。Reddit/HN/Polymarket/GitHub/Web 开箱即用。之后可经 ScrapeCreators 添加 TikTok + Instagram（1 万次免费调用）。"
- "Manual setup（手动设置）" - 描述："逐项展示需要手工配置的来源和凭证。"
- "Skip for now（暂且跳过）" - 描述："只用免费免设置的来源：Reddit（含评论）、HN、Polymarket、GitHub、Web。"

**Step 3 - 按选择运行设置。**

**用户选 Skip for now 时：** 把 `SETUP_COMPLETE=true` 和 `BROWSER_CONSENT=false` 写入 `~/.config/last30days/.env`（保留其他键，替换已有的同意标记，文件不存在则以 `0600` 权限创建），向导就不会在后续每次运行重新触发，且后续运行保持禁用浏览器读取。不要运行任何 `setup` 命令：常开来源（Reddit、HN、Polymarket、GitHub、Web）无需设置。调用已含主题时立即研究，然后在发现之后于同一次运行恢复 Step 4（若保存了 key 还有 Step 5）；Step 6 保持跳过，因为主题已提供。否则进入 Step 6。

**用户选 Auto setup 时：**

先取得 cookie 同意。检查 `~/.config/last30days/.env` 中是否已有 `BROWSER_CONSENT=true`；有就跳过同意提问，直接运行 `setup --allow-browser-cookies`。否则**调用 AskUserQuestion：**
问题："自动设置无论如何都会安装免费 CLI：yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance。现在以及今后的研究运行中，可以读取你浏览器的 x.com cookie（用于 X/Twitter 和其他登录来源）吗？macOS 上我先检查 Chrome 和其他 Chromium 浏览器，然后是 Firefox 和 Safari。Windows 和 Linux 上我用 Firefox，WSL 下以 Windows Firefox 兜底。你已有的浏览器选择优先。设置只记住成功的浏览器名，绝不保存 cookie 值。macOS 钥匙串在后续运行中可能再次弹窗；想持续授权 OS 访问就选"始终允许"。在 ~/.config/last30days/.env 中设置 BROWSER_CONSENT=false 或 FROM_BROWSER=off 可停止原生、CDP 和 sidecar 读取。要包含 X 吗？"
选项（每个选项附上下列描述）：
- "是 - X cookie + 全部 CLI" - 描述："读取 x.com cookie 用于 X/Twitter 检索，并安装 yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance。" 运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --allow-browser-cookies`。引擎保存 `BROWSER_CONSENT=true`；不要追加重复标记。
- "跳过 X - 只装 CLI" - 描述："不读 cookie。仍安装 yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance。" 运行 `FROM_BROWSER=off "${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup`。引擎保存 `BROWSER_CONSENT=false`，该拒绝在后续运行同样生效。调用已含主题时，立即用 `--no-browser-cookies` 研究该主题，然后在发现之后于同一次运行恢复 Step 4（若保存了 key 还有 Step 5）；Step 6 保持跳过，因为主题已提供。
- "改用 X 的 xAI API key" - 描述："用 api.x.ai 的 key 做 X 检索（不读 cookie），并安装 yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance。" 让用户粘贴，把 `XAI_API_KEY` 写入 `.env`，再运行 `FROM_BROWSER=off "${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup`。

**Grok CLI 是自愿开启的备选，不是设置时的推荐项。** 设置期间不要先检查 grok，也不要把它作为首选选项提供。残留的 `~/.grok/auth.json` 绝不能抢占 X 通道。用户提到有 Grok 账号时告诉他们："运行 `grok login` 后，在 `.env` 中固定 `LAST30DAYS_X_BACKEND=grok` 即可使用 Grok CLI。这是自愿开启项：残留的 grok 登录不应自动接管 X。" 不要说它免费：它需要 Grok 套餐。

获准的 `setup --allow-browser-cookies` 运行按提示中解释的平台顺序提取 cookie。除非已配置 `FROM_BROWSER`，设置会把提供了完整 cookie 的浏览器保存为逗号分隔的 `FROM_BROWSER` 列表，包括 Chromium 浏览器。它把 Windows Firefox 的 `firefox-wsl` 来源标签规范化为 `firefox`。它绝不保存 cookie 值。后续研究再次读取这些浏览器会话；macOS 钥匙串可能再次提示。`BROWSER_CONSENT=false` 或 `FROM_BROWSER=off` 会禁用原生、CDP 和 sidecar 读取。之后一次获准的设置会替换已保存的拒绝，但显式的 `FROM_BROWSER=off` 在修改前始终阻止读取。`AGENTCOOKIE=off` 只禁用 sidecar；`on` 不能推翻拒绝。

设置还会尽力安装 yt-dlp（YouTube）、免费无 key 的 Digg CLI（`digg-pp-cli`，经 `@mvanhorn/printing-press-library install digg --cli-only`；仅在 **agent 子进程 PATH** 上时激活，通常为 `$HOME/.local/bin`；不在 PATH 上时如实报告；`npx` 不可用时仅推荐），以及免费无 key 的 arXiv、Techmeme、Yahoo Finance CLI。向用户展示找到并安装了什么，包括每个 CLI 是落在 PATH 上（已激活）还是 PATH 外（已安装但未激活）。

**Extras 宿主的 X 登录（Linux / Mac mini / Darwin agentcookie sink。MacBook 跳过此步，`LAST30DAYS_HOST=grok-bot` 宿主也跳过，从不运行）。** MacBook 上，只要 OS 允许读取浏览器数据，上文 Keychain/Firefox/Safari 提取即可服务 X。extras 宿主上本地 Chrome 存储无法解密，该提取一无所获，X 保持为空，除非你再经 CDP 捕获一次实时登录。cookie 同意的设置运行之后：运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/box_chrome_login.py"`，它会打印确切的宿主正确命令（或用 `--exec` 直接启动），在 MacBook 上它打印 "no launch needed" 且不启动任何东西。`box-chrome` 在 PATH 上时，它在 last30days extras 端口 **18800**（last30days 约定 `SAND_CHROME_REMOTE_DEBUG_PORT=18800`，不是 box-chrome 默认值）上启动一次性配置档案：`CHROME_USER_DATA_DIR=/tmp/last30days-x-chrome SAND_CHROME_REMOTE_DEBUG_PORT=18800 box-chrome --new-window https://x.com/login`。等 x.com 登录页出现后，把桌面交给真人输入：绝不要代填或驱动表单。他们登录后，向 `.env` 追加 `BROWSER_CDP_URL=http://127.0.0.1:18800`（绝不写 `AUTH_TOKEN`/`CT0`；采集期间保持 `AGENTCOOKIE=off`），然后重跑 `setup --allow-browser-cookies`，extras CDP 即可读取实时 cookie 对。完整步骤和封锁/限流停止规则见下方 **X on Linux / Mac mini**。这个 extras 宿主登录只在获准的 "是 - X cookie" 路径上运行；用户对 X 说了 yes 时，研究继续覆盖规则也不会跳过它。

**macOS 浏览器数据权限补救。** 获准的 `setup` 之后，stderr 显示 `X cookie access was permission denied` 时点出浏览器名；显示 `Permission denied reading Cookies.binarycookies` 时点出 Safari。建议：`检查"系统设置 > 隐私与安全性"中终端或 agent 应用的权限。"完全磁盘访问"（Full Disk Access）可能有帮助，但未必能解锁其他应用的数据。你可以手动提供 AUTH_TOKEN 和 CT0，或改用 XAI_API_KEY。` 没有待研主题时才提供一次重试；否则用可用来源继续。

**Step 4: ScrapeCreators 提议（每次首次运行都展示，除非研究继续覆盖规则已让待研主题开工）。** 先以纯文本展示，再弹模态框：

ScrapeCreators 增加 TikTok/Instagram 帖子和热评，外加 YouTube 评论。key 附赠 1 万次免费调用（之后按量付费，无需绑卡、无抽成），并把额度花在：免费 Reddit 检索结果少于 5 条时的 Reddit 检索、YouTube 检索不足 3 个 yt-dlp 视频时的搜索，以及 YouTube 字幕抢救。设 `LAST30DAYS_REDDIT_SC_MIN_ITEMS=0` 或 `LAST30DAYS_YT_SC_MIN_ITEMS=0` 可把搜索兜底改为"仅空结果时"。每次 YouTube 回填可抓字幕；重试可能再次扣费。Reddit 评论经 shreddit 仍然免费。

模态框之前，用 Bash 静默运行 `which gh`；存为 gh_available。

**调用 AskUserQuestion：**
问题："要添加 TikTok 和 Instagram 吗？key 还会把额度花在少于 5 条的 Reddit 检索、少于 3 个的 YouTube 检索和字幕抢救上。设 LAST30DAYS_YT_SC_MIN_ITEMS=0 可让 YouTube 检索仅在空结果时兜底。"
选项：
- "经 GitHub 开通 ScrapeCreators（推荐：免费调用最多）" - 描述："打开 GitHub，代码自动复制到你的剪贴板，你只需粘贴（Cmd+V），约 20-30 秒。授予全部 1 万次免费调用，多于网页注册。"（推荐它而非网页选项，因为 GitHub 路径免费调用更多。）这是**双命令流程**：`--github-start` 快速返回代码（前台），然后 `--github-poll` 等你授权。代码会出现在命令输出里，不会错过：
   1. **在前台运行 `--github-start`**（约 1-2 秒返回，不会阻塞轮询）：`"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --github-start`。它提交设备授权流程、复制代码到剪贴板、打开浏览器，并在 stdout 返回一个 JSON 块和一行纯文本 `Your GitHub code: XXXX-XXXX`。
      - 返回 `status == "already_registered"`（已保存过 key）时：告诉用户"你已设置完成：现有的 ScrapeCreators key 已生效"，然后停止（不要运行 poll）。
      - `status == "error"` 时：展示消息并提供下方的网页选项。
   2. **展示代码。** 从输出读 `user_code`，输出一条聊天消息："在 GitHub 页面输入这个代码：**XXXX-XXXX**，它已在你的剪贴板上，直接粘贴（Cmd+V）并点 Continue。"（输出说剪贴板复制失败时，让他们手动输入。）代码就在第 1 步的输出里，把它亮出来正是要点。
   3. **运行 `--github-poll`**（后台、5 分钟超时；或前台）：`"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --github-poll`。解析其 stdout 的**最后一条** JSON 行得到最终状态：
      - `status == "success"`：引擎已持久化 key（`"persisted": true`，`api_key` 已脱敏，绝不回显）；确认"你已开通！1 万次免费调用。TikTok/Instagram、少于 5 条的 Reddit 检索、少于 3 个的 YouTube 检索、字幕抢救均已生效。LAST30DAYS_YT_SC_MIN_ITEMS=0 让 YouTube 检索仅在空结果时兜底。"
      - `status == "success"` 但 `"persisted": false`（key 写入失败）：不要声称来源已生效。告诉用户注册成功但保存 key 失败，让他们手动把 `SCRAPECREATORS_API_KEY=<key>` 加进 `~/.config/last30days/.env`。
      - `status == "error"` 且 `message == "Authorized but failed to fetch API key"`（精确匹配；常伴随 `"reason": "no_api_key"`）：GitHub 授权成功，不要说授权失败。这通常意味着你的 GitHub 已关联 ScrapeCreators 账号。告诉用户："GitHub 已授权，但我没能自动取到你的 ScrapeCreators key：你的 GitHub 可能已关联账号。到 scrapecreators.com 拿 key 粘贴到这里，或跳过。" 然后接受粘贴的 key（写 `SCRAPECREATORS_API_KEY` 到 `.env`）或提供网页/跳过选项。
      - `status == "error"` 且 `message` 含 `ScrapeCreators profile failed`（或 `"reason": "upstream_error"`）：GitHub 授权成功，不要说授权失败，也**不要**说 GitHub 已关联账号。ScrapeCreators 在授权后返回了服务器错误。告诉用户："GitHub 已授权，但 ScrapeCreators 铸造 key 时发生服务器错误：是他们那边的问题，不是你的。到 scrapecreators.com 注册或登录，在那里拿 key 粘贴，或跳过/稍后重试。" 接受粘贴的 key 或提供网页/跳过选项。不要暗示他们已有可用的关联账号。
      - `status == "timeout"` 或任何其他 `status == "error"` 消息：展示"GitHub 授权没有完成。没关系，到 scrapecreators.com 注册，或稍后再试。"，然后提供下方网页选项。
   - **单命令兜底：** 偏好单次调用的宿主仍可前台运行 `setup --github`（串起 start+poll）；先告诉用户剪贴板会出现一个代码供粘贴。
- "打开 scrapecreators.com（Google 登录）" - 经 Bash 运行 `open https://scrapecreators.com`，然后让他们粘贴 API key。把 `SCRAPECREATORS_API_KEY={key}` 写入 `~/.config/last30days/.env`。
- "我已有 key" - 接受 key，写入 `.env`。
- "暂且跳过" - 不用 ScrapeCreators 继续。TikTok/Instagram、付费 Reddit/YouTube 回填和字幕抢救保持关闭；免费来源和 Reddit 评论仍可用。

**Step 5: 来源开启（仅在保存了 ScrapeCreators key 时，跳过则不弹）。** 评论是默认开启，绝不是可选项：没有"只发帖"档位。先纯文本后模态框：

key 已配置。默认开启：TikTok + Instagram（帖子加热评）和 YouTube 评论。Reddit 检索走免费无 key 路径（结果少于 5 条时由 ScrapeCreators 回填）；Reddit 评论经 shreddit 保持免费。要撒最大的网吗？

**调用 AskUserQuestion：**
问题："要开启哪些 ScrapeCreators 来源？"
选项：
- "TikTok + Instagram + 全部评论（推荐）" - 默认：TikTok + Instagram 的帖子和热评（按票数排序），外加 YouTube 评论。向 `~/.config/last30days/.env` 追加 `INCLUDE_SOURCES=tiktok,instagram,youtube_comments,tiktok_comments,instagram_comments`（列表必须包含 `tiktok,instagram`，否则它们会被当作排除项）。确认："TikTok、Instagram 和 YouTube/TikTok/Instagram 热评已开启。"
- "全部（另含 Threads + Pinterest）" - 上述全部外加 Threads 和 Pinterest 检索。覆盖最广，扣费最多。追加 `INCLUDE_SOURCES=tiktok,instagram,youtube_comments,tiktok_comments,instagram_comments,threads,pinterest`。确认："全部开启：TikTok/Instagram/YouTube 的帖子加评论，外加 Threads 和 Pinterest。"

**Step 6: 首主题选择器。** `SETUP_COMPLETE=true` 写入后，**调用 AskUserQuestion：**
问题："你想先研究什么？"
选项：
- "Claude Code vs Codex"：技术对比
- "Sam Altman"：新闻人物
- "Warriors Basketball"：体育
- "AI Legal Prompting Techniques"：细分/专业领域
- "自己输入主题"

用户选了示例就用它运行研究。选"自己输入"就问他们想研究什么。**用户在命令中已提供主题（如 `/last30days Mercer Island`）时，跳过本选择器，直接使用其主题。**

**首次运行向导到此结束。** 模态框流程中的一切只在首次运行。`SETUP_COMPLETE=true` 存在时全部跳过：没有欢迎、没有模态框、没有主题选择器，直接进入研究（Parse User Intent）。

**用户在 Step 2 选了 Manual setup 时，** 走下方 **Manual Setup Guide** 而非 Auto 分支（该指南自己会写 `SETUP_COMPLETE=true`），然后继续 Step 6。

---

### 非模态散文流程

适用于没有交互模态框的宿主（OpenClaw、Codex、Cursor、Gemini CLI、raw CLI）。同样的工作，以对话完成。按序执行；要求等待处就等待。

**1. 欢迎。** 运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" --welcome`，把 stdout **原样**展示给用户（不要摘要或重排）。欢迎语归引擎所有，各处渲染一致。

**2. Cookie 同意（读取任何东西之前先问）。** 先检查 `~/.config/last30days/.env` 中是否已有 `BROWSER_CONSENT=true`（例如之前 Claude Code 会话里授过）；有就跳过本提问，直接运行 `setup --allow-browser-cookies`。否则发问。示例："现在以及今后的研究运行中，可以读取你浏览器的 cookie（用于 X/Twitter 和其他登录来源）吗？macOS 上我先检查 Chrome 和其他 Chromium 浏览器，然后是 Firefox 和 Safari。Windows 和 Linux 上我用 Firefox，WSL 下以 Windows Firefox 兜底。你已有的浏览器选择优先。设置只记住成功的浏览器名，绝不保存 cookie 值。macOS 钥匙串在后续运行中可能再次弹窗；想持续授权 OS 访问就选"始终允许"。在 ~/.config/last30days/.env 中设置 BROWSER_CONSENT=false 或 FROM_BROWSER=off 可停止原生、CDP 和 sidecar 读取。(yes / no)" **等待回答。**
   - 回答 **yes** → 运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --allow-browser-cookies`（引擎保存 `BROWSER_CONSENT=true`；不要追加重复标记）。除非已配置 `FROM_BROWSER`，设置会把提供了完整 cookie 的浏览器保存为逗号分隔的 `FROM_BROWSER` 列表，包括 Chromium 浏览器。它把 Windows Firefox 的 `firefox-wsl` 来源标签规范化为 `firefox`。它绝不保存 cookie 值。后续研究再次读取这些浏览器会话；macOS 钥匙串可能再次提示。`BROWSER_CONSENT=false` 或 `FROM_BROWSER=off` 会禁用原生、CDP 和 sidecar 读取。之后一次获准的设置会替换已保存的拒绝，但显式的 `FROM_BROWSER=off` 在修改前始终阻止读取。`AGENTCOOKIE=off` 只禁用 sidecar；`on` 不能推翻拒绝。设置还会尽力安装 yt-dlp（YouTube）、免费无 key 的 Digg CLI（`digg-pp-cli`，经 `@mvanhorn/printing-press-library install digg --cli-only`；仅在 agent 子进程 PATH 上时激活，通常为 `$HOME/.local/bin`；不在 PATH 上时如实报告；`npx` 不可用时仅推荐），以及免费无 key 的 arXiv、Techmeme、Yahoo Finance CLI。
     - **Extras 宿主（Linux / Mac mini / Darwin agentcookie sink）。MacBook 跳过此步，`LAST30DAYS_HOST=grok-bot` 宿主也跳过。** 这些宿主上 Chrome cookie 存储无法解密，上文提取一无所获，X 保持为空，除非你经 CDP 捕获一次实时登录。运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/box_chrome_login.py"`（打印宿主正确命令；`--exec` 直接启动；MacBook 上打印 "no launch needed" 且不启动任何东西）。`box-chrome` 在 PATH 上时，它在 last30days extras 端口 **18800**（`SAND_CHROME_REMOTE_DEBUG_PORT=18800`，不是 box-chrome 默认值）上启动一次性配置档案：`CHROME_USER_DATA_DIR=/tmp/last30days-x-chrome SAND_CHROME_REMOTE_DEBUG_PORT=18800 box-chrome --new-window https://x.com/login`。等 x.com 登录页出现后，把桌面交给真人输入：绝不要驱动表单。他们登录后，向 `.env` 追加 `BROWSER_CDP_URL=http://127.0.0.1:18800`（绝不写 `AUTH_TOKEN`/`CT0`；采集期间保持 `AGENTCOOKIE=off`），再重跑 `setup --allow-browser-cookies`。完整步骤和封锁/限流停止规则见下方 **X on Linux / Mac mini**。这个 extras 宿主登录只在获准的 **yes** 路径上运行；用户对 X 说了 yes 时，待研主题也不会跳过它。
   - 回答 **no** → 运行 `FROM_BROWSER=off "${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup`。跳过所有 cookie 读取；仍安装 yt-dlp（YouTube）、Digg、arXiv、Techmeme、Yahoo Finance，仍写入 `SETUP_COMPLETE`。引擎保存 `BROWSER_CONSENT=false`，后续运行同样跳过原生、CDP 和 sidecar 读取。调用已含主题时，立即用 `--no-browser-cookies` 研究该主题，然后在发现之后于同一次运行恢复被推迟的引导：ScrapeCreators 提议（第 4 步），以及保存了 key 时的来源档位（第 4b 步）。恢复过程不要重新询问 cookie 同意。

**3. 浏览器数据权限补救（仅 macOS）。** 获准的 `setup` 之后，stderr 显示 `X cookie access was permission denied` 时点出浏览器名；显示 `Permission denied reading Cookies.binarycookies` 时点出 Safari。建议：`检查"系统设置 > 隐私与安全性"中终端或 agent 应用的权限。"完全磁盘访问"（Full Disk Access）可能有帮助，但未必能解锁其他应用的数据。你可以手动提供 AUTH_TOKEN 和 CT0，或改用 XAI_API_KEY。` 没有待研主题时才提供一次重试；否则用可用来源继续。

**4. ScrapeCreators 提议（每次首次运行；浏览器启动前先征得同意）。** 解释：key 为 TikTok/Instagram 附赠 1 万次免费调用，并把额度花在免费结果少于 5 条的 Reddit 检索、不足 3 个 yt-dlp 视频的 YouTube 检索和字幕抢救上。`LAST30DAYS_REDDIT_SC_MIN_ITEMS=0` / `LAST30DAYS_YT_SC_MIN_ITEMS=0` 让回填仅在空结果时触发；`LAST30DAYS_REDDIT_BACKEND=scrapecreators` 把 Reddit 固定到 SC。YouTube 回填可抓字幕并重试。GitHub 注册比网页注册送的免费调用多，并会打开一个页面显示短代码。提问，例如："要添加 TikTok 和 Instagram 吗？key 还会把额度花在少于 5 条的 Reddit 检索、少于 3 个的 YouTube 检索和字幕上。LAST30DAYS_YT_SC_MIN_ITEMS=0 让 YouTube 检索仅在空结果时兜底。GitHub 注册送 1 万次免费调用并打开浏览器显示代码。(yes / no)" **等待回答。**
   - 回答 **yes** → 两条命令。先在前台运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --github-start`：约 1-2 秒返回，输出 `Your GitHub code: XXXX-XXXX` 行加一个 JSON 块，把代码复制到剪贴板并打开浏览器。从输出读 `user_code`，立刻告诉用户：代码是什么、它已在剪贴板上，在 GitHub 页面直接粘贴（Cmd+V）即可，不要让他们自己找。（`status == "already_registered"` 时到此为止：现有 key 已生效。输出说剪贴板复制失败时，让他们手动输入代码。）然后运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" setup --github-poll`（后台、5 分钟超时；或前台），解析其 stdout 的**最后一条** JSON 行得到最终状态。成功时引擎自动持久化 key，返回 `"persisted": true` 和脱敏的 `api_key`（绝不索要或回显原始 key）。确认付费来源已生效。
   - **成功但 `"persisted": false`**（授权完成但 key 写入失败）→ 不要声称来源生效。告诉用户注册成功但保存失败，让他们手动把 `SCRAPECREATORS_API_KEY=<key>` 加进 `~/.config/last30days/.env`（输出中的原始 key 已脱敏：重跑 `setup --github` 或到 scrapecreators.com 取值）。
   - **`status == "error"` 且 `message == "Authorized but failed to fetch API key"`**（精确匹配；常为 `"reason": "no_api_key"`）→ GitHub 授权成功，不要说授权失败。这通常意味着该 GitHub 账号已关联 ScrapeCreators 账号。告诉用户："GitHub 已授权，但我没能自动取到你的 ScrapeCreators key：你的 GitHub 可能已关联账号。到 scrapecreators.com 拿 key 粘贴，或跳过。" 接受粘贴的 key 或提供网页/跳过选项。
   - **`status == "error"` 且 `message` 含 `ScrapeCreators profile failed`**（或 `"reason": "upstream_error"`）→ GitHub 授权成功；不要说授权失败，也**不要**说账号已关联。ScrapeCreators 在授权后返回了服务器错误。告诉用户："GitHub 已授权，但 ScrapeCreators 铸造 key 时发生服务器错误：是他们那边的问题，不是你的。到 scrapecreators.com 注册或登录，在那里拿 key 粘贴，或跳过/稍后重试。" 接受粘贴的 key 或提供网页/跳过选项。
   - **超时或其他任何错误** → 告诉用户没有完成，提供重试或到 scrapecreators.com 网页注册。
   - 回答 **no** → 说明以后想配随时可以再提，然后继续。

**4b. 来源档位（保存 key 之后）。** 评论默认开启：TikTok/Instagram 帖子和热评，外加 YouTube 评论。回填与档位无关：Reddit 免费结果少于 5 条、YouTube 不足 3 个 yt-dlp 视频时都会跑。提问："推荐档添加 TikTok + Instagram 帖子和热评，外加 YouTube 评论。全部档另加 Threads + Pinterest（扣费更多）。(recommended / everything)" **等待回答。**
   - 回答 **recommended** → 向 `~/.config/last30days/.env` 追加 `INCLUDE_SOURCES=tiktok,instagram,youtube_comments,tiktok_comments,instagram_comments`（包含 `tiktok,instagram`，否则它们会被当作排除项）。确认 TikTok/Instagram/YouTube 的帖子加热评已开启。
   - 回答 **everything** → 追加 `INCLUDE_SOURCES=tiktok,instagram,youtube_comments,tiktok_comments,instagram_comments,threads,pinterest`。确认 Threads 和 Pinterest 也已开启。

**5. 完成。** `SETUP_COMPLETE=true` 写入后即进入研究。设置 stdout 反映的是本次安装了什么，不是运行时来源清单；研究确认时引擎的诊断才是权威。Codex desktop、Cursor、Gemini CLI 和 raw 文件夹模式宿主上，隐藏的 `.claude/last30days.env` 项目配置默认被忽略，除非从进程环境或全局配置设置了 `LAST30DAYS_TRUST_PROJECT_CONFIG=1`；只有引擎把项目文件报告为配置来源时，才把它报告为生效。

---

### Grok Bot 散文流程

适用于 Grok Bot 宿主。根 SKILL.md 的 GROK BOT HOST RULE 全程适用：运行引擎的每个 shell（含下方每条命令）都导出 `LAST30DAYS_HOST=grok-bot`。对话形态与非模态散文流程相同，无模态框，bot 自带 X 工具优先：该宿主上引擎绝不读取浏览器会话，X 只走官方访问。按序执行；要求等待处就等待。

**1. 宿主标记 + 欢迎。** 持久化宿主信号，让后续运行和 `doctor` 都能看到：`~/.config/last30days/.env` 缺失时执行 `mkdir -p ~/.config/last30days && touch ~/.config/last30days/.env`；然后追加一行 `LAST30DAYS_HOST=grok-bot`（只用 `>>` 追加，绝不 `>`）。然后运行 `"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" --welcome`，stdout 原样展示。

**2. X 工具（首选：提供任何 key 之前先查）。** 在本会话中找 X 帖子搜索工具，例如 `search_posts_all`：先是 Grok Bot 内置 X 工具（命名空间 `x`），然后是 "X for Grok Bot" 插件的工具。任何按查询搜索帖子的工具都算；两者靠工具来源区分，绝不靠名字。
   - **存在** → 告诉用户："X 已就绪：它经 Grok Bot 自带的 X 访问运行，覆盖完整 30 天，无需配置。" 每次研究运行按 Research Execution 中的 Grok Bot X 配方执行，并且只在抓取返回了帖子的引擎 shell 中、在 `LAST30DAYS_HOST=grok-bot` 旁边导出 `LAST30DAYS_X_HOST_LANE=1`：一次 `topic` 调用，规模按深度取 10 / 30 / 60（`--quick` / 默认 / `--deep`），带 `-is:retweet` 和时间窗；每个 `--x-handle`，一次 `from` 调用 8 条、一次 `mention` 调用 5 条；每个 `--x-related` 句柄，一次 `related` 调用 3 条；写入 `last30days-x-posts/1` 信封（含 `generated_at`、`topic`、`window`、`status`、按 `topic` / `from` / `mention` / `related` 标注的 `calls`，每条帖子只含 `id`、`author_handle`、`created_at`、`text`、`likes`、`reposts`、`replies`、`quotes`，别无其他）；工具拒绝窗口或数量参数时省略它们并写 `status: partial` 加 `error: window-unsupported`；文件作为 `--x-posts <file>` 传入。跳过第 3 步。
   - **不存在** → 进入第 3 步。

**3. 备用 key（两者都没有时才走）。** 先说，再等待："本会话没有 X 搜索工具，X 需要 key。最佳方案：添加 "X for Grok Bot" 插件并在 Grok Bot 内连接 X（它会为你开通 X 开发者账号，含赠送额度）。否则粘贴来自 X 开发者控制台的 X_BEARER_TOKEN（近期帖子，约最近一周，除非你的 X 开发者项目有全库访问），或来自 console.x.ai 的 XAI_API_KEY。或暂且跳过 X。(bearer / xai / skip)"
   - 用户粘贴 key → 只经引擎的 key 写入路径持久化，用单引号 heredoc 从 stdin 喂入。绝不用临时 shell 命令写值，绝不把值插进命令行：

     ```bash
     "${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" setup --store-key X_BEARER_TOKEN <<'KEY_EOF'
     {PASTED_VALUE}
     KEY_EOF
     ```

     xAI key 用 `setup --store-key XAI_API_KEY`。引擎打印 `X_BEARER_TOKEN=****`（或 `XAI_API_KEY=****`）和一行 JSON `persisted`；绝不回显值，只以脱敏的 `NAME=****` 形式确认。换新值重跑会替换已存值（被拒的 key 就是这样轮换的）。`"persisted": false` 表示写入失败：如实说明，不要声称 X 已生效。
   - **跳过** → 向 `~/.config/last30days/.env` 追加 `X_DECLINED=grok-bot`（只追加），后续运行对 X 保持安静：不解锁推销，不再问 key。调用已含主题时，第 4 步之后立即研究，发现之后恢复第 5-6 步。

**4. 设置（免费 CLI，不读浏览器）。** 运行 `"${LAST30DAYS_PYTHON:-python3}" "${SKILL_DIR}/scripts/last30days.py" setup`（普通形式；该宿主上不读任何浏览器数据）。它尽力安装 yt-dlp（YouTube）、Digg CLI、arXiv、Techmeme、Yahoo Finance，并写入 `SETUP_COMPLETE=true`。展示安装了什么，包括 Digg 是否落在 PATH 上。

**5. ScrapeCreators 提议与来源档位。** 完全按非模态散文流程的第 4、4b 步执行（GitHub 设备码注册：先 `setup --github-start` 后 `setup --github-poll`；引擎持久化并脱敏 key）。

**6. 完成。** 确认 `~/.config/last30days/.env` 中有 `SETUP_COMPLETE=true`（`setup` 没跑就追加一行），然后进入研究（带宿主信号；X 抓取返回了帖子时导出 `LAST30DAYS_X_HOST_LANE=1`）。设置 stdout 反映本次安装了什么，不是运行时来源清单；研究确认时引擎的诊断才是权威。

---

### Manual Setup Guide（手动设置指南）

Claude Code 用户选择 "Manual setup" 时展示，或供任何想手动配置的人使用。以纯文本呈现（不要用引用块）。

/last30days 的魔力在于 Reddit 评论 + X 帖子合在一起，而且两者都免费。把下面这些加进 `~/.config/last30days/.env`：

**X/Twitter（选一种：最重要的来源）：**
- `X_BEARER_TOKEN=xxx`：官方 X API v2（`api.x.com`），使用来自 X 开发者控制台的 app-only bearer。Basic 档约能取最近一周的帖子，除非你的 X 开发者项目有全库访问。用 `setup --store-key X_BEARER_TOKEN` 持久化（值走 stdin，输出脱敏）。非 Grok Bot 宿主还要加 `LAST30DAYS_X_BACKEND=xapi`，引擎才会选中它（设了 bearer 但没设它时 `doctor` 会提示）。
- **Grok CLI（无需 X 凭证）：** 用 `curl -fsSL https://x.ai/cli/install.sh | bash` 安装，然后 `grok login`。不需要 X 账号、cookie 或 API key。需要 Grok 套餐；调用从套餐扣。
- `FROM_BROWSER=auto`：免费。检索时实时读取你的 x.com 登录 cookie：macOS 上先 Firefox 和 Safari，再 Chromium 浏览器；Windows 和 Linux 只用 Firefox，WSL 下以 Windows Firefox 兜底。cookie 值绝不落盘。Chromium 读取可能再次请求 macOS 钥匙串访问；想持续授权 OS 访问就选"始终允许"。已保存的 `BROWSER_CONSENT=false` 会阻止这些读取，直到你再次同意。设 `BROWSER_CONSENT=false` 或 `FROM_BROWSER=off` 可禁用原生、CDP 和 sidecar 读取。
- `XAI_API_KEY=xxx`：无需浏览器访问。到 api.x.ai 取 key。最适合服务器。
- `XQUIK_API_KEY=xxx`：经 Xquik 的无 key 式 X。
- `AUTH_TOKEN=xxx` + `CT0=xxx`：手动粘贴你的 X cookie（x.com → F12 → Application → Cookies）。

**Grok Bot 上的 X（修复）。** `LAST30DAYS_HOST=grok-bot` 宿主上 X 只走官方访问，因此 X 返回为空时：确认 Grok Bot 内置 X 工具（命名空间 `x`）在会话中且抓取先于引擎命令运行；否则添加 "X for Grok Bot" 插件并在 Grok Bot 内连接 X（X 连接器通道），或经 `setup --store-key <NAME>` 添加 `X_BEARER_TOKEN`（近期帖子，约最近一周，除非你的 X 开发者项目有全库访问）或来自 console.x.ai 的 `XAI_API_KEY`；页脚报告 X API 额度用尽（`payment-required`）时，到 X 开发者控制台充值。下方 Linux / Mac mini 修复节的内容在 Grok Bot 上一概不适用。

**Linux / Mac mini 上的 X（修复）。** 这些宿主（绝不是 `LAST30DAYS_HOST=grok-bot` 宿主）无法解密本地 Chrome cookie 存储，X 返回为空时，用下列方式之一喂给引擎一对 cookie（MacBook **不做**其中任何一项：它用 Keychain / Firefox / Safari 提取；不要在 MacBook 上启动 box-chrome）：
- **agentcookie sidecar：** 安装 `agentcookie` CLI，引擎即可自动从中读取你的 `auth_token`/`ct0`。cookie 拒绝会阻断它；`AGENTCOOKIE=off` 也会禁用它。
  - 只想用 sidecar 时，先取得读取 `agentcookie` cookie 的明确许可并撤回拒绝。设 `AGENTCOOKIE=on`；从进程环境、全局 `.env`（遵循 `LAST30DAYS_CONFIG_DIR`）和受信的 `.claude/last30days.env` 中移除 `BROWSER_CONSENT` 与 `FROM_BROWSER`。两者必须保持不存在，原生/CDP 读取才会保持关闭；`BROWSER_CONSENT=true` 会允许 CDP。
- **经 CDP 的实时 Chrome 登录（extras 宿主的成熟路径）。** 引擎经 DevTools 协议读取一个实时已登录的 Chrome，但你必须先在 extras 端口启动该 Chrome 并登录：仅跑 `setup --allow-browser-cookies` 不会打开任何窗口。步骤（MacBook 全部跳过）：
  1. 本次采集设 `AGENTCOOKIE=off`，防止 sidecar 混入另一对 cookie（成功后恢复为不设置）。
  2. 在 last30days extras 端口 **18800** 上启动一次性登录 Chrome：该端口是 last30days 的约定（`SAND_CHROME_REMOTE_DEBUG_PORT=18800`），不是 box-chrome 的内置默认值（`9222` 加显示编号）。**用宿主的 `box-chrome` 包装器启动**（它设置 `--class=box-chrome`）；不要直接启动 `google-chrome-stable`，尤其不要用自定义 `--class` 启动原生 Chrome：带 `--class=l30d-…` 的原生 Chrome 失败过，而 `box-chrome`（class `box-chrome`）成功过。不要依赖任何 `GrokAgent` user-agent 令牌：它不是必需的，宿主上可能已禁用（`/tmp/sand-ua-token-disabled`），绝不要告诉用户它必须存在。运行 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/box_chrome_login.py"` 打印确切的宿主正确命令（加 `--exec` 直接启动）；MacBook 上它打印 "no launch needed" 且不启动任何东西。`box-chrome` 在 PATH 上时命令是：
     ```
     mkdir -p /tmp/last30days-x-chrome
     CHROME_USER_DATA_DIR=/tmp/last30days-x-chrome SAND_CHROME_REMOTE_DEBUG_PORT=18800 box-chrome --new-window https://x.com/login
     ```
     缺少 `box-chrome` 时，不要拼凑一堆 google-chrome 参数（带自定义 `--class` 的原生 Chrome 就是失败案例）：改在某个已开放远程调试端口的 Chrome 里登录 x.com，并把 `BROWSER_CDP_URL` 固定到那个端点。
  3. 绝不代填登录表单，绝不驱动页面（不用 Playwright/Puppeteer/computerUse/xdotool，不输入凭证）。等 x.com 登录页真正可见后，把桌面/电脑预览交给真人："请在这个 Chrome 窗口里登录 X。"（登录页上方的 HUD 只能作为交接提示，绝不能用来点页面。）
  4. 他们交还后，确认窗口已登录（x.com/home）。向 `~/.config/last30days/.env` 追加 `BROWSER_CDP_URL=http://127.0.0.1:<port>`（只追加），用 Chrome 实际监听的调试端口：用上文命令启动就是 `18800`，否则用真实端口（一次实际采集固定的是 `http://127.0.0.1:9334`）。绝不写 `AUTH_TOKEN` 或 `CT0`：这对 cookie 每次运行实时读取。然后运行 `setup --allow-browser-cookies`，extras CDP 即读取实时 cookie 对。登录后固定 `BROWSER_CDP_URL` 也是一道防线：万一 18800 上应答的是一个过期/已登出的 Chrome。
  5. X 出现封锁/验证挑战/限流就停止：让他们稍后重试。不要继续启动 Chrome。
- **`XAI_API_KEY=xxx`**：基于 key 的 X，完全不碰浏览器。
- **Grok CLI**：运行 `grok login`，然后固定 `LAST30DAYS_X_BACKEND=grok`（仅手动固定；残留的 grok 登录绝不自动抢占 X 通道）。需要 Grok 套餐。

**Reddit（免费，开箱即用）：**
- 免费无 key 发现（Reddit 检索 + shreddit）提供帖子加热评和顶数。无需设置。
- `SCRAPECREATORS_API_KEY=xxx`：可选的 Reddit 检索回填，仅当免费路径返回**不足 5 条**（默认下限）时。每次运行对每个不同的查询、日期窗口和 subreddit 组合至多做一次 ScrapeCreators Reddit 回填，一次回填是若干次 API 调用（检索加评论抓取，默认深度约 10 次）。设 `LAST30DAYS_REDDIT_SC_MIN_ITEMS=0` 则仅在免费路径一无所获时回填，或设 `LAST30DAYS_REDDIT_BACKEND=scrapecreators` 让 ScrapeCreators 成为主路径。

**YouTube（免费，开源）：**
- 运行 `brew install yt-dlp`（或 `pip install yt-dlp`）：启用 YouTube 检索 + 字幕。
- `SCRAPECREATORS_API_KEY=xxx`：付费检索回填（不足 3 个 yt-dlp 视频时）和字幕抢救。`LAST30DAYS_YT_SC_MIN_ITEMS=0` 让检索仅在空结果时兜底；重试可能再次扣费。

**Digg（免费，无 key）：**
- 运行 `npx @mvanhorn/printing-press-library install digg --cli-only`：安装 Digg CLI，用于热点新闻、GitHub 星标和 pipeline 动态。`digg-pp-cli` 在你的 PATH（通常 `$HOME/.local/bin`）上时激活。

**GitHub Issues/PRs（免费，无需 key）：**
- `gh` CLI 已安装并登录（`brew install gh && gh auth login`）时，GitHub 检索自动可用。无需 API key。

**加项：TikTok、Instagram、YouTube 评论（ScrapeCreators）：**
- `SCRAPECREATORS_API_KEY=xxx`：scrapecreators.com 提供 1 万次免费调用。
- 添加 key 后，设 `INCLUDE_SOURCES=tiktok,instagram` 开启热门来源。（高级用户还可经 `INCLUDE_SOURCES=threads,pinterest,linkedin,meta_ads` 开启 Threads、Pinterest、LinkedIn 和 Meta Ads。）

**其他可选来源（随时可加）：**
- `PERPLEXITY_API_KEY=xxx`：带引用的首选 Agent/Search API 路径；设 `INCLUDE_SOURCES=perplexity`。已装 `OPENROUTER_API_KEY` 的保留同步 Sonar 兜底。
- `XIAOHONGSHU_API_BASE=http://localhost:18060`：经已登录的 x-mcp 浏览器插件或 `xiaohongshu-mcp` 服务使用小红书；本地服务跑在自定义 URL 时才需要。单次运行用 `--search xhs` 开启，或经 `INCLUDE_SOURCES=xiaohongshu` 持久开启。
- DripStack（付费财经通讯检索）仅限主动开启：单次运行用 `--search dripstack`，或经 `INCLUDE_SOURCES=dripstack` 持久开启。免费公开搜索 API，无需 key；不主动开启绝不激活。
- Telegram（公开频道）经 `--telegram-sources=handle1,handle2`（该次运行自动激活）或经 `TELEGRAM_SOURCES=handles` + `INCLUDE_SOURCES=telegram` 持久开启。需要 `SCRAPECREATORS_API_KEY`。仅支持具名公开频道；不支持关键词发现。
- `BSKY_HANDLE=you.bsky.social` + `BSKY_APP_PASSWORD=xxx`：Bluesky（免费 app password）。
- `BRAVE_API_KEY=xxx` 或 `EXA_API_KEY=xxx`：网页搜索后端。

**关键：绝不覆盖已有 `.env`。** 写入任何 key 之前：
1. 检查文件是否存在：`test -f ~/.config/last30days/.env`
2. 存在则先读取，再用 `>>`（双重定向）只追加缺失的键。
3. 绝不用 `>`（单重定向）：它会摧毁已有内容。
4. 不存在则：`mkdir -p ~/.config/last30days && touch ~/.config/last30days/.env`

始终在最后加这一行：`SETUP_COMPLETE=true`。然后进入研究。

设置向导的机械工作放在一个 Python 模块里，从而跨所有宿主（Claude Code、Codex、Cursor 等）运行，同意对话由你主持。本文件中的常见情形（已设置）路径保持很短。

---
