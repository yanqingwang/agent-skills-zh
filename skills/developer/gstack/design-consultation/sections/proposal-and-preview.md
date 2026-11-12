<!-- AUTO-GENERATED from proposal-and-preview.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
<!-- The font-selection procedure and the three-looks calibration in this section are derived from pbakaus/impeccable reference/new-work.md (Apache-2.0), rewritten and modified. See NOTICE.md. -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`design-consultation/sections/proposal-and-preview.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Phase 3：完整提案

完整读本节，然后应用其设计/字体规则 → 独立起草 → 征求外部声音 → 为
Q2 综合。预览与写入需要各自的后续批准。

### 你的设计知识（用于给提案提供依据，**不要**以表格形式展示）

**校准：三种观感。** 避免可预测的构图：米色/衬线/陶土色；近黑/霓虹/
发光边缘；或大开张细线/斜体衬线/微小字距等宽。只有 brief 明确要求时才
用其中一种。否则选一个扎根于**这些用户**的方向，而不是品类刻板印象或
其显而易见的反面。例如书籍产品可以从封面与布料的颜色取色，而不是默认
米色加衬线。

**美学方向**（选贴合产品的那个）：
- Brutally Minimal：只有字体与留白。无装饰。现代主义。
- Maximalist Chaos：密集、分层、图案重。Y2K 遇上当代。
- Retro-Futuristic：复古科技怀旧。磷光配色、点阵字体、数据用暖等宽
  （不用发光光晕，不用网格纸背景）。
- Luxury/Refined：衬线、高对比、慷慨留白、贵金属。
- Playful/Toy-like：圆润、有弹性（不过冲）、大胆原色。亲和好玩。
- Editorial/Magazine：强排版层级、非对称网格、拉引语。
- Brutalist/Raw：暴露结构、单一实用 grotesk、可见网格、不修饰（仅在
  用户点名时才用系统字体栈）。
- Art Deco：几何精确、金属点缀、对称、装饰边框。
- Organic/Natural：大地色、圆润形态、手绘质感、颗粒。
- Industrial/Utilitarian：功能优先、数据密集、等宽点缀、低饱和配色。

**装饰层级：**minimal（排版承担全部）/ intentional（微妙质感、颗粒或
背景处理）/ expressive（完整创意方向、分层纵深、图案）

**布局手法：**grid-disciplined（严格栏宽、可预测对齐）/
creative-editorial（非对称、重叠、破网格）/ hybrid（应用用网格，营销用
创意）

**配色手法：**Restrained（1 个强调色加中性色，颜色稀少且有意义）/
Committed（一个色相主导页面，中性色由它派生）/ Full palette（primary
加 secondary 加语义色构建层级）/ Drenched（颜色是主设计工具，由表面
承载）

**动效手法：**minimal-functional（只保留帮助理解的过渡）/ intentional
（微妙的入场动画、有意义的状态过渡）/ expressive（完整编排、滚动驱动、
俏皮）

**选字体：一个流程，不是一份菜单。**（1）点名受众所处的世界（出版物、
记号法、他们阅读的身份或物体）与模式：Persuade（营销）、Operate（任
务）、Read（长内容）、Experience（沉浸）。匹配其语气。（2）为
display/body/label/mono 每个角色各列三个候选。（3）应用角色排除。
（4）经 WebSearch/Aside 核对每个拟用字族在 Google Fonts/Fontshare 官方
条目上的确切名称、所需字重、许可与加载 URL；本地字体则检查其文件与许
可。无法核实的字体直接去掉。（5）写明核实过的加载来源与策略。

**字体验证兜底：**跳过竞品调研不免除字体验证。离线就检查本地文件/许
可。否则描述角色/字重/比例，并在 DESIGN.md 中把字体选择标为待验证。继
续配色/布局；把预览推迟到字体可验证之后，或尊重用户跳过。不发明字体或
URL。

**过度使用，不得作 display**（任何表面的 display 声部都不用；下方
body/UI 例外是唯一例外；检测器会把其中几个标为 `overused-font`）：
Inter、Roboto、Arial、Helvetica、Open Sans、Lato、Montserrat、
Poppins、Space Grotesk、Space Mono、Fraunces、Playfair Display、
Cormorant、Lora、Crimson、Newsreader、Syne、IBM Plex Sans、
IBM Plex Serif、DM Sans、DM Serif、Outfit、Plus Jakarta Sans、
Instrument Sans、Geist。

**在 Operate 或 Read 表面作 body/UI 可以，当提案如此声明时：**
DM Sans、Instrument Sans、IBM Plex Sans。**数据与代码用等宽：**
JetBrains Mono、IBM Plex Mono、Fira Code。

**任何角色都禁用：**Papyrus、Comic Sans、Lobster、Impact、Jokerman、
Bleeding Cowboys、Permanent Marker、Bradley Hand、Brush Script、Hobo、
Trajan、Raleway、Clash Display、Courier New。

**不在任何默认清单里但可自由获取的字体**（2026-09-08 核实；会话内重
验；离线见字体验证兜底）：Satoshi、General Sans、Clash Grotesk、
Cabinet Grotesk（Fontshare）；Instrument Serif、Source Sans 3、
JetBrains Mono、Fira Code（Google Fonts）。清单故意短。列一长串"好"
字体，正是上一次趋同发生的方式。

用户点名要清单内的字体：照办，把权衡说一次。

**反趋同指令：**跨项目生成时变化美学、字体与配色；重复要有理由。明暗
不是可调项之一：按使用场景（谁、在哪、什么光线）定死，直到场景改变。
无故趋同就是 slop。

**AI slop 反模式**（绝不出现在你的推荐里）：
- 紫/紫罗兰/靛蓝渐变背景，或蓝到紫的配色
- **三列功能网格**：彩色圆里的图标加粗标题加两行描述，对称重复三次。
  最能认出 AI 的布局。
- 彩色圆里放图标作分区装饰（SaaS 模板外观）
- 全部居中（所有标题、描述、卡片都 `text-align: center`）
- 每个元素都用同样圆润的 border-radius（所有东西同一个大圆角）
- 装饰性斑块、漂浮圆、波浪 SVG 分隔（某节显得空，是需要更好的内容，
  不是装饰）
- Emoji 当设计元素（标题里的火箭、把 emoji 当 bullet）
- 卡片左侧彩色边框（`border-left: 3px solid <accent>`）
- 泛用 hero 文案（"Welcome to [X]"、"Unlock the power of..."、
  "Your all-in-one solution for..."）
- 模板化分区节奏（hero → 3 个功能 → 推荐语 → 定价 → CTA，每节同高）
- system-ui 或 `-apple-system` 当**主** display/body 字体：那句"我放弃
  排版了"的信号。选一个真正的字体。
- 圆角卡片上的彩色边：穿了戏服的侧标签。用背景色调、图标或标签示意
  状态。
- 把训练数据里的默认值当 display 声部，说明你已经停止观察。作为
  Operate 或 Read 表面的 body/UI，其中几个是可以的。说明是哪些、为什么。
- 标题与正文只差一档大小。选一个刻度，让层级之间的差异大于一个字重。
- 强调就靠字重或字号。渐变文字是穿了戏服的强调。
- 米色底、衬线 display、陶土色点缀：观感一号。brief 要求时没问题；没
  要求时就是默认值。
- 卡片里套卡片永远是错的。卡片是懒惰的容器；嵌套它们等于懒惰的平方。
- 用 CSS 形状拼出插图替代素材。要么产出素材，要么什么都不发。
- 深色表面上的发光边缘：观感二号。纵深是有偏移的；零偏移的彩色光晕是
  装饰。
- hero 内容后面的径向渐变光晕。又是观感二号。
- 洗刷页面顶部的聚光灯。与光晕同族。
- 无限滚动的 logo 条。logo 重要就静态展示；不重要就删掉。
- 每个标题上方一个圆角方块图标。试试并排，或去掉容器。
- 观感三号：为求编辑可信度而拉斜的 display 衬线。用内容挣来，或把
  display 站正。
- hero 大标题上方漂浮的胶囊标签。大标题自带分量；删掉那个 chip。
- 标题上方的 kicker 是最强的默认项：标题自带分量，删掉标签。用户坚持
  要就照办，把权衡说一次。
- "Seamless"、"effortless"、"supercharge"、"streamline"：什么也没描述
  的词。说产品做了什么。
- 短。有力。断句。每句都是口号。像人在解释一件事那样写。
- 在不是海报的页面上把 display 字体排到 6rem 以上。尺寸不是层级。
- "Built for the way you work"、"Designed for teams like yours"、
  "Meet your new..."：在表演发布而不是描述发布的句子。
- 渐变按钮当主 call to action。用配色拥有的一个实色。
- 泛用图库照片 hero，或用灰占位 div 顶替。展示产品，或什么都不展示。
- 圆角卡片加投影当一切内容的容器。用堆叠卡片做应用 UI 不是布局。
- 一排头像、五颗星、没人真的说过的推荐语。真名加真实主张，否则删掉。
- 模板化 hero：标题在左、截图在右、两个按钮。每个生成器抓的第一个模板。
- "Get Started" 与 "Learn More" 是唯一的 call to action。点名这次点击
  买到什么结果。
- hero 下方三个大数字配小标签（"10k+ users"、"99.9%"）。那是模板在
  数数，不是产品。
- 一堆同形、同图标位、同两行的卡片。把不等重的内塞进等大的盒子。
- 磨砂玻璃面板加模糊背景当默认表面。只在能解释纵深的地方用一层半透
  明，不是到处用。
- 用生成的 SVG 涂鸦与吉祥物替代艺术指导。委托或授权一个素材，或什么
  都不发。
- 每个次要动作都进模态框。内联、侧栏或新页面通常更省用户成本。
- 用火花线、进度环、假头像填满本该放内容的空间。真实数据或诚实的空
  状态。
- 因为它是开发工具就深色，因为它是健康产品就浅色。明暗来自使用场景：
  谁、在哪、什么光线下。
- 只设计 happy path。空、加载、错误与长内容状态都是组件的一部分。

### 一致性校验

任何覆盖之后，温和地标出不匹配并给出替代：Brutalist/Minimal 加表现型
动效 → 更安静的动效或保留为有意为之；Drenched 加 minimal 装饰 → 加支
持性装饰；editorial 加密集数据 → hybrid 布局。绝不阻塞；接受用户的最
终选择并继续。

### 独立提案，然后综合

先从 brief 起草你自己的方向：在派发任一声音之前，填好 Q2 的美学、配
色、角色专属字体、布局、间距、动效与两个有意为之的风险。把这份草稿排
除在两个评审者的提示词之外；发**同一个 brief**，不是你的答案。外部声
音仅在用户 opt-in 后运行；`enabled` 记录该选择，第二次 harness 检查守
护后续的派生。

## 设计外部声音（独立）

用 AskUserQuestion：
> "要外部设计声音吗？Codex 提出一个独立设计方向；Claude 子代理做一份
> 独立设计方向提案。"
>
> A) 要：跑外部设计声音
> B) 不要：直接继续

用户选 B，按下文记录一次 declined 结果，跳过两个声音，带着你的草稿继续
Q2。

**接受时：**为 Phase 1 产品简报创建私有文件，含 Phase 2 调研状态：
```bash
_DESIGN_BRIEF=$(mktemp "${TMPDIR:-/tmp}/gstack-design-brief-XXXXXXXX") || exit 1
printf 'DESIGN_BRIEF=%s\n' "$_DESIGN_BRIEF"

