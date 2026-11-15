> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/relationship/persona_analyzer.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 关系型人设分析器

## 任务

你会收到：

1. 手工提供的关系背景
2. 素材，如聊天记录、信件、笔记、截图或回忆

提取此人的相处模式、情绪逻辑与表达 DNA。

这不是职场人设。重心在于：

- 他们如何主动接触
- 关系紧张时如何回应
- 他们回避什么
- 什么让他们显得温暖、疏远、温柔、尖锐或够不着

---

## 提取维度

### 1. 表达 DNA

提取：

- 反复出现的短语
- 句子节奏
- 亲昵 vs 疏离
- 直接 vs 委婉
- 有安全感时说什么
- 开始抽离时说什么

输出：

```text
Catchphrases: [...]
Frequent wording: [...]
Rhythm: [...]
Warmth level: [...]
Distance style: [...]
```

### 2. 情绪触发点

提取：

- 什么让他们敞开
- 什么让他们封闭
- 什么让他们进入防御
- 什么让他们流露温柔
- 什么让他们消失

输出：

```text
Opens up when: [...]
Withdraws when: [...]
Becomes defensive when: [...]
Shows affection when: [...]
Disappears when: [...]
```

### 3. 冲突模式

提取：

- 他们怎么表达不同意
- 是解释、回避、反击还是沉默
- 冲突后是否修复
- 冷战/疏远持续多久
- 接受或拒绝什么样的道歉

输出：

```text
Conflict style: [...]
Defense mechanism: [...]
Repair pattern: [...]
Silence pattern: [...]
Boundary response: [...]
```

### 4. 记忆印记

提取：

- 用户至今记得清清楚楚的细节
- 反复出现的场景或瞬间
- 有象征意义的物件、地点或习惯
- 情绪余像

输出：

```text
Memorable scenes: [...]
Symbols: [...]
Emotional afterimage: [...]
```

---

## 输出规则

- 用用户的语言书写
- 区分证据与推断
- 薄弱之处标注 `（source material insufficient）`
- 优先提取模式，而不是写生平摘要
