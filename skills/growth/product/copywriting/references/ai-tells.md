> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/growth/product/copywriting/references/ai-tells.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# AI 破绽：文案黑名单

让营销文案读起来像机器写的那些模式。客户和买家很快就能识别它们；而一旦读者认定页面是生成的，也会开始怀疑其内容是否属实。

这些大多是人类的老修辞。AI 文案露馅，是因为它**默认使用**、**叠加堆砌**，且**背后没有任何具体事实**。因此下面的规则混合了两类：硬性禁用（针对出现一次就算破绽的模式）和频率上限（针对有意选用时没问题的手法）。

**标记说明**
- **Ban（禁用）**：出现一次就是破绽。不要写。
- **Cap（限频）**：用一次没问题，重复或叠加就是破绽。不要超过上限。

**作用范围说明**
- **短文案**：标题、副标题、首屏、CTA、广告、社交帖子、邮件主题行。
- **长文案**：页面的正文区块、文章、长邮件。
- **区块**：一个首屏、一个页面区块，或一篇完整短文。
- CTA 微文案（"No card required"）不计入碎句上限。

**仍然没问题：** FAQ 问题、单独一句 "No card required"、确实有三个功能时的三项列表、单独一个 "without" 式标题，以及做出具体主张的正式品牌语气。

---

## Contents
- 结构模式（最严重的惯犯）
- 开场、收尾与铺垫
- 营销套话
- 词汇
- 含糊、吹嘘与滑头措辞
- 语气
- 排版
- 第二代破绽
- 构建写作者
- 重写规则
- 自检
- 来源

---

## 结构模式

这些比任何词表都重要。一份草稿可以避开所有被禁词汇，却仍因结构形状而读起来像 AI。

### 1. 反转揭示："Not X. Y."（Ban）

先立一个没人说过的假设，否认它，然后给出"真正"的答案。

变体："It's not X, it's Y." "Not because X. Because Y." "This isn't X. This is Y." "Not just X, but Y." "Less X, more Y." "The question isn't X, it's Y." "X? Think again."

- ✗ Most marketing teams have a list of campaign ideas that never launch. Not because they're bad. Because each one needs a developer.
- ✓ Most marketing teams have a list of campaign ideas that never launch, because each one needs a developer they can't get.

**为什么算破绽：** 它是最常被引用的 AI 模式之一。Wikipedia 的 AI 清理指南称之为 "negative parallelism"（负向平行），EQ-Bench 的 Slop Score 给 "not X, but Y" 模式单设了一个加权类别。

**改写：** 直接说出 Y，并附上具体原因或代价。如果读者持有你需要纠正的错误观念，就陈述正确的事实和证据；不要排演这场否认。

### 2. 否定列表："No X, no Y, no Z."（Ban）

用"没有什么"来定义产品，通常凑成三个，常在后面缀一个碎句。

变体："No X. No Y. Just Z." "Without X, without Y." "Zero X, zero Y."

- ✗ No setup call, no templates to fill in, no waiting on IT. No contract.
- ✓ Install it from the app store and it's running on your data in five minutes.

**改写：** 按发生的顺序说出确实会发生什么。如果某种"没有"确实是卖点（无需信用卡、无需安装），就在 CTA 旁边平实地说明一次："Free to start. No card required." 一份含多个"没有"的 brief 不需要列表：把其余的转成"会发生什么"（"no signup form" 改成 "Log in with your Shopify account"）。

单独一个 "without" 式或 "Never X again" 式标题没问题。不要在副标题里跟一个否定列表。

### 3. 尾部堆叠（Ban）

一个完整的主张，然后一个逗号，然后一串附加物：否定列表、"-ing" 从句，或一串额外好处。

- ✗ Reports pull directly from the data you already have, no exports, no spreadsheets, no second copy to keep updated.
- ✗ It syncs your calendar automatically, ensuring nothing slips through the cracks.
- ✓ Reports pull from the data you already have. There's nothing to export.

**改写：** 主张说完，句子就结束。如果那个好处重要，给它单独一个短句，带一个具体细节。检验方法：主句说完之后，下一个逗号之后凡是不提供新事实的内容一律删掉。真正补充新事实的从句可以留（"Imports run nightly, keeping your existing IDs"）；一串复述不行。

