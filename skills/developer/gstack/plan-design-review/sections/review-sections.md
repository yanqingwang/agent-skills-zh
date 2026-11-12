<!-- AUTO-GENERATED from review-sections.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`plan-design-review/sections/review-sections.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## 评审章节（7 个 pass，范围达成一致之后）

**反跳过规则：**无论计划类型（战略、规格、代码、基础设施），绝不压缩、缩写
或跳过任何评审 pass（1-7）。本 Skill 的每个 pass 都有存在理由。"这是战略
文档，所以设计 pass 不适用"永远是错的：设计缺口正是实现崩掉的地方。某
pass 确实零发现就说"未发现问题"继续，但你必须评估它。

**上下文：**本节延续 `plan-design-review/SKILL.md`。它的设置已不在上下文时，
Read `~/.claude/skills/gstack/plan-design-review/SKILL.md` 取系统审计、设计
哲学、Step 0、Step 0.5 mockup 设置（`$D`）与节自检。用其既有结果；不要重
启评审。

**反捷径条款：**每个未决发现完成一个决策循环：说明缺口、推荐选项、取得其
逐项决策、然后应用所选修复。范围、聚焦、设置与下一步选择都不批准补救。绝
不用最后的下一步 AskUserQuestion 来满足问题审批循环。没有未决发现时无需发
问题。

**跨 pass 延续决策。**一个问题就是一个未决的设计要求或权衡，即使它出现在
计划的多处。每个 pass 之前，比对计划、DESIGN.md 与已做的决策：

| 情形 | 必需动作 |
|-----------|-----------------|
| 该确切修复已有逐项用户决策，或前导授权的逐问题自动决策。 | 复用该决策。应用到全部受影响引用与匹配 token；不再问。 |
| 已接受的要求需要原样复制进必需产物，如旅程分镜。 | 直接创建该产物，不另问格式。它记录要求，不批准任何新补救。 |
| 计划违反 DESIGN.md 或有缺口，且没有逐项决策批准过其修复。 | 就该问题提问并等待，再修复；即使输入已点明缺口、或 DESIGN.md 已规定确切 token 也一样。其间把拟议补救保持待定。 |
| 新证据引入缺失要求、冲突或新权衡。 | 点名新问题、给出备选，取得其逐项决策后再改计划。 |

写报告、映射 token、创建 mockup 或列任务都不批准补救。有发现但只回答了导航
时，评审仍在等它的第一个问题决策。

## Prior Learnings

搜索既往会话中的相关学习：

```bash
_CROSS_PROJ=$(~/.claude/skills/gstack/bin/gstack-config get cross_project_learnings 2>/dev/null || echo "unset")
echo "CROSS_PROJECT: $_CROSS_PROJ"
if [ "$_CROSS_PROJ" = "true" ]; then
  { _LE=$(~/.claude/skills/gstack/bin/gstack-learnings-search --limit 10 --cross-project 2>&1 >&3 3>&-); _LR=$?; } 3>&1
else
  { _LE=$(~/.claude/skills/gstack/bin/gstack-learnings-search --limit 10 2>&1 >&3 3>&-); _LR=$?; } 3>&1
fi
[ "$_LR" = 0 ] || { _LE=${_LE%%$'\n'*}; echo "LEARNINGS: unavailable (${_LE:-exit $_LR})"; }

```

`CROSS_PROJECT` 为 `unset`（首次）：用 AskUserQuestion：

> gstack 可以搜索你本机其他项目的学习，找出可能适用于此处的模式。全程本
> 地（无数据离开你的机器）。推荐单人开发者使用。若你在多个客户代码库之间
> 工作、担心交叉污染，则跳过。

选项：
- A) 启用跨项目学习（推荐）
- B) 学习仅限项目内

选 A：运行 `~/.claude/skills/gstack/bin/gstack-config set cross_project_learnings true`
选 B：运行 `~/.claude/skills/gstack/bin/gstack-config set cross_project_learnings false`

然后用相应 flag 重跑搜索。

找到学习时，把它纳入分析。评审发现与既往学习匹配时，展示：

**"应用既往学习：[key]（置信度 N/10，来自 [日期]）"**

这让复利可见。用户应看到 gstack 在其代码库上越来越聪明。

用计划与被引用的既有契约评估每个 pass。被显式排除的产物不是缺失要求：用允许
的证据评估同一维度。只为具体设计缺口重开那个排除，并在改动前先问。

**Pass 协议（1-6）：**记录初始 0-10 分。下方每个 `FIX TO 10` 都是提议：逐
问题提问、等批准、然后改计划并带分数变化理由重评该 pass。绝不先改再问。

被拒绝的修复仍然记录在案：未决缺口使评分停在 10 以下。把每个 pass 的前后分
数与剩余缺口带进下方的 Completion Summary。按 Completion Summary 的规定计算
总分；不要把试金石答案或 Pass 7 的决策计数当数值评分。Pass 7 是未打分的决策
登记表，不是第七个评分。

忠实复述既有或已批准的契约（如未变布局的线框）是评审证据而非新设计选择。直
接记录；若产出它会引入或改变设计决策，才提问。以 Required Outputs 与末尾的
Plan File Review Report 收尾，含任何未回答的决策。

### Pass 1：信息架构
打 0-10 分：计划定义了用户第一、第二、第三看到什么吗？
FIX TO 10：把信息层级加进计划。含屏幕/页面结构与导航流的 ASCII 图。应用
"约束崇拜"：只能展示 3 样东西时，是哪 3 样？
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。无问题就说
明并继续。用户答复之前不推进。

### Pass 2：交互状态覆盖
打 0-10 分：计划规定了加载、空、错误、成功、部分状态吗？
FIX TO 10：把交互状态表加进计划：
```
  FEATURE              | LOADING | EMPTY | ERROR | SUCCESS | PARTIAL
  ---------------------|---------|-------|-------|---------|--------
  [each UI feature]    | [spec]  | [spec]| [spec]| [spec]  | [spec]
