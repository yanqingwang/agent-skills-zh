> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/live.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

交互式实时变体模式：在浏览器里选中元素、选一个设计动作，拿到 AI 生成的 HTML+CSS 变体，经开发服务器的 HMR 热替换。

## 前提条件

一个带 HMR 的开发服务器在跑（Vite、Next.js、Bun 等），或一个在浏览器中打开的静态 HTML 文件。如果开发服务器的默认端口被占用，应用很可能已经在跑；先探测默认 URL，再考虑起第二个服务器。

实时编辑需要本地检出；不支持注入已部署的生产站点（包括 HTTPS）。生产站点检查用 `.claude/skills/impeccable/scripts/impeccable detect <url>` 或浏览器扩展，不用 live helper。不要为了开启 live 模式而关闭浏览器安全机制或削弱生产 CSP。

## 契约（读一次）

按顺序执行。不跳步，不换序。live 模式下每个工具输出都可能带一个 `_instructions` 字段：它是该具体情形下权威的下一步，已代入真实 id 和路径；它与你对本文档的记忆冲突时，以 `_instructions` 为准。唯一例外：打印出的 `live-wrap` 若 `--element-id` 与 `--classes` 均为空，改按包裹步骤中的裸元素规则处理（两个都去掉，传 `--query`）。

1. `impeccable live --allow-missing-context --dev-url`：启动（永远带这两个 flag；见启动一节）。请求点名或暗示 monorepo 内的某个文件、路由或应用时，推断具体路径并加 `--target <path>`；然后本次 live 会话的其余部分都从返回的 `projectRoot` 运行。启动时从开发服务器配置文件解析应用根并持久化到 `.impeccable/live/roots.json`；每个 helper 启动时都重新锚定到该清单（错误的 cwd 无法分裂会话状态），PRODUCT.md / DESIGN.md 沿目录向上找到 git 根为止，`--file` 之类的相对 helper 参数相对应用根解析。
2. 打开页面。凡是启动输出的 `_instructions` 说要打开某个 `pageFiles` 页面，都用这个方法找 URL。`devUrl` 是在跑的开发服务器的 origin：追加请求点名的路由，或服务目标 `pageFiles` 条目的路径；光秃秃的 `devUrl` 只是根页面。`devUrl` 为 null 且项目没有 dev 脚本（静态文件夹）时，直接打开其 `pageFiles` HTML，包括 `file://`。为 null 但有 dev 脚本时，探测可能只是漏掉了跑在未列出端口或 HTTPS 上的服务器：先查终端输出、dev 配置的端口和已打开的标签页，只有确实没东西在跑才启动 dev 脚本（包管理器的 `dev`，放后台），然后重新 boot。绝不用 `serverPort`；那是 helper 的，不是应用的。永远用一行话把 URL 告诉用户，让你没有浏览器工具时他们可以自己打开；项目的第一次 Live 会话还要在同一句话里加上第一步：打开 Pick（页面底部栏的十字准星），点任意元素，说要改什么，按 Go。**Cursor：** 轮询之前先 `browser_navigate` 到该 URL；不要跳过。**其他 Harness：** 用可用的浏览器工具；找不到 URL 时问用户一次。
3. 轮询循环用默认长超时（600000 ms）。每个事件或 `--reply` 之后立刻再跑 `impeccable live-poll`；Codex 在前台跑这个一次性轮询。绝不传短的 `--timeout=`。没有任何东西在轮询 `/poll` 时，全局栏的 **Impeccable 标记**会变暗并带闪烁的琥珀色圆点；重启 `impeccable live-poll` 重连。
4. 收到 `generate`：有 `event.scaffold` 就复用；有截图就读；加载该动作的参考文档；交付变体；`--reply done`；再轮询。在本线程里生成：项目的 token 与布局你手里已经有。悬浮预览就是验证通道；generate 与 accept 之间不要截图、重渲染或 QA 变体。写作时就把 craft-floor 的对比度、间距与字体底线按构造保证；完整验证只在 accept 时对被选中的变体跑一次。
5. 收到 `steer`：读消息与 `pageUrl`；干活；`--reply steer_done`；再轮询。不发送接单确认。
6. 收到 `accept` / `discard`：轮询脚本运行 `impeccable live-accept`，确认交付，并打印 `_completionAck`。普通 accept/discard 立即终结；carbonize accept 在 `impeccable live-complete --id EVENT_ID` 跑过之前保持可恢复。先完成那次清理，再轮询。
7. 中断时先跑 `impeccable live-status` 或 `impeccable live-resume`，不要靠猜。`.impeccable/live/sessions/` 下的日志是权威状态，helper 重启后回放未确认的工作；注入的 `live.js` 在页面重开时重新附着。只有 `impeccable live-resume` 报告没有活动会话时才回退到直编循环，绝不因为断连感觉频繁而回退。
8. 收到 `exit`：执行文末的清理。

