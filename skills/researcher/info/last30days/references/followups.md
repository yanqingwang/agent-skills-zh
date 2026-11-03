> **中文汉化版** · 上游：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) · 原文件：`skills/last30days/references/followups.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 追问与提示词撰写

针对已有研究的追问阅读本文件。根文档的授权、来源诚实、引用与缓存数据规则一律保留。下面的直连引擎示例使用根文档绑定的解释器与引擎路径。

## 等待用户回应

**停下来等待**用户回应，此前先完成回复以及高优先级宿主/工具要求或用户指令所要求的引用。除非上位指令另有要求，邀请之后不要继续研究。只有在完全没有要求时才省略额外的来源清单。只有当引擎输出了保存路径时才宣称原始数据已保存；`LAST30DAYS_MEMORY_DIR` 为空则禁用保存及其页脚指针。

---

## 用户回应时

**读懂他们的回应并匹配意图：**

- 如果他们就该主题提**问题** → 用你的研究作答（不重新检索，不写提示词）
- 如果他们要求就某个子主题**深挖** → 用你的研究发现展开
- 如果他们描述了想要**创作**的东西 → 写一条完美的提示词（见下文）
- 如果他们明确要**提示词** → 写一条完美的提示词（见下文）
- 如果他们说**"more fun"**、**"too serious"**或类似说法 → 向 `~/.config/last30days/.env` 写入 `FUN_LEVEL=high`（追加，不要覆盖）。确认："Fun level set to high. Next run will surface more witty and viral content."
- 如果他们说**"less fun"**、**"too many jokes"**或类似说法 → 向 `~/.config/last30days/.env` 写入 `FUN_LEVEL=low`。确认："Fun level set to low. Next run will focus on the news."
- 如果他们在一次运行后说**"register exec"**、**"register dev"**、**"register creator"**或**"register default"** → 立即用该语气重新综合当前研究；不要重新抓取来源，也不要把这句短语当成新主题。如果他们要求为后续运行保留该设置，向 `~/.config/last30days/.env` 追加 `LAST30DAYS_REGISTER={name}`（绝不要覆盖该文件）。
- 如果他们说**"eli5 on"**、**"eli5 mode"**、**"explain simpler"**或类似说法 → 按 `register eli5` 处理：向 `~/.config/last30days/.env` 追加 `LAST30DAYS_REGISTER=eli5`，然后用 ELI5 指引立即重新综合当前研究，不要再次抓取。确认："ELI5 mode on. All future runs will explain things like you're 5."
- 如果他们说**"eli5 off"**、**"normal mode"**、**"full detail"**或类似说法 → 向 `~/.config/last30days/.env` 追加 `LAST30DAYS_REGISTER=default`。确认："ELI5 mode off. Back to full detail."
- 如果他们在一次运行后说**"drill into 3"**、**"go deeper on cluster 3"**、**"drill into the OpenClaw API ban discussion"**或类似说法 → 用 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" --drill "<their target>"` 调用引擎。引擎从新鲜的 `last-report.json` 缓存解析出 1 起始的簇编号或模糊的标题/实体描述，只对该簇涉及的来源以深层深度重新研究，合并并去重新证据，然后更新缓存，以便继续下一次下钻。转发渲染后的 **Original / Deeper** 简报。若缓存缺失或已过期，告诉他们先跑一次正常的 `/last30days <topic>` 研究。
- 如果他们说**"verify freshness"**、**"check whether those facts are still current"**，或在一次运行后要求以时效性为行动前提 → 不带主题调用 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" --verify-freshness`。它加载新鲜的报告缓存，仅对有依据支撑的数据做定点重抓，更新缓存中的裁决，并渲染紧凑的 Freshness Verification 表格。对于首次提出的这类请求，把意图转成常规引擎调用再加上 `--verify-freshness`。`LAST30DAYS_VERIFY_FRESHNESS=on` 让验证成为主题运行的默认行为；它不会把无主题的引擎调用变成隐式的缓存读取。
- 如果他们说**"mark <topic> as covered"**、**"I covered X on the podcast"**、**"we published that article"**或类似说法 → 用 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" queue cover "<topic name>" --save-dir="${LAST30DAYS_MEMORY_DIR}"` 调用引擎（与发现运行相同的 `--save-dir` 作用域——队列记录存放在该目录的 research.db 中）。标记已覆盖需要与队列中的主题名完全一致；若名称未知，引擎会以退出码 2 结束并指向 `queue list`——转发这条提示，运行 `queue list`，把队列中的名称给对方，而不是靠猜来重试。
- 如果他们说**"what's in my topic queue"**、**"what should I talk about next"**、**"show my content pipeline"**或类似说法 → 调用 `"${LAST30DAYS_PYTHON}" "${SKILL_DIR}/scripts/last30days.py" queue list --save-dir="${LAST30DAYS_MEMORY_DIR}"` 并转发渲染后的列表（尚未覆盖的已浮现主题，含领域、浮现次数与最近浮现日期）。空队列也是有效答案——建议跑一次 `/last30days trending` 或领域发现运行来填充它。（这两条覆盖的是会话内场景，即运行已在上下文中。同样的诉求在冷启动时到来——本会话还没有任何研究运行——由根文档把关的 library/queue 快速路径处理，它直接执行相同的命令，不会落入主题研究。）

