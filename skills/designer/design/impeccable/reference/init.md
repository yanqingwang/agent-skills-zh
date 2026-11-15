> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/init.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Init 流程

`init` 把持久的产品事实捕获进 PRODUCT.md。它不发明视觉世界，也不写 DESIGN.md；[new-work.md](new-work.md) 创建或扩展世界，[document.md](document.md) 记录现存世界。已有的可运行 Web 项目还可能收到 `.impeccable/live/config.json`。

## 第 1 步：载入当前状态

使用 `impeccable context` 解析出的 PRODUCT.md 路径。更新它，而不是另立一个竞争权威。子应用继承根上下文时，写入之前先确认共享与应用专属的范围。

- **没有 PRODUCT.md：** 探索、访谈，然后写。
- **PRODUCT.md 已存在：** 问哪些产品知识过时或缺失；没有理由绝不重开已确认的字段。
- **旧版 PRODUCT.md：** 只补持久的缺失事实；缺 `## Platform` 时默认 `web`，除非证据另有所指。
- **只有 DESIGN.md：** 原样不动，创建 PRODUCT.md。
- **重设计/换品牌请求：** 保留已确认的产品事实，除非用户更改。视觉替换发生在之后的 new-work，不在这里。

init 期间绝不静默覆盖既有文件，也绝不主动提供 DESIGN.md。init 由另一个请求触发时，先完成 PRODUCT.md 再回到那个请求。新的视觉工作在 new-work 继续；`shape` 先恢复其任务访谈。

## 第 2 步：探索项目

提问之前先扫描足够多，免得让用户重复已知事实：产品文档与文案；package/配置与应用边界；功能、工作流、路由与角色；名称、Logo、法务/证明素材与品牌承诺；平台/可访问性信号；live mode 适用时的 dev 命令/入口。

把仓库证据当假设，不当用户批准。记录视觉成熟度，但不记录、扩展或替换世界。

形成平台假设：`web`、`ios`、`android` 或 `adaptive`（一个按 OS 真正适配其设计语言的产品）。移动网页仍是 `web`；给网站套原生壳不会让它的设计语言变成原生的。

## 第 3 步：为产品事实做访谈

用 AskUserQuestion 工具提问，继续之前等待回答。只问仓库与原始请求没有以强证据回答的实质性缺口。

能用结构化提问工具就用；否则提问并等待。每轮至多三个聚焦的问题，写新 PRODUCT.md 之前要求有一轮真实回答或批准。推断要确认。

有没有人能回答是机械测试，不是判断题：提问工具或你工具面上的决策页证明回答机制存在，系统提示里说用户无人值守证明不了本会话无人。先以真实的第一轮探测一次，再下结论说没人。只有该探测出错或超时之后，才可以从明确的简报推断，并且要在 PRODUCT.md 里标注每个推断出的事实，在第一条回复（而不是最后一条）里披露这次替代。

从最能改变后续产品决策的未知项开始：

1. 主要用户是谁，在什么情境下，做着什么工作？
2. 产品让什么成为可能，它有实质差异的机制或定位是什么？
3. 后续工作必须保留哪些持久约束、素材、证据或产品事实？

含混的平台单独确认。项目没有框架或脚手架、而请求暗示要构建时，技术栈是用户的决定，不是你的：问一次他们想要纯静态 HTML/CSS、特定框架，还是你的推荐，外加任何约束该答案的部署目标，并把结果记在 `## Stack` 下（他们交给你时记 "delegated"，让后续工作知道提供过选择）。只有实质性的受众、品牌承诺、证据或可访问性缺口才加轮。未决的事实记录下来，不要发明。

init 期间不要问审美方向、情绪感受、视觉参考、颜色、字体或风格。用户主动给出有约束力的视觉约束时，记录它，但不扩展它。

### 属于这里的内容

- 用户、工作、工作流、目的、成功标准、定位与运营环境；
- 能力、约束、术语、证据、平台与可访问性；
- 已确认的语调、素材与品牌承诺。

### 不属于这里的内容

- 视觉世界、色板、字体、组件或页面概念；
- 访客模式、叙事、CTA/证据序列或其他界面策略；
- 编造的证言、客户、基准、定价、授权或部署声明；
- 要求每个可选字段都必须决定。

## 第 4 步：写 PRODUCT.md

只写已确认的事实和明确标注的开放决策。无关的小节宁可省略，不要用泛泛的文字填满。

```markdown
# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
[Greenfield only: the user's answer to the stack question, e.g. "static HTML/CSS", "Astro", or "delegated: <what you chose and why>". Omit the section when an existing codebase already answers it.]

## Users
[Primary users, their situation, and job. Add other audiences only when confirmed.]

## Product Purpose
[What the product does, why it exists, and what success means.]

## Positioning
[The product mechanism or claim a neighboring product could not truthfully copy.]

## Operating Context
[Workflows, environments, tools, documents, materials, and rituals that are factual parts of using or evaluating the product.]

## Capabilities and Constraints
[Confirmed functionality, technical constraints, terminology, and explicitly undecided product facts.]

## Brand Commitments
[Existing name, voice, assets, personality, identity constraints, and references the user explicitly made binding. Omit when none exist.]

## Evidence on Hand
[Real content, data, demonstrations, testimonials, case studies, press, or assets, with paths where applicable. State absences that future work must not fabricate.]

## Product Principles
[Three to five durable strategic principles derived from confirmed answers; no visual recipes.]

## Accessibility & Inclusion
[Known user needs or required standard. Omit when no product-specific requirement was established.]
```