```
每个状态描述用户**看到**什么，不是后端行为。
空状态是功能：规定温度、主操作、上下文。
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。

### Pass 3：用户旅程与情绪弧
打 0-10 分：计划考虑了用户的情绪体验吗？
FIX TO 10：把已接受的旅程渲染为必需的分镜；不要问是否要创建它：
```
  STEP | USER DOES        | USER FEELS      | PLAN SPECIFIES?
  -----|------------------|-----------------|----------------
  1    | Lands on page    | [what emotion?] | [what supports it?]
  ...
```
应用时间轴设计：5 秒本能层、5 分钟行为层、5 年反思层。
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。

### Pass 4：AI 腔风险

**Pass 4 评估：**打 0-10 分：计划描述的是具体、有意图的 UI，还是泛用模式？
记录每条硬性拒绝命中与试金石 YES/NO 及其证据。未解决的硬性拒绝把本 pass 钳
在 8 以下（未达设计完整），不自动把分数设为 0。试金石答案支撑发现，不是另一
个数值分。
用计划文本与任何可用 mockup 作为下方规则的证据。

#### 设计硬规则

把这些当作计划、获批 mockup 与被引用既有契约中的 UI 要求来评审。有已渲染表
面时检查像素或计算值；否则评估计划规定了什么并指出具体缺口。

**分类器：应用规则之前先点名模式。**模式是访客在**这个表面**上的赢面长什么
样，不是产品是什么。开发工具的落地页是 Persuade。时装屋的文档是 Read。
- **PERSUADE**（营销/落地页：hero 驱动、品牌优先、定价、活动）→ 他们决定并
  行动。设计**就是**产品。应用 Landing Page 规则。
- **OPERATE**（应用 UI：仪表盘、管理后台、设置、编辑器、工具）→ 他们完成任
  务。可扫读性与原生预期胜过表达；品牌活在细节里。应用 App UI 规则。
- **READ**（文档、文章、指南、changelog）→ 他们理解某事。为理解而结构化，
  然后让停留值得。应用 Read 规则。
- **EXPERIENCE**（作品集、画廊、展示）→ 他们身处作品之中。产物拥有首屏；界
  面让路。应用 Experience 规则。
- **HYBRID**（营销外壳加类应用区块）→ 按区块分类，不按页面。

**硬性拒绝标准**（即时失败模式：任一命中就标出）：
1. 第一印象是泛用 SaaS 卡片网格
2. 图片漂亮但品牌孱弱
3. 大标题没有清晰行动
4. 文字背后是杂乱影像
5. 各节重复同一情绪陈述
6. 没有叙事目的的轮播
7. 应用 UI 用堆叠卡片而非布局

**试金石检查**（逐条答 YES/NO 并给证据；有外部声音试金石记分卡时与之对比。
这些支撑发现，不是额外的数值分）：
1. 首屏品牌/产品是否明确无误？
2. 是否有唯一强视觉锚点？
3. 只扫标题能否理解页面？
4. 每节是否只有一个职责？
5. 卡片是否真的必要？
6. 动效是否改善层级或氛围？
7. 去掉全部装饰性阴影后设计是否依然高级？

**落地页规则**（分类器 = PERSUADE / 营销/落地页时应用）：
- 首屏读起来是一个构图，不是仪表盘
- 品牌优先的层级：品牌 > 大标题 > 正文 > CTA
- 排版：表现力强、有意图：不用默认字体栈（Inter、Roboto、Arial、system）
- 默认不用平淡纯色背景：质感来自品牌或真实素材，绝不用光晕、聚光灯、条
  纹或网格纸渐变（见下方 AI slop 黑名单与检测器规则 id）
- Hero：满幅、通边，不用内嵌/平铺/圆角变体
- Hero 预算：品牌、一个大标题、一句支撑句、一组 CTA、一张图
- hero 里不放卡片。只有卡片**就是**交互时才用卡片
- 每节一个职责：一个目的、一个大标题、一句简短支撑句
- 动效：首屏一个作者性时刻（入场或滚动联动揭示），从可见默认值开始 ease-out；
  hover 只在携带信息处使用
- 配色：定义 CSS 变量，避免白底紫的默认，默认一个强调色
- 文案：产品语言而非设计评论。"删掉 30% 会更好就继续删"
- 漂亮的默认值：构图优先、品牌是最响的文字、最多两种文字字体（加一种等宽
  用于数据与代码）、默认不用卡片、首屏是一个构图而非文档（姿态像海报，字号
  不像：display 保持 6rem 以下）

**App UI 规则**（分类器 = OPERATE / 应用 UI 时应用）：
- 平静的表面层级、强排版、少颜色
- 密集但可读、最少镀铬
- 组织：主工作区、导航、次级上下文、一个强调色
- 避免：仪表盘卡片马赛克、粗边框、装饰性渐变、装饰性图标
- 文案：实用语言：定位、状态、动作。不写情绪/品牌/愿景
- 只有卡片**就是**交互时才用卡片
- 分区标题说明该区域是什么、或用户能做什么（"Selected KPIs"、"Plan
  status"）

**Read 规则**（分类器 = READ 时应用）：
- 行宽 65-75ch，单一阅读栏，标题离后文比离前文更近
- 寻路是功能：我在哪、下一步是什么、在哪搜索
- 文档索引是 Read 不是 Persuade：没有 hero，没有 CTA 戏台

**Experience 规则**（分类器 = EXPERIENCE 时应用）：
- 作品填满首屏；镀铬的每个像素都要挣来
- 一个作者性过渡，不是劫持滚动的导览
- 绝不为套模板裁剪作品

**通用规则**（适用于所有类型）：
- 为配色系统定义 CSS 变量
- display 声部不用默认字体栈（Inter、Roboto、Arial、system）；Operate 或
  Read 表面的 body/UI，在提案明确指派该角色时允许 DM Sans、Instrument
  Sans、IBM Plex Sans
- 每节一个职责
- "删掉 30% 文案会更好就继续删"
- 卡片要挣得存在：不做装饰性卡片网格
- 绝不用小而低对比的字（正文 < 16px，或正文对比度 < 4.5:1）
- 绝不把标签放进表单字段当唯一标签（占位符当标签模式：字段有内容时标签必须
  可见）
- 始终保留已访问与未访问链接的区分（已访问链接颜色必须不同）
- 绝不让标题悬在段落之间（标题必须视觉上更靠近它所引导的章节，而非前一段）

**检测器抓不到的反身动作**（每次都要手工检查）：
- **浏览器表面承载设计。**选中色、光标、滚动条、焦点环、下划线偏移、表格数
  字全都带着属于任何设计系统的浏览器默认值。用配色给它们上主题。这是页面"被
  设计过"而非被拼装出来的最廉价线索，也是模型最常跳过的一项。
- **一个作者性动效时刻。**不是每节同样的入场，不是所有东西都加 hover。从已
  可见的默认值开始指数 ease-out。内容绝不藏在动画时序之后。
- **纵深是有偏移的。**阴影是有偏移加柔和模糊。零偏移的彩色光晕是装饰，不是
  纵深。
- **彩色表面上的次级文字由该色相染色。**绝不用灰。
- **标题上方的留白多于下方。**读计算值。
- **明暗来自使用场景。**谁、在哪、什么光线下：一句话。绝不来自品类。

**校准：三种观感。**AI 搭的界面无论产品是什么都落在三种观感之一：（1）米色
底、高对比衬线 display、陶土或信号红强调；（2）近黑、一个霓虹强调、发光边
缘；（3）大开张细线、斜体 display 衬线、微小字距等宽标签。brief 要求时每种
都好。brief 没定调而你仍落进其中一种，说明你停止观察了。检验：有人能只凭品
类猜出你的观感吗？凭"这个品类，但避开显而易见的那种"能猜出吗？两者任一，重
来。"这是讲书的，所以米色加衬线"过不了这个检验。书布与书封什么饱和色都有。

**AI slop 黑名单**（11 个尖叫"AI 生成"的模式）：
1. 紫/紫罗兰/靛蓝渐变背景，或蓝到紫的配色
2. **三列功能网格**：彩色圆里的图标加粗标题加两行描述，对称重复三次。最能
   认出 AI 的布局。
3. 彩色圆里放图标作分区装饰（SaaS 模板外观）
4. 全部居中（所有标题、描述、卡片都 `text-align: center`）
5. 每个元素都用同样圆润的 border-radius（所有东西同一个大圆角）
6. 装饰性斑块、漂浮圆、波浪 SVG 分隔（某节显得空，是需要更好的内容，不是装
   饰）
7. Emoji 当设计元素（标题里的火箭、把 emoji 当 bullet）
8. 卡片左侧彩色边框（`border-left: 3px solid <accent>`）
9. 泛用 hero 文案（"Welcome to [X]"、"Unlock the power of..."、
   "Your all-in-one solution for..."）
10. 模板化分区节奏（hero → 3 个功能 → 推荐语 → 定价 → CTA，每节同高）
11. system-ui 或 `-apple-system` 当**主** display/body 字体：那句"我放弃排
    版了"的信号。选一个真正的字体。

目录其余部分的检测器规则 id（发现里的 `[rule-id]` 就是其中之一）：
border-accent-on-rounded: 圆角卡片上的彩色边；overused-font: 过度使用的
display 字体；flat-type-hierarchy: 扁平排版层级；gradient-text: 渐变文字；
cream-palette: 米色默认配色；nested-cards: 嵌套卡片；monotonous-spacing:
单调间距；bounce-easing: 弹跳缓动；pulsing-dot: 脉冲状态点；blinking-cursor:
闪烁光标效果；shape-assembled-illustration: 形状拼装插图；dark-glow: 深色
模式发光；radial-halo: 径向光晕；radial-spotlight-glow: 径向聚光灯；marquee:
logo 跑马灯；icon-tile-stack: 每个标题上方的图标方块；italic-serif-display:
斜体衬线 display；hero-eyebrow-chip: hero 眉标 chip；kicker-above-heading:
标题上方 kicker；numbered-section-labels: 编号分区标签；em-dash-overuse:
破折号滥用；marketing-buzzword: 营销热词；aphoristic-cadence: 格言式节奏；
oversized-h1: 过大的 h1；extreme-negative-tracking: 极端负字距；
gpt-thin-border-wide-shadow: 细边框加大阴影；repeating-stripes-gradient: 重
复条纹渐变；codex-grid-background: 网格纸背景；theater-slop-phrase: 戏台句；
image-hover-transform: 图片 hover 缩放。
无检测器规则的判断性线索：渐变 CTA 按钮、图库照片 hero、卡片当默认组件、泛
用推荐语区块、左文右图 hero、泛用 CTA 标签、hero 指标模板、一模一样的卡片网
格、磨砂玻璃、手绘 SVG 插图、默认用模态框、等宽当戏服、内容占位、按品类选
明暗、未上主题的浏览器表面、缺失状态。

来源：[OpenAI "Designing Delightful Frontends with GPT-5.4"](https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4)
（2026 年 3 月）加 gstack 设计方法论。

FIX TO 10：把含糊的 UI 描述改写为具体替代：
- "带图标的卡片"：它们与每个 SaaS 模板的差别在哪？
- "Hero 区"：什么让这个 hero 感觉像**这个**产品？
- "干净、现代的 UI"：毫无意义。换成真实设计决策。
- "带部件的仪表盘"：什么让它**不**是其他仪表盘？
Step 0.5 生成过视觉 mockup 的话，对照上方 AI slop 黑名单评估它们。用 Read 工
具读每张 mockup 图。它落入泛用模式（三列网格、居中 hero、图库照片感）吗？
是就标出并提供用更具体方向重生成：
`$D iterate --feedback "$(cat "$FEEDBACK_FILE")"`（反馈在私有文件，绝不内
联）；任何后续查看、检查或 board 都用其打印的 `outputPath`。
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。

### Pass 5：设计系统对齐
打 0-10 分：计划与 DESIGN.md 对齐吗？
DESIGN.md 缺失时，评估计划中显式的 token 与组件规格。缺失的规格仍是发现；不
跳过评分，也不假设已对齐。
FIX TO 10：DESIGN.md 存在就标注具体 token/组件；它有 YAML front matter（开
放 DESIGN.md 格式）时按路径引用 token（`{colors.primary}`、`{rounded.md}`），
让计划与文件共用一套词汇。没有 DESIGN.md 就标出缺口并推荐
`/design-consultation`。
标出任何新组件：它贴合既有词汇吗？
提供 token 对齐修复之前，先查更早的 pass 是否已批准该结果。是则应用既定
token 并在该决策下更新每个过期缺口/引用；换计划位置或把同一修复写清楚都不是
新问题。只有新证据暴露未决要求或权衡时才再问，并点名它。未获批准的违规仍需
它的第一个逐项决策。
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。

### Pass 6：响应式与可访问性
打 0-10 分：计划规定了移动/平板、键盘导航、读屏吗？
FIX TO 10：按视口加响应式规格：不是"移动端堆叠"，而是有意图的布局变化。加
a11y：键盘导航模式、ARIA landmark、触摸目标尺寸（最小 44px）、对比度要求。
**STOP。**每个问题一次 AskUserQuestion。不批量。给推荐加 WHY。

### Pass 7：未决设计决策
从更早 pass 记录的未决选择起步。对每个新项，引用一个真实的范围内元素以及计
划、源码、DESIGN.md 或获批 mockup 中缺失的决策。页面/分区名与外部评审建议
不能确立某个控件存在。先查可用产物；其存在性未知时保持该项为条件式并写明必
须核实什么。不要发明控件，也不要为假想元素重开已接受的处置。只浮现真实的缺
失决策与具体冲突；批准一种处置不会了结另一个已知元素。

保留已接受的用户可见结果。选择实现机制不会重开它们；只有具体约束暴露新的设
计要求或权衡时才问。浮现会让实现陷入困境的其余含糊点：
```
  DECISION NEEDED              | IF DEFERRED, WHAT HAPPENS
  -----------------------------|---------------------------
  What does empty state look like? | Engineer ships "No items found."
  Mobile nav pattern?          | Desktop nav hides behind hamburger
  ...