```
把产品简报写进那个路径；在后续独立 Bash 调用中记住其绝对路径。两个声
音都不继承上下文：给两者同一份简报。把其完整内容连同下方的设计方向请求
一起放进 Codex 的外部提示词文件；在调用中用其 shell 引号绝对路径替换字
面 `<prepared-prompt-file>`。让你的草稿方向排除在两个提示词之外；把绝
对路径（产品简报的路径，不是 Codex 提示词文件）给原生 Agent。绝不把简
报文本粘贴进 shell 源码。

**检查 Codex 可用性：**
```bash

if ! _OUTSIDE_CFG=$("$HOME/.claude/skills/gstack/bin/gstack-config" get --stored codex_reviews) || [ "$_OUTSIDE_CFG" = disabled ]; then
  echo 'CODEX_MODE: disabled'
elif ( # GSTACK_ACTIVE_HOST names the harness, never the model.
if { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
  echo 'Codex outside review unavailable: harness mismatch; no outside process started. Missing coverage.' >&2
  if { [ -n "${CLAUDECODE:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = claude ]; } && { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
    echo 'Inherited harness markers conflict. Run setup --host <actual-harness> (claude or codex); do not guess a replacement provider.' >&2
  else
    echo 'Repair installed skills: run setup --host codex from your gstack checkout.' >&2
  fi
  exit 78
fi
); then
  if command -v codex >/dev/null 2>&1; then echo 'CODEX_MODE: ready'; else echo 'CODEX_MODE: not_installed'; fi
else
  echo 'CODEX_MODE: under_current_harness'
fi

```

历史 `CODEX_MODE` 变量在此描述 **Codex** 的可用性。
`CODEX_MODE: disabled` 或发送时的 `consent_missing` 行：`codex_reviews`
关闭或不可读；不要问；记 `outside_status: disabled`。认证与所配置模型的
有效性由实际调用检查，不覆盖任何一方。CLI 缺失/损坏：安装或修复
Codex；认证失败：运行 `codex login`。其余情况尊重调用方的 opt-in/skip
选择。任何非 ready 结果都是外部覆盖缺失；走调用方既有兜底。绝不替换为
其他外部提供方。

`CODEX_MODE: disabled` 或 CLI 非 ready：保留任何修复提示，只用原生声
音。调用会有意在派生前重查 harness；原生成功绝不可替代外部覆盖。

**就绪时**，跑两个声音并都等完再综合。支持就重叠调用；原生调用保持阻
塞。

1. **Codex 设计声音**（经 Bash）：
提示词（含实际计划/产品/前端源码上下文，不只是文件路径）：

"Given this product context, propose a complete design direction:
- Visual thesis: one sentence describing mood, material, and energy
- Typography: specific font names with display/body/UI roles (no Inter/Roboto/Arial/system defaults); the parent verifies font availability before adoption
- Color system: hex values and CSS variables for background, surface, primary text, muted text, accent
- Layout: composition-first, not component-first. First viewport as poster, not document
- Differentiation: 2 deliberate departures from category norms
- Anti-slop: none of purple gradient palette, the 3-column feature grid, centered everything, decorative blobs and dividers, nested cards, kicker above heading, icon tile above every heading, dark-mode glow

Be opinionated. Be specific. Do not hedge. This is YOUR design direction — own it.

End with Recommendation: <direction> because <product-specific reason>."

把**完整的提示词与上下文**（含实际计划/规格/源码）写进私有文件。用其
shell 引号路径替换 `<prepared-prompt-file>`；绝不把用户文本内插进 shell
源码。要求一份完整设计提案，结尾为 Recommendation: <direction> because
<product-specific reason>。

```bash
# GSTACK_ACTIVE_HOST names the harness, never the model.
if { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
  echo 'Codex outside review unavailable: harness mismatch; no outside process started. Missing coverage.' >&2
  if { [ -n "${CLAUDECODE:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = claude ]; } && { [ -n "${CODEX_THREAD_ID:-}" ] || [ -n "${CODEX_SANDBOX:-}" ] || [ "${GSTACK_ACTIVE_HOST:-}" = codex ]; }; then
    echo 'Inherited harness markers conflict. Run setup --host <actual-harness> (claude or codex); do not guess a replacement provider.' >&2
  else
    echo 'Repair installed skills: run setup --host codex from your gstack checkout.' >&2
  fi
  exit 78
fi

_REPO_ROOT=$(git rev-parse --show-toplevel) || { echo 'ERROR: not in a git repo' >&2; exit 1; }
_OUTSIDE_TMP=$(mktemp -d "${TMPDIR:-/tmp}/gstack-outside.XXXXXXXX") || exit 1
trap 'rm -rf "$_OUTSIDE_TMP"' EXIT
_OUTSIDE_INPUT="$_OUTSIDE_TMP/prompt"
cat -- '<prepared-prompt-file>' >"$_OUTSIDE_INPUT" || exit 1

_CODEX_PROBE="$HOME/.claude/skills/gstack/bin/gstack-codex-probe"
_CODEX_OUT=$("$_CODEX_PROBE" select-model exec) || exit 1
_CODEX_SEL=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SEL: //p')
_CODEX_SANDBOX_MODE=$(echo "$_CODEX_OUT" | sed -n 's/^CODEX_SANDBOX: //p')
"$_CODEX_PROBE" check-sandbox || exit 1
"$_CODEX_PROBE" show-first-use-notice
_OUTSIDE_EXIT=0
"$_CODEX_PROBE" run-with-timeout --effort medium 300 codex exec - -C "$_REPO_ROOT" -s "${_CODEX_SANDBOX_MODE:?}" -c "model=\"${_CODEX_SEL:?}\"" -c skills.include_instructions=false -c 'web_search="cached"' --json -o "$_OUTSIDE_TMP/text" <"$_OUTSIDE_INPUT" >"$_OUTSIDE_TMP/events" 2>"$_OUTSIDE_TMP/stderr" || _OUTSIDE_EXIT=$?
cat "$_OUTSIDE_TMP/text" 2>/dev/null || tail -n 20 "$_OUTSIDE_TMP/events"

cat "$_OUTSIDE_TMP/stderr" >&2 || { [ "$_OUTSIDE_EXIT" -ne 0 ] || _OUTSIDE_EXIT=1; }
_OUTSIDE_RC=0
bun --no-env-file --config=/dev/null "$HOME/.claude/skills/gstack/lib/outside-review-result.ts" --label 'Codex outside review' --exit "$_OUTSIDE_EXIT" --stderr "$_OUTSIDE_TMP/stderr" --events "$_OUTSIDE_TMP/events" proposal "$_OUTSIDE_TMP/text" || _OUTSIDE_RC=$?
case "$_OUTSIDE_RC" in
  0|3) ;;
  4) echo 'OUTSIDE_STATUS: unverified provider=codex host=claude'; exit 4 ;;
  *) [ "$_OUTSIDE_EXIT" -ne 0 ] && exit "$_OUTSIDE_EXIT"; exit 1 ;;
esac
echo 'OUTSIDE_STATUS: completed provider=codex host=claude'

```

Bash 用 `timeout: 360000`；完整响应放进 `tool-output` 围栏。要求执行成
功且标记有效。拒绝、空/畸形输出、缺 Recommendation 标记、超时或 CLI 失
败都算 `outside_status: unavailable`。P0/P1 发现与原生同等阻塞；
`OUTSIDE_STATUS: unverified` 是覆盖缺失。继续已完成的提案；原生完成不
算外部覆盖。任一结果之后，只删你的私有提示词；scratch 清理是自动的。

2. **Claude 设计子代理**（Agent 工具，支持时 `run_in_background:
   false`；等它的结果。收到启动回执说明进了后台：等它的完成通知。）：
"Read the complete product brief at [the absolute DESIGN_BRIEF path printed above].

Propose a surprising indie-studio direction beyond conventional enterprise UI.
- Propose an aesthetic direction, typography stack (specific font names), color palette (hex values)
- 2 deliberate departures from category norms
- What emotional reaction should the user have in the first 3 seconds?

Do not fall back on these defaults: a cream ground with a high-contrast serif and terracotta accent; near-black with one neon accent and glowing edges; broadsheet hairlines with an italic display serif and tiny tracked mono labels; italic accent words inside headlines; numbered 01 / 02 / 03 section labels; pill-shaped buttons; purple gradient palette, the 3-column feature grid, centered everything, decorative blobs and dividers, nested cards, kicker above heading, icon tile above every heading, dark-mode glow. If your first idea is one of these, name it and choose again.

Be bold and specific."

**错误处理（全部不阻塞）：**
- **认证失败：**stderr 含 "auth"、"login"、"unauthorized" 或 "API key"：
  "Codex authentication failed. Run `codex login` to authenticate."
- **超时：**"Codex timed out after 5 minutes."
- **空响应：**"Codex returned no response."
- Codex 任何错误：只用 Claude 子代理输出继续；把它标为唯一完成的独立
  提案。
- Claude 子代理也失败："Outside voices unavailable — continuing to Q2
  with my draft direction."

只呈现已完成、可用的声音输出，附其真实来源与状态。
输出标头：`CODEX SAYS (design direction):` 与
`CLAUDE SUBAGENT (design direction):`。

**移交：**保留每个已完成的提案（两个、一个或零个），附来源/状态。不要在
此处选方向。Q2 把这些提案与你早先的草稿对比。
两个声音都结束（含失败）后，用记住的绝对路径只删除你创建的私有简报。

**记录结果：**用户接受时把命令跑两次：每个声音一条记录，含不可用的声
音。用户拒绝时跑一次，STATUS=skipped、SOURCE=none、
OUTSIDE_STATUS=skipped。
```bash
~/.claude/skills/gstack/bin/gstack-review-log '{"skill":"design-outside-voices","timestamp":"'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'","status":"STATUS","source":"SOURCE","host":"claude","outside_provider":"codex","outside_status":"OUTSIDE_STATUS","phase":"design","commit":"'"$(git rev-parse --short HEAD)"'"}'

```
用实际完成的提案填日志字段。品味差异是替代方案，不是问题；
STATUS=issues_found 仅用于有未解决产品约束的可用提案。

| 结果 | STATUS | SOURCE | OUTSIDE_STATUS |
|---|---|---|---|
| 用户拒绝两者（一条记录） | skipped | none | skipped |
| Codex 完成且有有效标记 | clean 或 issues_found | codex | completed |
| Codex 不可用或非法 | unavailable | none | unavailable |
| 原生子代理完成 | clean 或 issues_found | in-host | Codex 实际结果：completed 或 unavailable |
| 原生子代理不可用 | unavailable | none | Codex 实际结果：completed 或 unavailable |

SOURCE 是完成的提供方或 in-host，否则 "none"。即使一个声音失败，两条
已接受运行记录都保留。

两条记录都带实际 CLI 结果：OUTSIDE_STATUS=completed 仅限带有效标记的成
功执行，否则 unavailable。`outside_provider`/`outside_status` 描述外部
覆盖，不是每条记录的 source。仅原生成功是 STATUS=clean、
SOURCE=in-host、outside_status="unavailable"。

保留历史 skill 标识符。历史 source:"claude" 仍指原生 Claude 子代理。保
留上报的 modelUsage，含多模型；未知模型身份保持未知。

对比已完成的部提案：说明一致处、差异、以及采纳的想法及其归属。采纳新
建议的字体之前，用上方同一流程核实。把推荐挂到"难忘之事"的答案上。不
把一致当投票，不编造缺失的提案。Q2 点名已完成、不可用或 declined 的声
音，并给出推荐。

**AskUserQuestion Q2：带 SAFE/RISK 分解呈现完整提案：**

```
Based on [product context] and [research findings / my design knowledge]:

AESTHETIC: [direction] — [one-line rationale]
DECORATION: [level] — [why this pairs with the aesthetic]
LAYOUT: [approach] — [why this fits the product type]
COLOR: [approach] + proposed palette (hex values) — [rationale]
TYPOGRAPHY: [display, body, label, mono assignments; a face may serve multiple roles] — [why these fonts]
SPACING: [base unit + density] — [rationale]
MOTION: [approach] — [rationale]

This system is coherent because [explain how choices reinforce each other].

INDEPENDENT INPUT: [completed/unavailable/skipped voices; agreements, differences, ideas adopted and product-specific reasons — omit comparisons if none completed]

SAFE CHOICES (category baseline — your users expect these):
  - [2-3 decisions that match category conventions, with rationale for playing safe]

RISKS (where your product gets its own face):
  - [2-3 deliberate departures from convention]
  - For each risk: what it is, why it works, what you gain, what it costs

Safe choices meet category expectations; risks make the product memorable.
Which risks appeal to you? Try others or adjust anything else?
```

只有一致性可能看起来泛用。至少提 2 个创意风险（字体、强调色、间距、布
局或动效），与品类的安全选择并列给出理由、收益与代价。

**选项：**A) 很好：字体已验证就进 Phase 5。B) 调整 [某节]：Phase 4，
然后重新 Q2。C) 换风险：修订提案，然后重新 Q2。D) 推倒重来：用同一份
确认过的 brief 另起方向。E) 跳过预览：进 Phase 6 的 Q-final，不要直接
开始写。

修订要重查字体与一致性。产品简报变了，就把旧提案标为过期并提供全新的独
立声音；绝不声称它们评审过新上下文。

---

## Phase 4：深入追问（仅当用户要求调整）

每个被请求的追问用一次聚焦的 AskUserQuestion：**字体：**3-5 个已验证候
选，附角色、理由/联想与预览提议；**配色：**2-3 组 hex 配色与色彩理论；
**美学：**贴合产品的方向及原因；**布局/间距/动效：**具体的产品专属权
衡。把选定的调整带进完整 Q2 提案，再次 Q2 之前重查其字体验证与一致
性。

---

## Phase 5：设计系统预览（默认开启）

Q2 批准之后：字体待定或用户跳过预览 → 带局限进 Phase 6。生成不可用/失
败 → 提供 Path B 或跳过，不做无界重试。

### Path A：AI Mockup（`DESIGN_READY` 时）

把拟议系统应用到真实产品界面：

```bash
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null)
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
_DESIGN_DIR="$GSTACK_STATE_ROOT/projects/$SLUG/designs/design-system-$(date +%Y%m%d)"
mkdir -p "$_DESIGN_DIR"
echo "DESIGN_DIR: $_DESIGN_DIR"

```

Brief：Phase 3 的美学/配色/字体/间距/布局加 Phase 1 产品上下文，写进私
有文件：

```bash
_GT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp"
mkdir -p "$_GT" && chmod 700 "$_GT" || { echo "Not sent: cannot create $_GT for the text file." >&2; exit 1; }
_EX=$(git rev-parse --git-path info/exclude 2>/dev/null) && mkdir -p "$(dirname "$_EX")" && { grep -qxF '/.gstack/tmp/' "$_EX" 2>/dev/null || echo '/.gstack/tmp/' >> "$_EX"; }
BRIEF_FILE=$(mktemp "${_GT:?}/brief.XXXXXX") || { echo "Not sent: mktemp failed in $_GT." >&2; exit 1; }; echo "BRIEF_FILE: $BRIEF_FILE (name: ${BRIEF_FILE##*/})"

```

用你的文件写入工具把文本写进每个打印出的文件（Claude Code 的 Write 工
具需要先 Read 一次空文件），内容与应出现的一字不差。文本绝不进 shell
命令、heredoc 或带引号参数。写入失败或被拒时不发送：打印原因、文件路径
和下方命令，供手工发送。

Brief 形状：`Product name: [name]. Product type: [type]. Aesthetic:
[direction]. Colors: primary [hex], secondary [hex], neutrals [range].
Typography: display [font], body [font]. Layout: [approach]. Show a
realistic [page type] screen with [specific content for this product].`
然后 `<brief-file-name>` 用打印出的名字：

```bash
BRIEF_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<brief-file-name>"
[ -s "$BRIEF_FILE" ] || { echo "Not run: $BRIEF_FILE is missing or empty. Write the brief, then rerun this block." >&2; exit 1; }
_OUT=$($D variants --brief "$(cat "$BRIEF_FILE")" --count 3 --output-dir "$_DESIGN_DIR/"); _RC=$?
printf '%s\n' "$_OUT"; echo "EXIT: $_RC"

```

<!-- design:round-accounting -->
**轮次记账：**名字绝不覆盖（被占用的会递增），所以只用打印出的 `saved`
路径。告诉用户 `requested` 的付费图片保存了几张，并点名每个 `failures`
条目。exit 2 表示什么都没存：报告 `failures` 并在此停止（提供 Path B 或
跳过）；不跑 `$D check`，不出 board。

对每个保存路径（从第一个开始）用同一 brief 文件跑质量检查；绝不纳入失败
的变体：

```bash
BRIEF_FILE="$(git rev-parse --show-toplevel 2>/dev/null || pwd)/.gstack/tmp/<brief-file-name>"
[ -s "$BRIEF_FILE" ] || { echo "Not run: $BRIEF_FILE is missing or empty. Write the brief, then rerun this block." >&2; exit 1; }
$D check --image "<first path from the printed saved list>" --brief "$(cat "$BRIEF_FILE")"

```

读 JSON，不读 exit code：`pass: false` 表示按 `issues` 重生成后重查。
`pass: true` 但带 unavailable/skipped 警告是自动化覆盖缺失；披露它并目
视检查。

**呈现之前自设门：**一位人类设计师会为每个变体署名而难堪吗？会就丢弃并
重生成。硬性拒绝：紫色渐变 hero、三列 SaaS 网格、全部居中、过度使用的
display 字体、泛用图库照片、system-ui、渐变 CTA、到处气泡圆角。任一触
发都要求重生成。

内联 Read 每个被接受的 PNG，然后用这些路径打开 board，再邀请选择/remix。

### 对比板加反馈循环

<!-- design:board -->
用 Write 工具把本轮 board 图（按序打印的、通过检查的路径）作为 JSON 数
组写入 `$_DESIGN_DIR/board-images.json`；board 字母 A、B、C 按该顺序。
然后归档任何更早的 Submit，使其无法批准这些图，并构建 board：

```bash
[ -f "${_DESIGN_DIR:?set _DESIGN_DIR to the design dir printed above}/feedback.json" ] && mv "${_DESIGN_DIR:?}/feedback.json" "${_DESIGN_DIR:?}/feedback-$(date -u +%Y%m%dT%H%M%SZ).json"
$D compare --images-file "$_DESIGN_DIR/board-images.json" --output "$_DESIGN_DIR/design-board.html" --serve

```

它发布到常驻 daemon、打开 board 并退出。从捕获的 stderr 读启动标记；PID
不等于就绪。exit 0 且带 `BOARD_URL` 表示 daemon 在托管。保存其完整的
`http://127.0.0.1:N/boards/<id>/` URL。只有 legacy `--no-daemon` 需要宿
主后台任务；`SERVE_STARTED: port=N` 给出根 URL
`http://127.0.0.1:N/`。

**用 AskUserQuestion 等待：**"审阅 <BOARD_URL>，Submit 或请求新变体，然后
告诉我；或在这里粘贴偏好。"board 做选择，问题只负责等。不要轮询。

答复之后，读 board HTML 旁的当前反馈：
- `feedback.json`：Submit（preferred/overall 可能为 null）：
```json
{"preferred":"A","ratings":{"A":4},"comments":{"A":"Good spacing"},"overall":"Go with A","regenerated":false}
```
- `feedback-pending.json`：Regenerate：
```json
{"preferred":"B","ratings":{"B":4},"comments":{},"overall":"Keep layout","regenerated":true,"regenerateAction":"more_like_B"}
```

`regenerateAction`：`different`、`match`、`more_like_<letter>` 或自定义文
本（含 remix）。board 用文本；它不发出必需的 `remixSpec`。用户粘贴了映射
（`{"layout":"A","colors":"B"}`）就照它办；细节缺失就问。

**board 或聊天：**修订走重生成；最终选择需要摘要确认；跳过则不带 mockup
进 Phase 6。没有选择或细节就问；绝不从缺失文件推断批准。带修订说明的
Submit 是一次修订。

**重生成：**
1. 在 brief 文件里修订 brief，保留无关约束。归档本轮反馈文件，让旧
   Submit 无法批准新图（重建时 board 块会做这一件事）。
2. 用新 brief 跑 `$D variants`（无 session），同样的捕获与轮次记账。对每
   张新图（其打印路径）重跑质量检查与视觉自设门。
3. 用上方 board 块重建（它会重写 board-images.json），不带 `--serve`。
4. 在保存的 URL 重载（保留其 per-board 路径；legacy 用根）：
   `jq -nc --arg html "$_DESIGN_DIR/design-board.html" '{html: $html}' | curl -sS -X POST "${BOARD_URL}api/reload" -H 'Content-Type: application/json' --data-binary @-`
5. 检查重载成功，然后在同一 URL AskUserQuestion 直到最终选择、跳过或停
   止。生成/重载失败走兜底，不是再等一次。

**SERVER 兜底：**非零 exit 或无就绪标记：用 Read 内联展示每个变体，然后
AskUserQuestion："对比板服务启动失败。哪个变体？要改什么？"聊天反馈按上
文路由。

**收到反馈后（任一路径）：**总结 PREFERRED、RATINGS、YOUR NOTES、
DIRECTION；AskUserQuestion "Is this right?"。确认的最终选择允许写入
`$_DESIGN_DIR/approved.json`，含 `approved_variant`、`approved_path`
（该字母在本 board `board-images.json` 中的条目的文件名，绝不是目录列
表）、`feedback`、`date`（UTC）、`screen`（所选 mockup 描绘的产品页
面）、`branch`（`git branch --show-current` 结果，detached 时为空）。
用合法 JSON，绝不用 shell 插值。这只批准图片；Q-final 才门控项目写入。

最终图片确认之后，`$D extract` 会在 Git 仓库里写 DESIGN.md：只在全新的
非仓库 scratch 目录里跑它。把 `$D` 与 `APPROVED_IMAGE`（确认字母在
`board-images.json` 中的条目）绑到绝对路径：

```bash
_EXTRACT_DIR=$(mktemp -d "${TMPDIR:-/tmp}/gstack-design-extract-XXXXXXXX") || exit 1
(
  cd "$_EXTRACT_DIR" || exit 1
  if git rev-parse --show-toplevel >/dev/null 2>&1; then
    echo "Extraction refused: scratch directory resolves to a Git repository" >&2
    exit 1
  fi
  "$D" extract --image "$APPROVED_IMAGE"
)

```

把提取出的 token 与获批图片及已验证字体对比；在 Q-final 展示差异。空数
组、"Unable to extract" 语气或命令失败 → 披露回退到 Phase 3 取值，绝不
发明测得的 token。

后期视觉变更回到反馈循环：重生成、重查、再确认，然后重新提取。只有
`generate` 提供 `sessionFile` 供
`$D iterate --session "<returned sessionFile>" --feedback "$(cat "$FEEDBACK_FILE")" --output "$_DESIGN_DIR/refined.png"`；
用其打印的 `outputPath`。变体必须重生成。

**计划模式：**把获批 mockup 路径/token 带进 Phase 6 的
"## Proposed DESIGN.md" 计划节。其 Q-final 批准决定保存该内容；真正的
DESIGN.md 推迟到实现阶段。

### Path B：HTML 预览页（`DESIGN_NOT_AVAILABLE` 时的兜底）

创建并打开 HTML 预览：

```bash
PREVIEW_FILE="/tmp/design-consultation-preview-$(date +%s).html"

```

把预览 HTML 写进 `$PREVIEW_FILE`，然后打开：

```bash
open "$PREVIEW_FILE"

```

### 预览页要求（仅 Path B）

写**单个自包含 HTML 文件**，不用框架：

1. 经 `<link>` 从第（4）步核实过的 Google Fonts/Fontshare/自托管来源加
   **载拟用字体**。
2. 全篇**使用拟用配色**。
3. hero 里展示**产品名**，不是 Lorem Ipsum。
4. **字体样张节：**每个候选在其 hero/body/button/table 角色里；用真实
   领域内容并排对比同角色替代项（如政务科技：政府数据）。
5. **配色节：**具名 hex 色块；primary/secondary/ghost 按钮、卡片、输
   入、success/warning/error/info 提示；背景/文字对比对。
6. **真实产品 mockup：**用完整系统、产品名、领域内容与拟议间距/布局/圆
   角渲染 2-3 个 Phase 1 产品类型布局：
   - **仪表盘/web 应用：**指标表、侧栏导航、头像页头、统计卡片。
   - **营销页：**真实文案 hero、功能、推荐语、CTA。
   - **设置/管理：**带标签输入、开关、下拉、保存。
   - **认证/onboarding：**品牌化登录、社交按钮、校验状态。
7. **明暗切换：**CSS 自定义属性加一个 JS 按钮。
8. **干净、专业的布局。**
9. **每个宽度都响应式。**

展示他们产品的感观，而不只是一份字体/配色清单。

`open` 失败（无头环境）时告诉用户：*"我把预览写到 [path] 了，在你的浏览
器里打开就能看到字体与颜色的实际渲染。"*

用户说跳过预览，直接进 Phase 6。

---

## Phase 6：写 DESIGN.md 并确认

只有 Path A 会调 `$D extract`，按上文隔离。Path B 用获批 HTML 预览的
CSS 值。没有预览：用批准的 Phase 3 取值；只把未验证的字体标为待定。保
留理由与未变的既有决策。

**写之前确认。**准备下方完整的 DESIGN.md 内容，标出每个 token 来源（获
批 mockup 提取、获批 HTML 或 Phase 3 兜底），把未验证字体标为待定，并展
示你要新增或更新的确切 CLAUDE.md 指引。把决策与 agent 选定的默认值连同
该预览一起展示。AskUserQuestion Q-final：
- A) 批准：写 DESIGN.md 与 CLAUDE.md；计划模式下只把 Proposed DESIGN.md
  存进计划
- B) 修订：回 Phase 3，然后重新确认
- C) 推倒重来：回 Phase 1

