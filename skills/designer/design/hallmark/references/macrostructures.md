> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/macrostructures.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 宏观结构

二十一个有名字的落地页形态。每个都是一份完整指纹（标题位置、正文构图、分隔语言、按钮语气、图像处理、reveal 模式），打包在一个名字之下。**这是一套词汇表，不是菜单。** 先设计提示词要的页面，再给你设计的那个形态起名，让 Rotation 和关卡 32 有东西可读；先翻这里、照搬翻到的东西，正是二十一个形态塌缩成同样三个的原因。这里没有适合你所设计形态的条目时，直说，把形态按指纹描述（§ 指纹，见下），并给它起个短名字供印记和日志使用（*一个季节页*）。

## 21 个宏观结构，索引

**只读你落在的那个形态的文件**，从 `references/macrostructures/` 里读。不要加载整个目录。slug 稳定；Rotation 从印记和日志里读形态。Nav 和 footer 是形态的一部分，与 hero 一起定案。每个形态文件都点名它由哪些 `layout.md` 构图组成；代码是你的。

- **01 · Bento Grid.** 大小不一的模块块铺成不规则网格。每块是一个功能、一个数字、一张图或一条用户给的引言。节奏来自尺寸变化，不是卡片均质。[`macrostructures/01-bento-grid.md`](macrostructures/01-bento-grid.md)
- **02 · Long Document.** 读起来像一份备忘录、一封信或一篇日志。没有营销结构。连续散文加行内小节标题。页面是关于产品的文学。[`macrostructures/02-long-document.md`](macrostructures/02-long-document.md)
- **03 · Marquee Hero.** hero 就是首屏之上的整页。一句陈述或一个视觉填满视口。首屏之下页面变成别的东西（一份列表、一个网格、散文）。[`macrostructures/03-marquee-hero.md`](macrostructures/03-marquee-hero.md)
- **04 · Stat-Led.** hero 是用户给的一个数字，配上说明它意义的那句话。之后的一切都在支撑或限定它。[`macrostructures/04-stat-led.md`](macrostructures/04-stat-led.md)
- **05 · Workbench.** 真实产品截图是主要内容。页面是对使用中应用的一次导览，短说明字幕代替营销文案。[`macrostructures/05-workbench.md`](macrostructures/05-workbench.md)
- **06 · Conversational FAQ.** 加粗的问题，利落的回答。页面读起来像对产品的一次诚实访谈。每一对问答都可以是一个折叠。[`macrostructures/06-conversational-faq.md`](macrostructures/06-conversational-faq.md)
- **07 · Manifesto.** 论战式大字。页面先告诉读者该相信什么，再告诉他们买什么。[`macrostructures/07-manifesto.md`](macrostructures/07-manifesto.md)
- **08 · Photographic.** 每一屏由一张巨图主导。文字是小注解，不是标题。设计先说"看"，再说"读"。[`macrostructures/08-photographic.md`](macrostructures/08-photographic.md)
- **09 · Quote-Led.** hero 是用户给的一条引文，带署名。标题是别人的声音。[`macrostructures/09-quote-led.md`](macrostructures/09-quote-led.md)
- **10 · Specimen.** 大号衬线展示字、不对称跨栏、发丝线、字排式 CTA、大量留白。只给关于字体、出版或写作的提示词（一家字厂、一本期刊、一家出版社）；光"编辑风"体裁不够格。[`macrostructures/10-specimen.md`](macrostructures/10-specimen.md)
- **11 · Catalogue.** 同一事物各种变体的均匀网格：字体、色板、SKU。页面是库存的视觉索引。[`macrostructures/11-catalogue.md`](macrostructures/11-catalogue.md)
- **12 · Letter.** 第一人称、书面、亲密。以问候开场。读起来像创始人的一张私人便条。[`macrostructures/12-letter.md`](macrostructures/12-letter.md)
- **13 · Index-First.** 页面就是一份链接列表。没有 hero 图，没有叙事流。导航即设计。[`macrostructures/13-index-first.md`](macrostructures/13-index-first.md)
- **14 · Narrative Workflow.** 编号的阶段讲出用户随时间使用产品的故事。每一节是一个阶段；页面是一条流程时间线。[`macrostructures/14-narrative-workflow.md`](macrostructures/14-narrative-workflow.md)
- **15 · Split Studio.** 双联画。每个主要块都把屏幕一分为二，文字一侧，证据另一侧；证据守住自己的那半，各行靠字重变化。[`macrostructures/15-split-studio.md`](macrostructures/15-split-studio.md)
- **16 · Feature Stack.** 左侧吸顶面板放标题，右侧滚动同步切换相关截图。节奏像电影。[`macrostructures/16-feature-stack.md`](macrostructures/16-feature-stack.md)
- **17 · Type Specimen.** 字体就是设计。字厂页面和以定制字体为证据的设计系统。[`macrostructures/17-type-specimen.md`](macrostructures/17-type-specimen.md)
- **18 · Portfolio Grid.** 可筛选的项目卡片。作品即产品的 studio 和设计师主页。[`macrostructures/18-portfolio-grid.md`](macrostructures/18-portfolio-grid.md)
- **19 · Map / Diagram.** 一张大空间图组织整个页面：流程图、平面图、网络图、系统图。[`macrostructures/19-map-diagram.md`](macrostructures/19-map-diagram.md)
- **20 · Ecosystem Index.** 多个发现入口：精选、最新、按分类、按人。平台的价值在浏览，不在宣告。[`macrostructures/20-ecosystem-index.md`](macrostructures/20-ecosystem-index.md)
- **21 · Component Playground.** 可交互的代码加预览块是页面的主要内容。每块预览一个东西并展示怎么复制它。[`macrostructures/21-component-playground.md`](macrostructures/21-component-playground.md)