面向用户的斜杠交互是自然语言（`drill into N`），不是带 shell 语法的斜杠命令。`--drill` 是宿主模型把该意图翻译出来的直连引擎标志；不要告诉用户往 `/last30days` 上追加管道符或引擎标志。

**只有用户想要提示词时才写。** 别把提示词硬塞给一个问"what could happen next with Iran."的人。

### 撰写提示词

用户想要提示词时，用你的研究专长写**一条高度定制的提示词**。

### 关键：匹配研究推荐的格式

**如果研究要求使用特定的提示词格式，你必须使用该格式。**

**反面做法**：研究说"用带设备规格的 JSON 提示词"，你却写成散文。这会让研究完全白做。

### 质量检查清单（交付前逐项过）：
- [ ] **格式与研究一致**——研究说是 JSON/结构化等，提示词就必须是那个格式
- [ ] 直接回应用户说要创作的东西
- [ ] 用上研究中发现的具体模式/关键词
- [ ] 可直接粘贴，无需任何修改（或只需替换少量且明确标注的 [PLACEHOLDERS]）
- [ ] 长度与风格适配 TARGET_TOOL

### 输出格式：

```
Here's your prompt for {TARGET_TOOL}:

---

[The actual prompt IN THE FORMAT THE RESEARCH RECOMMENDS]

---

This uses [brief 1-line explanation of what research insight you applied].
```

---

## 如果用户要求更多选项

只有当他们要求备选或更多提示词时，才提供 2-3 个变体。除非被要求，不要一次丢出一包提示词。

---

## 每次交付提示词后：保持专家模式

交付提示词后，主动提出可以再写：

> Want another prompt? Just tell me what you're creating next.

---

## 上下文记忆

在本次对话余下时间里，记住：
- **TOPIC**：{topic}
- **TARGET_TOOL**：{tool}
- **KEY PATTERNS**：{列出你学到的 3-5 个主要模式}
- **RESEARCH FINDINGS**：研究中的关键事实与洞察

**关键：研究完成后，把你当成这个主题上的专家。**

用户提出追问时：
- **不要发起新的 WebSearch**——研究你已经有了
- **用你学到的内容作答**——引用 Reddit 讨论串、X 帖子和 web 来源
- **如果他们提问题**——用你的研究发现回答
- **如果他们要提示词**——用你的专业知识写一条

只有当用户明确问到**另一个主题**时才重新做研究。

---

## 输出摘要页脚（每次交付提示词后）

交付提示词后，以这段收尾：

```
---
📚 Expert in: {TOPIC} for {TARGET_TOOL}
📊 Based on: {n} Reddit threads ({sum} upvotes) + {n} X posts ({sum} likes) + {n} YouTube videos ({sum} views) + {n} TikTok videos ({sum} views) + {n} Instagram reels ({sum} views) + {n} HN stories ({sum} points) + {n} web pages

Want another prompt? Just tell me what you're creating next.
```

---
