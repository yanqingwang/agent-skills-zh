> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/document.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

在项目根目录生成一个 `DESIGN.md` 文件，记录当前的视觉设计系统，让生成新界面的 AI 代理保持品牌一致。

DESIGN.md 遵循[官方 DESIGN.md 格式规范](https://raw.githubusercontent.com/google-labs-code/design.md/main/docs/spec.md)：可选的 YAML frontmatter 承载机器可读的设计 token，随后是按固定顺序排列的最多八个 markdown 小节。**token 是规范性的；正文只为如何应用它们提供背景。**不相关的小节可以省略，但保留的小节必须保持指定顺序。请使用下方的规范标题，让文件在识别 DESIGN.md 的工具之间保持可移植。

## frontmatter：token schema

YAML frontmatter 是机器可读层。Stitch 的 linter 校验的就是它，实时面板渲染磁贴所用的也是它。保持精炼；每一条都应对应项目实际使用的 token。

```yaml
---
name: <project title>
description: <one-line tagline>
colors:
  primary: "#b8422e"
  neutral-bg: "#faf7f2"
  # ...one entry per extracted color; key = descriptive slug
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: "4.5rem"
    fontWeight: 300
    lineHeight: 1
    letterSpacing: "0em"
  body:
    # ...
rounded:
  sm: "4px"
  md: "8px"
spacing:
  sm: "8px"
  md: "16px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-bg}"
    rounded: "{rounded.sm}"
    padding: "16px 48px"
  button-primary-hover:
    backgroundColor: "{colors.primary-deep}"
---
```

重要的规则：

- **token 引用**使用 `{path.to.token}`（例如 `{colors.primary}`、`{rounded.md}`）。组件可以引用基础项（primitives）；基础项之间不能互相引用。
- **颜色接受任何合法的 CSS 颜色字符串。**为可移植性考虑，推荐默认使用 hex，但当项目既有的 `rgb()`、`hsl()`、`oklch()`、广色域或混合颜色值才是项目的规范来源时，应原样保留。没有明确理由不要拆分唯一事实来源。
- **组件子 token** 限定为 8 个属性：`backgroundColor`、`textColor`、`typography`、`rounded`、`padding`、`size`、`height`、`width`。阴影、动效、焦点环、backdrop-filter 都放不下。放进 sidecar（Step 4b）。
- **scale 键名是开放的。**用项目已经在用的名字（`oxblood-deep`、`surface-container-low`）。不要改成 Material 默认名。
- **变体是命名约定，不是 schema。**`button-primary` / `button-primary-hover` / `button-primary-active` 作为兄弟键。

## markdown 正文：八个小节（规范顺序）

1. `## Overview`
2. `## Colors`
3. `## Typography`
4. `## Layout`
5. `## Elevation & Depth`
6. `## Shapes`
7. `## Components`
8. `## Do's and Don'ts`

省略不相关的小节，而不是用编造的规则去填充。响应式布局放在 Layout，深度放在 Elevation & Depth，圆角和形态语言放在 Shapes，各组件的行为放在 Components。格式会保留未知小节，但新的视觉指导只要适用就应采用规范结构。

## 何时运行

- new-work 发现了连贯的既有视觉系统但没有 `DESIGN.md`。
- 一个新世界的首次实现已完成，其临时决定需要固化下来。
- 已有的 `DESIGN.md` 已经过时（设计发生了漂移）。
- 大型重设计之前，把当前状态留档作为参考。

如果 `DESIGN.md` 已经存在，**不要默默覆盖**。先把现有文件展示给用户。用 AskUserQuestion 工具提问并等待回答后再继续。选项是刷新（refresh）、覆盖（overwrite）或合并（merge）。唯一的例外是种子世界上的首次构建（见下文）：直接刷新，不提问。

由 `impeccable world` 写出的 DESIGN.md 会在 frontmatter 中带一行 `world: "<id>"`，其 sidecar 带一个 `seededFrom` 对象。两者都指明这套系统所源自的目录世界，并且都必须在每次选择之后保留下来：把 `world:` 行原样复制进新的 frontmatter，把 `seededFrom` 复制进重新生成的 sidecar。它们是下方各 schema 之外唯二保留的 frontmatter 键和 sidecar 键。

## 两条路径

- **扫描模式（Scan mode）**（默认）：项目已有设计 token、组件或渲染输出。先提取，再确认描述性语言。有代码可分析时使用。
- **种子模式（Seed mode）**：项目尚未开始实现。先确保 PRODUCT.md 存在，再复用 new-work 的视觉世界工作坊并写出方向性的 DESIGN.md 种子。有了代码后再以扫描模式重跑。

先扫描再决定（扫描模式的 Step 1）。如果扫描没有发现 token、组件文件和已渲染的站点，就提供种子模式选项；不要默默切换。`/impeccable document --seed` 请求的是 new-work 的世界工作坊，但它并不授权替换连贯的代码：当存在既有系统时，提供扫描模式，或把明确的身份替换请求交给 new-work 处理。

## 扫描模式（方案 C：先自动提取，再确认描述性语言）

### Step 1: 找出设计资产

按优先顺序搜索代码库：

1. **CSS 自定义属性**：在 CSS 文件（通常是 `src/styles/`、`public/css/`、`app/globals.css` 等）中 grep `--color-`、`--font-`、`--spacing-`、`--radius-`、`--shadow-`、`--ease-`、`--duration-` 声明。记录名称、值以及定义所在文件。
2. **Tailwind 配置**：如果存在 `tailwind.config.{js,ts,mjs}`，读取 `theme.extend` 块中的 colors、fontFamily、spacing、borderRadius、boxShadow。
3. **CSS-in-JS 主题文件**：styled-components、emotion、vanilla-extract、stitches；查找 `theme.ts`、`tokens.ts` 或等价物。
4. **设计 token 文件**：`tokens.json`、`design-tokens.json`、Style Dictionary 输出、W3C token community group 格式。
5. **组件库**：扫描主要的 button、card、input、navigation、dialog 组件。记录它们的变体 API 和默认样式。
6. **全局样式表**：根 CSS 文件通常带有基础排版和颜色赋值。
7. **可见的渲染输出**：如果有浏览器自动化工具，加载线上站点并采样关键元素（body、h1、a、button、.card）的计算样式。这能捕获 token 遗漏的值。

### Step 2: 自动提取可以自动提取的部分

基于发现的 token 构建结构化草稿。对每个 token 类别：

- **颜色**：归入 Primary / Secondary / Tertiary / Neutral（Stitch 使用的 Material 衍生角色）。如果项目只有一个强调色，就表达为 Primary + Neutral；省略 Secondary 和 Tertiary，而不是凭空编造。
- **排版**：把观察到的字号和字重映射到 Material 层级（display / headline / title / body / label）。记录字体族堆栈和比例系数。
- **海拔**：盘点阴影词汇。如果项目是扁平的、改用色调分层，这也是合法答案；要明确说出来。
- **组件**：对每个常见组件（button、card、input、chip、list item、tooltip、nav），提取形状（radius）、颜色分配、hover/focus 处理和内边距。
- **布局 + 间距**：把网格、容器、断点、节奏和密度行为提取进 Layout。
- **形状**：把 radius、圆角、边框、裁剪和反复出现的形态行为提取进 Shapes。

### Step 2b: 暂存 frontmatter

现在就从自动提取的 token 起草 YAML frontmatter（在 Step 4 把它写到 DESIGN.md 顶部）。这是机器可读层：实时面板和 Stitch 的 linter 消费的就是它。

- **颜色**：每个提取到的颜色一条。键 = 描述性 slug（`oxblood-deep`、`editorial-magenta`，而不是 `blue-800`）。值 = 项目视为规范的格式（OKLCH 或 hex；见上文 frontmatter 规则）。不要拆分唯一事实来源：frontmatter 里只用一种格式，不要在正文中用另一个值重定义同一个 token。
- **排版**：每个角色一条（`display`、`headline`、`title`、`body`、`label`）。typography 是一个对象；只包含对项目真实成立的属性（`fontFamily`、`fontSize`、`fontWeight`、`lineHeight`、`letterSpacing`、`fontFeature`、`fontVariation`）。
- **Rounded / Spacing**：项目实际使用的刻度档位，键名沿用项目自己的刻度名（`sm` / `md` / `lg`，或 `surface-sm`，或数字档位）。
- **组件**：每个变体一条（`button-primary`、`button-primary-hover`、`button-ghost`）。通过 `{colors.X}`、`{rounded.Y}` 引用基础项。如果某个变体需要 Stitch 的 8 属性集覆盖不了的属性（阴影、焦点环、backdrop-filter），就把完整片段放进 sidecar。

项目没有的就跳过。空的 scale 键或编造的 token 会污染规格。

### Step 3: 向用户询问定性语言

以下各项需要无法自动提取的创意输入。分两轮结构化提问，每轮不超过三个问题（或 Harness 的更低上限），两轮之间等待：

- **创意北极星**：整个系统的单一命名隐喻（"The Editorial Sanctuary"、"The Golden State Curator"、"The Lab Notebook"）。给出 2-3 个符合 PRODUCT.md 品牌个性的选项。
- **Overview 语调**：情绪形容词、2-3 句的美学哲学，以及任何已确认的视觉反参照。
- **颜色性格**（针对自动提取的颜色）：描述性名称（"Deep Muted Teal-Navy"，而不是 "blue-800"）。按色相/饱和度为每个关键颜色建议 2-3 个选项。
- **海拔哲学**：扁平/分层/抬升。如果有阴影，它们的作用是氛围性的还是结构性的？
- **组件哲学**：用一句话概括按钮、卡片、输入框的质感（"有触感且自信" vs "精致且克制"）。

只有当 PRODUCT.md 里的一句话是真正约束视觉系统的持久品牌承诺时才搬进来。页面策略和表面概念不属于这里。

### Step 4: 写 DESIGN.md

文件以 Step 2b 暂存的 YAML frontmatter 开头（schema 见本参考顶部），随后是采用下方规范结构的 markdown 正文。

```markdown
---
name: [Project Title]
description: [one-line tagline]
colors:
  # ... staged frontmatter from Step 2b
---

# Design System: [Project Title]

## Overview

**Creative North Star: "[Named metaphor in quotes]"**

[2-3 paragraph holistic description: personality, density, and aesthetic philosophy. Start from the North Star and work outward. State only confirmed visual rejections. End with a short **Key Characteristics:** bullet list.]

## Colors

[Describe the palette character in one sentence.]

### Primary
- **[Descriptive Name]** (#HEX / oklch(...)): [Where and why this color is used. Be specific about context, not just role.]

### Secondary (optional; omit if the project has only one accent)
- **[Descriptive Name]** (#HEX): [Role.]

### Tertiary (optional)
- **[Descriptive Name]** (#HEX): [Role.]

### Neutral
- **[Descriptive Name]** (#HEX): [Text / background / border / divider role.]
- [...]

### Named Rules (optional, powerful)
**The [Rule Name] Rule.** [Short, forceful prohibition or doctrine, e.g. "The One Voice Rule. The primary accent is used on ≤10% of any given screen. Its rarity is the point."]

## Typography

**Display Font:** [Family] (with [fallback])
**Body Font:** [Family] (with [fallback])
**Label/Mono Font:** [Family, if distinct]

**Character:** [1-2 sentence personality description of the pairing.]

### Hierarchy
- **Display** ([weight], [size/clamp], [line-height]): [Purpose; where it appears.]
- **Headline** ([weight], [size], [line-height]): [Purpose.]
- **Title** ([weight], [size], [line-height]): [Purpose.]
- **Body** ([weight], [size], [line-height]): [Purpose. Include max line length like 65–75ch if relevant.]
- **Label** ([weight], [size], [letter-spacing], [case if uppercase]): [Purpose.]

### Named Rules (optional)
**The [Rule Name] Rule.** [Short doctrine about type use.]

## Layout

[Describe the grid or spatial model, container behavior, density, responsive changes, and the spacing rhythm. Include exact values only when observed.]

## Elevation & Depth

[One paragraph: does this system use shadows, tonal layering, or a hybrid? If "no shadows", say so explicitly and describe how depth is conveyed instead.]

### Shadow Vocabulary (if applicable)
- **[Role name]** (`box-shadow: [exact value]`): [When to use it.]
- [...]

### Named Rules (optional)
**The [Rule Name] Rule.** [e.g. "The Flat-By-Default Rule. Surfaces are flat at rest. Shadows appear only as a response to state (hover, elevation, focus)."]

## Shapes

[Describe the form language: corner/radius strategy, borders, clipping, and any recurring silhouette or geometry.]

## Components

For each component, lead with a short character line, then specify shape, color assignment, states, and any distinctive behavior.

### Buttons
- **Shape:** [radius described, exact value in parens]
- **Primary:** [color assignment + padding, in semantic + exact terms]
- **Hover / Focus:** [transitions, treatments]
- **Secondary / Ghost / Tertiary (if applicable):** [brief description]

### Chips (if used)
- **Style:** [background, text color, border treatment]
- **State:** [selected / unselected, filter / action variants]

### Cards / Containers
- **Corner Style:** [radius]
- **Background:** [colors used]
- **Shadow Strategy:** [reference Elevation section]
- **Border:** [if any]
- **Internal Padding:** [scale]

### Inputs / Fields
- **Style:** [stroke, background, radius]
- **Focus:** [treatment, e.g. glow, border shift, etc.]
- **Error / Disabled:** [if applicable]

### Navigation
- **Style, typography, default/hover/active states, mobile treatment.**

### [Signature Component] (optional; if the project has a distinctive custom component worth documenting)
[Description.]

## Do's and Don'ts

Concrete visual guardrails grounded in the incumbent implementation or the user's chosen world. Lead each with "Do" or "Don't" and include exact values only when established. Do not turn a task-specific concept or surface strategy into a system-wide prohibition.

### Do:
- **Do** [specific prescription with exact values / named rule].
- **Do** [...]

### Don't:
- **Don't** [specific prohibition confirmed by the incumbent system or the user].
- **Don't** [...]
- **Don't** [...]
```

### Step 4b: 写 .impeccable/design.json sidecar（仅扩展内容）

frontmatter 拥有 token 基础项（colors、typography、rounded、spacing、components）。`.impeccable/design.json` 的 sidecar 承载 **Stitch 的 schema 放不下的内容**：每个颜色的色调梯度、阴影/海拔 token、动效 token、断点、完整的组件 HTML/CSS 片段（面板把它们渲染进 shadow DOM），以及叙述内容（北极星、规则、Do/Don't）。它扩展 frontmatter，而不是复制它。

每次重新生成根 `DESIGN.md` 时都要重新生成 sidecar。如果用户只要求刷新 sidecar（例如从实时面板的过期提示发起），保留 `DESIGN.md`，只写 `.impeccable/design.json`。

#### Schema

```json
{
  "schemaVersion": 2,
  "generatedAt": "ISO-8601 string",
  "title": "Design System: [Project Title]",
  "extensions": {
    "colorMeta": {
      "primary":        { "role": "primary",  "displayName": "Editorial Magenta", "canonical": "oklch(60% 0.25 350)", "tonalRamp": ["...", "...", "..."] },
      "cool-paper": { "role": "neutral",  "displayName": "Cool Paper",    "canonical": "oklch(96% 0.005 230)", "tonalRamp": ["...", "...", "..."] }
    },
    "typographyMeta": {
      "display": { "displayName": "Display", "purpose": "Hero headlines only." }
    },
    "shadows": [
      { "name": "ambient-low", "value": "0 4px 24px rgba(0,0,0,0.12)", "purpose": "Diffuse hover glow under accent elements." }
    ],
    "motion": [
      { "name": "ease-standard", "value": "cubic-bezier(0.4, 0, 0.2, 1)", "purpose": "Default easing for state transitions." }
    ],
    "breakpoints": [
      { "name": "sm", "value": "640px" }
    ]
  },
  "components": [
    {
      "name": "Primary Button",
      "kind": "button | input | nav | chip | card | custom",
      "refersTo": "button-primary",
      "description": "One-line what and when.",
      "html": "<button class=\"ds-btn-primary\">SAVE CHANGES</button>",
      "css": ".ds-btn-primary { background: #191c1d; color: #fff; padding: 16px 48px; letter-spacing: 0.05em; text-transform: uppercase; font-weight: 500; border: none; border-radius: 0; transition: background 0.2s, transform 0.2s; } .ds-btn-primary:hover { background: oklch(60% 0.25 350); transform: translateY(-2px); }"
    }
  ],
  "narrative": {
    "northStar": "The Editorial Sanctuary",
    "overview": "2-3 paragraphs of the philosophy, pulled from DESIGN.md Overview section.",
    "keyCharacteristics": ["...", "..."],
    "rules": [{ "name": "The One Voice Rule", "body": "...", "section": "colors|typography|elevation" }],
    "dos":   ["Do use ..."],
    "donts": ["Don't use ..."]
  }
}
```

**与 schemaVersion 1 相比的变化。**旧 sidecar 携带的是 token 基础项数组（`tokens.colors[]`、`tokens.typography[]` 等）。这些值现在放进 frontmatter。sidecar 只承载无法放进 frontmatter 的元数据（色调梯度、hex 只是近似值时的规范 OKLCH、显示名、角色提示），按 frontmatter token 名作键（`colorMeta.<token-name>`、`typographyMeta.<token-name>`）。组件仍然携带完整 HTML/CSS，因为 Stitch 的 8 属性集放不下它们。

#### 组件翻译规则

`html` 和 `css` 字段必须是**自包含、即插即用的片段**，注入 shadow DOM 后即可正确渲染。面板直接应用它们：没有后处理，没有框架运行时。

1. **Tailwind 展开。**如果源码使用 Tailwind（className="bg-primary text-white rounded-lg px-6 py-3"），把每个工具类展开为 `css` 字符串里的字面 CSS 属性。**不要**引用 Tailwind 类名；**不要**假设已加载 Tailwind CSS bundle。每个组件都必须自包含。
2. **token 解析。**如果项目把 token 暴露为 `:root` 上的 CSS 自定义属性（例如 `--color-primary`、`--radius-md`），就用 `var(--color-primary)` 引用；它们会穿过 shadow DOM 继承并保持实时绑定。如果 token 只存在于 JS 主题对象（styled-components、CSS-in-JS）中，就在生成时解析为字面值。
3. **图标。**内联为 SVG。不要引用 Lucide/Heroicons 包、图标字体或 `<img src="...">`。典型图标为 16-24px；直接复制 SVG path 数据。
4. **状态。**在 CSS 里内联包含 `:hover`、`:focus-visible` 以及（如有意义）`:active` 规则。只含静态默认态的快照会让面板显得死气沉沉。CSS 里的 hover + focus 规则让它活起来。
5. **reset 膨胀。**只提取组件*独特*的 CSS（background、color、padding、border-radius、typography、transition）。跳过通用 reset（`box-sizing: border-box`、`line-height: inherit`、`-webkit-font-smoothing`）。面板已有中性画布；不要重复携带 reset。
6. **类名加作用域。**每个类都加 `ds-` 前缀（例如 `ds-btn-primary`、`ds-input-search`），避免组件 CSS 在同一个 shadow DOM 里与其他组件的 CSS 冲突。

#### 该收录什么

目标是精选最能代表视觉系统的 **5-10 个组件**：

- **规范基础组件（项目有就一定收录）：**button（每个变体作为独立的组件条目）、input/text field、navigation、chip/tag、card。
- **签名组件（有特色就收录）：**真正定义了已实现系统的、反复出现的自定义模式。
- **跳过其余。**工具型组件、表单积木、包装布局：除非视觉上有特色，否则不值得记录。

如果项目**还没有组件库**（纯落地页、全新项目），就用与 DESIGN.md 规则一致的最佳实践默认值，从 token 合成规范基础组件。每个 `.impeccable/design.json` 都要有*东西*可渲染，哪怕是第 0 天。

#### 色调梯度

为每个颜色 token 生成 8 档的 `tonalRamp` 数组：从暗到亮，色相不变，接近白和黑处降低彩度，亮度从约 15% 到 95% 分档。面板把它渲染成色块下方的色带。如果项目已经定义了色调刻度（Material 的 `surface-container-low` 家族、Tailwind 风格的 `blue-50..blue-900`），就用那些值。否则在 OKLCH 中合成。

#### 叙述映射

直接取自你刚写好的 DESIGN.md：

- `narrative.northStar` → Overview 里的 `**Creative North Star: "..."**` 行
- `narrative.overview` → Overview 中的哲学段落
- `narrative.keyCharacteristics` → `**Key Characteristics:**` 列表项
- `narrative.rules` → 所有小节中的每条 `**The [Name] Rule.** [body]`，并打上 `section` 标签
- `narrative.dos` / `narrative.donts` → Do's and Don'ts 的列表项，逐字保留

不要改写措辞。面板把它们显示为二级折叠上下文；Markdown 里的那份语调要原样贯穿过去。

### Step 5: 确认并打磨

1. 把你写的完整 DESIGN.md 展示给用户。简要指出非显而易见的创意选择（描述性颜色名、氛围语言、命名规则）。
2. 说明 `.impeccable/design.json` 也一并写好了；实时面板现在渲染的是本项目真实的 button/input/nav 基础组件，而不是通用近似。
3. 提议细化任何小节："需要我修改某个小节、补充我遗漏的组件模式，或调整氛围语言吗？"

你自己刚写的就是最新来源；本会话中的后续命令不需要重新加载。

## 种子模式

面向还没有视觉系统可提取的项目。产出由用户选定的视觉世界脚手架，而不是编造的 token 规格。

### Step 1: 经由 new-work 的工作坊

PRODUCT.md 是前提。如果缺失，加载 [init.md](init.md) 并先完成其产品访谈。不要在没有持久产品上下文的情况下创造视觉身份。

如果 PRODUCT.md 已存在，加载 [new-work.md](new-work.md) 并确定视觉权威。种子模式需要一个具体的首个表面：用用户指名的目标，或询问他们想先做什么。运行 new-work 的 **Create or replace the visual world** 流程，然后 **Commit the world**，让视觉世界和它的第一次表达一起被选定。在方向性的 DESIGN.md 种子和表面简报完成之后停下；不要实现。结构化的模拟用户也算作用户，必须得到同样的选择。

如果 new-work 已在本会话中完成了工作坊，直接使用其选定方向。不要再次询问。

### Step 2: 写种子 DESIGN.md

使用扫描模式的规范小节顺序。填入选定的工作坊方向，把未解决的实现事实留作诚实的占位符。种子提交的是一个世界及其不变量；它不假装实现 token 已经存在。

文件开头放：

```markdown
<!-- SEED: established with the user before implementation; re-run /impeccable document once there's code to capture the actual tokens and components. -->
```

种子模式下的分节指导：

- **Overview**：选定的设计论题、布局行为、材质性格、图像立场、动效语法和可复用签名。把选定的首个表面表达留在其表面简报里；不要把它的构图提升为全局世界。
- **Colors**：选定的调色板策略和角色。只有当用户、现有资产或 new-work 的探索确立了具体值时才写值；否则标注 `[to be resolved during implementation]`。
- **Typography**：选定的字体性格和角色关系。只有确立了才写字体名；否则把配对标注为 `[to be resolved during implementation]`。
- **Layout**：选定的空间语法和响应式行为，不假装精确尺寸已经敲定。
- **Elevation & Depth**：选定的材质和深度行为，作为不变量来陈述，而不是从通用预设推断。
- **Shapes**：选定的形态和圆角语言。
- **Components**：完全省略；还没有任何组件。
- **Do's and Don'ts**：记录世界选择过程中确认的持久护栏，而不是任务局部的拒绝。

种子模式只写仅含 `name` 和 `description` 的最小 frontmatter；colors、typography、rounded、spacing、components 都还没有。真正的 token 在下一次扫描模式运行时落地。出于同样原因，种子模式跳过 `.impeccable/design.json` sidecar：没有东西可渲染。

### Step 3: 确认

1. 展示种子 DESIGN.md。明确指出它是种子（那个标记就是字面意义上的承诺）。
2. 告诉用户："等有了一些代码后再重跑 `/impeccable document`。那一轮会提取真实的 token 并生成 sidecar。"

你自己刚写的就是最新来源；无需重新加载。

## 风格指南

- **frontmatter 在前，正文在后。**token 放进 YAML frontmatter；正文为它们提供背景。不要在两处重定义同一个 token 值；frontmatter 是规范。
- **只携带持久的产品约束。**PRODUCT.md 里有约束力的 logo、身份资产、无障碍需求或品牌承诺可以约束 DESIGN.md。表面策略留在其表面简报里。
- **匹配规范。**按顺序使用它的八个规范小节，省略不相关的。动效指导放在它影响的世界或组件旁边，而不是创建 schema 不支持的 token 组。
- **描述性 > 技术性**："Gently curved edges (8px radius)" > "rounded-lg"。把技术值放进括号，描述先行。
- **功能性 > 装饰性**：对每个 token，解释它用在哪里（WHERE）、为什么用（WHY），而不只是它是什么（WHAT）。
- **括号里给出精确值**：hex 码、px/rem 值、字重；描述旁总是带上括号里的数字。
- **使用命名规则**：`**The [Name] Rule.** [short doctrine]`。它们好记、可引用，对 AI 消费者来说比列表的粘性强得多。Stitch 自己的输出就大量使用它们（"The No-Line Rule"、"The Ghost Border Fallback"）。每个小节 1-3 条。
- **证据确凿处就要果断。**对真正的不变量用硬性语言，对临时指导用较软的语言。
- **只有当具体审计测试植根于观察到的系统或已确认的用户决策时才使用。**一句话的测试胜过一段原则。
- **有选择地引用 PRODUCT.md。**产品事实解释这个世界为何契合；它默认不提供页面构图或视觉禁做清单。
- **按角色给颜色分组**，而不是按 hex 顺序或色相顺序。Primary / Secondary / Tertiary / Neutral 是规范顺序。

## 陷阱

- 不要粘贴原始 CSS 类名。翻译成描述性语言。
- 不要提取每一个 token。止步于真正复用的；一次性的值会污染系统。
- 不要发明不存在的组件。如果项目只有按钮和卡片，就只记录这些。
- 不要在未经询问的情况下覆盖已有的 DESIGN.md。
- 不要重复 PRODUCT.md 的内容。DESIGN.md 严格只管视觉。
- 不要用近义词替换规范小节。布局和响应式行为放 `Layout`；动效放在受影响的世界或组件旁。
- 不要哪怕轻微地改名小节。"Colors" 而不是 "Color Palette & Roles"。"Typography" 而不是 "Typography Rules"。工具解析依赖精确标题。
- 不要在 frontmatter 和正文之间重复 token 值。如果某个颜色在 `colors.primary` 里是 hex，正文可以命名它并描述其角色，但不应重申另一个 hex。frontmatter 是规范。
- 不要发明 Stitch schema 之外的 frontmatter token 组（顶层不要有 `motion:`、`breakpoints:`、`shadows:`）。Stitch 的 Zod schema 只接受 `colors`、`typography`、`rounded`、`spacing`、`components`。其他任何内容都属于 sidecar 的 `extensions`。