Harness 策略：
- **Claude Code**：把轮询作为**后台任务**跑（不设短超时）；harness 完成时通知你。不要阻塞 shell。
- **Cursor**：在**后台终端**跑**一次性**轮询，监听 `"type":"(steer|generate|accept|discard|manual_edit_apply|variant_mount_failed|prefetch|exit)"` 的通知；处理、`--reply`、重启轮询。Cursor 上**不要**用 `--stream`（实测取件约 5 秒，一次性轮询亚秒）。
- **Codex**：默认在**让出的前台 exec 会话**里跑一次性轮询。不用 `&`，不用 `--stream`，绝不在没有活动前台轮询的情况下离开 Live。启动轮询还不够：要**照看**它（持续读这个 exec 会话直到它返回一个事件）。绝不宣布"等待用户"然后闲置；没人读的让出式轮询是死会话，用户的 Go 无人应答。
- **其他 Harness**：默认前台一次性轮询，除非你确知 shell 退出时 stdout 能可靠返回。

交付策略：处处原子化单次编辑交付；除非已知某 Harness 的轮询循环不会因额外调用而阻塞，否则不要把它切到渐进发布。

对话是开销。不复述、不输出教程、不粘贴 PRODUCT / DESIGN 正文。token 花在工具与编辑上；失败时给一两句短话。

## 轮询循环

```
LOOP:
  .claude/skills/impeccable/scripts/impeccable live-poll   # default long timeout; no --timeout=
  Read JSON; dispatch on "type"

  "generate"  → Handle Generate; reply done; LOOP
  "steer"     → Handle Steer; reply steer_done; LOOP
  "accept"    → Handle Accept; complete carbonize cleanup if required; LOOP
  "discard"   → Handle Discard; LOOP
  "prefetch"  → Handle Prefetch; LOOP
  "manual_edit_apply" → Handle Manual Edit Apply; reply done|partial|error; LOOP
  "variant_mount_failed" → Fix the variant files; reply done --file <path>; LOOP
  "timeout"   → LOOP
  "exit"      → break → Cleanup
```

`variant_mount_failed` 表示浏览器无法渲染你发布的东西（`variant`、模块 `url`、`error`）。用户看到的是一张持续存在的错误卡，不是变体。修好变体文件，然后 `--reply EVENT_ID done --file <manifest or source path>`；浏览器会自行重试。

**Stream 模式**（`--stream`，实验性，Cursor 上绝不用）：一个长驻进程，每个事件一行 JSON，`--reply` 用单独的命令发。只给能可靠读取增量 stdout 的 harness 用。

## 启动

```bash
.claude/skills/impeccable/scripts/impeccable live --allow-missing-context --dev-url
```

输出 JSON：`{ ok, serverPort, serverToken, pageFiles, roots, targetPath, devUrl, contextMissing, hasProduct, product, productPath, hasDesign, design, designPath, hasSurfaceBrief, surfaceBrief }`。`devUrl` 是服务该页面的在跑开发服务器，没有响应时为 null。`contextMissing` 在 PRODUCT.md 或 DESIGN.md 缺失时列出它们：Live 从不等 init 或 document。按下文直接从页面干活，`init` 或 `document` 在会话结束后再提议，不要提前。`roots` 是解析出的根清单；`projectRoot` 即 `roots.appRoot`。surface brief 随启动结果一起给出，不要另外 shell 调 `impeccable surface-brief`。生成优先级：**视觉决策 DESIGN.md 优先；长期产品与语气决策 PRODUCT.md 优先；本界面的策略以 surface brief 为准。** DESIGN.md 缺失不代表身份缺失；从 CSS 变量、计算样式与相邻组件中提取（第 4 步 Phase A）。保留身份是默认；偏离需要用户明确的重新设计意图。

`serverPort`/`serverToken` 属于小型 helper HTTP 服务器（`/live.js`、SSE、`/poll`），不是你的开发服务器；页面 URL 是服务某个 `pageFiles` 条目的任意 origin。

输出为 `{ ok: false, error: "config_missing" | "config_invalid", path }` 时，该项目需要一次性配置。常见情形一步搞定：应用根下有一个作为页面外壳的 `index.html`（Vite、React 或纯 HTML 文件夹），且 `.claude/skills/impeccable/scripts/impeccable detect-csp` 报告 `shape: null`，就在启动输出报告的 `path` 处写入 `{"files":["index.html"],"insertBefore":"</body>","commentSyntax":"html","cspChecked":true}`，然后重新 boot。页面名不同的静态文件夹把那个文件列进 `files`。其他情况（别的框架、有 CSP、多个 HTML 文件）：读 [live-setup.md](live-setup.md) 并照做。输出带非空 `configDrift` 时，向用户提一次哪些 HTML 文件未被覆盖，建议补充或把 `files` 换成 glob；绝不自动改配置。

## 恢复命令

`.impeccable/live/sessions/` 下的只追加日志是权威持久状态（不是项目源码）。对话被打断、轮询被漏掉、helper 重启或浏览器重载之后：

```bash
.claude/skills/impeccable/scripts/impeccable live-status      # helper state, active sessions, queued events; works with the helper down
.claude/skills/impeccable/scripts/impeccable live-resume --id SESSION_ID   # active snapshot, pending event, next safe action
.claude/skills/impeccable/scripts/impeccable live-complete --id SESSION_ID # canonical manual final acknowledgement after verified cleanup
```