```
Step 0.5 生成过视觉 mockup 就在浮现未决决策时引用它们作证据。mockup 让决策
变具体：如"你获批的 mockup 显示侧栏导航，但计划没规定移动端行为。这个侧栏在
375px 上怎样？"
每个决策 = 一次 AskUserQuestion，带推荐加 WHY 加备选。决策做出即改计划。
**STOP。**每个答复之后才编辑或推进。未回答的决策记为未决。

### Pass 之后：更新 Mockup（若已生成）

Pass 7 之后：适用时提议下方的 mockup 更新，解决推迟的 TODO 提案，对账批准，
然后综合任务与 Completion Summary。

Step 0.5 生成过 mockup 且评审 pass 改变了重要设计决策（信息架构重构、新状
态、布局变化）时，提议重生成（一次性，不成环）：

AskUserQuestion："评审 pass 改变了 [列出主要设计变化]。要我重生成 mockup 以反
映更新后的计划吗？这保证视觉参照与实际要建的东西一致。"

同意就用 `$D iterate` 带总结变化的反馈，或用更新 brief 的 `$D variants`；两种
文本都进 brief 或反馈文件，绝不内联。存进同一个 `$_DESIGN_DIR` 目录；什么都
不覆盖，所以做轮次记账并把打印路径带进任何新 board（用 board 块重建它，它会重
写 `board-images.json`）或检查。

## 如何提问
遵循上方前导的 AskUserQuestion 格式。计划设计评审的附加规则：
* **一个问题 = 一次 AskUserQuestion 调用。**绝不把多个问题塞进一次提问。每次
  调用恰好一个问题；一次调用里多个问题 tab 也是批量。用户可以选择一个补救而
  不选另一个时，即使两者影响同一组件或 token 文件也分开问。共享实现工作不会
  让独立设计选择变得不可分割。
* 具体描述设计缺口：缺什么、不规定的话用户体验到什么。
* 给 2-3 个选项。每个含：现在规定的成本、推迟的风险。
* **映射到上方设计原则。**一句话把推荐接到某条具体原则。
* 标注为 问题编号 + 选项字母（如 "3A"、"3B"）。
* **零发现：**某节零发现就说"无问题，继续"并推进。否则每个缺口都用
  AskUserQuestion：带"显而易见修复"的缺口仍是缺口，改动落进计划前仍需用户批
  准。
* **绝不用 AskUserQuestion 问用户偏好哪个变体。**始终先创建对比板
  （`$D compare --serve`）并在浏览器打开它。板有评分控件、评论、remix/
  regenerate 按钮与结构化反馈输出。AskUserQuestion **只**用来告知用户板已开
  并等他们完成，不是内联呈现变体问"你更喜欢哪个？"那是降级体验。

## 必需输出

### "NOT in scope" 节
考虑过并显式推迟的设计决策，各附一行理由。

### "What already exists" 节
计划应复用的既有 DESIGN.md、UI 模式与组件。

### TODOS.md 更新
把已批准修复的实现与验证放进计划任务。不要让范围内验证变成可选后续。推迟的
TODO 提案只留给未决/范围外债务或新的范围决策或权衡。pass 之后逐个询问每个此
类 TODO；绝不批量。尊重用户显式推迟。都不剩就说明。

设计债务：缺 a11y、未决响应式行为、推迟的空状态。每个 TODO 含：
* **What：**一行描述这项工作。
* **Why：**它解决的具体问题或解锁的价值。
* **Pros：**做这件事你得到什么。
* **Cons：**做它的成本、复杂度或风险。
* **Context：**足够让 3 个月后接手的人理解动机的细节。
* **Depends on / blocked by：**任何前提。

然后给选项：**A)** 加进 TODOS.md **B)** 跳过：不够有价值 **C)** 这个 PR 里
现在就做，不推迟。

综合任务或完成总结之前，执行
`~/.claude/skills/gstack/plan-design-review/SKILL.md` 里节自检的批准对账（不在
上下文就 Read 它）。只导出已同意的实现工作；未批准的补救作为待定发现保留。
"Decisions made" 与评审日志只计逐项批准的新决策；拟议补救或下一步答案贡献为
零。

## 实现任务

结束本次评审之前，把上方发现综合成一份扁平的、可构建任务清单。每个任务源自
一个具体发现：不注水。既输出 markdown 节，也写一份 JSONL 产物供 `/autoplan`
跨阶段聚合。

### Markdown 节（始终输出）

```markdown
## Implementation Tasks
Synthesized from this review's findings. Each task derives from a specific
finding above. Run with Claude Code or Codex; checkbox as you ship.

