> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/generate.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

> **需要补充上下文**：仅目标元素一项，当请求没有指名一个能在页面上唯一解析的元素时。

Generate 是进入 live 模式的快车道：用户一句话说清元素、方向与数量，一分钟内就在浏览器里轮换变体。一条命令启动 helper，把元素交给你的 harness 已经显示的那个页面上的浮层（它会滚动到该元素、选中它、并触发与点击相同的 Go），然后返回 generate 事件；一次编辑写入变体；一次调用回复并等待用户的选择，helper 把选择直接烧进源码。本文件负责这条车道的管道；从事件开始，设计工作就归 [live.md](live.md)，原样不变，所以本会话若还没读过它，现在就去完整读一遍。

**仅限 Web。**Live 模式的浏览器浮层没有原生等价物；在 `ios` / `android` / `adaptive` 项目上，拒绝本命令，改为对源码提供 `bolder` 或 `quieter`。

管道正是这条车道省时间的地方：一条命令在你的 harness 已经显示的页面四周启动会话，一次调用回复并等待，这里没有任何需要你照看的浏览器。设计工作不是它省时间的地方。准备照任何命令一样执行（`impeccable context`、本参考文件、编辑前读 craft-floor.md），变体的计划、编写与接受完全照 live 会话的方式。

三条禁令覆盖本命令已知的出错方式：

- **绝不运行 init 或 document，绝不要 PRODUCT.md 或 DESIGN.md。**它们存在时，start 命令在 `boot` 下打印它们，你直接使用。不存在时，它会说明（`contextMissing`、`contextNote`），你从事件里提取身份（Step 3）。缺文件绝不是在本命令里访谈用户的理由；会话结束后用一行话提供 `init`。
- **绝不手写 variants 包装器，绝不发明 session id。**只有浏览器铸造 session id（8 个十六进制字符，在 Go 时）。缺事件就重跑 Step 2 来修，绝不直接改源码。
- **live 标记还在文件里时，不根据 hook 的发现行动**，也不为了安抚它们去重设变体样式；变体固化之后，接受步骤会验证一次文件。

## Step 1: 解析请求

三个部分，全部来自用户的句子：

- **请求里有数字**：它就是数量。**没有数字**：3。协议把数量封顶在 8。
- **方向措辞**映射到 live 动作词表；绝不发明新的 action 值：
  - **大胆、更大胆、更强、更有冲击力**：`bolder`
  - **安静、更平静、更柔和、收敛一点**：`quieter`
  - **更简单、极简、做减法**：`distill`
  - **更精致、更收紧、更打磨**：`polish`
  - **字体与排印类措辞**：`typeset`
  - **颜色类措辞**：`colorize`
  - **排布与间距类措辞**：`layout`
  - **设备与断点类措辞**：`adapt`
  - **动效类措辞**：`animate`
  - **趣味类措辞**：`delight`
  - **打破规则类措辞**：`overdrive`
  - **有意图但没有词表词的措辞**（"让它像一家银行"、"更暖一点"、"更高级"）：`impeccable`，用户的措辞作为 prompt 传入。
  - **动作匹配且额外意图搭车**（"更大胆，但保持单色"）：用该动作，其余作为 prompt。
  - **措辞完全没有方向**（"更好"、"改进"、"好看点"、"换个样"、"新鲜"、"新的"、"重新设计"、"修一下"、"来几个选项"、"给点想法"、"其他方案"，或只说"变体"再无其他）：用 AskUserQuestion 工具提问，等答案出来再继续。问一个问题，给出词表：*"变体往哪个方向走？bolder、quieter、更简单（distill）、更精致（polish）、字体排印（typeset）、颜色（colorize）、布局（layout）、动效（animate）、趣味（delight），还是打破规则（overdrive）。"* 按这张表映射答案；仍然开放的答案（"给我惊喜"、"你定"）用 `impeccable`、以用户原话作为 prompt，Step 2 从那个答案开始。
- **元素描述**（"价格卡"、"Hero 标题"）：Step 2 把它解析成选择器。

完成条件：手里有词表中的一个动作（请求没指名方向时，是问出来的）、一个 1 到 8 的数量，以及元素描述。

## Step 2: 先复用页面，再启动

**复用**已在跑的 dev server 与你的 harness 已经显示它的那个标签页；第二台服务器或第二个浏览器窗口，正是本步要阻止的失败。

