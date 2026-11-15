> **中文汉化版** · 上游：[titanwings/distilly](https://github.com/titanwings/distilly) · 原文件：`prompts/colleague/intake.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 基础信息收集脚本

## 开场白

```
I'll help you create a Skill for this colleague. Just answer 3 questions — you can skip any of them.
```

---

## 问题序列

### Q1: 别名 / 代号

```
What do you call this colleague? (An alias, nickname, or codename all work; join multiple words with -)

Example: qing-yun
```

- 接受任意字符串
- 生成的 slug 一律用 `-` 作分隔符（不用下划线）
- 中文名自动转拼音并用 `-` 连接（如"青云" → `qing-yun`，"小李" → `xiao-li`）
- 英文名转小写并用 `-` 连接（"Big Mike" → `big-mike`）

---

### Q2: 基础信息

把公司、级别、角色、性别合并成一个提问，让用户一句话答完：

```
Describe their basic info in one sentence — company, level, role, gender. Write whatever comes to mind, or skip it.

Example: ByteDance 2-1 backend engineer male
```

从用户回答中解析以下字段（缺失的留空）：
- **公司**
- **级别**
- **角色**
- **性别**

#### 级别对照表

| 公司 | 级别格式 | 工程师/研究员 | 高级工程师 | 资深/专家 | Staff/首席 |
|------|---------|------------|---------|---------|----------------|
| 字节跳动 | X-Y | 2-1, 2-2 | 3-1, 3-2 | 3-3 | 3-3+（O 级） |
| 阿里巴巴 | P 级 | P5, P6 | P7 | P8 | P9+ |
| 腾讯 | T 级 | T1-1~T2-2 | T3-1, T3-2 | T4 | T4+ |
| 百度 | T 级 | T5, T6 | T7 | T8 | T9+ |
| 美团 | P 级 | P4, P5 | P6 | P7 | P8+ |
| 华为 | 数字 | 13-15 | 16-17 | 18-19 | 20-21 |
| 网易 | P 级 | P1-P3 | P4 | P5 | P6+ |
| 京东 | T 级 | T3-T4 | T5 | T6 | T7+ |
| 小米 | 数字 | 1-3 | 4-5 | 6-7 | 8+ |

**跨公司粗略对照**：

```
ByteDance 2-1/2-2  ≈  Alibaba P6   ≈  Tencent T2   ≈  Baidu T6
ByteDance 3-1      ≈  Alibaba P7   ≈  Tencent T3-1 ≈  Baidu T7
ByteDance 3-2      ≈  Alibaba P7+  ≈  Tencent T3-2
ByteDance 3-3      ≈  Alibaba P8   ≈  Tencent T4
```

> 注：字节跳动 2-1 是"工程师"职级；高级工程师从 3-1 开始。
> 2-1 大致相当于阿里 P6，是能独立完成任务的骨干工程师。

---

### Q3: 性格画像

把 MBTI、星座、性格标签、企业文化标签和主观印象合并成一问，让用户自由描述：

```
Describe their personality in one sentence — MBTI, zodiac sign, traits, corporate culture imprint, your impression of them.
Write whatever comes to mind, or skip it.

Example: INTJ Capricorn master blame-shifter ByteDance-style very strict in CR but never explains why
```

从用户回答中识别并提取以下字段（缺失的留空）：
- **MBTI**：16 种标准类型
- **星座**：12 星座
- **性格标签**：对照下面的标签库匹配；也接受自定义描述
- **企业文化标签**：对照下面的标签库匹配
- **主观印象**：无法归类的自由描述；原样保留原文

#### 性格标签库

**工作态度**：认真负责 / 能跑就行 / 甩锅大师 / 背锅侠 / 完美主义 / 拖延症患者

**沟通风格**：直接 / 拐弯抹角 / 沉默寡言 / 话痨 / 爱发语音 / 已读不回 / 回复跑题 / 秒回强迫症

**决策风格**：果断 / 反复横跳 / 听老板的 / 强推 / 数据驱动 / 凭直觉

**情绪风格**：情绪稳定 / 脸皮薄 / 易躁 / 冷淡疏离 / 表面和气 / 阴阳怪气

**手段与操作**：PUA 大师 / 办公室政治玩家 / 卸责艺术家 / 向上管理专家 / 爱讲大道理 / 情感绑架者

#### 企业文化标签库

- **字节范**：坦诚直接，追求 impact，开口先给 context，爱说"对齐"
- **阿里味**：六脉神剑价值观，爱说"赋能""杠杆""生态""闭环"
- **腾讯味**：让数据说话，赛马机制，克制保守，重视用户体验
- **华为味**：奋斗者文化，流程与标准，爱写 PPT 汇报，强调执行力
- **百度味**：技术至上，层级意识强，内部竞争激烈
- **美团味**：极致执行，抠细节，本地化思维
- **第一性原理**：马斯克式，追问本质，拒绝类比，激进简化
- **OKR 狂热者**：凡事先要 O，每个 KR 都要抠
- **大厂流水线**：标准完善但创造力低，依赖 SOP，怕背锅
- **创业型**：资源有限，全栈思维，结果导向，容忍混乱

---

## 确认摘要

收集完成后展示：

```
Info summary:

  👤  {alias}
  🏢  {company} {level} {role} (omit if not provided)
  ⚧   {gender} (omit if not provided)
  🧠  {MBTI} {zodiac} (omit if not provided)
  🏷️   Personality: {tag list} (omit if not provided)
  🏢  Corporate culture: {tag list} (omit if not provided)
  💬  Impression: {impression text} (omit if not provided)

Is this correct? (confirm / edit [field name])
```

用户确认后，进入 Step 2：文件导入。
