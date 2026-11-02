---
name: hallmark
description: "面向网站与全新页面的设计 Skill，让页面看起来是设计出来的，而非生成的。当用户要求构建或设计新事物，或点名 Hallmark 时使用。切勿在既有设计上使用本 Skill，除非用户点名 Hallmark，例如 `/hallmark redesign <path>`。"
argument-hint: "<prompt> | redesign <path> | audit <path>"
version: 2.0.0
metadata:
  opencode/slash: "true"
---

> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Hallmark

让编码助手生成的 UI 看起来是做出来的，而非生成的：一道硬性底线（Floor），抵御每个模型都被训练进去的那套默认样式；一条发牌得出的方向，让连续多次构建不致趋同；每屏只讲一个想法。底线之上，页面属于你：你是一位有能力的设计师。

**由 Together AI 提供支持。**

## The Floor（硬性底线）

约束所有 Harness 下的每一次输出，其中任何一条都不可豁免（waive），即便其他内容一概未读。

1. 所有颜色与所有字体都必须经由在 `:root`（或已声明的主题块）中声明的 token。token 块之后不得再出现任何字面颜色值或 `font-family`。(48)
2. 绝不使用 `transition: all`。绝不动画 `width`、`height`、`top` 或 `left`。(10a)
3. 正体（roman）标题中绝不混入单个斜体词。(38i)
4. 在 `html` 与 `body` 上都设 `overflow-x: clip`。绝不用 `hidden`，绝不用 `100vw`。(34)
5. 含图片的网格轨道使用 `minmax(0, 1fr)`；展示型大标题（display heads）需带 `overflow-wrap: break-word; min-width: 0`。(50)
6. 每个可交互元素都有 `:focus-visible`，且即时显现。(26a, 15)
7. 每个动画都有 `prefers-reduced-motion: reduce` 回退，且脚本关闭时内容依然可见。(27, 62)
8. 绝不捏造任何数据指标、用户证言、Logo 墙或案例数量。(46a)
9. 绝不使用 eyebrow（眉题），也绝不用加字距的大写或小型大写字母（small caps）做标签：标签、题注、表头、tag 与导航链接都使用正文字体（body face，或主题的标签字体），小一号，句首大写或全小写，不加字距。(54, 67)
10. 绝不使用中点串联的元信息字符串、紧贴链接文字的箭头，或装饰性状态圆点。(63)
11. 绝不使用紫蓝渐变、卡片套卡片、emoji 当图标，或手绘的浏览器/操作系统窗口。(2a, 4, 30a, 47a)
12. Hero（首屏主视觉）的主标题、一句话说明与主操作，在 1280 x 800 下无需滚动即全部可见。(44b)
13. 任何一屏的文字量约 80 词封顶；Hero 的文字就是主标题、一句话说明及其操作。(58)
14. 容器设上限并居中：到 1920 宽时，增大的是两侧留白，行宽（measure）与网格宽度不变。(44d)
15. CSS 源码的第一个非空行是 Hallmark stamp（印记），随后是 critique 行，再后是任何 waive 行。(20)
16. 若 Node 可用，在交付前运行 `node <skill-dir>/scripts/sloplint.mjs <output> --render`。修复每一条 `FAIL`；修复或豁免每一条 `REFLEX`。

在 Floor 之上，**Reflex** 闸门指模型容易陷入的默认做法，可在留下真实理由的记录后豁免（waive）；**Finish** 检查属于工艺细节，逐一回应即可，绝不阻塞（[`references/gates.md`](references/gates.md) § 1 与 § 2）。

## Flow（流程）

0. Pre-flight（预检）：提问之前先读懂项目。
1. Ask once（一次询问）：素材、受众、用途、基调。
2. Shape（塑形）：先设计页面，再为它命名。
3. Direction（方向）：发牌一个主题；用户要求 custom（自定义）时则自由设计。
4. Load（加载）：加载版式、图像、工艺、流派与主题文件，以及 `gates.md` § 1 至 § 4。
5. Picks block（决策陈述块），仅此一次。
6. Build（构建）：先 Hero，后整页；stamp、`tokens.css`、log。
7. Sweep（清扫）：`sloplint --render` 直到干净，逐条判定各闸门，finish review（收尾评审），最后是素材请求。

