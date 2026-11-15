> **中文汉化版** · 上游：[morluto/rea](https://github.com/morluto/rea) · 原文件：`.agents/skills/reverse-engineer-anything/references/environments.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 从运行中的应用生成 Agent 环境

当用户需要一个 Web 应用的 agent 环境（AgentEnv bundle）时使用本节：
一个可部署的 `agent-env` 文件夹，其 MCP 工具基于对该应用的一次录制
所观测到的内容作答，并提供该录制确认过的写操作。
工作流先用 `capture_browser_scenario` 录制一次应用，检查环境会提供什么，
若提示指出缺口则再次录制，最后用 `export_environment_bundle` 写出 bundle。
若用户已有 HAR，可通过 `inspect_web_network_capture` 跳到[导出](#export-and-hand-off)，
或使用 `rea environment-build <capture.har> <dir>`。
若任务针对桌面应用导出的环境，阅读[对应章节](#tasks-for-a-desktop-application-environment)。

## 录制之前

- 只对用户声明为可丢弃或为此目的专门填充数据的实例录制：
  每个写步骤都会创建、修改或删除其数据。用户没有说过时，
  先询问再执行任何会写入的场景。REA 不会启动、填充或重置应用。
- 凭据来自用户指定的环境变量。把每个凭据声明为场景 secret，
  即 `{secret_id, environment_variable}`；该变量必须在 REA MCP 服务器
  启动时所在的环境中已设置。绝不要在聊天中索要密码。
  已声明的 secret 会随录制进行脱敏。
- 先用 `inspect_web_page` 摸清应用（布局重要时加 `capture_web_screenshot`）：
  登录表单的定位器，以及列出和编辑用户所关心实体的页面背后的 API 调用。
- `inspect_web_page` 无法登录。要查看登录后的页面，运行一个简短的
  `capture_browser_scenario`，先登录再打开这些页面，并带上
  `"capture": {"after_each_step": ["accessibility"]}`（要标记文本用 `"dom"`）。
  用 `inspect_analysis_view` 读取步骤的树：
  `view: {kind: "browser-scenario", collection: "text", step_index,
  artifact: "accessibility", offset: 0, limit: 2048}`，用 `offset` 翻页。
  捕获选项只有 `after_each_step`、`at_end`、`events`、`network` 和 `limits`。

## 录制一个能让环境学会写操作的会话

一次 `capture_browser_scenario` 录制整个会话。
以下面的结构为起点，替换为应用自己的定位器、路径与头部：

```json
{
  "browser": { "mode": "launch", "executable_path": "/usr/bin/chromium" },
  "start_url": { "url": "http://127.0.0.1:3000/login" },
  "secrets": [
    { "secret_id": "admin_password", "environment_variable": "APP_PASSWORD" }
  ],
  "capture": {
    "network": {
      "request_body": true,
      "response_body": true,
      "header_values": true
    }
  },
  "actions": [
    {
      "step_id": "user",
      "action": "fill",
      "timeout_ms": 15000,
      "locator": { "kind": "css", "selector": "input[name=username]" },
      "value": { "source": "literal", "value": "admin" }
    },
    {
      "step_id": "password",
      "action": "fill",
      "timeout_ms": 15000,
      "locator": { "kind": "css", "selector": "input[name=password]" },
      "value": { "source": "secret", "secret_id": "admin_password" }
    },
    {
      "step_id": "sign-in",
      "action": "press",
      "timeout_ms": 15000,
      "locator": { "kind": "css", "selector": "input[name=password]" },
      "key": "Enter"
    },
    {
      "step_id": "signed-in",
      "action": "wait_for",
      "timeout_ms": 15000,
      "locator": { "kind": "css", "selector": "nav a[href='/settings']" },
      "state": "visible"
    },
    {
      "step_id": "folders-1",
      "action": "request",
      "timeout_ms": 15000,
      "method": "GET",
      "path": "/api/folders",
      "expected_status": [200]
    },
    {
      "step_id": "new-folder-1",
      "action": "click",
      "timeout_ms": 15000,
      "locator": { "kind": "role", "role": "button", "name": "New folder" }
    },
    {
      "step_id": "folder-title-1",
      "action": "fill",
      "timeout_ms": 15000,
      "locator": { "kind": "css", "selector": "input[name=title]" },
      "value": { "source": "literal", "value": "Scratch folder 1" }
    },
    {
      "step_id": "create-folder-1",
      "action": "click",
      "timeout_ms": 15000,
      "locator": { "kind": "role", "role": "button", "name": "Create" },
      "save_response": {
        "method": "POST",
        "path": "/api/folders",
        "save": [{ "name": "folder_1", "json_pointer": "/id" }]
      }
    },
    {
      "step_id": "read-folder-1",
      "action": "request",
      "timeout_ms": 15000,
      "method": "GET",
      "path": "/api/folders/{saved:folder_1}",
      "expected_status": [200]
    }
  ]
}
```

给每个接受 `timeout_ms` 的步骤设置时限。没有时限时，步骤会一直等待
直到完成或场景被取消，一个永远匹配不上的定位器会让捕获连同客户端一起挂起。
`wait_for_timeout` 暂停改用 `duration_ms`，不接受 `timeout_ms`。
`wait_for` 的定位器要恰好匹配一个元素。

1. 通过 UI 登录：`fill` 用户名与密码字段（密码用 secret 引用），提交，
   然后 `wait_for` 一个只有已登录用户才能看到的元素。
2. 用 `request` 步骤读取：环境需要的每个集合，在任何写之前读两次，
   让自发变化的字段显形；然后把每个列表展示的对象按 id 读一遍，
   每个集合最多十个。只从列表得知、而列表又省略了其单读会展示的字段的对象，
   在环境中无法按 id 读取或更新。
3. 按应用 UI 的方式写：填它的表单、点它的按钮，让每个请求带上 UI 会发送的
   字段，包括服务器本来会自行推导的字段。提交创建的点击或按键要带
   `save_response` 以保留新对象的 ID，然后 `goto` 其页面
   （`/items/{saved:item_1}`）或用 `request` 步骤读取。
   绝不猜测 ID，也绝不为了探出下一个 ID 而创建探测对象。
   只在 UI 无法触达该操作（纯 API 资源，或不调用 JSON API 的 UI），
   或覆盖以 `unexplained-change` 或 `contradicted` 扣留 UI 形态的写时，
   才改用 `request` 步骤写；这算两次重录额度中的一次。
   被覆盖以这种方式扣留的 `request` 步骤写，通常是缺少 UI 会发送的字段：
   改回通过 UI 录制。若某条路径无法脚本化，就不提供该写并在报告中说明限制。
   每种写类型录制两个带编号的草稿对象，自由文本要有变化。
   每次写之后、下一次写之前，先按 id 读回该对象再读它的列表：
   创建 1、读 1、列清单、创建 2、读 2、列清单；绝不在读取之前连做多次写。
4. 两次创建之间、以及创建与首次编辑之间留出超过一秒的间隔
   （用 `duration_ms: 1100` 的 `wait_for_timeout`），
   让按创建时间排序的列表能按序显示它们。
5. 更新两个对象并各自读回，修改人真正会改的字段（名称、邮箱、状态、截止日期），
   而不是只改描述：环境提供的更新只接受已录制更新存储过的成员。
   在同一对象上连续执行两次开关型操作（加星、收藏、归档），每次之后读回：
   第二次调用能显示它是设置还是翻转该字段，
   环境只有在一个调用展示了这一点后才提供该操作。
   删除两个对象并各自读回（预期 404，或对象被标记为已删除），再读列表。
6. 无论用什么方式写，两次创建发送的内容要有变化：第一次带上应用接受的
   每个字段，第二次只给人必须给的字段（标题或名称），其余字段省略或留空。
   环境提供的创建要求两次创建都填过的成员必填，并允许调用方省略
   某次创建省略或发空的成员，因此只给标题的 agent 不会因
   它没有理由设置的字段而被拒绝。

关于 `request` 步骤：

- `path` 位于起始 URL 的 origin 上；页面必须在该 origin 上。
- 头部值可以是字面量、已声明的 secret、浏览器持有的 cookie
  （`{source: "cookie", name}`）、localStorage 条目
  （`{source: "local_storage", key, json_pointer}`）、已保存值
  （`{source: "saved", name}`），或 Basic 凭据
  （`{source: "basic_credentials", parts: [username, password]}`，
  以 `username:password` 的 base64 发送并脱敏），
  另可加可选 `prefix`，如 `"Bearer "` 或 `"Basic "`。
- 每个凭据组成部分可以是字面量、secret、已保存值、cookie 或 localStorage 条目，
  因此前端由登录令牌（用户名与令牌）构造的头部也能复制；
  密码必须是 secret 或已保存值，绝不能是字面量。
- 复制应用自身请求发送的头部（如来自 `csrftoken` cookie 的 `X-CSRFToken`
  这类 CSRF 头、bearer token）。从页面读取的值，在其被读取之后的记录中
  会被脱敏，但返回它们的登录响应不受影响；短于 8 个字符的值完全不脱敏。
- `save: [{name, json_pointer, secret}]` 从步骤的 JSON 响应中保留一个字符串
  或数字（如所创建对象的 `/id`）供后续步骤使用；`secret: true` 会对其脱敏
  （适用于 API 返回的令牌），因此所有保存下来的 token、密钥或会话值
  都要标记为 secret。这也会在所选源响应的 body 或头部被保留前对其保护。
  压缩或大小未知的 UI 响应无法提供保存值。在 `click` 或 `press` 上，
  `save_response: {method, path, save}` 从步骤等待期间观测到的新请求的响应中
  保留值（`path` 中的 `{*}` 匹配一个路径段）。匹配不证明 UI 因果：
  所选路径要区别于轮询；观测到多个匹配会因歧义而失败。
  除非在 `timeout_ms` 之前收到 2xx JSON 响应，否则步骤失败。
  后续步骤在请求 `path`（含查询串）或 `goto` URL 中用 `{saved:name}` 发送
  已保存值；在 `json` body 中，仅由 `{saved:name}` 组成的字符串会保留
  已保存值的 JSON 类型；或在头部或凭据组成部分中用 `{source: "saved", name}`。
- 读取页面值会让后续 body 的保留成本上升：读取 CSRF token 之后，
  超过约 47 KiB 的 body 会按 `unavailable` 保留。
  当 API 返回更大的响应时，调高 `capture.limits`
  （`max_network_body_allocation_bytes`、`max_total_event_allocation_bytes`）。
- `request` 步骤不跟随重定向：重定向会使步骤失败，
  `expected_status` 也不能写 3xx 状态。改用重定向指向的路径，
  例如带尾斜杠的那个。
- 每个步骤都设置 `expected_status`，这样被拒绝的调用会让其步骤失败、
  后续步骤报告未运行，而不是录下一堆对空内容的读回。

请求总数控制在约 60 到 160 个。没有 `request` 步骤的场景按以前的方式原样录制。

捕获会返回其全部 Evidence，包括每个已录制的 body，
通常超出客户端内联展示的量。检查覆盖之前，先确认
`normalized_result.steps` 的每一项都是 `status: "completed"`；
若客户端把结果存到了文件，在其中搜索 `"status":"failed"` 并读取该步骤的 `error`。
登录或写步骤失败会取消其后的每个步骤。
用结果的 `evidence_id` 做覆盖检查与导出；不要把 Evidence 粘贴回另一个工具。

## 检查覆盖

用 `inspect_analysis_view`，`source: {kind: "retained-evidence", evidence_id}`
（捕获的 id），`view: {kind: "environment-coverage", template_rules:
["after-uid-literal", "opaque-token", "sibling-variance", "prefix-variance"]}`。
它会报告从状态作答或重放的读工具（`reads.recorded_reasons`）、
被提供的写工具，以及每个被扣留的写及其 `reason` 与 `hint`。
它不应用提供时的目录与状态规模检查；这些由导出来报告。

被扣留的写最多重录两次，且仅限录制缺口。原因属于应用行为时立即停止，
并将该写连同其 hint 报告为被扣留：

| 原因                | 处理方式                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `no-state-target`     | 检查路径模板与已录制视图；补录缺失的读取。该路由形态可能不支持作为变更目标。 |
| `no-observation`      | 重录：写之后按 id 读回该实体；更新或删除前先读取它。                               |
| `unconfirmed`         | 重录：写之后读取该实体及其列表。                                                    |
| `incomplete-entities` | 重录：通过列出该实体的每个视图都读取一遍。                                          |
| `unexplained-change`  | 用同一写的第二次不同调用重录一次。                                                  |
| `no-call`             | 用一次成功的写重录。                                                                |
| `side-effect`         | 停止：应用会改动其他实体。                                                          |
| `contradicted`        | 停止：后续读取与建模的效果不一致。                                                  |
| `body-unusable`       | 用 `request` 步骤重录一次 UI 写（其 body 未暴露）；否则停止。                       |

每次尝试用新的草稿名称，并在重录之前删除上一次尝试创建的对象
（通过 UI，或用捕获所示 id 的 `request` 步骤）：环境从录制首次读取的内容出发，
遗留对象会变成写任务随后能找到的种子数据。
新的浏览器场景捕获包含请求时间，因此时间完整的捕获能学会写时钟，
并提供会盖修改时间戳的更新。旧捕获或缺少请求起点的捕获保持记录顺序，
学不到时钟。当覆盖报告该限制时，先用当前版本重录，
再断定时间戳变更无法提供。

## 导出与交接

用 `export_environment_bundle`，传 `source: {kind: "retained-evidence", evidence_id}`
（或 `{kind: "evidence-file", path}`）、一个尚不存在但其父目录存在的
绝对 `output_directory`，以及 `name`（应用运行在 `localhost` 或 IP 地址上时必填）。
它会再次返回覆盖情况、`tool_count`、写出的文件与警告；
`dry_run: true` 只报告不写。bundle 会从 registry 安装本 REA 版本的 `rea-agents`；
当用户运行未发布的 REA 构建时，改为传入他们提供的 `package_tarball`
（打包好的 `rea-agents` tarball）。

告诉用户有多少工具从状态作答、哪些写被提供、哪些被扣留及其原因，
以及运行命令（`agent-env run <folder>`）。说明 bundle 携带已录制的响应
与捕获的本地路径（浏览器场景为浏览器可执行文件的路径），
并列出 `credential-named-members` 警告指针供审阅。
绝不要自行发布或分享该 bundle。

状态、重放与 bundle 能确立什么见
[agent 环境](https://github.com/morluto/rea/blob/main/docs/agent-environments.md)；
manifest 与状态视图见 [evidence 工作流](evidence-workflows.md)。

## 桌面应用环境任务

当用户有 `rea capture-desktop-application` 产出的文件夹，并想为
`rea export-desktop-application` 由此生成的环境创建任务时使用本节：
给计算机操作 agent 的提示词，以及给该 agent 在应用文件中留下的结果打分的检查项。
提示词与检查项由你撰写；REA 依据捕获校验任务并导出。
这些命令只有 CLI。若要从一条请求出发构建环境及其任务，
改走 [desktop 构建](desktop-build.md)。

### 描述变更

运行 `rea describe-desktop-application-task CAPTURE --format json`。读取：

- `owned_paths`：应用只服务这些路径下的文件，因此检查项也只能读这些文件。
- `files`：其中首末版本状态不同的每个文件，附其 `role`、`baseline` 与
  `final` 版本及净 `change`。文本变更把每条新增与删除行各列一次，
  `line_counts` 给出两端都存在但数量变化的行。
- 这些文件各自的 `values`：变更新增、修改和删除了什么，`before` 与 `after`，
  位于检查项引用它的 pointer 上，`refers_to` 说明诸如 `category="44"`
  的键所指的元素。跳过标注为 `by_position` 或噪声的条目。
  只有 XML 文件、归档、JSON 与 key 文件有 values：
  文本文件或数据库的变更已直接列出其行与行记录。
- `task`：一份草稿，其 `checks` 来自用户处理过的文档的净变更，
  或（无文档变更时）应用自身状态的净变更。
- `guards`：可选检查，验证其余内容保持种子值，例如同类兄弟条目的字段
  或文本文件的相邻行；加一两条以证明其余内容未被改动。
- `notes`：说明 `files` 为何为空，或某文件的建议为何单薄，
  例如没有属性指明被改元素时的 `by_position`。

### 撰写提示词

用用户的话和应用的术语说清要做什么，并点名应用：
"在 Mousepad 中，把 buy milk 加进我的待办清单并保存"。
解题 agent 自己的 shell 看不到计算机的文件；应用的名称把它引向屏幕。
绝不要说明文件如何存储内容：不给用户不会说出的路径、行格式、XML、键名或 SQL，
更不要透露检查项。替换草稿中的占位符；导出会拒绝含占位符的任务。

### 挑选检查项

检查项只能表达已观测到的变更：

- 只有描述了用户所做之事的建议才保留。凡由应用保存方式推出来的都要丢弃：
  格式重写、重新编号的行、计数器。一张 LibreCAD 图纸新增四个孔后被
  从 DXF R12 重写为 2007 格式，草稿建议检查 `SECTION`、`ENDSEC` 与 `CIRCLE`
  的数量；只有 `CIRCLE` 等于 9 是用户的变更。
- 绝不检查未变更的内容、整个文件或应用自动加盖的值：时间、它分配的 id、
  窗口尺寸。REA 拒绝 ISO 8601 与 `asctime` 日期时间（`Thu Nov  5 09:20:31 2026`）；
  其余由你判断。
- 优先少量稳健的检查项：整行优于位置，按有意义列匹配行优于生成 id，
  用户可能继续添加时用 `at_least`。

种类有：`file_present` 与 `file_absent`；`lines_present` 与 `lines_absent`（`lines`）；
`line_count`（`exact` 或 `contains`，配合 `equals`、`at_least` 或 `at_most`）；
`value_equals` 与 `value_absent`（指向视图的 JSON `pointer`，key 文件如
`/groups/GROUP/KEY`）；`text_equals` 与 `text_contains`（`pointer` 处 XML 元素的
完整文本，可选 `normalize_whitespace`）；`row_present` 与 `row_absent`
（`table`，按列 `where`）以及 `row_count`。
每个检查项把 `file` 写成 home 下的路径。保存为 zip 归档的文档
（如 FreeCAD 的 `.FCStd`）按其条目读取：指向条目的视图，
并用 selector 而不是位置命名数组成员，如
`/entries/[name=Document.xml]/view/root/children/[name=Object][@name=Hole]`，
这样即使应用换了个顺序写入，检查项仍然有效。
gzip 压缩的文档（如 Gnumeric 的 `.gnumeric`）按其内部的文档读取：
当作同一文档未压缩时那样指向它。应用把数字按文本写出时
（如 `"5.0000000000000000"`），给 `value_equals` 加 `tolerance` 以便与数字比较。
检查用户在文档中写的内容，要对段落元素用 `text_equals`，
而不是对文本节点用 `value_equals`：AbiWord 和 Writer 这类应用保存时
会把段落拆成多个 run，第一个文本节点只承载其中一部分；
句子内的某个值（如时间）用 `text_contains`。
二进制文档（如 GIMP 的 `.xcf`）没有视图：给任务加一个 `readers` 条目，
即应用自己的无头命令、输出 `REA ` 行，并让一个检查项在 `reader` 中引用它，
做法见 [desktop 构建](desktop-build.md#read-a-binary-file-with-a-reader)。
确切规则见 [desktop 应用任务](https://github.com/morluto/rea/blob/main/docs/desktop-application-tasks.md) 指南。

### 导出任务

把任务写成 JSON，含 `name`、`prompt` 与 `checks`，然后运行
`rea export-desktop-application CAPTURE DIRECTORY --task TASK.json`。
只有检查项在种子上失败、且在捕获的最终状态上全部通过，REA 才会保留该任务。
拒绝时会指明检查项：在最终状态上失败的检查项不符合用户留下的状态；
"所有检查项在种子上就已通过"表示没有任何检查项捕获该变更。
一个捕获要出多个任务时，重复 `--task`，并用 `--task-end NAME=CHECKPOINT`
为每个后续任务指明结束点。

当导出拒绝一个 apt 仓库装不到的应用时，向用户索要其安装所用的 `.deb` 文件
并用 `--package-file` 捕获，然后询问计算机可以从哪里下载该文件，
并作为 `--package-url` 传入。绝不要自己去抓厂商下载页：
这类网站常常拒绝自动下载，且副本与其许可证应由用户选择。

告诉用户任务的名称、提示词与检查项，以及如何测得解决率：
用 `--model MODEL` 运行 `agent-env run DIRECTORY --task NAME --agent claude-code`
三次，统计报告为 `passed` 的次数。运行需要模型端点：
`LITELLM_BASE_URL` 与 `LITELLM_API_KEY`，或 `.agentenv/config.toml` 中
`[model]` 下的 `base_url` 与 `api_key`。未被要求时不要运行 agent。
bundle 的种子是用户的真实数据：保持本地。
