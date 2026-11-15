> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/flows/sources.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 素材导入

由 `prompts/flows/create.md` 的 Step 2 与 `prompts/flows/evolve.md` 的追加流程使用。所有 `prompts/...` 与 `tools/...` 路径都相对 `{distilly_skill_root}` 解析（见 `SKILL.md`）。

| 任务 | 工具 |
|------|------|
| 读取 PDF 文档 | `Read` 工具（原生 PDF 支持） |
| 读取图片截图 | `Read` 工具（原生图片支持） |
| 读取 MD/TXT 文件 | `Read` 工具 |
| 解析飞书消息 JSON 导出 | `Bash` → `python3 "{distilly_skill_root}/tools/feishu_parser.py"` |
| 飞书自动采集（推荐） | `Bash` → `python3 "{distilly_skill_root}/tools/feishu_auto_collector.py"` |
| 飞书文档（浏览器会话） | `Bash` → `python3 "{distilly_skill_root}/tools/feishu_browser.py"` |
| 飞书文档（MCP App Token） | `Bash` → `python3 "{distilly_skill_root}/tools/feishu_mcp_client.py"` |
| 钉钉自动采集 | `Bash` → `python3 "{distilly_skill_root}/tools/dingtalk_auto_collector.py"` |
| 解析邮件 .eml/.mbox | `Bash` → `python3 "{distilly_skill_root}/tools/email_parser.py"` |

**凭证规则（飞书 / 钉钉 / Slack）**：App Secrets、user_access_token、refresh_token、Bot Tokens 和 OAuth codes 绝不能进入对话上下文。
- **绝不**让用户把这些值发给你，也不要把它们放进命令参数、脚本源码、输出文件或回复里。
- 配置时，请让用户**在自己的终端里**运行脚本的 `--setup`（飞书私聊还要 `--login`）。Secret 以隐藏输入方式键入，存入系统钥匙串（装了 `keyring` 时）或 `~/.distilly/*_config.json`（权限 0600）。用户也可以改为导出环境变量（`FEISHU_APP_ID` / `FEISHU_APP_SECRET` / `FEISHU_USER_ACCESS_TOKEN` / `DINGTALK_APP_KEY` / `DINGTALK_APP_SECRET` / `SLACK_BOT_TOKEN`）。`--setup` / `--login` 在没有交互终端时会拒绝运行，所以你无法代替用户执行。
- 用 `--check` 查看凭证是否就绪；它只显示来源（env / 钥匙串 / 配置文件），从不显示值。
- 如果你自己写脚本调用这些 API，请从环境变量或 `tools/credentials.py` 里的 `credentials.resolve(...)` 加载凭证，并且绝不打印。
- 如果用户还是把 secret 粘贴进了聊天：不要复述或使用它，让用户去开放平台轮换该密钥，然后按上文重新配置。

标注 Lark 的兼容采集器目前连接的是中国区 `open.feishu.cn` / `feishu.cn` 端点。国际版 `larksuite.com` 的租户路由尚未实现。

## 选择来源

询问用户想如何提供素材：

```
How would you like to provide source materials?

  [A] Lark Auto-Collect (recommended)
      Enter name, auto-pull messages + docs + spreadsheets

  [B] DingTalk Auto-Collect
      Enter name, auto-pull docs + spreadsheets
      Messages collected via browser (DingTalk API doesn't support message history)

  [C] Lark Link
      Provide doc/Wiki link (browser session or MCP)

  [D] Upload Files
      PDF / images / exported JSON / email .eml

  [E] Paste Text
      Copy-paste text directly

Can mix and match, or skip entirely (generate from manual info only).
```

---

### 选项 A：飞书自动采集（推荐）

首次使用先配置。检查凭证是否就绪：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" --check
```
如果没有就绪，让用户**在自己的终端里**运行（不要自己运行，也不要在聊天里索要 App Secret）：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" --setup
```

**群聊采集**（使用 tenant_access_token，机器人必须在群里）：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" \
  --name "{name}" \
  --output-dir ./knowledge/{slug} \
  --msg-limit 1000 \
  --doc-limit 20