服务器重启规则：重新启动 `impeccable live-server`，然后轮询；启动时会重新入队未确认的事件，所以绝不请用户再点一次 Go，除非 `impeccable live-resume` 说没有活动会话。

## 处理 `generate`

**替换模式**（默认）：`{id, action, freeformPrompt?, count, pageUrl, element, screenshotPath?, comments?, strokes?}`。

**插入模式**（`event.mode === "insert"`）：`{id, mode: "insert", count, pageUrl, insert: { position, anchor }, placeholder: { width, height }, freeformPrompt?, screenshotPath?, comments?, strokes?}`。没有 `action`；要求非空 `freeformPrompt` **或**标注。`placeholder` 是软性尺寸提示。

速度要紧；用户正盯着选中的元素。复用 preflight 元数据，尽量少做发现调用。

### 插入模式分支

1. 有截图就读（只包含标注）。
2. 有 `event.scaffold` 就用它，**不要**再跑 helper。否则：

```bash
.claude/skills/impeccable/scripts/impeccable live-insert --id EVENT_ID --count EVENT_COUNT --position after \
  --element-id "ANCHOR_ID" --classes "class1,class2" --tag "section" --text "ANCHOR_TEXT"
```

`--position` ← `event.insert.position`；锚点 flag 的映射与 wrap 完全一致。脚手架里**没有** `data-impeccable-variant="original"`；变体是在 `insertLine` 处全新写的 HTML+CSS。source-preview 目标上脚手架带 `sourceWritten: false`，附 `wrapperBlock` 与 `replaceEndLine < replaceStartLine`（一次插入）：把变体拼进 `wrapperBlock` 的标记处，并按 wrap 一节所述在**一次编辑**中插入到 `replaceStartLine`。从界面判断 visitor 模式，并在写全新标记之前加载 [craft-floor.md](craft-floor.md)。Svelte 目标遵循与下文 wrap 相同的组件流程（manifest 中 `mode: "insert"`）：每个变体都是 `componentDir` 下真实单根组件，不带 `data-impeccable-*` 属性；生成期间绝不编辑 route；accept 机械地把被选中的标记拼进 `sourceFile`。非 Svelte 目标上，accept/discard 会移除包裹层；锚点不动。

### 替换模式（默认）

### 1. 读截图（如有）

`event.screenshotPath` **只在用户按 Go 前做了标注时**发送；是一张把标注烧进画面的元素 PNG。规划前先读。没有时不要索要、也不要自己截页面：没有标注的截图会把你的注意力锚在现有设计上，与"三个方向各不相同"的简报相悖；从 `element.outerHTML`、计算样式和提示词出发。

标注语义：评论的 `{x, y}` 是元素局部坐标，把文字绑定到该点下的子元素（标题附近的评论说的是标题）。评论与笔迹相互独立，除非明显成对。笔迹按形状读：闭合圈 = "这个东西"（强调，不是裁剪区域）；箭头 = 方向或运动；叉/斜线 = 删除；涂画 = 按上下文判断强调或删除。笔迹意图确实模糊且影响简报时，生成前先问一个短问题；否则用一句话陈述你的解读。

### 2. 包裹元素

有 `event.scaffold` 时，helper 已找到源码并算出包裹层；当作成功结果处理，跳过命令。`event.scaffoldAttempted` 带 `scaffoldError` 表示 preflight 没跑完；用下面的命令。

**source-preview 目标上 `event.scaffold` 带 `sourceWritten: false`。** helper 没有写包裹层；它交给你 `scaffold.wrapperBlock` 加选中元素的源码范围（`replaceStartLine`、`replaceEndLine`，1 起始）。包裹层与全部变体写在**一次编辑**里：把变体拼进 `wrapperBlock` 的 "Variants: insert below this line" 标记处，然后用结果替换 `[replaceStartLine, replaceEndLine]` 行。分开写会让框架在你的变体落地之前就重载，浏览器停在 0/N。`replaceEndLine < replaceStartLine` 表示插入模式：只插入，不删除任何东西。`svelte-component` 路径从不设置 `sourceWritten`。

```bash
.claude/skills/impeccable/scripts/impeccable live-wrap --id EVENT_ID --count EVENT_COUNT --element-id "ELEMENT_ID" --classes "class1,class2" --tag "div" --text "TEXT_SNIPPET"
```

