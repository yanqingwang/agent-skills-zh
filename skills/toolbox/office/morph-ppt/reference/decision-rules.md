---
name: decision-rules
description: "PPT 规划提示词——推断受众、目的与叙事，然后输出 brief.md。当幻灯片的受众或目的未明确指定时，在主配方之前运行。"
---

> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/decision-rules.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# PPT 规划器

**使用方法。** 在 `SKILL.md` §Morph Pair Planning 阶段、**写下任何** `officecli add / set` 命令**之前**读本文件。从用户的主题推断受众、目的与叙事；输出单个 `brief.md`，供主配方使用。缺少叙事主线的 morph 弧线会退化成"带动画的幻灯片"，而不是"有故事的运动"。下面的规划正是为了防止这一点。

角色：深入思考用户的主题，产出一份高质量的 PPT 规划。

输出：单个 `brief.md`，包含抽取摘要、大纲和详细页面简报。

---

## 推断受众

**思考方法**：基于主题关键词和使用场景，问"谁会看这份 PPT？他们最关心什么？"

**常见模式（示例，非穷举）**：

- 融资 / 路演 → 投资人
- 教学 / 培训 → 学员
- 产品介绍 → 客户
- 分析 / 报告 → 高管
- 内部分享 → 同事
- 无法判断 → 通用商务

---

## 推断目的

**思考方法**：基于主题关键词，问"用户想用这份 PPT 达成什么结果？"

**常见模式（示例，非穷举）**：

- 融资 / 路演 → 说服投资
- 产品介绍 → 展示价值
- 分析 / 报告 → 输出洞察
- 培训 / 教学 → 传授知识
- 无法判断 → 呈现信息

---

## 推断叙事结构

**思考方法**：根据目的选择合适的叙事主线。

**常见结构（示例，非穷举）**：

| 适用场景           | 叙事结构            | 页面顺序示例                                          |
| ----------------------------- | ------------------- | ----------------------------------------------------- |
| 融资 / 销售 / 投标 | problem_solution    | hero → statement → pillars → evidence → cta           |
| 汇报 / 分析          | insight_driven      | hero → statement → evidence → pillars → cta           |
| 推广 / 演讲            | vision_driven       | hero → quote → pillars → evidence → cta               |
| 教学 / 培训           | educational         | hero → statement → pillars → pillars → showcase → cta |

**自由组合**：可根据具体内容灵活调整。

---

## 构建大纲

### 思考方法：金字塔原理

1. **结论先行**：每页从核心论点出发，而不是信息罗列
2. **自上而下**：整份结论 → 页级论点 → 支撑要点
3. **同类分组**：同一页上的要点属于同一逻辑类别
4. **逻辑递进**：按时间 / 重要性 / 因果 / 并列组织

### 六步思考流程

1. 这份 PPT 的一句话结论是什么？
2. 需要几个支撑论点？
3. 每一页的核心论点是什么？
4. 什么证据 / 数据 / 案例支撑每一页？
5. 哪些页必不可少？哪些"有则更好"？
6. 受众最可能在哪里提出异议？

### 页数指引（仅供参考）

- 快速介绍 / 单一主题：3–5 页
- 标准演示：5–8 页
- 深度分析 / 年度报告：10–15 页

---

## brief.md 输出格式

把所有内容写进单个 `brief.md`，分三节：

### 第 1 节：摘要

```
Topic: ...
Audience: ... [provided / inferred]
Purpose: ... [provided / inferred]
Narrative: ...
Style direction: ... [provided / inferred based on topic + mood, not habit]
```

**风格选择原则**：

1. **匹配主题气质** → 商务≠活泼，科技≠有机（除非有意反差）
2. **项目间要有变化** → 浏览 `reference/styles/` 目录，避免重复近期用过的风格
3. **考虑 6 大类** → dark (16), light (10), warm (11), bw (5), vivid (6), mixed (7)
4. **优先"意外但贴切"** → 不要给所有科技主题都默认"dark + neon"
5. **点名具体风格** → 用"warm--earth-organic palette"，不用"warm tones"

### 第 2 节：大纲

```
Overall conclusion: AI Agent Platform lets every enterprise have its own AI workforce
---
S1: [hero] "AI Agent Platform — Let agents work for you"
S2: [statement] "From automation to autonomy: why agents are needed now"
S3: [pillars] "Three core capabilities: Perceive / Reason / Execute" ★key slide
S4: [evidence] "10M+ API Calls / 99.95% Uptime / 50ms P95"
S5: [cta] "Start building your agent"
```

### 第 3 节：页面简报

对每一页，回答 6 个问题：

```
S3 [pillars] ★key slide
├── Objective: Help the audience understand the three differentiated capabilities
├── Core information (detailed):
│   ① Perception: Supports text, image, voice, video multimodal input, 95%+ accuracy
│   ② Reasoning: Chain-of-Thought technology, 40% improvement on complex tasks
│   ③ Execution: Auto-calls 20+ tools and APIs, end-to-end task completion
├── Evidence: Specific metrics for each capability
├── Page type: pillars (multi-column)
├── Hierarchy: Number ① largest → capability name next → description smallest
└── Transition: S2 asks "why needed" → S3 answers "how it works"
```

**关键**：核心信息必须详尽完整（标题、描述、数据、案例）。不要写"多模态理解"这类缩略要点。设计专家将直接使用这些内容。

---

## 兜底策略

| 失败场景            | 兜底策略                                         |
| --------------------------- | ----------------------------------------------- |
| 无法推断受众       | 通用商务                                |
| 无法推断目的        | 呈现信息                             |
| 无法确定页数 | 按内容量决定；避免 <3 或 >20 |

---