### 4. 设问后自答（Ban）

"The result? 3x faster onboarding." "The catch? There isn't one." "Why does this matter? Because..."

- ✗ The result? Onboarding that takes minutes, not weeks.
- ✓ New hires finish onboarding on day one.

**改写：** 删掉问题，保留答案。

仍然没问题：FAQ 问题（"Does it work with Shopify?"），以及用读者口吻问其自身需求、随后给出做法的问句（"Need to share a screenshot? Drop it in the thread."）。破绽是那种给自己主张贴标签的问句（"The result?" "The catch?" "Why does this matter?"）。

### 5. 冒号揭示（Ban）

"The best part: it learns." "Here's the secret: consistency." "One word: speed."

**改写：** 写成正常句子（"It learns from every correction"）。冒号只留给列表、标签和引文。

### 6. 碎句鼓点（Cap：每区块一个）

堆叠碎句或单行段落，制造人为的力度。"Simple. Fast. Done." "That's it. That's the whole thing."

**改写：** 把它们合并成一个承载事实的完整句。落在一个真实收益上的单个碎句是文案手法；整段碎句是毛病。

### 7. 条件反射式三连（Cap：每区块一个）

什么都凑三个：形容词、好处、从句、列表项。"Fast, secure, and scalable." "Save time, cut costs, and grow revenue."

**改写：** 事实支撑几个就用几个：一、二或四。通常的修法是换成唯一那个最强的具体主张："Fast, secure, and scalable" → "Handles 40,000 webhooks a second on the free plan."

### 8. 破折号（短文案禁用；长文案每页 1-2 个为上限）

把破折号当默认停顿，每段好几个，常常承载反转揭示（"It's not a tool — it's a teammate"）。

**改写：** 改用句号、逗号、冒号或括号。首屏、广告、主题行和社交帖子中一个都不要用。

### 9. 节奏均匀（Cap）

每句 12-18 个词。每段都是主题句 → 展开 → 收束。每节一样长。每次都是三个优点、三个缺点。

**改写：** 有意制造变化。一句长，再一句短。某节只需要两行，就让它只有两行。有时候把收益放在最前面。

### 10. 躲避 "is" 和 "has"（Cap）

"Serves as a central hub." "Stands as a testament." "Boasts a library of 200 templates." "Represents a new approach."

**改写：** 用 "is" 和 "has"，或者更好的是真正的动词："Tracks every contract, renewal date, and owner in one place."

### 11. 抽象主语（Cap）

"The platform empowers teams to..." "Our solution enables..." 没有任何人做了任何事。

**改写：** 让客户当主语。"Your team ships experiments without filing a ticket."

### 12. 虚假区间（Cap）

"From startups to enterprises." "From onboarding to renewal." 两端并不构成真实的跨度。

**改写：** 写明你实际服务的人群，或你实际覆盖的环节。

### 13. 同义词轮换（Cap）

在同一页里把同一个东西一会儿叫 dashboard、一会儿叫 interface、portal、hub，只为避免重复一个词。

**改写：** 选客户用的那个词，然后重复它。

---

## 开场、收尾与铺垫（Ban）

| 模式 | 示例 | 改为 |
|---------|---------|---------|
| 时代开场 | "In today's fast-paced world..." | 直接从客户的问题切入 |
| 假两难开场 | "Whether you're a solo founder or a Fortune 500..." | 写明这个页面给谁看 |
| "Imagine..." | "Imagine never chasing an invoice again." | 展示真实的转变前后 |
| "When it comes to..." | "When it comes to billing, ..." | 直接从主题开始 |
| 清嗓子 | "Here's the thing:" "The truth is" "Let me be clear" "Here's what nobody tells you" | 删掉。主张若站不住，需要的是证据，不是锣鼓点 |
| 宣布式开场 | "In this guide, we'll explore..." "Let's dive in" | 直接从内容开始 |
| 总结式收尾 | "In conclusion" "Ultimately" "At the end of the day" | 收在最后一个具体要点或 CTA 上 |
| 假深刻结尾 | "Because growth shouldn't wait." "And that changes everything." | 删掉。收在一个具体句子上 |
| 填充式过渡 | "It's worth noting" "Moreover" "Additionally" "Importantly" | 删掉。通常没有它句子照样成立 |