等待。只有 A 允许下方写入；B/C 不动项目文件。把对这些确切写入的既往显
式批准直接兑现，不再追问。任何后续 token、字体或方向变化都使那份批准作
废：更新提案、重验受影响字体/预览，再次 Q-final。产品简报改变也会让既
往独立提案作废。

**计划模式中：**把 DESIGN.md 内容作为 "## Proposed DESIGN.md" 节写进计
划文件。**不要**写实际文件：那发生在实现时。

**非计划模式：**应用批准的 Phase 0 格式选择，然后写根 `DESIGN.md`。
新建、全新与转换过的文件用下方 google-labs-code/design.md 格式：所有
token 都放进五个规范 YAML 组；散文解释理由/用法，不重复取值。保留第 2
行格式标记。kept-legacy 或 unknown 格式的 Update 改为保留自己的形态；只
为选定的 legacy 路径持久化 `legacy-keep`。全新替换之前把既有文件备份。

```markdown
---
# gstack: design-md-format=spec
name: [Project Name]
description: [one sentence: mood, material, energy]
colors:
  primary: "#..."          # descriptive slugs; hex, or the project's canonical color space
  on-primary: "#..."
  surface: "#..."
  text: "#..."
  text-muted: "#..."
  accent: "#..."
  success: "#..."
  warning: "#..."
  error: "#..."
typography:
  display:
    fontFamily: [face]
    fontWeight: [weight]
    fontSize: [clamp() or rem]
    letterSpacing: [em]
  body:
    fontFamily: [face]
    fontSize: 1rem
    lineHeight: 1.5
  label:
    fontFamily: [face]
    fontSize: 0.75rem
    letterSpacing: 0.04em
  mono:
    fontFamily: [face]
    fontFeature: tnum
rounded:
  sm: 4px
  md: 8px
  lg: 12px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-hover:
    backgroundColor: "#..."
  input:
    borderColor: "{colors.text-muted}"
    rounded: "{rounded.sm}"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
  nav-link:
    textColor: "{colors.text}"
---

# [Project Name]

## Overview

**Creative North Star:** [one sentence: aesthetic + why it fits these users]
**Product context:** [product, users, category/peers, project type]
**Mode per surface:** [one line each: Persuade / Operate / Read / Experience]
**Reference sites:** [URLs, if research was done]
**Key characteristics:** [3-5 bullets: first-five-second impressions]

## Colors

**Strategy:** [Restrained / Committed / Full palette / Drenched] — [why]
**Light or dark:** [decided by the use scene: who, where, under what light]
[Explain which tokens signal interaction or emphasis, how neutrals derive from the palette, and how dark-mode surfaces preserve hierarchy rather than merely inverting lightness.]

## Typography

[Faces' source world, mode/register, roles and display boundaries; loading, scale rationale, justified overused-list exceptions]

## Layout

[Breakpoint grids, max width, density, large/small spacing rhythm, intentional grid breaks]

## Elevation & Depth

[Depth: offset + soft-blur shadows, tints, borders; no zero-offset glow]

## Shapes

[Radius hierarchy/uses; nested inner radius = outer radius − gap]

## Components

[Per component: hover/focus-visible/active/disabled states, invariants and adaptations]

## Do's and Don'ts

- Do: [3-5 specific, checkable rules]
- Don't: [3-5 system-specific anti-patterns, including this category's tempting catalog entries]

## Motion

- **Approach:** [minimal-functional / intentional / expressive]
- **Easing:** enter(ease-out) exit(ease-in) move(ease-in-out)
- **Duration:** micro(50-100ms) short(150-250ms) medium(250-400ms) long(400-700ms)
- **The one authored moment:** [what it is]

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| [today] | Initial design system created | Created by /design-consultation based on [product context / research] |

```

用真实 token 值，不用占位符；省略编造的 `components` 条目与未验证的
fontFamily 值。待定的字体角色改用散文描述。非计划模式下，写完 DESIGN.md
之后跑
`bun --no-env-file --config=/dev/null run ~/.claude/skills/gstack/bin/gstack-design-md.ts check DESIGN.md`：
新建/全新/转换/spec 文件要求 `DESIGN_MD_FORMAT: spec`，保留的 legacy 文
件要求 `legacy` 加 `legacy-keep`，保留的 unknown 文件要求所披露的
`unknown` 格式。绝不为让校验说 spec 而转换一个保留的文件。

**非计划模式下更新 CLAUDE.md**（不存在则创建）：追加本节：

```markdown
## Design System
Read DESIGN.md before visual or UI work: it defines the fonts, colors, spacing, and
aesthetic direction. Ask the user before departing from it. When reviewing or QA-ing
UI, flag code that doesn't match DESIGN.md.
```

DESIGN.md 落地之后，若会话产出了界面级 mockup 或页面布局（不只是系统级
token），建议：
"想把这个设计系统做成能跑的 Pretext 原生 HTML 看看吗？运行
/design-html。"

---
