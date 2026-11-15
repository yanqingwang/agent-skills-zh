> **中文汉化版** · 上游：[Nutlope/hallmark](https://github.com/Nutlope/hallmark) · 原文件：`skills/hallmark/references/redesign.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 重设计

只在用户点名 Hallmark 并带 `redesign` 或 `audit` 时加载（`/hallmark redesign <target>`，*redesign the site with Hallmark*）。不点名 Hallmark 而要改动既有设计的要求（restyle、换色或换主题、polish、重设计、小修改）绝不加载本文件：按原样照做，用项目自己的系统。重设计是一场以既有页面为材料的建造：SKILL.md 仍然约束全程，本文件说明运行保留什么、用什么替代 Step 1 的提问、清扫步骤额外做什么。目标是用户自己的代码（一个文件、一个文件夹、开发服务器上的一个路由）；没有源码支撑的 live URL 只能通过 `--url` 做审计。

## 重设计保留什么

- **内容。**页面陈述的每一个事实、主张、名字、价格、日期与引语。已有的数字、引语与标志是用户的材料：照原样带过来，并在交接单中列出让用户核对，gate 存疑的那份（没人测量过的趋势，46a）也在内。什么都不新增：除了用户交来的与 gate 要求的（循环上的暂停，18；焦点环），不加页面没有的动作、区块、主张或图片。用页面自己的事实画出的图（它的渠道、步骤、某个数字）属于构图，full 深度可以做一张。
- **接线。**每一个链接、表单、字段、handler、路由、id 与测试钩子；每一个脚本、数据调用与统计调用。在拥有它的组件内部编辑标记。绝不移动逻辑、重命名 prop，或删掉脚本或测试读取的 `name`、`id`、`key`、`type`、`href` 或 `data-testid`。Floor 清空的 prop（当图标传的 emoji）可以随之而去，在交接单中注明。界面没有对应逻辑的状态（加载失败、撤销）列出来交给所有者，绝不擅自实现。
- **文件。**没有用户批准的文件级计划，就不删文件、不移除路由、不替换组件树；也不为了让重设计通过而改测试。仓库里的文档（README、prompt、演示文稿）是解释产品的，不是页面文案。git 项目里，从干净的树开始（`.hallmark/` 除外；请用户自己 commit 或 stash，绝不代劳），让重设计成为一个用户读得懂、也能回滚的 diff。样式表归重设计编辑：append-only 规则防的是建造，防不了它自己的重设计。
- **品牌，**如果有。品牌是选出来的：项目点名（品牌文件、标志资源、具名令牌、自己的字体文件）或用户说出的 logo、颜色或字体。它在所有深度都保留，其取值从项目文件读取，绝不凭记忆。框架默认值或 gate 点名的外观（紫到蓝的渐变、Inter 当标题字、现成色卡）不是品牌：restyle 与 full 会整体替换它，Picks 块会写明以防它原本就是。锁定的 `design.md` 是所有深度上的系统。
- **文字，**除非 gate 点名。未通过文案 gate（19、54、58、63、69）的措辞，用页面上已有的事实收紧，交接单列出每一行改动的前后。eyebrow 绝不只是删掉了事：它的标题是比喻时，平实的标签升为标题（*When to find us* 上方的 *Opening hours* 变成 *Opening hours*）。条款、免责声明与同意文本绝不改写。用户要求一字不动时，盖 `copy: verbatim` 章：19、58 与 69 随后以备注形式报告。

## 深度

这个动词是 **full** 重设计：内容与接线保留，系统与构图改变。更轻的深度只在同一请求原话点名时才运行，Picks 块写明深度：

| 深度 | 保留 | 改动 | 仅当请求原话说出 |
| --- | --- | --- | --- |
| **full** | 内容与接线 | 系统与构图：形状、首屏、区块对象、界面框架 | 无其他条件：它就是动词本身 |
| **restyle** | 布局 | 系统：颜色、字体、圆角、阴影、动效、控件 | *keep the layout*、*restyle*、*reskin*、*only the colours and type* |
| **polish** | 系统与布局 | 只改 gate 点名的：AI 痕迹、对比度、状态、动效、令牌 | *polish*、*keep our look*、*only fix what looks generated* |

深度之间不混用：polish 发现概念错了就说出来并建议跑 full，绝不偷偷夹带。

**应用界面上的 full 深度**在既有的壳内重排每一屏：什么领先呈现，数字、表格与表单如何布局（`flow.md` § App screens）。路由、去向与每个组件的逻辑保留；没有 hero 舞台，也没有 hero 评审。

*From scratch* 是一次建造，不是一种深度：按 SKILL.md 原文执行，旧页面作为其 Step 2 盘点，新文件与旧文件并存。

## 之前

1. 跑 pre-flight（Step 0），然后列出目标中的页面：路由、文件，以及每一项是页面还是应用界面（`flow.md` § App screens）。框架项目里启动开发服务器并通过 `--url` 记录；linter 不渲染磁盘上的空壳 `index.html`。未盖章的页面没有体裁：像 Step 1 从提示词推断那样从页面推断体裁，并说明这一点。
2. 按现状记录页面：

```
node <skill-dir>/scripts/sloplint.mjs <target> --genre <genre> --render --before [--url <route> ...] [--scope app]
```

它按 gate 分组打印发现，写入 `.hallmark/before.txt`，截图写入 `.hallmark/before/`，记录写入 `.hallmark/before.json`：每个链接、表单、字段、行内 handler、测试钩子、脚本标签、脚本查询的选择器、标题与图。Git 忽略该文件夹的截图与记录。

3. 先看截图再衡量发现，别让 linter 代写结论，然后用四行给出解读：页面是做什么的（受众、那个动作）；什么有效且保留（至少一条）；什么读起来像 AI 生成（最重的痕迹，按 gate）；什么坏了。

**`audit <target>` 到此为止。**它加载 `gates.md` § 1、§ 4 与 § 5，从截图逐个走受评的 gate，按层级报告发现并附 `file:line`、解读、能解决它们的最轻深度，以及只有更深一层才能解决的。它不改动项目的任何文件。

## 提问

一条消息替代 Step 1 的提问；请求已经回答过、或无人能答时跳过：

> *重设计之前，问三件事。1. **什么必须保留**：品牌、某个区块、某个页面？说 *keep the layout*，我就只做 restyle。2. **它有什么问题**，用你的话说，以及你想要什么感觉。3. **有新材料要给我看吗**：截图、照片、数字、一段引语。或者说 **go ahead**，我就直接完整重设计。*

## 计划

Picks 块以自己的四行开场，用户看到 Files 行之前什么都不删：

```markdown
- **Redesign** · full · 3 pages (/, /pricing, /docs)
- **Before** · Floor 14 FAIL · Reflex 9 · a centred template in a stock indigo; the pricing table is clear and stays
- **Keeps** · every link, field and handler · the green and the brand face · the pricing table
- **Files** · edit: app/page.tsx, app/pricing/page.tsx, app/globals.css · create: app/tokens.css, app/base.css · delete: none
```

然后是深度到达的建造行：restyle 与 full 有 Theme（dealt、`brand` 或 locked）；Shape、Chrome、Hero、Signature 与 Sections 仅 full 有，此时 Step 2 以页面自己的内容为盘点运行。polish 时该块在 Files 之后为止。deal 的 `--prompt` 是解读的第一行（页面是做什么的，用平实的名词），绝不是页面自己的文案，那是重设计要甩掉的东西。

## 建造

- **Polish** 就是 `flow.md` § The sweep，用在用户自己的页面上：就地修复，单个元素与令牌，绝不重构，盖 check 章，`built: the project · redesign: polish`。它加载 `gates.md` § 1 到 § 5 与 `patterns.md`，页面有表单时加载 `interaction-and-states.md`，旧章点名的主题文件，`craft.md` 只加载发现指向的那一节。
- **布局保留时**（polish 与 restyle），章上的 `redesign:` 字段让 sloplint 把布局 gate（6b、8、9、32、42、44a、44c、58、77、79）按备注报告；polish 时间距与字号阶梯 gate（24b、59、78）也是，这样 polish 不会给一个要求保留的站点重新排间距。把它们连同能解决它们的深度打印给用户；不重建。任何深度下 58（屏幕预算）都是备注：文字是所有者的，只有文案 gate 能删一条。app 范围内这些 gate 被跳过，交接单的 Layout 行来自解读与评审。主题自己的构图规则（它的禁忌、页面间变化的旋钮）让位于保留的布局：主题借出它的系统，每一页取一套旋钮。
- **Restyle 与 full** 从脚手架开始，深度写进章里：`theme.mjs scaffold <slug> --redesign <depth>`，保留品牌时用 `scaffold --brand --redesign <depth>`，其令牌由 pre-flight 找到的色板与字体填充（不 `check`：坐标是用户的）；应用界面加 `--scope app`。它把 `tokens.css` 与 `base.css` 写在项目样式表旁边，并打印适配它的导入（`export-formats.md` 有 Tailwind 与 shadcn 的名称）。然后是共享组件与界面框架，再是页面，访问最多的先做，每页做完先清扫再进下一页。
- **restyle 或 full 下超过一页**：脚手架跑完后锁定系统（`design-md.md`）。每页都读它，多样性规则反转：页面共享主题、字体与强调色，只在形状上不同。一份样式表服务多页时按路由列出 hero 姿态，`hero: Settled (/), Stage (/contact)`。超过三页、且 Harness 有子代理时，把每页交给自己的子代理，附 `design.md`、该页的文件与本文件。
- **Full 深度**跑 hero 舞台与 hero 评审；polish 与 restyle 两者都跳过。该阶段旧区块仍在新 hero 之下：舞台只评第一屏，它报告的折叠线以下内容等清扫处理。Gate 8 评的是构图，不是内容顺序：新构图中的既有顺序在记录上豁免。

## 之后

1. 对照记录清扫：`sloplint <target> --genre <genre> --render --kept`。页面曾有而现在没有的东西，是一条 `FAIL kept`（链接、表单、字段、handler、测试钩子、脚本、脚本仍查询的选择器）或 `WARN kept`（标题、图、图片、id）。恢复它，或在章里记上一笔：`/* Hallmark · dropped /blog, #team · the user is retiring the blog and the team section */`；文案 gate 点名的行用 `/* Hallmark · reworded "Built for modern teams" to "Out of your way" · 19 names the opener */`；gate 整条砍掉的行用 `dropped "<the line>" · 69 names it`。运行还会写出 `.hallmark/compare.html`，前后截图并排：把路径给用户。
2. 项目自己的检查，有的话：类型检查、构建、测试。弄坏其中任何一项的重设计就不算完成。
3. 收尾评审也看 `before` 截图，并回答旧页面哪里做得更好（`review-finish.md`）。polish 只交给它 1440 下的整页前后图，最多取五条发现。属于普通缺陷的发现（错位、坏字形、说谎的标签）任何深度都修；要求新构图的发现并入布局发现；要求页面从未有过的内容的发现，进交接单交给所有者。
4. 日志条目带 `mode: redesign`、`depth` 与 `scope`（page、site 或 app），full 深度下再加建造的字段。
5. 交接单，放在素材提问之前；布局保留时加一行 Layout（只有 full 重设计才能解决的发现）：

```
Redesign · full · 3 pages
Before   Floor 14 FAIL · Reflex 9
After    Floor 0 · Reflex 1 waived (47b)
Kept     14/14 links · 5/5 fields · 9/9 handlers · 11/11 headings · every figure
Changed  the system and the composition: shape, hero, sections, chrome
Dropped  none
Yours    2 claims kept as found ("50,000+ teams", the Acme quote) · 4 lines reworded, listed below
Compare  .hallmark/compare.html
```