```

**私聊（P2P）采集**（需要 user_access_token + p2p chat_id）：

私聊消息只能通过用户身份（user_access_token）访问。应用身份无法访问私聊。

**前置条件**（以下由用户在开放平台和自己的终端里完成，你只做引导）：
1. **飞书应用凭证**：通过 `--setup` 或环境变量配置好 `app_id` / `app_secret`（用 `--check` 确认）
2. **用户权限（user scopes）**：应用必须开启这些用户权限：
   - `im:message`：以用户身份收发消息
   - `im:chat`：以用户身份读取会话列表
3. **重定向 URL**：在应用的“安全设置 → 重定向 URL”下添加 `http://www.example.com`

如果用户缺少其中任何一项，引导其完成配置。不要假设任何东西已预先配置好。

**获取 user_access_token**：让用户**在自己的终端里**运行：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" --login
```
脚本会打印授权 URL；用户在浏览器里完成授权后，把回调 URL 粘贴回终端（隐藏输入），token 会直接进入钥匙串或配置文件。绝不要让用户在聊天里发送 code 或 token。

token 过期后（约 2 小时），你可以自行刷新，无需输入任何 secret：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" --refresh
```

**获取 p2p chat_id**：

用户通常不知道自己的 chat_id。用户可以在飞书里打开该私聊，从会话链接或开发者工具里找到 `oc_` 开头的 chat_id。如果你写脚本来获取它，脚本必须从 `credentials.resolve("feishu", ...)` 或环境变量读取 token，且不得打印：

- **方法**：向对方 open_id 发一条消息，响应里会带 chat_id（这会真的发出一条消息，所以先征得用户同意）
  ```python
  POST https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=open_id
  Header: Authorization: Bearer <read via credentials.resolve, never hard-coded>
  Body: {"receive_id": "{target_open_id}", "msg_type": "text", "content": "{\"text\":\"hello\"}"}
  # The chat_id in the response is the p2p chat ID
  ```
- **重要**：`GET /im/v1/chats` 不返回 p2p 会话：这是 API 限制，不是权限问题。不要试图用它来找私聊。
- 如果用户不知道对方的 open_id，用 tenant_access_token 搜索联系人：
  ```python
  GET https://open.feishu.cn/open-apis/contact/v3/scopes
  # Returns open_ids of all users visible to the app
  ```

**执行采集**：

凭证就绪、拿到 chat_id 之后（脚本自己加载 token，命令行上不会出现）：
```bash
python3 "{distilly_skill_root}/tools/feishu_auto_collector.py" \
  --open-id {target_open_id} \
  --p2p-chat-id {chat_id} \
  --name "{name}" \
  --output-dir ./knowledge/{slug} \
  --msg-limit 1000
```

**灵活性原则**：上述 API 调用不必经过采集器脚本。如果脚本跑不通或不匹配场景，直接对同样的端点写 Python 脚本，但凭证必须通过 `credentials.resolve("feishu", feishu_auto_collector.load_config())` 或环境变量加载，绝不能出现在脚本源码、命令参数或输出里。关键 API 参考：
- 获取 token：`POST /auth/v3/tenant_access_token/internal`（采集器里的 `get_tenant_token` 封装了它）
- 发消息（拿 chat_id）：`POST /im/v1/messages?receive_id_type=open_id`
- 拉取消息：`GET /im/v1/messages?container_id_type=chat&container_id={chat_id}`
- 搜索联系人：`GET /contact/v3/scopes`、`GET /contact/v3/users/{user_id}`

自动采集到的内容：
- 群聊：他们发出的消息（过滤系统消息和表情包）
- 私聊：双方的完整对话（用于理解上下文）
- 他们创建/编辑过的飞书文档和 Wiki
- 相关电子表格（如果有权限访问）

采集完成后，用 `Read` 读取输出文件：
- `knowledge/{slug}/messages.txt`：消息（群聊 + 私聊）
- `knowledge/{slug}/docs.txt`：文档内容
- `knowledge/{slug}/collection_summary.json`：采集摘要

如果采集失败，先诊断错误再尝试修复。常见问题：
- 群聊：机器人没被拉进群
- 私聊：user_access_token 过期（2 小时有效期；运行 `--refresh`，若无 refresh_token 则让用户在自己的终端里重跑 `--login`）
- 权限不足：引导用户开启权限并重新授权
- 或改用选项 B/C