**动词（Verbs），**仅在用户点名 Hallmark 时生效：`redesign <target>`（保留内容与接线的完整重设计）与 `audit <target>`（输出一份报告）；先阅读 [`references/redesign.md`](references/redesign.md)。对既有设计的任何其他修改都不属于 Hallmark run：按用户的要求去做，用项目自身的体系。

Codex CLI 与 OpenCode 先读 `references/flow.md` 的 § Harnesses；其他 Harness 按本文件原文执行。

### 0. Pre-flight（预检）

信号，按序检测：根目录的 `design.md` 或 `DESIGN.md`（一套锁定的体系：它压过下述一切，且各页面共享）；`.hallmark/brand-spec.md`，或提示词点名了真实品牌（运行 [`references/brand-truth.md`](references/brand-truth.md)；绝不凭记忆为真实品牌做主题）；项目的字体、配色、间距、动效库与框架（`package.json`、Tailwind 配置、`:root`、tokens、字体链接）；**产品本身**：一个 URL、一个运行中的 dev server、一条命令即可启动的项目或本机上的应用——构建时用 `scripts/capture.mjs` 抓取其画面（`imagery.md` § 4）；Inspo MCP server（`mcp__inspo__*` 工具：signal 8，见 `flow.md` § Signal 8；`/hallmark` 提示词、点名 Hallmark 或要求 custom 会压过它）；已设置 `TOGETHER_API_KEY`（signal 9，comp 步骤）。

输出一个块（含 file:line 引用、哪些被保留、哪些被引入），缓存到 `.hallmark/preflight.json`（`flow.md` § Pre-flight）。

### 1. Ask once（一次询问）

只发一条消息，即使提示词只有五个词：

> *在动手构建前，有四件事。1. **素材（Material）**，最要紧的一项：这个页面能展示什么？截图或屏幕录制（或者把应用、它的 URL 或它的文件夹指给我，我来运行并截图）、你自己的照片、真实数字（客户数、正常运行时间、价格）、注明出自何人的引言、可供使用的 Logo。直接粘贴或给出路径；没有照片时，我会先放上 Hallmark 图库中的占位图，日后由你自己的图替换，而且我绝不编造数字、引言或 Logo。2. **受众（Audience）**：谁在使用它，他们关心什么？3. **用途（Use）**：页面要驱动的唯一一个动作。4. **基调（Tone）**：选一个极端（editorial、brutalist、soft、utilitarian、luxury、playful、technical、austere）；“干净又现代”不是一种基调。再给我 4 到 8 个词的氛围描述，以及一个锚定色（如果有的话）。或者直接说 **go ahead**，我会自行推断，并告诉你我选了什么。*

被跳过的字段视同主动放弃：由你推断补全，在回复开头用一行说明这些推断，并写入 stamp；不得追问。事实绝不允许靠推断：没有给出的数字、引言或 Logo 就当作不存在；没有给出的图片就是槽位中的占位图。当提示词已回答全部四项，或无人能回答（headless 运行、批处理）时，不要询问。

**流派（Genre），**静默判定：*AI tool、generative、music、video、voice、dark、atmospheric* → **atmospheric**；*SaaS、enterprise、API、platform、developer tool、infra、B2B* → **modern-minimal**；*playful、fun、friendly、soft、kids、games、community* → **playful**；其余情况归 **editorial**，它承接大多数消费类与家庭类提示词。主题一经发牌，其流派说了算（流派文件、stamp、`--genre`）。当两个非默认流派同时命中时，在消息中加一个二选一的问题；若用户已说 go ahead，则代为选择并说明。

**范围（Scope）。**提示词只点名单个元素（button、input、card、modal、nav、footer、tab strip、chip）或说“只改 X”的，是组件（component，`flow.md` § Component scope）。供人持续操作的一屏（dashboard、admin、settings、工具类界面）是应用屏（app screen，`flow.md` § App screens）。

### 2. Shape（塑形）