- [ ] **T1 (P1, human: ~2h / CC: ~15min)** — <component> — <imperative title>
  - Surfaced by: <section name> — <specific finding text or line reference>
  - Files: <paths to touch>
  - Verify: <test command or manual check>
- [ ] **T2 (P2, human: ~30min / CC: ~5min)** — ...
```

规则：
- P1 阻塞发布；P2 应同一分支落地；P3 是后续 TODO。
- 某发现没产出可执行任务就不要编一个。
- 某节零发现就输出 `_No new tasks from <section>._`
- 展示人类团队与 CC+gstack 工作量估算。默认任务类型比例（人类 ÷ CC 时间）：
  脚手架约 100 倍、测试约 50 倍、功能约 30 倍、带回归的 bug 修复约 20 倍、
  架构约 5 倍、调研约 3 倍。按实际工作调整并说明假设。

### JSONL 产物（始终写，即使零任务）

`/autoplan` 读这个文件跨阶段聚合。每行都用 `jq -nc` 构建，让含引号、换行或
反斜杠的标题与来源发现干净序列化：绝不用手搓 `echo` / `printf`。

```bash
GSTACK_STATE_ROOT=$(~/.claude/skills/gstack/bin/gstack-paths --get GSTACK_STATE_ROOT); : "${GSTACK_STATE_ROOT:?gstack-paths failed; reinstall with ./setup or /gstack-upgrade}"
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null)
TASKS_DIR="$GSTACK_STATE_ROOT/projects/${SLUG:-unknown}"
mkdir -p "$TASKS_DIR"
TASKS_FILE="$TASKS_DIR/tasks-design-review-$(date +%Y%m%d-%H%M%S).jsonl"
COMMIT=$(git rev-parse HEAD 2>/dev/null || echo unknown)
# The task record keeps the raw git branch; artifact filenames keep gstack-slug's sanitized BRANCH.
GIT_BRANCH=$(git branch --show-current 2>/dev/null || echo unknown)
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)-$$"

