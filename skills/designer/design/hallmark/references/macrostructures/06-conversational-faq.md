> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/hallmark/references/macrostructures/06-conversational-faq.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

## 06 · Conversational FAQ

加粗的问题，利落的回答。页面读起来像对产品的一次诚实访谈。每一对问答都可以是一个折叠。

- **标题：** 每个小节是一个问题：以 `?` 结尾的短而直接的短语。
- **正文：** 答案是一两段短文，直接放在问题之下。
- **分隔：** 每对之间一条发丝线，或不用线而换纸。
- **按钮：** 答案内一条带动词的字排链接（"Read the policy"，读政策条款）；页脚一个描边 CTA。
- **图像：** 稀疏；每个长答案至多一幅图解。
- **Reveal：** 加载时不做；折叠展开用 `--dur-long` 配 `--ease-out`，作用于 `grid-template-rows`，从 `0fr` 到 `1fr`。

价格页附近、会遭遇怀疑的产品、受监管或教育领域选它。

作为主页面时，它以一个问出第一个问题的 hero 开场；否则它与另一个开场形态搭配。

```html
<section class="faq">
  <details>
    <summary><h2>How long does setup take?</h2></summary>
    <div class="answer"><p>…</p></div>
  </details>
</section>
```

**样例开篇句**（问题是真问题；答案短而具体）：
> *"What is this for? A single-binary CLI for parsing log streams from stdin."*（这是干嘛的？一个解析 stdin 日志流的单二进制 CLI。）点出形态与输入（Streampipe）。
> *"How is it different? It runs where the logs are, so nothing leaves the box."*（有什么不同？它在日志所在的地方运行，所以什么都不离开机器。）用事实回答，不做比较。
> *"Who built this? Three of us, in Lisbon, since 2014."*（谁做的？我们三个，在里斯本，从 2014 年起。）日期、地点、人数；没有营销。