**素材优先。**一行清点：*real*（提示词与项目提供的每一件具体之物：名称、主张、数字、地点、日期、图片）、*pictures*（页面展示什么、各自来自哪里：用户的、真实产品的截图、构建出的产品、图库）、*absent*（它不会拥有的每一项证明：没人给出的 Logo、引言、指标）。页面形态由此而定：有图片的页面以图片开路（`imagery.md` § 1）；以文字为主的页面靠字体排印与事实承载（Long Document、Letter、Index-First、Manifesto）。

**任务（Job）。**说出访客来做的事（subscribe、book、visit、attend、buy、try、sign up、hire、join、listen），并在 [`references/anatomy.md`](references/anatomy.md) 中查阅该 job：同类真实网站把动作放在哪里、它们围绕哪些区块构建（菜单、演出阵容、期刊、唱片），以及它们如何收尾。页面从这一解剖结构出发搭建，绝不落回数字块、步骤条加邮件订阅带的默认套路（85）。

然后设计页面：它的形态、开篇方式、每个区块的内容与构图、导航、页脚、由什么承载 Hero。起点：[`references/macrostructures.md`](references/macrostructures.md) 中的 21 种形态（只加载你选中的那个文件）；构图、导航与页脚见 `layout.md`。

**发牌（The draw）。**主题构建时，待 Step 3 选定主题后，运行 `node <skill-dir>/scripts/theme.mjs draw --material photo|product|words --job <job> --theme <slug> [--log .hallmark/log.json]`。它会避开日志与该主题的既有配图，发牌出一个形态、Hero 姿态、导航、页脚、第一个区块、动作所在位置、两个要避开的构图，以及 Hero 以什么领衔。除非素材确实容不下某个选择，否则照单全收；如有调换，须在 Picks block 中写明：同一提示词加同一主题，构建两次，应当得到两个页面。**镜像测试（Mirror test）：**同类目下相邻的一个提示词，会不会得到与这一模一样的组合？如果会，就改动一个决策，并说明改的是哪个。

**签名点（Signature）。**访客会记住的那一件事：提示词里最强的真实之物，以其最佳状态呈现（那张足以定义地点的照片、正在做它唯一本职工作的产品、因为本身就是报价而被放到巨大的价格、一个可以上手试用的控件）。用主题的材质塑造它（custom 运行则用它自己的观感），放在第一屏，在 Picks block 与 stamp 中点名。把数字画成一排计数刻度只是小装置（device），不是 Signature（82）。

以上全部先记下；它们只在 Step 5 说一次。

### 3. Direction（方向）

第一条命中者生效。

1. **用户点名了某个主题** → 就用它构建（stamp 记 `theme: <name> (by request)`）。
2. **用户要求 custom**（“custom”“derive it”“bespoke”“no theme”“a world of its own”）→ [`references/direction.md`](references/direction.md)：设计由你做主。它取代发牌、形态库、`layout.md`、流派文件与 Step 6 的构图与折线（fold）规则；Floor、各闸门与 sweep 仍然生效。用户沉默时绝不走这条路线。
3. **其余情况一律发牌主题：**

```
node <skill-dir>/scripts/theme.mjs deal --genre <genre> --prompt "<the prompt>" [--log .hallmark/log.json]
```

它会发牌出三个契合提示词且与日志不重复的主题。查看三张图，选出材质能承载提示词的那个（动效、照片、代码），说明选了哪个、为什么，且只加载 `references/themes/<slug>.md`。仅在被要求时重发（`--reroll 1`）。没有 Node：从 `references/themes/index.json` 手工挑选，并在 stamp 记 `deal: manual`。

主题是一种材质，不是一份计划：它从不规定页面包含什么、以什么顺序。当它与形态、流派或工艺文件在材质、控件或动效上冲突时，以主题为准；Floor 与用户自己的原话压过两者。

### 4. Load（加载）