1. **找到 dev server**，从最便宜的来源开始，命中即停：用户的消息、已开着该应用的浏览器标签页（Claude Code：`tabs_context` 里的 origin）、你的 harness 启动的服务器（Claude Code：`preview_list`）、打印过它 URL 的终端。它的 origin 就是你的 `--dev-url`。**没有命中**：不带 `--dev-url`、以无等待方式跑 start 命令；boot 会探测在跑的服务器，其裁决指明下一步。`browser_needed` 带来它找到的 `devUrl`：照第 2 点打开它，再以 `--dev-url <devUrl> --wait-for-browser 60000` 重跑。`no_dev_server` 表示没有任何东西在伺服这个应用：按裁决说的方式启动 dev 脚本（Claude Code：`preview_start`；Cursor：一个后台终端；Codex：一个你让出权后的 exec），等它的 URL，再以 `--dev-url <url>` 重跑。
2. **在你的浏览器里打开渲染该元素的页面，然后启动。**用请求指名的路由，否则用 `--target` 伺服的那个；`--dev-url` 只取 origin。
   - **Cursor**（`browser_navigate`）与 **Claude Code**（`navigate`，面板关着时会打开 Browser 面板，已有标签页在该 origin 上时从 `tabs_context` 取 `tabId`）：打开 URL，然后以 `--dev-url <url> --wait-for-browser 60000` 跑 start 命令。boot 注入浮层，命令等待期间页面重载进浮层。在这几个 harness 上，你的浏览器工具是唯一的开启者；引擎在那里忽略 `--open`。
   - **没有浏览器工具**（Codex 等）：以 `--open --wait-for-browser 120000` 跑 start 命令；它会打开系统浏览器，更长的等待覆盖用户找到标签页的时间。**`browser_open_failed` 返回**：用一行话把 `url` 告诉用户，再以 `--wait-for-browser 120000` 重跑。

```bash
.claude/skills/impeccable/scripts/impeccable live-generate --target src/App.jsx --dev-url http://127.0.0.1:5173/ --selector ".pricing-grid" --action bolder --count 3 --boot --wait-for-browser 60000
```

在 Cursor 与 Claude Code 里前台运行（它会在等待时间内返回）；在 Codex 上，放进一个你让出权的 exec，与 Step 3 跑 poll 的方式相同。

- `--target`：请求或项目让出处显而易见时，渲染该元素的文件；否则省略。
- `--dev-url`：第 1 点得到的 origin；省略则 boot 探测。
- `--selector`：先用唯一的 class，其次地标标签加 class，id 放最后（每个变体都会挂载一份该元素的副本，id 会在 DOM 里重复）。**请求以复数指名一个重复组件**（"价格卡"）：指向装着这组的容器，让一张 scoped 样式表重设每个实例。选择器不明显时，允许读一次渲染该元素的源文件；拿不准时 `--dry-run` 只解析并报告，不启动任何东西。
- `--boot`：跑车道的 boot（为 helper 再次载入 PRODUCT.md 与 DESIGN.md，容忍缺失文件，找到 dev URL，helper 存续期间隐藏底栏），并复用已在跑的 helper。其结果随 `boot` 附带。
- 另可用：`--prompt`、`--text`（只保留可见文本含该片段的匹配）、`--index`（按 1 起数在匹配中选取）。

按这个顺序读输出：先 `boot`（或带 `boot.contextNote` 的 `boot.contextMissing`：按注释，页面是事实来源），然后 `event`，即 `sessionId` 的 generate 事件，带着与用户按 Go 相同的 `_instructions`。每条裁决都带 `_instructions`，它们压过你对本文件的回忆；其中下一步由你决策的是：

- **`ambiguous`**：候选已列出；指向它们的公共容器，或以 `--text "<可见文本>"` 或 `--index <n>` 重跑。
- **`dev_server_gone`**：命令等待页面时 dev server 停止应答（Cursor 上，另一个会话启动的服务器随那个会话死掉）。按裁决说的方式启动它，再以 `--dev-url <url>` 重跑。
- **`no_match`**：标签页在一条不渲染该元素的路由上（导航到正确路由再重跑），或选择器错了（从源码推一个更好的，或加 `--text`）。
- `bootError` 下的 **`config_missing` / `config_invalid`**：先照 [live-setup.md](live-setup.md)，再重跑。
- `ok: true` 且 **`event: null`**：事件比等待慢；跑一次 `.claude/skills/impeccable/scripts/impeccable live-poll` 把它收回来，然后继续。

