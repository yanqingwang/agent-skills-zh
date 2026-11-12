> **中文汉化版** · 上游：[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) · 原文件：`skills/taste-skill/references/type.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 字体排印

访客看到的大部分是文字，一个页面看起来是"被设计的"还是"拼凑出来的"，也主要由文字决定。
方向表会发给你一套字体系统（字族、字重、参数）。本文件讲的是如何使用它。

## 目录

1. 研究测了什么
2. 字阶：字号很少，差距很大
3. 排展示大字
4. 排正文字
5. 正确加载字体
6. 一个字族还是两个
7. 区分"排出来的字"与"打出来的字"的细节
8. 检查器看不见的错误

## 1. 研究测了什么

在被研究的 247 个站点中，202 个可测量（Chrome，1440×900 与 390×844）：

| | 中位数 | 中间一半 | 备注 |
| --- | --- | --- | --- |
| Hero 标题字号 | 72px（5.0vw） | 43–109px | 得分最高站点：中位数 6.0vw |
| 页面最大字号 | 6.4vw | 最高 10.4vw | 得分最高站点 8.4vw，弱站 5.0vw |
| 手机上的 hero 标题 | 40px | 32–59px | |
| Hero 字距 | -0.01em | -0.03 至 0 | 字号越大收得越紧 |
| Hero 行距 | 1.0 | 0.95–1.1 | |
| 正文字号 | 16px | 14–18px | |
| 标题÷正文字号 | 4.3 | | 得分最高站点 4.7 |
| 实际使用的字族数 | 2 | 31% 用一个，45% 用两个，22% 用三个 | |
| Hero 字重 | regular 48%，medium 18%，bold 或更重 22% | | 大字不需要加粗 |
| Hero 全大写 | 24% | | |
| Hero 居中 | 39% | | 弱站为 52% |

从中得出两件事。第一，字号对比是主要杠杆，最好的站点把它拉得更开。第二，字重不是：一半的
hero 用 regular 字重。让文字显得自信的是字号与间距；加粗只是众多选项之一。

## 2. 字阶：字号很少，差距很大

评审团把 114 个最强站点中的约 30 个描述为只用两三个字号、中间没有任何过渡，没有一个被描述为
使用分级的五六档字阶。所以：一个展示字号、一个正文字号加一个小字号撑起整个页面；lead 字号
和标题字号备着，需要时才用。五档是上限。常见的失败是九个彼此接近的字号（16、18、20、24、28、
32…），读起来像一团浆糊。选择明显不同的档位：

```css
:root {
  --step-small: clamp(0.8125rem, 0.79rem + 0.1vw, 0.875rem);   /* 13–14px  captions, legal */
  --step-body:  clamp(1.0625rem, 1rem + 0.25vw, 1.1875rem);    /* 17–19px  paragraphs */
  --step-lead:  clamp(1.25rem, 1.1rem + 0.7vw, 1.625rem);      /* 20–26px  supporting line, large body */
  --step-head:  clamp(2rem, 1.3rem + 3.2vw, 4rem);             /* 32–64px  section headings */
  --step-display: clamp(3rem, 1rem + 9vw, 9rem);               /* set by the hero blueprint */
}
```

- `--step-display` 属于方向本身。纪念碑式字标是 16–24vw；一件安静仪器的标题是 28px。使用
  hero 蓝图给定的字号，写成 `clamp()`，让它随视口缩放，同时在手机和超宽屏上有边界。
- 保持差距：桌面端展示字号至少是正文字号的四倍，`--step-lead` 与 `--step-head` 之间不应再
  有字号，除非设计真的需要第六档。
- 别给每张卡片和标签都配一个"副标题"字号。如果两个字号看起来几乎一样，就让它们成为同一个。

## 3. 排展示大字

大字会暴露在小字号下看不见的间距问题。对超过 40px 的文字全部应用以下设置：

```css
.display {
  font-size: var(--step-display);
  line-height: 0.95;              /* 0.85–1.05; tighter for capitals and condensed faces */
  letter-spacing: -0.035em;       /* -0.02 to -0.05em; use the value on the direction sheet */
  font-kerning: normal;
  text-wrap: balance;
  max-width: 14ch;                /* choose the measure so lines break where you want */
  margin: 0;
}
```

- **字距随字号缩放。** 字越大，字距要收得越紧；适合 120px 的值会让 32px 喘不过气。按档位
  设置字距，不要对所有标题设一次了事。
- **行距低于 1.0 需要检查。** 看看下一行的下行字母与上一行的上伸部或重音符号是否相撞。两行
  标题最容易用肉眼验证这一点。
- **全大写**即使在展示字号下也要稍开的字距（0 到 +0.03em），行距 0.9 左右。
- **视觉对齐。** 左边缘为圆形或斜线的大字母（O、C、A、T、W）看起来像缩进了。把标题向左拉
  约 0.04–0.06em（`margin-left: -0.05em`），让它与下方文字视觉对齐。
- **横贯视口的大字。** 必须横跨整屏的一行字用 `vw` 定字号，并在 390 和 1440 下验证；设
  `white-space: nowrap`，让容器裁切而不是换行。字号按字符数计算：
  `font-size ≈ container width ÷ (characters × k)`，k 见 `copy.md` §2。
- 永远不要给展示大字加文字阴影、描边或渐变填充。

## 4. 排正文字

```css
body { font-size: var(--step-body); line-height: 1.5; font-kerning: normal; text-rendering: optimizeLegibility; }
p { max-width: 62ch; text-wrap: pretty; margin: 0; }
p + p { margin-top: 0.9em; }
.lead { font-size: var(--step-lead); line-height: 1.35; max-width: 40ch; }
small, .caption { font-size: var(--step-small); line-height: 1.45; }
```

- 每行字数：45–75 个字符。更宽眼睛就会找不到下一行；检查器在约 88 之后会发出警告。
- 行距：正文 1.45–1.6，较大的 lead 字号更紧（1.3–1.4），长文阅读可更松。
- 次要文字用同一字族配更淡的墨色（`--muted`），不是更轻的字重，也不小于 13px。
- 不要居中超过三行的段落。不要两端对齐。
- 深色底上的浅色字看起来更重：降一档字重或加 0.01em 字距，并把行距稍微调大。

## 5. 正确加载字体

方向表会给一个 `<link>` 标签。原样使用；不要换成你偏好的字族。

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="…from the direction sheet…" rel="stylesheet">
```