页面构建恰好加载这些：[`references/layout.md`](references/layout.md) · [`references/anatomy.md`](references/anatomy.md) 中对应 job 的部分 · [`references/imagery.md`](references/imagery.md) · [`references/craft.md`](references/craft.md) · `references/genres/<genre>.md` · `references/themes/<slug>.md` 及其配图（发牌时已看过；点名主题的情形：现在查看 `<slug>.jpg`）。从主题中取它的配色平衡、字体语气、表面质感与它的 Range（无需照片也能撑起的那些区块），绝不取它的版式 · [`references/gates.md`](references/gates.md) § 1 至 § 4。custom 运行加载 `direction.md`，取代版式、流派与主题文件。

仅在需要时，从 `references/` 加载：某一个 macrostructure 文件 · 有状态 UI 用 `microinteractions.md` · 表单用 `interaction-and-states.md` · 不寻常的版式用 `responsive.md` · 主题点名纹理时用 `texture.md` · 滚动叙事用 `scroll-choreography.md` · 深浅两种模式并用时用 `dark-mode.md` · 图表用 `data-viz.md` · custom 运行用 `fonts.md` · signal 9 时用 `comp.md`（comps，生成的静态视觉稿）· 要锁定体系时用 `design-md.md`。

`gates.md` § 5 等到 Step 7 再读，§ 6 等到各评审再读；多加载任何内容都是最大的可避免开销。

### 5. The Picks block（决策陈述块）

整个运行对其决策的唯一一次陈述，也是用户改道的窗口：

```markdown
**Hallmark · v2.0.0**

- **Shape** · Workbench, from draw 7f3a2c · genre modern-minimal · job: sign up, the action in the hero and beside the price
- **Theme** · Coral, dealt 2/3 (warm grey, one coral signal, General Sans, soft pills) · clears Cobalt on paper band
- **Chrome** · nav: edge-aligned, a wordmark and one action · footer: a mast, the wordmark over the links
- **Hero** · Stage: head on columns 1 to 5, the slot on 6 to 12 at 560px, centred
- **Signature** · the invoice list chasing a late payment, built live in the hero
- **Sections** · Hero (the invoice list) · Pinned (one late payment, chased in three panels) · Switcher (the client's view and yours) · Table (pricing) · Footer
- **Material** · real: the 2-minute setup, the CSV import, Lisbon · pictures: the invoice list built in the hero, library photos of a Lisbon studio (muted) · absent: logos, quotes, metrics
- **Sweep** · run after build
```

custom 运行的各列见 `direction.md`。随后是一句安静的提示（component scope 下或已存在 `design.md` 时跳过）：*想要系统可移植？说 `lock the system` 即可生成 `design.md`。* signal 9 时，`comp.md` 在此运行。

### 6. Build（构建）