完成条件：输出显示 `ok: true`、一个 `sessionId` 与一个 `event`，且至多由你启动了一台服务器、打开了一个标签页。

## Step 3: 生成

事件是一个标准 `generate` 事件：所选元素的上下文、一份预检过的脚手架、指名该动作参考文档、计划小节与确切拼接点的 `_instructions`。完全照 live.md 的 **处理 `generate`** 一节处理，它拥有从身份锁到完成回复的一切：照它说的读该动作的参考文档与 craft-floor.md，按第 4 节规划（先身份，再模式，再三根不同的主轴，然后眯眼测试），按第 7 节声明参数，按第 6 节交付（每个变体一份完整的元素替换，预览 CSS 加全部变体一次编辑写进脚手架的拼接点）。这条车道不改变变体可以是什么：live 会话在这个元素上会走的招（一个提升的档位、一组重构、一张重排的卡、一个不同的表面）这里同样开放。绝不截屏页面；accept 之前，浮层预览就是评审通道。

**一次调用里回复并等待**，带上你写的文件：

```bash
.claude/skills/impeccable/scripts/impeccable live-poll --reply EVENT_ID done --file src/App.jsx --then-poll
```

它先回复 done（浏览器挂载变体），然后阻塞到用户的选择到来，所以按你的 harness 跑长等待的方式跑它：**Claude Code** 前台、用你工具的最长超时（600000 ms），你在选择到来前保持暂停；**Codex** 放进让权的前台 exec；**Cursor** 放进后台终端、notify 监听 `"type":"(accept|discard|variant_mount_failed|exit)"`。绝不传短的 `--timeout=`。它运行期间无事可做：绝不 sleep、绝不定时轮询它的输出；把它放入后台的 harness 会在它返回时叫醒你。`{"type":"timeout"}` 表示用户还没选：再跑一次 `live-poll`，继续等。如果浏览器翻到 GENERATING 之后编辑失败，用 `--reply EVENT_ID error "简短原因"`（不带 `--then-poll`），让底栏复位。

然后用一行话告诉用户变体在哪里：*"三个 [bolder] 变体已在 [价格卡] 上跑起来：用浮动条的箭头轮换，调 Tune 旋钮，Accept 留下的那一个。"*

replace 路径之外，行动前先读 live.md 对应小节：`scaffold.previewMode: "svelte-component"`（Svelte 预览按组件编辑，其接受是机械的）、`mode: "insert"`、`variant_mount_failed`、`steer`、`manual_edit_apply`，以及任何 `fallback: "agent-driven"` 的包装错误。

## Step 4: 接受并收尾

Step 3 的调用返回用户的选择。**`discard`**：无事可做。**`accept`**：`_acceptResult.carbonize: true` 是正常情况，清理就是 live.md 的 **accept 之后必须做（carbonize）**，原样不变：把被接受变体的规则用真实选择器移进已经拥有该元素的样式表，烧入选定的参数值，解开元素包装并去掉所有 `data-impeccable-*` 属性，删除内联 `<style>` 块与两个 `impeccable-carbonize` 标记，然后 `.claude/skills/impeccable/scripts/impeccable live-complete --id SESSION_ID` 并确认 `phase: "completed"`。（`baked: true` 只在接受带着 `--bake` 跑过时出现；那时 helper 已把变体固化，不再欠一次 `live-complete`。）

无需被要求，选择一处理完就收尾：

```bash
.claude/skills/impeccable/scripts/impeccable live-server stop
```

停止会移除注入的脚本并重载页面一次：用户看到被接受的设计、没有浮层装饰，仍由他们的 dev server 伺服。**绝不 kill 或重启 dev server**，包括你在 Step 2 里启动的那台。

- **你还没收尾，用户就要更多变体**：跳过收尾，对下一个元素重跑 Step 2（helper 会复用），最后一个选择之后再收尾。
- **被打断或不确定状态**：`.claude/skills/impeccable/scripts/impeccable live-status`，然后 `live-resume`；`.impeccable/live/sessions/` 下的日志是权威。

完成条件：helper 已停止，dev 站点仍以被接受的设计应答。