flag 映射（分开传，绝不并进 `--query`）：`--element-id` ← `event.element.id`；`--classes` ← class 用逗号连接；`--tag` ← tagName；`--text` ← textContent 前 80 字符左右，**每次都传**：它用来区分重复的兄弟组件，不传时 wrap 会落到第一个匹配。`event.pageUrl` 能推知文件时传 `--file PATH`。`--text` 仍匹配到多个候选时，wrap 以 `{ error: "element_ambiguous", candidates, fallback: "agent-driven" }` 退出：从页面上下文选出正确范围，按回退流程手写包裹层。映射的唯一例外是既无 id 也无 class 的元素（裸 `<h1>`，新页面上的常见首选）：两个空 flag 会让 wrap 以 `Need at least one of` 退出，所以去掉它们，把开始标签前缀当作查询，h1 就传 `--query "<h1"`（它也能匹配带其他属性的标签），`--tag` 与 `--text` 照旧。少于八个字符的文本区分不了重复标签，wrap 会落到第一个：文件里有多个该标签元素时，读 wrap 返回的行，若原槽位里的元素与所选元素不同，在写任何变体之前先手工重做 wrap：删掉 wrap 添加的行（两个标记、包裹 div、围绕该元素的原槽位 div），让文件恢复原样，然后按回退流程在所选元素所在处写同样的包裹层。包裹层必须落在所选元素的位置：accept 与 discard 都在包裹层位置写。绝不用 `live-accept --discard` 撤销错误的 wrap：那会把会话记为已丢弃，用户随后的 Accept 会被拒绝。

成功输出：`{ file, insertLine, commentSyntax, styleMode, styleTag, cssSelectorPrefixExamples, cssAuthoring }`（source-preview 目标上另加上面的 `sourceWritten: false` 字段）。没有 preflight 脚手架直接运行时，它自己写包裹层，你在 `insertLine` 处拼入变体。`styleMode` 决定预览 CSS 必须怎么写。把它当作检测出的能力模式，不是框架猜测：`scoped` 表示用 `@scope ([data-impeccable-variant="N"])` 规则；`astro-global-prefixed` 表示显式 `[data-impeccable-variant="N"]` 前缀，并用返回的精确 `styleTag`。把 `cssAuthoring` 当作当前文件的唯一事实来源（styleTag、选择器策略、要求、禁止模式）；它没说的框架例外不要套用。

Svelte/SvelteKit 目标上，`impeccable live-wrap` 返回 `previewMode: "svelte-component"`，`file` 指向临时 `node_modules/.impeccable-live/<id>/manifest.json`，`componentDir` 装变体组件，`sourceFile` 是真实 route。脚手架基于 AST：控制流块（`{#each}`、`{#if}`）原样保留，自由 each 集合以单个结构化 prop（kind `collection`）跨过契约。payload 含 `componentStubMarkup`（已替入 prop 并写进每个 stub 的标记），所以不要回读 manifest 或 stub。就地**编辑** `v1.svelte`、`v2.svelte`…；绝不删除重建；保留 stub 的控制流与 `propContract` 的 prop 名；绝不把循环摊平成字面量条目。stub 的 `<style>` 已预置当前给选中内容定样式的源规则；随意改写或删除。accept 时，变体未重新声明的预置规则会从源码中**移除**（预览从未应用它，用户批准的是没有它的设计）。用语义 class 选择器，不用 `@scope`，不用 `data-impeccable-*`。回复时 `--file` 设为 manifest 路径；浏览器挂载编译后的组件，Svelte HMR 因此不重置页面状态。accept 机械地把所选组件并回（标记还原为 route 表达式、CSS 对账、参数烘焙、缩进保留）；这条路径上你没有 accept 后的清理。选中内容包含脱离式预览无法支持的结构（组件标签、`bind:`/`use:`、await 块、内联脚本、展开属性）时，wrap 返回普通 source-preview 包裹层并带 `previewFallback: { from: "svelte-component", reason }`；照返回的形状走即可。

**组件预览路径上的参数放在 sidecar 里，绝不作为属性**（Svelte 把属性值里的 `{` 解析为表达式）。在 `componentDir/params.json` 中按变体号声明，用第 7 节的 schema：

```json
{ "1": [ {"id":"density","kind":"steps","default":"snug","label":"Density","options":[
    {"value":"airy","label":"Airy"},{"value":"snug","label":"Snug"} ]} ] }
```

组件 `<style>` 针对 `range`/`toggle` 用 `var(--p-<id>, default)`、`steps` 用 `[data-p-<id>="…"]` 来写，包在 `:global(...)` 里，让挂载根上的运行时旋钮值能命中你的规则。

**回退错误。** wrap 拒绝写入非源码文件（生成文件、未跟踪文件）：accept 进那种文件是静默数据丢失。三种形状，都带 `fallback: "agent-driven"`（见 **处理回退**）：`file_is_generated`（你的 `--file` 指向生成文件）、带 `generatedMatch` 的 `element_not_in_source`（元素只存在于生成结果中）、`element_not_found`（多半是运行时注入的）。

### 3. 加载动作的参考文档

`event.action` 是 `impeccable`（自由发挥）：从 SKILL.md 的设计规则加 [craft-floor.md](craft-floor.md) 出发；从界面判断 visitor 模式；不加载子命令参考。自由发挥不是跳过参数的通行证：遵守第 7 节的预算与自由发挥偏好。其他动作（`bolder`、`quieter`、`distill`、`polish`、`typeset`、`colorize`、`layout`、`adapt`、`animate`、`delight`、`overdrive`）：规划前读 `reference/<action>.md`；其 MUST 参数叠加在第 7 节预算之上。