# Repeat ONE jq invocation per task identified during this review.
# Substitute the placeholders inline with shell variables you set per task:
#   TASK_ID (T1, T2, ...), PRIORITY (P1/P2/P3), COMPONENT, TITLE,
#   SOURCE_FINDING, EFFORT_HUMAN, EFFORT_CC, FILES_JSON (a JSON array literal
#   like '["browse/src/sanitize.ts","browse/src/server.ts"]').
jq -nc \
  --arg phase 'design-review' \
  --arg run_id "$RUN_ID" \
  --arg branch "$GIT_BRANCH" \
  --arg commit "$COMMIT" \
  --arg id "$TASK_ID" \
  --arg priority "$PRIORITY" \
  --arg component "$COMPONENT" \
  --arg effort_human "$EFFORT_HUMAN" \
  --arg effort_cc "$EFFORT_CC" \
  --arg title "$TITLE" \
  --arg source_finding "$SOURCE_FINDING" \
  --argjson files "$FILES_JSON" \
  '{phase:$phase, run_id:$run_id, branch:$branch, commit:$commit, id:$id, priority:$priority, component:$component, files:$files, effort_human:$effort_human, effort_cc:$effort_cc, title:$title, source_finding:$source_finding}' \
  >> "$TASKS_FILE"

```

`jq` 未安装时，回退为跳过 JSONL 写入并警告用户安装 jq 以便 autoplan 聚合。
绝不手搓 JSONL。

本次评审零任务时，仍 touch 该 JSONL 文件（`: > "$TASKS_FILE"`），让聚合器看
到本阶段本次运行产出了输出（空文件意为"跑了，无发现"，与"没跑"区分）。


### 完成总结
为保存的评审准备它；在下方 Read-back 门之后宣布完成。
在计划文件里把它写为独立的 `## Design Review Completion Summary` 节（下方
框、推迟清单与 Unresolved Decisions），放在终结的 `## GSTACK REVIEW REPORT`
之前，替换本次评审更早的那一份。绝不要写进报告内部：下一次计划评审会删除并
重生成该标题下的全部内容。

**整体设计分：**用六个已评分 pass（1-6）中的最低分，分别在批准修复前后。Pass 7
不打分。Step 0 的初始印象保留在自己那行。因此整体 8+ 意味着每个已评分 pass
都是 8+；未决发现仍阻止干净的评审日志。

```
  +====================================================================+
  |         DESIGN PLAN REVIEW — COMPLETION SUMMARY                    |
  +====================================================================+
  | System Audit         | [DESIGN.md status, UI scope]                |
  | Step 0               | [initial rating, focus areas]               |
  | Pass 1  (Info Arch)  | ___/10 → ___/10 after fixes                |
  | Pass 2  (States)     | ___/10 → ___/10 after fixes                |
  | Pass 3  (Journey)    | ___/10 → ___/10 after fixes                |
  | Pass 4  (AI Slop)    | ___/10 → ___/10 after fixes                |
  | Pass 5  (Design Sys) | ___/10 → ___/10 after fixes                |
  | Pass 6  (Responsive) | ___/10 → ___/10 after fixes                |
  | Pass 7  (Decisions)  | ___ resolved, ___ deferred                 |
  +--------------------------------------------------------------------+
  | NOT in scope         | written (___ items)                         |
  | What already exists  | written                                     |
  | TODOS.md updates     | ___ items proposed                          |
  | Approved Mockups     | ___ generated, ___ approved                  |
  | Decisions made       | ___ added to plan                           |
  | Decisions deferred   | ___ (listed below)                          |
  | Overall design score | ___/10 → ___/10                             |
  +====================================================================+
```