---

## 营销套话（Ban）

| 套话 | 改为 |
|--------|---------|
| "Say goodbye to X" / "Say hello to Y" | 展示新工作流："Reconciliation runs nightly. You review the exceptions." |
| "Unlock / unleash the power of X" | 直接给出结果和数字 |
| "X, reimagined" / "X, redefined" | 说出实际不同之处："Billing that retries on payday" |
| "Take X to the next level" | 说出那个层级：指标和目标值 |
| "Transform the way you work" | 带数字的转变前后 |
| "The X you deserve" | 你弥补的那个具体缺口 |
| "The future of X is here" | 今天就能上线的东西 |
| "Built for teams who move fast" | 真实客户与触发场景："For subscription teams past $1M ARR fighting failed payments" |
| "Everything you need to X" / "all-in-one" | 买家实际会核对的 2-3 件事 |
| "Effortless" / "in just a few clicks" | 真实步骤数或耗时："3 steps, about 4 minutes" |
| "Join thousands of happy customers" | 真实数字、客户 logo，或具名引用 |
| "Game-changer" / "this changes everything" | 什么变了、对谁变、变多少 |

---

## 词汇

把被禁词换成同义词只会制造新的破绽。用这个词所替代的事实来替换它："robust" → "99.99% uptime over two years"；"seamless" → "imports your Stripe data in about 90 seconds"。

**Ban：** delve, tapestry, testament to, realm, embark, beacon, multifaceted, paradigm, synergy, myriad, plethora, meticulous, intricate, utilize, leverage (as a verb), supercharge, turbocharge, game-changer, "ever-evolving landscape," "plays a crucial role"

**Cap（一段出现两个就该重写）：** seamless, robust, streamline, empower, elevate, unlock, unleash, harness, foster, enhance, optimize, cutting-edge, innovative, revolutionary, transformative, holistic, comprehensive, pivotal, crucial, vital, powerful, next-level, world-class, best-in-class, landscape, navigate, ecosystem, journey (unless literal)

**Cap（空洞加强词）：** truly, genuinely, incredibly, deeply, fundamentally, significantly, simply, actually, literally, quietly

受偏好词汇会随模型迭代而漂移（"delve" 在 2024 年达到峰值；随后 "enhance"、"showcase"、"foster"、"align with" 升高）。把这些列表当作当前示例，重点依靠结构模式和下文的检验方法，它们不会过时。

---

## 含糊、吹嘘与滑头措辞

- **堆叠含糊**（Cap）："can help you potentially reduce..."。写出你知道的，或诚实地限定主张范围。
- **重要性吹嘘**（Ban）："marks a pivotal moment," "redefines the category."。陈述事实，让读者自己判断。
- **滑头信源**（Ban）："experts agree," "studies show," "trusted by industry leaders."。写明来源或客户，否则删掉。
- **自造标签**（Cap）："the integration tax," "the growth trap."。只有当你会在全站定义并使用这个词时才造它。

---

## 语气

- **套近乎开场**（邮件与社交中 Ban）："Great question!" "Let's be honest..." "We get it."
- **假装坦白**（Ban）："I'll be honest, I was skeptical too..."，背后没有真实故事。
- **过度解说**（Cap）："Let's break this down," "Think of it as..."。直接给出解释。
- **炒作标点**（Ban）："Ready to level up?!"。正文中使用感叹号和感叹问号。

---

## 排版

- **Emoji 当结构**（B2B 中 Ban）：🚀 ✨ ✅ 领起列表项或标题。
- **每条都加粗标签**（Cap）："**Seamless integration:** ..."。留给参考表用，不是每个列表都要。
- **列表项开头平行**（Cap）：每条都以 "Ensures... / Provides... / Enables..." 开头。让列表项以客户收益开头，并变化句式。
- **到处 Title Case**（Cap）：除非品牌风格指南另有规定，否则用 sentence case。
- **Unicode 装饰**（Ban）：正文中的箭头、×、𝗯𝗼𝗹𝗱 字母。
- **标签式标题**（Cap）："What / Why / How" 式分节。写有主张的标题。