### 4. 规划三个变体：先身份，再模式，再变化轴

Live 在既有界面上运行；品牌已经选定。任务是**身份之内**的变化，不是在身份之间挑选。最糟的失败是三个跑出品牌的、用户无法接受的变体。四个阶段，按顺序。

#### Phase A: 提取身份（不可跳过）

来源按优先级：DESIGN.md 的视觉系统字段；CSS 自定义属性（事实上的 token）；选中元素及其父级的计算样式；相邻组件的视觉修辞。写**一句话**记录屏幕上实际存在的东西：主导表面与强调色（真实值，不是"暖色"）、已加载的字体搭配、布局拓扑（堆叠 / 并排 / 网格 / 非对称 / 叠放）、表面处理（圆角、边框、阴影、装饰密度），以及文案透出的语气。要具体；宁可跳过某个轴也不要编造；不要给美学流派命名（那是结论，不是数据）。这句话就是**身份锁**：每个变体与它并排看都必须是同一个品牌。DESIGN.md 缺失绝不是借口。

#### Phase B: 选模式（默认 vs 偏离）

**默认**保留身份、在其内部变化表达；约 90% 的会话适用。**偏离**否定身份；只在用户当前请求或提示词里明确要求时触发（"redesign this"、"rebuild from scratch"、"something completely different"）；过时的批评或旧笔记不是授权。拿不准就选默认：错选默认的代价是"三个品牌内、感觉相近的变体"（可恢复），错选偏离的代价是三个跑出品牌的变体（不可恢复）。

#### Phase C: 规划三个变体

**默认模式。** 每个变体坚持一条不同的**主轴**，保留身份句。六条轴：1 **层级**（哪个元素统治视线）、2 **布局拓扑**（堆叠 / 并排 / 网格 / 非对称 / 叠放）、3 **字体排印系统**（搭配逻辑、比例阶梯、大小写/字重，*限现有字体*）、4 **颜色策略**（现有色板的哪个角色承担表面：Restrained / Committed / Full palette / Drenched；只用现有 token）、5 **密度**（极简 / 舒适 / 密集）、6 **结构分解**（合并、拆分、渐进披露）。三个变体，三条**不同**轴：同一品牌的三个角度。新字体、新色相或新美学流派信号只属于偏离模式。

**偏离模式。** 每个变体锚定到一条从品牌派生的不同美学方向，绝不用固定目录：读 PRODUCT.md 的 Brand Personality 词汇；推导能体现它们的实体、空间或材质体验；从中推出三条彼此真正不同、也与当前界面不同的方向；拒绝那种理由放在隔壁产品上也成立的条件反射式选择。每条方向必须是一句具体话，点名一个现实世界参照物（"a museum exhibition label system"，不是"干净极简"）。

**两种模式下都要在规划时说清每个变体的 2 或 3 个参数旋钮**（第 7 节预算）。参数是设计的一部分；规划阶段就决定"什么可调"，好过事后补。

#### Phase D: 眯眼测试

**默认：** 把每个变体对照 Phase A 的锁检查；色板、字体语气或修辞漂移说明它无意中越进了偏离：返工。然后确认三条不同的主轴；三个"密度更紧"的变体就是失败。**偏离：** 两遍检查，先流派后句子。流派遍（不可妥协）：给你自己选的具体流派给每个变体贴标签；标签相同或可互换意味着返工。句子遍：三句一行描述并排放；有两句押韵意味着返工。主轴是颜色或主题时，三件套不得共用主题 + 主导色相：三个色彩世界，不是三个深浅。

**动作专属调用**必须沿该动作的维度变化；默认模式下每次变化都留在现有字体与现有 token 之内：

- `bolder`：每个变体放大不同维度（尺寸 / 饱和度 / 结构变化）。
- `quieter`：每个变体收回不同维度（颜色 / 装饰 / 间距）。
- `distill`：每个变体去除不同类别的冗余（视觉噪声 / 冗余内容 / 嵌套结构）。
- `polish`：不同的精修轴（节奏 / 层级 / 微观细节）。
- `typeset`：偏离时每个变体同时变搭配与比例阶梯；默认时保留字体，各变比例阶梯、大小写与字重。
- `colorize`：偏离时每个变体不同色相族，并变化色度与对比策略；默认时每个变体用不同的现有色板角色承担表面（Restrained / Committed / Full palette / Drenched），并配不同对比策略。
- `layout`：不同的结构排布，不是间距微调。
- `adapt`：每个变体不同的目标语境（移动优先 / 平板 / 桌面 / 印刷或低带宽）。
- `animate`：不同的运动词汇（级联错峰 / 裁切擦除 / 缩放聚焦 / 形变 / 视差）。
- `delight`：不同口味的人格（微交互 / 字体排印惊喜 / 插画点缀 / 声音或触感 / 彩蛋）。
- `overdrive`：打破不同的惯例（尺寸 / 结构 / 运动 / 输入模型 / 状态转换）；跳过它的"提议并询问"步骤，live 是非交互的。

### 5. 应用自由提示词（如有）