Read-back 之后，全部 pass 8+ 时："Plan is design-complete. Run
/design-review after implementation for visual QA."
任何低于 8：说明什么未决、为什么（用户选择推迟）。

### Unresolved Decisions
在此列出每个未决发现，含尚未提问的发现或未回答的 AskUserQuestion。绝不静默默
认某个选项。

### Approved Mockups

本次评审生成过视觉 mockup 时，在计划文件里加：

```
## Approved Mockups

| Screen/Section | Mockup Path | Direction | Notes |
|----------------|-------------|-----------|-------|
| [screen name]  | [absolute $_DESIGN_DIR]/[filename].png | [brief description] | [constraints from review] |
```

含每张获批 mockup 的完整路径（用户选中的变体）、方向的一行描述与任何约束。
实现者靠它确切知道从哪张图建。它们跨对话与工作区持久。没生成 mockup 就省略本
节。

## 计划文件评审报告

记录或宣布完成之前，保存已接受计划变更与完整评审输出（含下方报告）。

### 检测计划文件

优先用显式请求的输出/报告文件。否则用用户点名的被评审计划，再否则用宿主活跃
计划。范围内无文件就跳过本节；常规的无文件评审记录照常适用。

### 生成报告

跑 `~/.claude/skills/gstack/bin/gstack-review-read` 取既往评审条目。
用当前 Completion Summary 或 DX Scorecard 作为本次评审的状态与发现；应用下方
Review Log 字段规则并在其既往运行数上加恰好一。不要为填充报告而预先记录本次
运行。其他评审用既往条目，保留其状态、归属与新鲜度。

用记录的 provenance 解析每条 JSONL 条目。历史 source "claude" 是原生 Claude
子代理；"claude-code" 是外部 CLI。保留历史 codex 标识符，绝不用当前 harness
重新标注旧记录。未知模型身份保持未知。新记录展示 host、outside_provider、
outside_status 与 phase。只有已完成的 external 记录确立外部覆盖；原生兜底不
算。

每个 Skill 记录的字段不同：

- **plan-ceo-review**：`status`、`unresolved`、`critical_gaps`、`mode`、
  `scope_proposed`、`scope_accepted`、`scope_deferred`、`commit`
  → Findings："{scope_proposed} proposals, {scope_accepted} accepted,
  {scope_deferred} deferred"
  → scope 字段为 0 或缺失时（HOLD/REDUCTION 模式）："mode: {mode},
  {critical_gaps} critical gaps"
- **plan-eng-review**：`status`、`unresolved`、`critical_gaps`、
  `issues_found`、`mode`、`commit`
  → Findings："{issues_found} issues, {critical_gaps} critical gaps"
- **plan-design-review**：`status`、`initial_score`、`overall_score`、
  `unresolved`、`decisions_made`、`commit`
  → Findings："score: {initial_score}/10 → {overall_score}/10,
  {decisions_made} decisions"
- **plan-devex-review**：`status`、`initial_score`、`overall_score`、
  `product_type`、`tthw_current`、`tthw_target`、`mode`、`persona`、
  `competitive_tier`、`unresolved`、`commit`
  → Findings："score: {initial_score}/10 → {overall_score}/10, TTHW:
  {tthw_current} → {tthw_target}"
- **devex-review**：`status`、`overall_score`、`product_type`、
  `tthw_measured`、`dimensions_tested`、`dimensions_inferred`、
  `boomerang`、`commit`
  → Findings："score: {overall_score}/10, TTHW: {tthw_measured},
  {dimensions_tested} tested/{dimensions_inferred} inferred"
- **codex-review**：`status`、`gate`、`findings`、`findings_fixed`
  → Findings："{findings} findings, {findings_fixed}/{findings} fixed"

当前行与其后续日志必须描述同一份已保存评审。

产出这张 markdown 表：

```markdown
## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | {runs} | {status} | {findings} |
| Outside Review | {recorded provider and trigger} | Independent 2nd opinion | {runs} | {outside_status} | {findings} |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | {runs} | {status} | {findings} |
| Design Review | `/plan-design-review` | UI/UX gaps | {runs} | {status} | {findings} |
| DX Review | `/plan-devex-review` | Developer experience gaps | {runs} | {status} | {findings} |
```

表下加这几行。**OUTSIDE COVERAGE** 与 **CROSS-MODEL** 是条件性的：阶段运行
过、被禁用/跳过/不可用、或有发现时包含；没有此类阶段时才省略。**VERDICT** 永
远在：

- **OUTSIDE COVERAGE：**提供方、阶段、完成状态和发现。不可用、被禁用和被跳
  过的阶段都要包含；绝不从其他阶段推断完成。
- **CROSS-MODEL：**仅当存在原生评审和已完成的 external 评审时：重叠分析要写
  记录的提供方与已知模型身份。不要从 harness 名推断模型家族。
- **VERDICT：**列出 CLEAR 的评审（如 "CEO + ENG CLEARED — ready to
  implement"）。Eng Review 不 CLEAR 且未被全局跳过时，追加
  "eng review required"。

**未决决策状态（强制：绝不可省；报告最后一个非空白行）。** VERDICT 之后，以
以下之一结束报告（`## GSTACK REVIEW REPORT` 标题下的内容：一个粗体标签，绝不
是新的 `## ` 标题；豁免于"为空即省略"规则）：精确的非粗体行
`NO UNRESOLVED DECISIONS`（粗体的不算），或 `**UNRESOLVED DECISIONS:**` 标头
加每个未决项一条 bullet（最后一条 bullet 是末行；仅当 N > 0 时加
`+ N unresolved from prior reviews`）。这避免重复计数：从上下文列出本次评审
的未决项；既往评审在你 DROP 当前 Skill 那一行之后，对每个 Skill 最新 fresh 行
的 `unresolved` 求和（dashboard 7 天窗口）；两者皆零才输出哨兵行。

### 写入计划文件

**PLAN MODE EXCEPTION — ALWAYS RUN：**只应用已接受变更地保存完整被评审计划/
报告；未决选择保持待定。