---

## SaaS 区块牌组：发牌，不要排序

形态是 **Bento Grid、Stat-Led、Workbench 或 Marquee Hero** 且提示词是 B2B SaaS 页面时，从这套牌组构建。卡片有角色，没有位置。牌组的底座由页面能诚实展示、无须编造的东西组成；牌组的顶层只在用户交来材料时才存在。

**基础牌**（始终可用）：

| 牌 | 作用 | 构图 |
| --- | --- | --- |
| Spec sheet | 用产品自带的数字说清它是什么：限额、格式、版本、地区 | Table 或 Rows（`layout.md` § 5） |
| Worked example | 产品在用户的材料上干一件真活：一条命令和它的输出，一张截图和它的说明 | Showcase 或 Split |
| Changelog | 最近三四条条目配真实日期；页面由此证明自己活着 | Rows |
| Comparison anatomy | 产品与今天的做法逐行并排，不打分 | Table |
| Pricing table | 真实价格，两三档；每一档都写"联系销售"，说明品牌不信任买家 | `craft.md` § 9 Pricing |
| FAQ | 像人一样回答真实疑虑；"是的，两家服务商都开箱即用"胜过"集成主流服务商" | [`macrostructures/06-conversational-faq.md`](macrostructures/06-conversational-faq.md) |
| CTA strip | 那个请求，一次，一个按钮 | Band |
| Footer | 收尾，用主题的语气 | `layout.md` § 7 |

**素材牌**（只在用户交来材料时存在，Picks 块点名交来的是什么）：

| 牌 | 需要什么 | 没有它 |
| --- | --- | --- |
| Hero visual | 一张真实截图 | 产品在 `data-slot` 里建（`imagery.md` § 4），或一个字排 hero；slot 之外绝不用样式化 div 冒充 UI（47c） |
| Logo row | 用户自己的客户标志，且有展示许可 | 这张牌不存在；不发明标志，不写"Trusted by"行（46a、54） |
| Three features | 三个具名能力，各配一张截图或数字 | 并进 worked example 或 spec sheet |
| Testimonials | 用户逐字提供的引言，姓名、头衔、公司按原样 | 这张牌不存在；不编像样的名字，不改写（46a、19） |

**每次发牌偏离两次。** (a) 至少弃掉一张基础牌并点名（常被弃的是 CTA strip；footer 绝不弃）。(b) 要么把第二张基础牌提进 hero 的位置（spec sheet 当 hero 说"数字就是卖点"；worked example 当 hero 说"看它干活"），要么把一对相邻的牌有意义地重排（pricing 排在例子之前说"价格就是卖点"）。两步都写进 Picks 块：`deck: -cta +changelog` 或 `deck: -faq · pricing<example`。保住至少五张牌的发牌仍读作完整；低于五张就是一条着陆跑道，不是落地页：补牌或换形态。

牌与牌之间按 `--section-gap` 的三档分隔，可混用（59），每张填满自己的区块（`layout.md` § 4）。

牌组不是盖了章就出的模板：形态决定每张牌长什么样。Bento Grid 页把 spec sheet 和 example 交错织进网格；Stat-Led 页让它们在数字之下自上而下排开；Marquee Hero 页让 marquee 扛主张、example 扛证据。

非 SaaS 的活（Editorial、Manifesto、Letter、Long Document、Quote-Led）不适用这套牌组。一家面包店不需要定价档位对比。

---

## 怎么挑

主题构建时，抽签发形态（SKILL.md 第 2 步）；这些步骤用于材料逼出来的换牌，或没有 Node 的运行。