`event.freeformPrompt` 是用户给方向设的天花板：所有变体遵守它，同时在 Phase B 模式之内探索不同解读。默认模式：提示词收窄的是轴，不是身份（"more confident" → 一个变体放大层级、一个押上强调色、一个收紧密度）。偏离模式：提示词收窄的是车道，不是流派（"newspaper front page" → 大报 vs 小报 vs 行业期刊，然后跑流派遍）。提示词与硬性品牌承诺或 DESIGN.md 不变量冲突时，保留不变量，除非用户明确撤销。

### 6. 交付变体

每个变体都是对原元素的完整 HTML 替换，不是只改 CSS 的补丁。预览 CSS 以 `<style>` 标签放在包裹层内。**原子默认：** CSS + 全部变体 + 参数清单在 `insertLine` 处一次编辑完成。

```html
<!-- Variants: insert below this line -->
<style data-impeccable-css="SESSION_ID">
  /* rules matching cssAuthoring.rulePattern */
</style>
<div data-impeccable-variant="1">
  <!-- variant 1: full element replacement (single top-level element) -->
</div>
<div data-impeccable-variant="2" style="display: none">
  <!-- variant 2 -->
</div>
<div data-impeccable-variant="3" style="display: none">
  <!-- variant 3 -->
</div>
```

工具返回不同的开头标签时，用 `cssAuthoring.styleTag` 替换 style 开标签，用 `cssAuthoring.styleClose` 收尾（`.vue` 上是 `</component>`）。**每个变体 div 恰好含一个顶层元素**，标签与原元素相同；散落的兄弟节点会破坏轮廓追踪与 accept。第一个变体可见，其余 `display: none`。浏览器的 MutationObserver 接受原子或渐进到达；accept 一个已到达的变体会给工作进程上栅栏，之后的发布会被拒绝。

