> **中文汉化版** · 上游：[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 原文件：`skills/taste-skill/references/copy.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 文案（Copy）

用陌生人在五秒内就能听懂的话，说清它是什么、能做什么。每一句都该是你会对顾客
当面说出口的话。不用比喻、诗意表达、生造词或广告用语（规则 3 里那一行品牌句
除外）。每个研读过的站点都只当描述素材：模仿示例的写法（平实、品类先行），
绝不照抄它们的用词、代码、图片或招牌特效。

## 文案层（The copy layer）

本文件收录每个页面都要遵守的规则。文案说什么、听起来是什么腔调，属于文案层，
在第 2 步、写下第一句话之前先读：

- `copy-voice.md`：来自简报的事实清单、语气卡片、由读者问题确定的页面形态、
  手法预算、各项检查。从这里开始。
- `copy-registers.md`：可选的语气风格，以及各自适合哪一行。
- `copy-moves.md`：页面每个部分的手法：点明品类的 hero 表单、标题、故事、
  特性、佐证、价格、按钮、微文案、页脚。
- `copy-tells.md`：哪些特征会暴露模型腔文案及其修法，过度矫正会催生什么，
  以及哪些不算破绽。

它们与本文件不一致时，以本文件为准：不生造任何内容、页面上不留方括号或空白、
不加图注、h1 点明品类、按钮是动词加宾语。

**copy-lint。** `node <skill>/scripts/copy-lint.mjs index.html --kind <kind>` 数出
一页可计数的破绽，每页远不到一秒（不开浏览器）。FAIL：残留物（`[NEED]`、模板
token、markdown、聊天机器人式语句）、陈旧的注水词与套话，以及用量超过其预算
两倍加一的手法（三个双片段标题、五个对比框架、五个美德词）：每一项都要修。
WARN：超出预算的手法、一排数字、默认选角的名字、页脚落款、把响应时间承诺
说了两遍、佐证数字、感叹号、浮夸吹捧、过时年份：要么修掉，要么保留并在报告中
说明理由。一次检查多页时，还会并排打印各页第一个标题以及它们共享的标题短语。
`--json` 供脚本调用；FAIL 时退出码为 1。门禁把它作为静态检查跑在页面上：
它的 FAIL 与检查器的一样阻断（id 为 `copy-*`），WARN 不阻断。

## 五条规则

1. **h1 点明品类；品牌无人知晓时，还要点出买家或所在地点**，用 2 到 8 个词：
   payroll app、dental clinic、standing desk，再加上面向谁或在哪里。地点类：
   40 个字符以内说清是什么、在哪里（"Bakery on Mill Street, Leith"；
   "Six-room guesthouse on a fjord"）。游戏类：名字加类型（"Kelpmoor, a co-op
   sailing game"），或者把 wordmark 压在一个点明类型的 h1 上；简报给出的发布
   日期或状态是硬事实。绝不许谜语、命令句、氛围句，或把品牌句压在平实副句上。
2. **首屏必须有一个硬事实：** 一个数字、一个地点、一个价格或一个日期。
3. **每个标题都有一个指名实物的名词：** 产品、产品的部件、地点、区块名词
   （prices、rooms、menu、opening hours、questions、getting here、visit）或一个
   数字。每页最多一句品牌句，且绝不放在 h1：它是该页唯一的修辞或双关，其下
   一行要带一个事实。
4. **按钮是动词加访客得到的东西，** 1 到 5 个词，以 book、buy、order、
   pre-order、reserve、try、start、get、download、compare、see、watch、read、
   find、join、subscribe、sign up、contact、configure、add、send、email 或
   request 开头；只有当链接打开的就是那个东西本身时才用光杆名词。绝不用
   "Learn more"、"Read more"、"Discover"、"Explore"、"More" 或 "Click here"。
5. **动作要少，每个动作只有一种措辞：** hero 区最多 2 个（地点类 1 个），
   每页最多 10 个不同标签。主动作点名交易本身（Book a room、Order a cake、
   Start a free trial；地点类用简报里的下单或预订说法，否则用 Get directions，
   绝不是某个附带活动），并在导航、hero、结尾与手机栏里保持同一措辞，其余
   地方不用。一屏最多出现两次：桌面端是导航按钮与 hero 按钮（检查器对此
   WARN，所以要确认没有别的元素在重复它）；手机端是 hero 按钮（system.js
   会把手机栏避开已展示该动作的屏幕）；同一屏出现第三处则 FAIL [action-repeat]。

## 平实版本

句子含糊时：品类名词在前，然后接简报里的一个数量、地点或价格，不用修辞。

| 含糊 | 平实 |
| --- | --- |
| "Every shift, sorted" | Shift planning for restaurant teams |
| "Where the city climbs" | Climbing gym with 180 routes in Leipzig-Plagwitz |
| "Come climb" | Day pass 14 €, shoes included |
| "A second read of every word" | AI proofreader for book publishers |

## 标题与正文

- **Hero 副句：** 软件、产品与服务：写明工作方式与主要收益，15 到 30 个词，
  一行到两句。地点类：陈述事实，80 字符以内，带今日营业时间（"Sourdough, rye
  and cardamom buns from 7:30, Tuesday to Sunday."）；酒店写房型与城镇。
- **区块标题** 点名事物（"Rooms and prices"、"Works with your tools"）或做一个
  简短平实的断言（"Pays staff on the same day"），1 到 6 个词，最多两行。用名词
  短语、"we do X for Y" 或动词加其作用对象（"Send invoices from the van"）；
  绝不用光杆命令（"Get started"、"Come climb"）、疑问句（FAQ 条目可以是疑问句）、
  冒号式标题，或读完页面才说得通的句子（"Continuity slips"、"It reads everything
  you decide"）。双片段（"Twelve rooms. Three ways to stay."）每页至多一次
  （`copy-tells.md`）。**卡片标题：** 动词加宾语（"Warns about double shifts"），
  一行，用真实的话，绝不用故作俏皮的标签（"The market run"）。标题后半段是
  灰色的，那就是两句话：第一句在 `.muted` span 前以句号收尾（"Rooms and prices.
  <span class="muted">Breakfast included.</span>"），绝不是连成一体的两个短语
  [run-on]。
- **标题之下** 一行到两句（10 到 40 个词）；卡片正文 1 到 2 句、最多 25 个词，
  用买家的话，带一个具体细节；1440 宽度下没有超过五行的段落。价格自己会卖货，
  不用氛围标题（"Rooms from 140 € a night, breakfast included"）。
- **每屏字数** 保持低位：产品 47、地点 44、服务 34；每页约 900 词封顶，页脚
  不计。长文案放到子页面。
- **技术词预算**（软件、游戏、硬件）：1440 宽度下每屏 60 到 80 个词，计数
  排除 UI 模型图、示意图与代码（标题、正文行、卡片标题与正文、按钮、标签）；
  超过 80 检查器会 WARN（实测：某金融科技页每屏 117 词，读起来冗长）。按此
  顺序删：标题下的第二句、卡片正文删到一句 12 到 18 个词、第四张卡片、某个
  片段已表达过的列表。其余让 UI 去说。
- **数字** 带着单位嵌在句子里（"4.5 hours a week"），真实数据要参差（212、38%）。
  需要出处的真实断言（来自简报）在页脚附近加编号脚注（13px 及以上）。
- **图片** 与短文案并置，绝不替代文案；文字也绝不站本该放照片的位置。每个
  词都是活文本。
- **表单用语：** label 写明该填什么（"Arrival"、"Guests"），绝不用提问，也不让
  占位符顶替 label；错误信息点名字段并说明该填什么（"Write the day you want to
  come"）；发送后的那句话用按钮自己的措辞点名发送了什么（"Your table request
  is in. We reply within a day."）。其余做法见 `system.md` 的 Forms 一节。
- **自检：** 把每句话念给顾客听。能听清产品做什么吗？听不清就重写。然后跑
  文案层的检查（`copy-voice.md` 第 6 节），先跑 copy-lint。

## 哪些可以假设

- **价格、地址、营业时间与日期来自简报；** 报告要列出你自行假设的每一项。
  简报缺失时只有两样可以假设：一个生造的品牌名（见下），以及地点类按行业
  给出合理、参差、用当地货币（3.60，不是 4.00）的营业时间与价格。其余一律
  不生造：简报里没有价格的产品或服务写 "Price on request"，或干脆不显示价格。
  每个假设的价格、时间、日期或地点，在自己的元素上带 `data-assumed`
  （`<span class="rows__value" data-assumed>3.60 €</span>`、
  `<dl class="hours" data-assumed>`）；检查器把每一处列进报告 [assumed]，且
  假设的营业时间绝不驱动"现在营业"的判断 [open-now]。
- **不生造佐证：** 不虚构评论、评分、评论数、引语、推荐语、统计数据、客户数、
  客户名、人物肖像、客户名单、奖项、媒体报道或产品。客户 logo 只用于简报点名
  且允许展示的真实客户；产品能对接的真实工具保留其真实图标与原色（`icons.md`），
  绝不画仿制版。没有佐证时，放一段来自简报的平实事实，或什么都不放。
- **不带样例标注：** 任何地方都不出现 "sample"、"(sample)"、"examples"、
  "illustrative" 之类的标签、注记或星号脚注。简报自身给出的目标值写进句子里
  （"target 2 days"）。
- **不用占位物：** 不用方括号、"lorem ipsum"、"your name here"、"to be added"、
  TODO、套件样例文本，也不链到 `#` 或空 href。要么写真词，要么删掉该元素。
  "Coming soon" 只用于简报确实说了即将上线的对象。
- **任何视觉物之下或之上不加图注、标签或说明**（内部规则）：不写 "A drawing
  made in code"、"Photographs follow"、"Representative image"，光秃图片下面不放
  名称、价格或链接行，不加话题标签。一个标题为整组图片命名；已售品的名称与
  价格放在其卡片的内边距之内。图片要么展示实物，要么删掉；报告列出客户必须
  供图的照片。
- **署名：** 页脚末尾一行短句，只点名用到的素材来源，绝不点名摄影师：
  "Photographs via Unsplash and Wikimedia Commons"（按 `photos.mjs credits` 打印
  的样式；110 字符以内，1024 起单行），链接或打开署名清单。这行字与清单都按
  `photos.mjs credits` 的输出原样粘贴；绝不给每张照片在页脚写署名链接（实测：
  页脚 18 条与 20 条署名链接读起来像署名墙）。地图数据署名并入其中。页面
  展示真实 logo 时加一句 "Product names and logos are trademarks of their owners"。
- **每个事实只出现一次：** 营业时间、价格或地址只有一个值、一种措辞，仅在
  属于它的位置逐字重复（hero、到访面板、手机页、结尾、页脚）；绝不为同一天
  写两套时间。

## 简报没给的联系方式

简报给的内容按原样打印。各类别相互独立：只给了电话号码的简报，依然适用
地址、邮箱与 Imprint 规则。

- **地址：只写街道和街区**（"Elmgatan, Malmö-Möllevången"）。绝不写门牌号、
  邮编或地图坐标。每页一个街道地址（到访区块与页脚，390 宽度下也一样），
  绝不只是出现在照片里的招牌上。多家店：先各店名，再跟其街道。需预约的
  工作室要写明。
- **简报没给街道：** 只打印街区（"Eimsbüttel, Hamburg"），没提街区就写城镇，
  绝不生造街道或门牌；type moment `address` 输出该街区。把缺失的街道列入
  报告，标注为客户需提供。
- **地图：** 页面不加载任何地图。Get directions 打开
  `https://www.openstreetmap.org/search?query=<street>+<district>`，不带坐标、
  不带路线；手机上点地址打开同样的搜索。没给街道：链接写 "See the area"，
  打开 `?query=<district>+<town>`；只有城镇：不放地图链接，也不放路线按钮，
  因为全城搜索不会把任何人带到门口 [map-link]。只有简报给出的街道才画地图
  （`fx-map` 烘焙成静态图，图钉压在街道线上，绝不在建筑物上）；建筑商的
  真实街道绝不配真实地图，因为图钉会钉到陌生人的门口。绝不用 iframe。
- **电话：一律没有，除非简报给了。** 不放号码、不放 `tel:` 链接、不放 Call
  按钮。可以用 "Request a call" 表单顶上。
- **不做 Imprint 页、不放公司信息：** 不放注册号（HRB）、增值税号或税号、
  公司编号、董事总经理或法院信息。法律行放品牌名、当前年份、Privacy、Terms
  与署名行；只有简报给出公司自身信息时才放 Imprint 链接。
- **邮箱与网页：** 用表单（`system.md` 的 Forms 一节：简报给了表单地址就发到
  客户的表单地址，否则其 `.example` 的 `mailto:` 顶上，并在报告中列出），或用
  按钮（"Email us"），其 `mailto:` 落在 `.example`（`hello@brand.example`）。绝不
  打印邮箱地址、域名或社交账号，`.example` 的也不行。`.socials` 保持为空，
  除非简报给了账号。
- **名字是生造的，** 不能是词典词，也不能是实际存在的商家，除非简报给了
  名字；绝不反复用模型惯造的那些名字（Kestrel、Halcyon、Lumen、Nimbus、
  Fieldnote：`copy-tells.md`；copy-lint 对作为页面自身名字（title 或 h1）的这类
  词判 FAIL，在 logo 墙或 mock 等其他位置则 WARN）；人名只来自简报。生造的
  名字要连同行业一起搜索（"name coffee"），并作为域名搜索；若前 10 条结果里
  有同行业商家或名人恰用此名，另造一个。把每次查询与结果写进页面旁的
  `names.json`（没有搜索工具时写 `"searched": false`）。
- **链接** 落在其标签所说的地方：页面的某个部分（`#rooms`）或一个真实存在的
  页面；绝不写 "here"，绝不用两个不同标签指向同一目标，绝不链接到已关闭的
  答案。
- **订阅邮件（Newsletter）：** 只问一次，放在页脚内或页脚正上方，用
  "Subscribe" 或 "Sign up"，只有一个邮箱输入框；绝不放弹窗里，绝不问两次。

## 禁用

比喻和 "where X meets Y"；hero 里的口号、问候与自夸；疑问句当大标题；感叹号；
全大写标签；生造的大写概念（"the Proof Layer"）；来路不明的项目名；标签里玩
笑话或俚语；氛围段落；全屏横幅里放文学引语；填充词（seamless、effortless、
cutting-edge、unlock、elevate、supercharge、reimagine、next-generation、
game-changing、powerful、robust，以及 `copy-tells.md` 里的其余词条）；形容客户
的美德词（honest、calm、quiet、actually、simply）；页脚里的落款或双关；模型的
默认腔调（`copy-voice.md` 第 2 节）。copy-lint 对陈旧注水词、套话、残留物和
用量超过两倍预算的手法判 FAIL；其余能数出来的判 WARN，数不出来的由同行竞名
排查与朗读检查（`copy-voice.md` 第 6 节）兜住。