---

### 选项 B：钉钉自动采集

首次使用先配置。先运行 `--check`；如果未配置，让用户**在自己的终端里**运行 `--setup`（AppSecret 隐藏输入），或者导出 `DINGTALK_APP_KEY` / `DINGTALK_APP_SECRET`。绝不要在聊天里索要 AppSecret：
```bash
python3 "{distilly_skill_root}/tools/dingtalk_auto_collector.py" --check
python3 "{distilly_skill_root}/tools/dingtalk_auto_collector.py" --setup   # run by the user
```

然后输入姓名：
```bash
python3 "{distilly_skill_root}/tools/dingtalk_auto_collector.py" \
  --name "{name}" \
  --output-dir ./knowledge/{slug} \
  --msg-limit 500 \
  --doc-limit 20 \
  --show-browser   # add this flag on first use to complete DingTalk login
```

采集到的内容：
- 他们创建/编辑过的钉钉文档和知识库
- 电子表格
- 消息（⚠️ 钉钉 API 不支持拉取历史消息：自动切换为浏览器抓取）

采集完成后，用 `Read` 读取：
- `knowledge/{slug}/docs.txt`
- `knowledge/{slug}/bitables.txt`
- `knowledge/{slug}/messages.txt`

如果消息采集失败，提示用户上传聊天截图。

---

### 选项 C：飞书链接

用户提供飞书文档/Wiki 链接时，询问用哪种方式：

```
Lark link detected. Choose read method:

  [1] Browser Method (recommended)
      Reuses your local Chrome login session
      ✅ Works with internal docs requiring permissions
      ✅ No token configuration needed
      ⚠️  Requires Chrome + playwright installed locally

  [2] MCP Method
      Uses a Lark App Token via the official API
      ✅ Stable, no browser dependency
      ✅ Can read messages (needs chat ID)
      ⚠️  Requires App ID / App Secret setup
      ⚠️  Internal docs need admin authorization for the app

Choose [1/2]:
```

**方式 1（浏览器）**：
```bash
python3 "{distilly_skill_root}/tools/feishu_browser.py" \
  --url "{feishu_url}" \
  --target "{name}" \
  --output /tmp/feishu_doc_out.txt
```
首次使用会打开浏览器窗口登录（一次性）。

**方式 2（MCP）**：

首次使用先配置（与选项 A 共用飞书凭证）。先运行 `--check`；如果未配置，让用户**在自己的终端里**运行 `--setup`：
```bash
python3 "{distilly_skill_root}/tools/feishu_mcp_client.py" --check
python3 "{distilly_skill_root}/tools/feishu_mcp_client.py" --setup   # run by the user
```

然后直接读取：
```bash
python3 "{distilly_skill_root}/tools/feishu_mcp_client.py" \
  --url "{feishu_url}" \
  --output /tmp/feishu_doc_out.txt
```

读取消息（需要 chat ID，格式 `oc_xxx`）：
```bash
python3 "{distilly_skill_root}/tools/feishu_mcp_client.py" \
  --chat-id "oc_xxx" \
  --target "{name}" \
  --limit 500 \
  --output /tmp/feishu_msg_out.txt
```

两种方式都输出到文件，然后用 `Read` 把结果载入分析。

---

### 选项 D：上传文件

- **PDF / 图片**：直接用 `Read` 工具
- **飞书消息 JSON 导出**：
  ```bash
  python3 "{distilly_skill_root}/tools/feishu_parser.py" --file {path} --target "{name}" --output /tmp/feishu_out.txt
  ```
  然后 `Read /tmp/feishu_out.txt`
- **邮件文件 .eml / .mbox**：
  ```bash
  python3 "{distilly_skill_root}/tools/email_parser.py" --file {path} --target "{name}" --output /tmp/email_out.txt
  ```
  然后 `Read /tmp/email_out.txt`
- **Markdown / TXT**：直接用 `Read` 工具

---

### 选项 E：粘贴文本

用户粘贴的内容直接作为文字素材使用，不需要任何工具。