```css
:root {
  --font-display: "Family From Sheet", "Helvetica Neue", Arial, sans-serif;
  --font-text: "Family From Sheet", Georgia, serif;
}
```

- 只请求你用到的字重（通常总共两三个）。
- 总是提供同一大类（sans 配 sans，serif 配 serif）的回退字族栈。
- 在框架里，用框架的字体加载器加载同一字族和字重（`next/font/google`，或自托管 `@font-face`
  配 `font-display: swap`）。Fontshare 字族从方向表上的 `api.fontshare.com` 样式表加载。
- 构建之后，`inspect.mjs` 会报告实际渲染的字族。如果它警告某个字族没有加载，截图里显示的
  就是回退字体，你从截图判断出的一切都不作数。先修链接。

## 6. 一个字族还是两个

被研究站点中有三分之一对所有文字只用一个字族，这是显得统一的最稳妥方式。当发下的系统有
两个字族时：

- 给每个字族分配职责，绝不互换：一个排标题，另一个排其余一切。
- 不要为标签、数字或引用引入第三个字族。
- 不要在一个标题内混用两个字族。
- 斜体用于作品名和段落内的真正强调，绝不用作装饰。

## 7. 区分"排出来的字"与"打出来的字"的细节

- 弯引号和弯撇号、真正的破折号、真正的省略号（见 `copy.md` §7）。
- 价格、表格、成列的日期用 `font-variant-numeric: tabular-nums`；`oldstyle-nums` 适合 serif
  正文。
- 链接上加 `text-underline-offset: 0.18em; text-decoration-thickness: 0.07em`，让下划线避开
  下行字母。
- 标题上用 `hyphens: none`。`overflow-wrap: anywhere` 只用于长 URL 或邮箱。
- 标题属于它后面的文字：标题上方的间距至少是下方的两倍。
- `::selection { background: var(--accent); color: var(--accent-ink); }`，加上 accent 色的可见
  `:focus-visible` 轮廓，让连浏览器自身的状态也属于设计。
- 不要在 hover 时改变字重；整行会回流。

## 8. 检查器看不见的错误

- 通过了两行规则但断行很糟的标题：第二行只剩一个孤词，或断点拆散了词组（"Stools for small /
  kitchens"）。亲手定断点。
- 收得太紧以致字母相碰的展示大字，或松散到散架的展示大字。
- 自信的 hero 之后跟着几乎一样大的分区标题。每屏只保持一个占主导的字号。
- 用展示字族排正文，而这个字族本只为大字号设计。
- 全部加粗。如果每一行都在强调，就没有一行被强调。