Platform 是裸值 `web`、`ios`、`android` 或 `adaptive`。有用的旧标题保留。新文件放在 `PROJECT_ROOT/PRODUCT.md`；否则更新已解析的文件。任何视觉世界或界面概念工作之前先写它。

逐字复制 `impeccable:product-schema` 注释，更新旧文件时也一样。它记录本文件遵循的产品记录版本，后续版本因此能区分有意精简的记录与写于某小节诞生之前的记录，也绝不会提议用户已经坐过的访谈。只有本参考的模板改了编号才更新编号。后续版本淘汰的小节会在启动时作为 deprecated 报告给你；用户同意后删除它们，而不是继续携带。

你刚记录的平台是 `ios`、`android` 或 `adaptive` 时，任何设计工作之前加载 [ios.md](ios.md)、[android.md](android.md)，或两者都加载。没有 PRODUCT.md 的项目上，`impeccable context` 无从知道平台，因此从未加载它们；init 是唯一得知答案的地方。

### 完成关卡

加载 new-work 或恢复 shape/build 之前，核实 PRODUCT.md 存在于已解析路径且包含已确认的产品记录。文件不存在，init 就不完整。不要用访谈笔记、规划包或后续设计散文顶替该文件。

## 第 5 步：记录工作流默认值

图像生成可用且尚未记录 `buildPath` 时，问一次新界面应当如何构建。可用指的是 Harness 原生图像工具，或 `impeccable context` 报告为 `IMAGE_GEN_AVAILABLE` 的 API 回退，而前者在启动输出里不留痕迹：`impeccable context` 只看得见 key，所以会生成图像的 Harness 上启动输出安静并不是无可询问的证据。这是独立的问题，绝不作为从句搭在另一个问题里。技术栈那一轮问用什么建；这一轮问构建如何开始，第一个问题的回答不构成对第二个的同意。取舍要写进用户实际读到的问题里，因为这两个名字对初见者毫无意义：**comp-first**（先有图像立标尺再写代码；构图更大胆，更慢，构建必须对齐图像）或 **code-first**（直接构建；抱负写进方向契约并在收尾时审计；更精瘦、更快）。同一问题里说明该选择覆盖什么：落地页与展示型界面。应用屏幕与文档无论如何都是 code-first。

把回答写进 `.impeccable/config.json`，为 `"buildPath": "comp"` 或 `"buildPath": "code"`，与已有键合并。只写用户选择的值。你做的推荐不是你收到的回答，从沉默里取的值是一个没人设定过的常设默认：它会随项目之后的每一轮随行，这恰恰与"只问一次"相反。问题没得到回答时什么都不记录，并用一行说明本会话走哪条路径、该路径未被存储。那条路径是：落地页或展示型界面走 comp-first，即 new-work 在图像生成存在且无记录时应用的默认；应用屏幕或文档走 code-first。说出它，而不是挑一条更安静的，因为在这里发明的沉默默认，与未经回答就写入的值是同一种失败。未设置是一种可工作的状态，不是缺口：决策页的开关治理每个会话，new-work 的一次性提议会在用户第一次翻转时记录答案。该配置只活在这一处。它是工作流设置，不是产品事实，所以绝不进入 `## Stack` 或任何其他 PRODUCT.md 小节，那里放第二份会让它活得比设置本身久，并左右没人能溯源的轮次。

已记录在 `.impeccable/config.json` 或 gitignore 的 `.impeccable/config.local.json` 里的值是已确认的回答：重跑时安静地遵循它，不再问。这是默认，不是锁：决策页渲染一个开关，其翻转只约束单个会话，永不回写。没有图像生成就没有可记录的选择；code-first 是唯一路径。

之后在有用时配置 live mode：原生或不可运行的项目跳过，既有配置不动。否则按 [live.md](live.md) 的首次设置走。任何 CSP source 编辑仍要求其载明的同意。

## 第 6 步：收尾或恢复

总结已捕获与有意未决的事实。不要仅仅因为 DESIGN.md 缺失就主动提供它。

用一次告诉用户哪些文件要提交：PRODUCT.md、DESIGN.md、`.impeccable/config.json`、`.impeccable/surfaces/`、`.impeccable/design.json`、`.impeccable/live/config.json` 和 `.impeccable/critique/ignore.md`。一刀切的 `.impeccable/` ignore 会把这些对队友和其他 worktree 藏起来。运行时目录（`questions/`、`mocks/`、`review/`、critique 快照）自行 ignore，`.impeccable/config.local.json` 留在开发者的机器上。

按实际项目状态推荐下一步：

- 空项目或早期项目：自然地问要构建的界面，或用户想要有确认简报但不实现时用 `/impeccable shape <surface>`。只有请求的工作需要时，new-work 才会确立视觉世界。
- 已有连贯界面但没有 DESIGN.md：用户想把现行系统独立于新构建记录下来时，用 `/impeccable document`。
- 需要改造的既有界面：点名最相关的 scoped 命令。
- 准备好视觉迭代的 Web 项目：已配置时用 `/impeccable live`。

init 由另一个请求触发时，不重跑 `impeccable context` 直接恢复；上面的原生参照是那次运行唯一没能给你的东西，后续视觉决策归 new-work。