---

## 第二代破绽

它们出现在已经去除了 AI 腔的文案里。被禁词汇和反转揭示都清掉了，但草稿仍像生成的，因为模型只是用另一套习惯替换了原来那套。修完上面的模式后再检查这些。

| 破绽 | 示例（✗） | 修法 |
|---|---|---|
| **格言形状的句子**（Ban） | "Great tools get out of the way." "Speed is a feature." | 一句话有洞见的形状，但没人会反对。用它所指的那个具体事实替换，或删掉 |
| **表演聪明**（Cap） | "Your inbox, minus the noise." "Spreadsheets with a pulse." | 为显得俏皮而组装的意外词组。如果品牌本身俏皮、且它说了真话，可以留一个；否则就平实地说 |
| **短句连发**（Cap） | "It's fast. It's simple. And it just works." | 连续三个以上短句、再接一个长句，作为节奏手段。合并成一个承载事实的句子（见"碎句鼓点"） |
| **完美均衡**（Cap） | 每节都是标题加两句加三个列表项；每个好处权重相同 | 真人作者会把更多笔墨花在他们在意的部分。让最强的那节写长，最弱的缩短或删掉 |
| **全知闲谈**（Cap） | 一种轻松闲聊的口吻，无所不知，从不承认局限 | 轻松语气加十足断言，读起来就是生成的。诚实限定主张范围，并说明产品不适合谁 |
| **自我旁白**（Ban） | "Here's why this matters." "This is where it gets interesting." "The takeaway is simple." | 对文案本身进行评论的句子。删掉；如果论点需要帮助，加一个细节 |
| **整齐收尾**（Ban） | "Because your team deserves better." "The future of billing starts now." | 一句均衡、可引用、能收任何页面的结尾句。收在数字、具名客户、报价或 CTA 上 |
| **条件反射式具体**（Cap） | 每个主张都配一个可疑的整数统计，或一个过于工整的客户轶事 | 把"具体"当风格来模仿。每个数字和故事都必须真实且有出处；缺口用 `[NEED: proof]` 标出，不要编造填满 |

---

## 构建写作者

把模式去掉之后，文案会干净但平淡。像人写的文案，来自一个具体的人：知识不均匀、有真实观点。在对 Situation A 文案做完整重写之前（见 SKILL.md 的 Diagnosis 一节），先在心里回答这些问题：

1. **谁在写？** 写明这个人及其角色：创始人、客服负责人、做了这个功能的工程师。说明他为什么写这个页面。
2. **什么内容他了如指掌？** 这些部分拿到最多的笔墨和最具体的细节。
3. **什么内容他觉得无趣或不熟悉？** 这些部分压缩，或删掉。
4. **对这个问题、这个品类、或旧做法，他有什么诚实且可争论的观点？**
5. **如果必须砍掉三分之一，先砍什么？** 现在就砍。

这些答案会产出生成文案缺少的特质：

- **密度不均。** 作者在意的部分最长。万事均匀覆盖本身就是破绽。
- **语域混杂。** 上一句用精确的技术术语，下一句用大白话。不要把每个词都打磨到同一水准。
- **诚实的边界。** 作者不知道的东西，文案就跳过或直说。说明产品不适合谁，是这一点的强化版。
- **失衡的结构。** 至少一节明显更长，至少一节很短，因为该说的本来就那么多。
- **句子长度来自想法本身。** 每个句子写到它的想法所需的长度。不要预设短-短-长的节奏。
- **有代价的观点。** 真实的观点是具体的，且有人可以反对（"Most onboarding checklists are busywork. Ours has three steps."）。"We believe in quality" 不付任何代价。
- **只在有意义时用第一人称。** "I built this after losing a client to a missed invoice" 里的 "I" 是挣来的。不增加事实的第一人称只是装饰。