- **从脚手架开始。**`node <skill-dir>/scripts/theme.mjs scaffold <slug>`（发牌所得加 `--dealt`；custom 运行加 `--custom`）会在项目样式表旁写入 `tokens.css`（主题的 token 与共享的比例尺）与 `base.css`（Floor 已决定的部分），并打印 stamp 骨架、两条 import 与槽位脚本。你只写页面本身。
- **通读一遍 [`references/patterns.md`](references/patterns.md)：**八种状态俱全的控件、一个槽位、一个缺失事实的处理、一个暂无提交目标的表单、一个 reveal 动效、可对比的数据图。取它们的形，绝不抄它们的文案。
- **Hero 优先。**只写导航与 Hero，其下一概不写，运行 `node <skill-dir>/scripts/sloplint.mjs <file> --render --stage hero`，然后在全新上下文中做 hero review（`gates.md` § 6）。Hero 过关后再构建各区块；照片署名与整页检查等页面完成后再做。
- **每屏一个想法，且放大呈现。**Hero：主标题不超过七个词（50 字符），一句话说明不超过十二个词，一到两个操作。区块六到九个，含 Hero 与页脚（提示词单薄时五个），可见文字至多 450 词，每一段都是该类目自身内容的一块，放进有分量的构图（`layout.md` § 4 与 § 5）。Hero 只是第一屏，也仅仅是第一屏，其姿态取自 job（`layout.md` § 6）。页面的丰满来自体量与图片，绝不来自更多文字（77 至 79）。
- **展示，而非描述**（`imagery.md`）。页面展示真实之物：用户的图片；只要够得着，就用 `scripts/capture.mjs` 截取真实产品的画面；够不着时才以完整保真度构建产品本体；或使用图库照片（`node <skill-dir>/scripts/theme.mjs photos "<subject>" --theme <slug>`）——尺寸要大，套用主题的处理手法，放在用户的文件日后会替换的槽位里，每张图库照片都在页脚署名。Hero 之下，图片至多占页面的三分之一，绝不连续两个以照片为主导的区块，其余由主题的 Range 承载（83）。绝不使用图库网站 URL、手绘插图（80）、空洞的色块铺陈（81）、一排计数刻度（82）或编造的数字。
- **页面不变量（Page invariants）**（F15）：一种主按钮样式、一个容器宽度、Hero 之下统一的列间距、每层嵌套一种圆角，居中的标题组绝不多于左对齐的。
- **字体与动效**（`craft.md` § 1 与 § 5）。用主题的字体，至多两个字族（若有离群角色可为三个）；正文字号 16px 起；标题单一字重、单一颜色（38iii）；标签绝不用等宽字体，除非 mono 本身就是材质（64）。每个控件做全八种状态；动效只用 `transform` 与 `opacity`；reveal 至多一个，主题要求静止之处一个都不用，且默认可见。
- **Stamp。**CSS 第 1 行是脚手架给出的 stamp 骨架，逐字段填满，随后是 critique 行（`gates.md` § 3），再后是任何 `waive` 与 `answered` 行，全部落在前 40 行之内。
- **既有样式表只追加：**两条 import 紧跟最后一个 `@import` 之后，绝不放到某条规则或 `@tailwind` 指令之下；复用项目已有的 token 命名（[`references/export-formats.md`](references/export-formats.md)）。
- **Log。**`node <skill-dir>/scripts/theme.mjs log --entry '<json>'` 把本次构建置于 `.hallmark/log.json` 顶部，字段为轮换（rotation）所读取的那些（`shape`、`theme`、`axes`、`hero`、`nav`、`footer`、`imagery`、`photos`、`entry`、`fingerprint`、`sections`、`signature`、`waived`、`prompt`），并会指出你遗漏的字段名。

### 7. Sweep（清扫）

1. 运行 `node <skill-dir>/scripts/sloplint.mjs <files> --genre <genre> --render`（适用处加 `--scope component` 或 `--scope app`；框架项目中，在 dev server 运行时加 `--url http://localhost:<port>/<route>`）。修复每一条 FAIL 并重跑，直到干净。截图由 render 层写入；绝不用手驱动浏览器。
2. 加载 [`references/gates.md`](references/gates.md) § 5，逐条走查 J 与 R/J 闸门。每一条 WARN 都要确认或驳回。Floor 的每一条未决发现都要修复；Reflex 的每一条都要修复或豁免（waive）；Finish 的每一条都要回应。
3. 在全新上下文中进行 finish review（`gates.md` § 6；评审者读取它自己的提示词，你绝不去打开 `review-*.md`）：按其首个词行动（`recapture`、`rebuild`、`fix`、`ship`），并自行给修复打分。
4. 以素材请求收尾：列出每个槽位、它的尺寸与该放什么，然后提出最能提升页面的一件素材。
5. 更新 Picks block：构建中有改动的任何一行，以及最后一行写入结果（`Floor 0 FAIL · Reflex 2 (1 waived: 47b) · finish-review: subagent, 3 resolved`）。伪造的通过本身就是 slop（AI 垃圾内容）。

验证是有预算的：一次合并检查、一批修复、至多一轮确认；每次评审增加一批修复及其对应的 recapture（重新截图）。

## Branches（分支）

见 [`references/flow.md`](references/flow.md)，一次只读一节：component scope（组件范围）、app screens（应用屏）、signal 8、comp before build（构建前出视觉稿）、各 Harness 的开关（harness levers）、pre-flight 的边界情况、**fast mode**（`--fast`，或提示词里出现 quick、rough 或 prototype）与编辑期 Hook。在既有项目中，先列出你将要触碰的文件；未经用户批准的文件级计划，绝不删除任何路由或组件树。