`styleMode: "scoped"` 时，每条 `:scope` 规则都带后代组合器：`@scope` 边界是变体包裹 div，不是你的元素，裸 `:scope { ... }` 只会作用于 `display: contents` 的壳。总要深入一层（`:scope > .card`、`:scope .hero-title`）。[repo agent template](https://github.com/pbakaus/impeccable/blob/8dac6ae7e020c43ab10ce9b41939f6fd42627b96/tests/live-e2e/agent.mjs) 里假测试 agent 的 CSS 是一份忠实的模板。

**JSX / TSX 目标：** 把 `<style>` 内容包进模板字面量（CSS 花括号会被解析成 JSX），用 `className=` / `style={{…}}`，`data-impeccable-*` 属性保持普通字符串：

```tsx
<style data-impeccable-css="SESSION_ID">{`
  @scope ([data-impeccable-variant="1"]) { ... }
`}</style>
<div data-impeccable-variant="2" style={{ display: 'none' }}>
  {/* variant 2 */}
</div>
```

wrap 脚本提供单根 JSX 包裹层，标记注释在内；把块放到标记处，源码仍是合法 TSX。

### 7. 参数（构图级，每变体 0-4 个）

每个变体可以暴露**粗粒度**旋钮；浏览器为每个参数停靠一个控件，零再生成成本（旋钮驱动你的 scoped CSS 所针对的 CSS 变量或数据属性）。用户可能随口说"再紧一点"或"强调色再多一点"而并不想再生成时，就把那条轴做成参数；微边距与一次性微调不是参数。自由发挥偏好：轴是你选的，就暴露出来；0 参数的 hero 几乎总是错的，1 个偏少，除非设计是真正的定点。

预算随元素的视觉重量伸缩（数视觉子元素，不是 DOM 深度）：

- **叶子 / 微型**（按钮、图标、裸标题）：**0 参数。**
- **小构图**（简单卡片、带标签输入框、约 ≤ 5 个视觉子元素）：**0-1**。
- **中构图**（区块、导航簇，6-15 个子元素）：**目标 2**；简单则 1。
- **大构图**（hero、完整区域，16+ 个子元素或子区块）：**目标 2-3，最多 4**，前提是各独立轴都能在 CSS 里表达。

**硬上限：每变体四个。** 具名子命令的参考文档要求 MUST 参数且可表达时不可协商；尊重上限，不加重复旋钮。

HTML/JSX 路径上以包裹层属性**声明**（组件预览路径改用 `componentDir/params.json`，schema 相同，按变体号作键；见 wrap 一节）：

```html
<div data-impeccable-variant="1" data-impeccable-params='[
  {"id":"color-amount","kind":"range","min":0,"max":1,"step":0.05,"default":0.5,"label":"Color amount"},
  {"id":"serif","kind":"toggle","default":false,"label":"Serif display"}
]'>
```

三种：`range`（滑杆；驱动 `--p-<id>`；写作 `var(--p-color-amount, 0.5)`；字段 min/max/step/default/label）、`steps`（分段单选；驱动 `data-p-<id>`；写作 `:scope[data-p-density="airy"] .grid { ... }`；字段 options/default/label）、`toggle`（同时驱动 `--p-<id>: 0|1` 与属性存在性；字段 default/label）。切变体时重置是已知限制：每个变体从自己声明的默认值开始。

**accept 时**，浏览器发送当前值，`impeccable live-accept` 把它们写成旁注注释：`<!-- impeccable-param-values SESSION_ID: {"color-amount":0.7} -->`。Carbonize 清理会烘焙它们：只保留匹配所选值的 `steps`/`toggle` 分支，删掉其余，把 `:scope[data-p-…]` 折叠成语义规则；替换 `range` 字面量或更新变量默认值。

### 8. 发完成信号

```bash
.claude/skills/impeccable/scripts/impeccable live-poll --reply EVENT_ID done --file RELATIVE_PATH
```

`RELATIVE_PATH` 相对项目根；开发服务器没有 HMR 时浏览器直接抓源文件。然后立刻再轮询。

### 中止进行中的会话

浏览器已切到 GENERATING 之后 wrap 或生成失败时，告诉**浏览器**，让它的栏复位：`.claude/skills/impeccable/scripts/impeccable live-poll --reply EVENT_ID error "Short reason"`。这件事绝不用 `live-accept --discard`（那是纯文件修改器，浏览器永远看不见，栏会卡在圆点）；`--discard` 只用于浏览器自己发起的丢弃的源码侧清理。

## 处理回退

wrap 返回 `fallback: "agent-driven"` 时，源文件由你自己选；目标不变：立刻给出三个预览变体，并把被接受的那个持久化到下次构建抹不掉的地方。

1. 从错误 payload **找出元素真正住在哪**：`element_not_in_source` + `generatedMatch` 表示所服务的 HTML 是生成的，去找生成器的模板或 partial；`element_not_found` 表示运行时注入，去找渲染组件或数据源；`file_is_generated` 同理解决。纯视觉变化可能属于共享样式表而非模板。
2. **在所服务的文件里预览**：手工把 `impeccable live-wrap` 会产出的同样包裹脚手架写进浏览器实际加载的文件，把元素本体挪进原槽位：`<!-- impeccable-variants-start ID --><div data-impeccable-variants="ID" data-impeccable-variant-count="3" style="display: contents"><div data-impeccable-variant="original">THE ELEMENT, UNCHANGED</div><!-- Variants: insert below this line --></div><!-- impeccable-variants-end ID -->`。把变体 div 插在标记之后，然后 `--reply EVENT_ID done --file <served file>`。起始标记与结束标记各占一行：accept 按整行替换从标记到标记的内容，与其他标记共用一行的标记会连那部分标记一起带走（单行或压缩过的文件，先把元素周围的行拆开）。绝不省掉原槽位：discard 从它恢复元素，没有原槽位的包裹层会被拒绝。这次编辑是临时的；重新生成把它抹掉也没关系。
3. **accept 时写到真实源码**（accept 拒绝生成文件，所以这里 `_acceptResult.handled` 通常是 `false`）：结构变化 → 模板/组件源码；纯视觉 → 对应的样式表；由数据渲染的内容 → 数据源或渲染逻辑。然后从所服务的文件中移除临时包裹层。
4. **discard 时**，只移除临时包裹层。

## 处理 `accept`

事件：`{id, variantId, _acceptResult, _completionAck}`。轮询脚本已确定性运行 `impeccable live-accept` 并确认交付；浏览器 DOM 已更新。

- accept 事件带 `pageUrl`；轮询脚本必须把它转发给 `impeccable live-accept --page-url PAGE_URL`，让 accept 时清理只擦除当前页面的暂存文案编辑。
- `_completionAck.ok !== true`：先不要轮询。跑 `impeccable live-status` / `impeccable live-resume`，必要时手工收尾清理，然后 `impeccable live-complete --id EVENT_ID`。
- `handled: true, carbonize: false`：无事可做；再轮询。
- `handled: true, carbonize: true`：需要下文的清理；`_acceptResult.todo`、`_completionAck.requiresComplete` 与 stderr 横幅都指向它。
- `handled: false, mode: "fallback"`：会话发生在生成文件里；回退第 3 步已写真实源码；清掉临时包裹层再轮询。
- `handled: false, mode: "error"`：**不要手改文件。** `source_locked`：重跑同一条 `impeccable live-accept` 命令（幂等），直到发布器释放。`accept_receipt_conflict`：会话已按 `priorOperation` 解决；跑 `impeccable live-status` 并告知用户。其他：简短报告，先跑 `impeccable live-status`。
- 没有 `mode` 的 `handled: false`：手工清理：读文件、找标记、编辑。

### accept 之后必须做（carbonize）

`carbonize: true` 表示被接受的变体以 helper 标记与内联 CSS 缝进源码（浏览器因此无间隙渲染）。这次缝入是临时的；先把它改写成永久形态再做任何其他事，否则死的 `@scope` 规则、包裹 div 与标记注释会跨会话累积。五步，同步完成，赶在下一次轮询之前：

1. 在 `_acceptResult.file` 中**定位 carbonize 块**：由 `<!-- impeccable-carbonize-start/end SESSION_ID -->` 包围，内含 `data-impeccable-css` style 元素；有 `<!-- impeccable-param-values -->` 注释就先读它，第 3、4 步靠它。
2. **把 CSS 规则搬进**项目真正的样式表（哪个样式表已经负责周边元素的样式就用哪个）。
3. **改写选择器时烘焙参数值**：把 `@scope ([data-impeccable-variant="N"])` 改指向真实语义类；只保留匹配所选值的 `:scope[data-p-<id>="VALUE"]` 分支；替换 `var(--p-<id>)` 字面量或更新变量默认值。
4. **给被接受的内容解包**：删除内层变体 div（JSX 上还有外层 `data-impeccable-carbonize` div）；去掉 `data-impeccable-params` 与所有 `data-p-*` 属性。
5. **删除**内联的 `data-impeccable-css` style 元素、参数值注释、两个 carbonize 标记，以及任何针对未接受变体的 `@scope` 规则。

然后运行 `impeccable live-complete --id SESSION_ID`，确认 `phase: "completed"` 后再轮询。这条命令是闸门，不是形式：只要还有任何 live 模式残留，它就以 `error: "source_dirty"` 加检查结果拒绝；修好重跑（`--force` 只用于误报）。

## 处理 `discard`

事件：`{id, _acceptResult, _completionAck}`。轮询脚本已恢复原元素并确认 `discarded`。无事可做，除非 `_completionAck.ok !== true`；那就 `impeccable live-complete --id EVENT_ID --discarded` 再轮询。

## 处理 `steer`

事件：`{id, message, pageUrl}`：来自全局栏 Steer 控件的页面级指令（打字或语音），没有元素上下文，不轮换变体。读 `message`，按需检查页面或文件，做编辑或用文字回答。回复 `.claude/skills/impeccable/scripts/impeccable live-poll --reply EVENT_ID steer_done ["Optional short toast"]`，失败则 `--reply EVENT_ID error "Short reason"`，然后立刻轮询。没有单独的接单回复；Steer 栏在 `steer_done` 或 `error` 时解锁。

## 处理 `prefetch`

事件：`{pageUrl}`：首次选中时每个路由触发一次；用户多半马上要在你没读过的页面上按 Go。把路由解析到文件（根 `/` 通常是启动输出的 `pageFile`；多页站点常把 `/foo` 映射到 `public/foo/index.html`；SPA 把一切都映射到同一个入口），读它，再轮询。不用 `--reply`。没有把握解析时，跳过并轮询。

## 处理 `manual_edit_apply`

事件：`{id, pageUrl, batch: {entries}, evidencePath?, chunk?, repair?, deadlineMs}`。

用户已经点了 Apply。不要问怎么办、不要丢弃、不要转回 Go。父 live 线程保持前台轮询循环，并发送最终的 `/poll --reply --data`。

原生子代理可用时，把源码编辑委托给 `impeccable_manual_edit_applier` / `impeccable-manual-edit-applier`。传入 cwd、脚本路径、事件 id、页面 URL、chunk/deadline、`batch`、`evidencePath` 以及规范 JSON 结果 schema。子代理不得轮询或回复。不可用时，按同样契约内联执行。

带 `deleted: true` 与 `removeElement: true` 的操作是浏览器的 Remove 徽标：从源码删除整个元素，子元素包含在内，不只是它的文本。先按 `sourceHint` 定位，再按 `leaf.outerHTML` 与 `originalText` 定位，精确移除该元素的源码范围；不留空包裹层、孤儿子元素或悬空标记。

有 `repair` 时，上一次 Apply 改了源码但最终验证失败。修当前源码并返回同一份规范 JSON 结果；不要自己回滚文件。任何回滚之前浏览器都会先问用户。

源码编辑完成后，只回复一次：`.claude/skills/impeccable/scripts/impeccable live-poll --reply EVENT_ID done --data '{"status":"done","appliedEntryIds":["8hexid"],"failed":[],"files":["src/page.html"],"notes":[]}'`。并非每个条目都应用成功时用 `status:"partial"` 或 `status:"error"` 加 `failed[]`。然后再轮询。绝不不带事件 id 回复；manual Apply 用 `--reply done --file ...` 无效。

## 退出

用户通过在对话里说停、关闭标签页（SSE 断开；轮询 8 秒后返回 `exit`）或浏览器退出按钮来停止 live 模式。收到 `exit`，杀掉仍在跑的后台轮询，然后清理。

## 清理

```bash
.claude/skills/impeccable/scripts/impeccable live-server stop
```

停止 helper 并运行 `impeccable live-inject --remove` 移除注入脚本（想快速重启就保留时用 `stop --keep-inject`；`.impeccable/live/config.json` 作为项目配置保留）。然后搜索并移除任何残留的 `impeccable-variants-start` 包裹层与 `impeccable-carbonize-start` 块。

## 首次配置

仅当 `impeccable live` 报告 `config_missing` / `config_invalid`、`configDrift` 需要解释、或配置缺少 `cspChecked` 时：读 [live-setup.md](live-setup.md)。它掌管配置 schema、各框架的 `files` 表、注入适配器、漂移修复，以及 CSP 检测与同意流程。
