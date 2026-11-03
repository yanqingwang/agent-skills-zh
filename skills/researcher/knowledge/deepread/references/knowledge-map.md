> **中文汉化版** · 上游：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) · 原文件：`research/deepread/references/knowledge-map.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 以证据为中心的知识地图

本参考用于 `map` 模式。一张有用的地图保留的是推理过程，而不只是标题结构。

## 节点类型

- `THESIS`：中心主张或解释性模型。
- `CLAIM`：支持性或反对性的命题。
- `REASON`：主张之间的逻辑桥梁。
- `EVIDENCE`：观察、引文、记录或研究。
- `DATA`：带单位、总体、时期与基线的数值证据。
- `EXAMPLE`：本身并不足以确立普遍性的说明性例子。
- `CONCEPT`：其定义对论证起关键作用的术语。
- `ASSUMPTION`：未言明的前提。
- `COUNTERARGUMENT`：替代性的结论或解释。
- `LIMITATION`：对适用范围或置信度的限定。
- `QUESTION`：尚未解决的问题或检索提示。

## 边标签

每条边都必须使用有意义的标签：`supports`、`explains`、`defines`、`illustrates`、`depends on`、`qualifies`、`contradicts` 或 `raises`。

绝不用无标签的相邻关系代替关系本身。

## 必需元数据

对证据节点与数据节点，要包含：

- 来源位置；
- 它们连接的主张；
- 置信度标签；
- 缺失的上下文或注意事项。

## Markdown 输出

```text
THESIS: [central claim]
├── supports → CLAIM: [supporting claim]
│   ├── because → REASON: [logical bridge]
│   ├── supports → EVIDENCE: [evidence] ([location])
│   └── qualifies → LIMITATION: [boundary]
├── depends on → ASSUMPTION: [unstated premise]
└── contradicted by → COUNTERARGUMENT: [strong alternative]
```

当用户要求兼容 FreeMind 或 XMind 的输出时，把同一层级渲染为合法的 FreeMind XML，并对 XML 属性中用到的全部原文派生文本做转义。

## 质量检查

交付地图之前，确认：

1. 每一条主要主张都连到中心论题。
2. 每一个证据节点都连到具体主张。
3. 例子被标注为例子。
4. 矛盾与局限保持可见。
5. 地图中不含仅因排版而出现的结论。

## 参考资料

1. Novak, J. D. & Cañas, A. J. — “The Theory Underlying Concept Maps and How to Construct and Use Them”（IHMC CmapTools 技术报告，2008）— 本地图结构所源自的概念制图方法。
2. Toulmin, S. — *The Uses of Argument*（1958）— 主张 / 根据 / 担保的分解，与“主张-理由-证据”字段一一对应。
3. Ahrens, S. — *How to Take Smart Notes*（2017）— 原子化、可链接的笔记作为持久的知识结构。
4. Adler, M. J. & Van Doren, C. — *How to Read a Book*（1972）— 综览式阅读：刻画多个来源如何回答同一个问题。
5. Weinstein, Y., Madan, C. R. & Sumeracki, M. A. — “Teaching the Science of Learning”，*Cognitive Research* 3（2018）— 编码进地图边标签中的精加工与具体例子策略。
6. Hattie, J. & Donoghue, G. M. — “Learning Strategies: A Synthesis and Conceptual Model”，*npj Science of Learning* 1（2016）— 组织 / 制图策略在习得→巩固循环中发挥作用之处。
