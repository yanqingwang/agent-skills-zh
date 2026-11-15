> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/02-long-document.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 02 · Long Document

读起来像一份备忘录、一封信或一篇日志。没有营销结构。连续散文加行内小节标题。页面是关于产品的文学。

- **标题：** 与正文同行；小节标题以短的加粗短语从段落流中浮现。
- **正文：** 单栏，line-height 1.65 或以上，行长 60 到 65ch。
- **分隔：** 负空间；缝隙就是分隔；至多一个居中的装饰符号用于强调。
- **按钮：** 段落内的字排链接，带动词，绝不是独立块。它是首屏唯一可见的动作（44b）。
- **图像：** 行内，按行长定尺寸；绝不满幅出血。
- **Reveal：** 不用。页面就那么摆着。

案例研究、创始人文章、使命页、售卖本身是哲学的产品选它。提示词说的是 "tell a story"（讲个故事），不是 "list features"（列功能）。

只有一个决定性动作要采取时避免使用。Long Document 把动作藏进句子里，这对交易型页面是错的。

标题：[`../craft.md`](../craft.md) § 7 第 3 条的行内引语式起笔。

```html
<article class="prose">
  <p class="lede">…</p>
  <h2 class="inline">A small heading.</h2>
  <p>… <a href="#prices">See the prices</a> …</p>
</article>
```

```css
.prose { max-width: 65ch; }
.prose h2.inline { display: inline; font: inherit; font-weight: 700; letter-spacing: normal; }
.prose h2.inline + p { display: inline; }
```

**样例开篇句**（模仿其具体性，不照搬措辞）：
> *"Saturday, 6:14 a.m. The dough went in at midnight."*（星期六，凌晨 6:14。面团是午夜进炉的。）以时间戳开场；品牌把自己介绍为一天中的一个时刻（Maple Street Bread）。
> *"A monthly publication for people who still read to the end."*（一份给仍然读到最后的人的月刊。）点出节奏与读者。
> *"We build one thing, and we have built it for nine years."*（我们只做一件事，已经做了九年。）一个动词，一个计数，没有声明。