0. **读材料清单**（SKILL.md 第 2 步）。建立在截图或数字上的形态需要它们，真实或有用户要的 slot；两者都没有，就挑一个靠字排和事实扛住的形态。
1. **读提示词。** 记下强烈指向某个形态的词（"data heavy"、"tell a story"、"a list of links"、"many small features"、"personal note"）。
2. **读 `.hallmark/log.json`**（最新在前）和项目里任何 Hallmark 印记的 `shape:` 字段；最近三个形态被排除。
3. **把提示词对到形态上**，用上面的索引行和 § 领域到三选，然后只打开你落在的那个文件。多数提示词命中两到四个；挑离日志形态最远的那个，并核对 SKILL.md 第 2 步的镜像测试。
4. **只声明一次选择**，写在 Picks 块的 Shape 行和印记的 `shape:` 字段。
5. 拿不准时，取该领域的三选（§ 领域到三选），挑离日志最远的那个。

Hallmark 为两个不同提示词建的两张页面，必须看起来像两个网站，而不是同一个模板的换色。

## 指纹：六根轴

**1. 标题位置。** 左边距（旁注贴着正文；标题旁的标签是眉题，关卡 54）· 悬空（标题浮在空白里）· 居中大字 · 底部对齐（标题锚住底部，内容在上）· 叠压（压在照片或色块上）· 吸顶或钉住 · 按结构编号（真 `<ol>` 配 `counter()`，或一个图形尺度的数字）· 与正文同行（不分段，标题从散文里长出来）。任何位置都行；读起来像错误的，是通栏左对齐内容上头一个窄的自动居中标题。

**2. 正文构图。** 单栏 · 双栏不对称（宽正文，窄边距放说明字幕）· 多栏两端对齐带断词 · 旁注（脚注放外侧边距）· 等宽三栏（参考密度）· 出血加边距重置（正文 65ch，引文提行和图片出血）· 不对称跨栏（网格上 2-1-3 比例）。

**3. 分隔语言。** 发丝线（0.5 到 1px，内缩或出血）· 花饰（一个 fleuron、一个点、一个记号）· 负空间（间隙就是分隔）· 出血色块（换纸就是边缘）· 双线。整页选一种语言，按接缝变化它的重量和位置（9）：每个接缝同样的线同样的间隙，就是模板。

**4. 按钮语气。** 实心（一个实心主按钮）· 描边 · 无样式链接（一个带下划线的词）· 超大实心 · 纯字排（一个有字重的词，不带盒子）· 表单即 CTA（动作就是"填这个字段"）。

**5. 图像处理。** 出血 · 紧贴网格裁切 · 与文字同行 · 边距对齐 · 无。

**6. reveal 模式。** 淡入上浮错开（一次，有编排）· 横向扫过 · 文字揭幕（clip-path 在文字上张开）· 数字跳动（counter，只用于真实数字）· 打字机（只给终端，光标在被敲的命令里）· 无。

指纹：每轴一个选择，写作 `Hanging|Asymmetric spans|Hairline|Outlined|Margin-aligned|None`。两条规则：连贯（选择来自同一个世界；两端对齐的报纸正文配的是字排式 CTA，不是超大实心按钮）和反重复（与最近三条日志条目共享的轴不超过六分之三；主题或材料逼出来的 Image 或 Reveal 上的 None 不算共享选择）。

## 领域到三选，提示词没有点名形态时

来自不同家族（网格主导、文档主导、海报主导、产品主导）的三个形态，都贴合该领域，绝不是三个近亲；离最近一条日志形态最远的那个就是选择：

| 领域词 | 三选 |
| --- | --- |
| 播客、音频、音乐、收听 | Photographic · Quote-Led · Letter |
| 商店、店铺、产品、周边、电商 | Catalogue · Photographic · Bento Grid |
| docs、CLI、SDK、API、库、开源 | Workbench · Long Document · Component Playground |
| 平台、基础设施、可观测性、B2B 工具 | Bento Grid · Workbench · Stat-Led |
| 代理公司、studio、案例、作品集 | Portfolio Grid · Split Studio · Index-First |
| 个人一页站、关于我、简历 | Long Document · Letter · Index-First |
| 餐厅、咖啡馆、酒吧、食物、菜单 | Photographic · Long Document · Catalogue |
| 时尚、服装、美妆、lookbook | Photographic（配真实照片）· Catalogue · Marquee Hero |
| 金融科技、银行、支付、交易 | Stat-Led · Workbench · Long Document |
| 宣言、campaign、公益、倡导 | Manifesto · Quote-Led · Stat-Led |
| 编辑、字厂、杂志、字体 | Specimen · Long Document · Type Specimen |
| 产品发布、SaaS 营销 | Bento Grid · Workbench · Stat-Led |
| 会议、活动、演讲者 | Marquee Hero · Manifesto · Photographic |
| 完全没有信号 | Bento Grid · Long Document · Manifesto |

开发者文档和开发者营销是不同的提示词（一份 walkthrough 要 Workbench；落地页要 Bento 加 Stat-Led），一页站和案例作品集也一样；第 1 步的用途说了算。含糊的语气词（"modern"、"clean"）经体裁解读，并作为推断陈述出来，绝不作为第二个问题。