报告必须永远是计划文件的最后一节：绝不在文件中部。
用单一的"删除后追加"流程：

1. 读既有计划/报告（若有）。保留其内容，只应用已接受变更；含完整评审输出。
   定位任何既有的 `## GSTACK REVIEW REPORT` 节。
2. 找到时，用 Edit 工具删除整个既有节。匹配从
   `## GSTACK REVIEW REPORT` 到下一个 `## ` 标题或文件末尾（先到者）。替换为
   空字符串。无论该节现在在哪都适用：中段删除是有意为之，不是特例。Edit 失
   败（如并发编辑改了内容）时，重读计划文件并重试一次。
3. 删除过报告时，Read 更新后的文件。在 EOF 追加新的
   `## GSTACK REVIEW REPORT`。用 Edit 匹配最近一次 Read 确认的文件后缀，或用
   Write 写全文件、报告最后。无论此前是否有报告都追加。
   "Unresolved Decisions" 在后面还有其他节时不是 EOF 锚点。
4. **Read-back 门：**Read 已保存文件。核验已接受变更、完整评审输出、当前评审
   行、判定与最终未决决策状态，且 `## GSTACK REVIEW REPORT` 是最后一节。写入
   或验证失败就报告错误并在 Review Log 或决策记录之前停止。

不要原地替换该节；删掉它、在 EOF 追加新报告，让评审报告永远是计划的最后一
节。

## Review Log

范围内有计划/报告文件时，只在其成功写入与上方 Read-back 之后持久化。失败就
报告错误并停止；不记录完成或已接受决策。
**PLAN MODE EXCEPTION — ALWAYS RUN after verification：**这些命令把评审元数据
写进 `~/.gstack/`；随后的 dashboard 读已保存结果。

```bash
~/.claude/skills/gstack/bin/gstack-review-log '{"skill":"plan-design-review","timestamp":"TIMESTAMP","status":"STATUS","initial_score":N,"overall_score":N,"unresolved":N,"decisions_made":N,"commit":"COMMIT"}'

```

用 Completion Summary 的值替换：
- **TIMESTAMP**：当前 ISO 8601 日期时间
- **STATUS**：整体分 8+ 且 0 未决时 "clean"；否则 "issues_open"
- **initial_score**：修复前的整体初始设计分（0-10）
- **overall_score**：修复后的最终整体设计分（0-10）
- **unresolved**：未决设计决策数
- **decisions_made**：加进计划的设计决策数
- **COMMIT**：`git rev-parse --short HEAD` 的输出

## Review Readiness Dashboard

完成评审后，读评审日志与配置以展示 dashboard。

```bash
~/.claude/skills/gstack/bin/gstack-review-read

```

**1. 选要展示的记录。**每行用最新记录。不用超过 7 天的记录清行，绝不用更旧
的成功顶替更新的失败。Ship 指标不是评审记录。

| 行 | 选最新的 | 状态后缀 |
|---|---|---|
| Eng Review | `review` 或 `plan-eng-review` | (DIFF) 或 (PLAN) |
| CEO Review | `plan-ceo-review` | — |
| Design Review | `plan-design-review` 或 `design-review-lite` | (FULL) 或 (LITE) |
| Adversarial | `adversarial-review` 或 legacy `codex-review` | — |
| Outside Voice | CEO 或 Eng review 的 `codex-plan-review` | — |

保留每条记录的 host、source、outside_provider、outside_status 与 phase。历史
source "claude" 是原生子代理；"claude-code" 是外部 CLI。不要用今天的 harness
推断旧提供方或未知模型。原生结果不填补缺失、禁用或跳过的外部覆盖。

**来源归属：**把记录到的 `via` 加进后缀（"CLEAR (PLAN via /autoplan)"）；没有
就保持 "CLEAR (PLAN)" 或 "CLEAR (DIFF)"。dashboard 下方，按工作流运行与阶段分
组展示 `autoplan-voices` 与 `design-outside-voices`。展示每阶段的 provider 与
outside_status；保留部分覆盖。这些细节不清 Eng Review。

**2. 选判定前先查新鲜度。**

- **内容优先规则：**对 `review`、`adversarial-review`、`codex-review`、ship
  阶段评审和 `design-review-lite`，用 `review_freshness.status` 并展示其
  `reason`。CURRENT 指一次完成的干净评审，其起止内容指纹等于当前
  `---WTREE---` 指纹。STALE 或 UNVERIFIED 清不了 Eng Review。缺
  `review_freshness`（含 legacy 仅日志记录）即 UNVERIFIED。绝不为 diff 证据
  回退到 HEAD 相等或 commit 距离，即使零 commit。展示记录的轮数、
  completed/converged 字段和缺失的 source/phase 覆盖。未知覆盖不是通过。
- **计划记录**（plan-ceo-review、plan-eng-review、plan-design-review 和
  codex-plan-review）用 7 天窗口，不用工作区指纹。有 `plan_sha256` 时可对比
  计划文件并报告不匹配。把记录的 commit 与 `---HEAD---` 对比；不同则运行
  `git rev-list --count STORED_COMMIT..HEAD` 并报告
  "Note: {skill} review from {date} may be stale — {N} commits since
  review"。命令失败即 UNKNOWN，按过期处理；无 commit 跟踪就建议重跑。全部评
  审都新鲜时省略注记。

**3. 选历史判定。**CLEARED 要求所选 Eng Review 为 `clean`、7 天内、且按第 2
步新鲜。否则报 NOT CLEARED 及其缺失、过期或 open-issue 的原因。
`skip_eng_review` 为 true 时，Eng Review 显示 "SKIPPED (global)" 且本
dashboard 判 CLEARED。Eng Review 默认必需；
`gstack-config set skip_eng_review true` 关闭该要求。

其他行提供上下文，不替代 Eng Review：
- 产品/业务或范围决策建议 CEO Review，例行修复或清理不必。
- UI/UX 工作建议 Design Review，后端、基础设施或纯提示词工作不必。
- Adversarial review 始终含原生 pass。可用且启用的外部挑战是补充；200+ 行的
  diff 还要过结构化 P1 门。