**凌驾于人设之上的规则：**
- **绝不虚构经历。** 写作者的观点和侧重可以构建；他的轶事、客户和结果不能。编造的 "when I ran my agency..." 故事是捏造，假客户引用同样是。用用户提供的素材，或标 `[NEED: founder story]`。
- **Situation B 中写作者已存在。** 对齐草稿或样本中的真实声音，不要另建一个。
- **保持品牌的语域。** 企业安全产品的人设仍然正式。密度不均和真实观点在正式语气里同样成立。

---

## 重写规则

1. **从事实出发重写。** 回到真实的东西（机制、数字、客户、步骤），然后写它。同义词替换和 "humanizer" 式替换只会制造新破绽。
2. **具体性检验。** 每个主张句都需要一个数字、一个名字、一个机制，或一个具体动作。
3. **换站检验。** 如果这句话原封不动放到竞品网站上照样成立，就重写它。
4. **叠加检验。** 一段里出现两个及以上 Cap 模式，就重写整段。
5. **不要为去 AI 腔而编造。** 用编造的数据替换 "industry-leading" 更糟。标 `[NEED: proof]` 并去问。
6. **有意选择手法。** 你为某个理由选用过一次的碎句，是文案手法；每行都用的同一手法是 AI 腔。
7. **保持品牌的语域。** 做出具体主张的正式句子没问题。不要把企业腔压平成短促的创业腔，那本身就是破绽。
8. **变化修法。** ✓ 示例只展示了一条出路。不要把它们当模板复用。如果每个揭示句都改成 ", because..."，每个否定列表都改成 "There's nothing to X,"，这些就成了新的毛病。
9. **标出缺失的差异点。** 如果手头素材撑不起任何能通过换站检验的标题，就写出最好的那个，并标 `[NEED: differentiator vs. named competitors]`。

---

## 自检

交付每份草稿前跑一遍：

1. **搜索禁用项。** 在标题、副标题和短文案中搜索 "not "、"isn't"、"no "、"without"、"?"、":" 和 "—"，逐个对照模式 1-5 和 8 核查。
2. **通读每个超过 20 词的句子。** 如果逗号超过两个，检查尾部堆叠（模式 3）。
3. **清点 Cap 项。** 每区块的碎句、三连和 Cap 词汇数量。
4. **朗读一遍。** 凡是听起来像新闻稿或 LinkedIn 帖子的地方，标出来。
5. **对标题、副标题和每个节标题做换站检验。**
6. **扫描第二代破绽。** 检查每节最后一行是否是整齐收尾，查找格言形状的句子，比较各节长度。如果都差不多，草稿就得了"完美均衡"。

如果某个修法需要你没有的信息（一个数字、一个客户、一个机制），把它标出来，不要绕过去。

---

## 来源

模式与证据来自以下来源，并以我们自己的话重写：

- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup)
- Kobak 等，15M+ 篇 PubMed 摘要中的冗余词汇（[arXiv 2406.07016](https://arxiv.org/abs/2406.07016)）
- Juzek & Ward, [Why Does ChatGPT "Delve" So Much?](https://aclanthology.org/2025.coling-main.426/) (COLING 2025)
- Paech 等，Antislop（[arXiv 2510.15061](https://arxiv.org/abs/2510.15061)）与 [EQ-Bench Slop Score](https://eqbench.com/slop-score.html)
- [tropes.fyi](https://tropes.fyi/tropes-md) AI 写作套路目录
- Charlie Guo, [The Field Guide to AI Slop](https://www.ignorance.ai/p/the-field-guide-to-ai-slop)
- Blake Stockton, [Don't write like AI: negation](https://www.blakestockton.com/p/dont-write-like-ai-1-101-negation)
- Profound 的 `humanizer` 与 `improved-copywriting` skill、Wispr Flow 的 `writing` skill，发布于 [skills-marketing-library](https://github.com/retieedra-profound/skills-marketing-library)（MIT）：构建写作者问题、人写文案特质与第二代破绽来自这些来源
- 反方观点：[A case for the defense](https://robotsatemyhomework.substack.com/p/ai-writing-patterns)（手法有意选用时没问题，默认滥用才是问题）

内容审查中使用的更完整的词汇级清单，见 seo-audit skill 的 `references/ai-writing-detection.md`。