- Outside Voice 是 CEO/Eng review 之后默认开启的计划评审。`codex_reviews`
  关闭该额外步骤。提供方失败用原生兜底并记录外部覆盖缺失；本 dashboard 行绝
  不当发布的门。

**4. 展示 dashboard。**缺失、过期、禁用或不可用的结果显式展示，绝不显示为
CLEAR。新鲜的 `clean` 结果显示 CLEAR，`issues_open` 显示 ISSUES OPEN，不改
存储状态。

```
+====================================================================+
|                    REVIEW READINESS DASHBOARD                       |
+====================================================================+
| Review          | Runs | Last Run            | Status    | Required |
|-----------------|------|---------------------|-----------|----------|
| Eng Review      |  1   | 2026-03-16 15:00    | CLEAR     | YES      |
| CEO Review      |  0   | —                   | —         | no       |
| Design Review   |  0   | —                   | —         | no       |
| Adversarial     |  0   | —                   | —         | no       |
| Outside Voice   |  0   | —                   | —         | no       |
+--------------------------------------------------------------------+
| VERDICT: CLEARED — Eng Review passed                                |
+====================================================================+
```

## 记录学习

本会话发现了非显而易见的模式、坑或架构洞见时，为未来会话记录：

```bash
~/.claude/skills/gstack/bin/gstack-learnings-log '{"skill":"plan-design-review","type":"TYPE","key":"SHORT_KEY","insight":"DESCRIPTION","confidence":N,"source":"SOURCE","files":["path/to/relevant/file"]}'

```

**Types：**`pattern`（可复用方法）、`pitfall`（不要做什么）、`preference`
（用户声明的偏好）、`architecture`（结构性决策）、`tool`（库/框架洞见）、
`operational`（项目环境/CLI/工作流知识）。

**Sources：**`observed`（你在代码里发现的）、`user-stated`（用户告诉你的）、
`inferred`（AI 推断）、`cross-model`（Claude 与 Codex 一致同意）。

**Confidence：**1-10。要诚实。代码中验证过的模式是 8-9。拿不准的推断是 4-5。
用户明确说过的偏好是 10。

**files：**写明该学习引用的具体文件路径。这支持过期检测：那些文件日后被删，
该学习可被标记。

**只记录真正的发现。**明显的东西不记。用户已经知道的东西不记。好的检验：这个
洞见能在未来会话省时间吗？能就记。



## Brain 校准回写（有门控）

除非设置了 `BRAIN_CALIBRATION_WRITEBACK`，且前导/brain-health 输出或 gstack
配置显示 `brain_trust_policy@<endpoint-hash>=personal`，否则跳过。未知则跳过。
两道门都通过时，用 `mcp__gbrain__takes_add` 记录一条持久的类型化预测；不可用
时改用带 gstack:takes 围栏块的 `mcp__gbrain__put_page`。

Take frontmatter：
```yaml
kind: bet
holder: <user identity from whoami>
claim: <one-line prediction the skill is making>
weight: 0.5
since_date: <today's date>
expected_resolution: <date in 1-3 months depending on skill>
source_skill: plan-design-review
```

写入之后，使受影响的摘要失效：

```bash
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null) || true
  ~/.claude/skills/gstack/bin/gstack-brain-cache invalidate brand --project "$SLUG" 2>/dev/null || true

```

## Brain 缓存后台刷新

本 Skill 的工作完成之后（且 telemetry 已记录），为接近 TTL 的缓存摘要踢一次
后台刷新。这是非阻塞的，用户不等。下次调用受益于热缓存。

```bash
SLUG=$(~/.claude/skills/gstack/bin/gstack-slug --get SLUG 2>/dev/null) || true
(~/.claude/skills/gstack/bin/gstack-brain-cache refresh --project "$SLUG" 2>/dev/null &) || true

```


## 下一步：评审链

展示 Review Readiness Dashboard 之后，按本次设计评审发现推荐下一次评审。读
dashboard 输出看哪些评审已跑、是否过期。

**若 eng review 未被全局跳过就推荐 /plan-eng-review**：在 dashboard 输出里查
`skip_eng_review`。为 `true` 时 eng review 已 opt-out：不要推荐。否则 eng
review 是必需的发布门。本次设计评审加入重要交互规格、新用户流程或改了信息架构
时，强调 eng review 需要验证架构影响。eng review 已存在但 commit hash 显示它
早于本次设计评审时，注明它可能过期，应重跑。

**考虑推荐 /plan-ceo-review**：但仅当本次设计评审暴露了根本的产品方向缺口。具
体是：整体设计分初评低于 4/10、信息架构有重大结构问题、或评审浮现了"是不是在
解决正确问题"的疑问，且 dashboard 里没有 CEO review。这是选择性推荐：多数设计
评审**不应**触发 CEO review。

**两者都需要时先推荐 eng review**（必需门）。

**适当时推荐设计探索 Skill**：/design-shotgun 与 /design-html 产出设计产物
（mockup、HTML 预览），不是应用代码。它们与评审一起属于计划模式。本次设计评审
发现值得探索新方向的视觉问题时推荐 /design-shotgun。已有获批 mockup 且需转成
可运行 HTML 时推荐 /design-html。

用 AskUserQuestion 呈现下一步。始终包含手动/停止选项 E；只提供适用的后续
Skill。用户选手动就不再启动其他 Skill 地结束：
- **A)** 接着跑 /plan-eng-review（必需门）
- **B)** 跑 /plan-ceo-review（仅在发现根本产品缺口时）
- **C)** 跑 /design-shotgun：为发现的问题探索视觉设计变体
- **D)** 跑 /design-html：从获批 mockup 生成 Pretext 原生 HTML
- **E)** 跳过：我自己处理下一步

## 格式规则
* 问题编号（1、2、3……），选项字母（A、B、C……）。
* 标注为编号 + 字母（如 "3A"、"3B"）。
* 每个选项最多一句。
* 每个未决问题都暂停。某 pass 没有就说清楚并继续；不要制造问题。
* 每个 pass 前后都打分，便于扫读。
