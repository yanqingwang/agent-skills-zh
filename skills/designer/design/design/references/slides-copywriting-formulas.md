> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/slides-copywriting-formulas.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 文案公式

25 个用于撰写有说服力的幻灯片文案的公式。

## 核心公式

### PAS（Problem-Agitate-Solution，问题-激化-方案）
**Use:** 问题页、痛点页
**Components:** Problem → Agitate → Solution
**Template:** "[痛点]？每隔[时间段]，[后果]。[解决方案]可以解决这个问题。"

### AIDA（Attention-Interest-Desire-Action，注意-兴趣-欲望-行动）
**Use:** 行动号召（CTA）、收尾页
**Components:** Attention → Interest → Desire → Action
**Template:** "[大胆的论断]。[收益细节]。[社会证明]。[行动号召]。"

### FAB（Features-Advantages-Benefits，功能-优势-收益）
**Use:** 功能页、产品展示页
**Components:** Feature → Advantage → Benefit
**Template:** "[功能]让你能够[优势]，从而获得[收益]。"

### 不作为的代价（Cost of Inaction）
**Use:** 激化页、紧迫感营造
**Components:** Status Quo → Loss → Time Decay
**Template:** "没有[解决方案]，你每[时间段]都在损失[金额]。"

### Before-After-Bridge（之前-之后-桥梁）
**Use:** 转变页、案例研究
**Components:** Before → After → Bridge
**Template:** "[之前的痛点]。[期望达成的状态]。[你的解决方案]就是那座桥。"

## 公式与幻灯片页型的对应

| 幻灯片页型 | 首选公式 | 情绪 |
|------------|-----------------|---------|
| 标题/钩子 | AIDA, Hook | 好奇 |
| 问题 | PAS, Agitate | 沮丧 |
| 成本/风险 | Cost of Inaction | 恐惧 |
| 方案 | FAB, BAB | 希望 |
| 功能 | FAB | 自信 |
| 增长势头 | Proof Stack | 信任 |
| 社会证明 | Testimonial | 信任 |
| 定价 | Value Stack | 自信 |
| 行动号召（CTA） | AIDA, Urgency | 紧迫 |

## 标题句式

### 有力词汇
- "停止[坏事物]"
- "在[时间段]内获得[期望结果]"
- "[行动]的[形容词]方法"
- "为什么[受众]选择[产品]"
- "[数字]种实现[目标]的方法"

### 对比句式
- "[旧方式]已死。来认识[新方式]。"
- "不要[坏做法]。相反，[好做法]。"
- "从[痛点]到[收益]。"

### 社会证明句式
- "[数字]+ 家[用户/公司]信赖[产品]"
- "加入[知名公司]和[知名公司]的行列"
- "曾刊于[出版物]"

## 搜索命令

```bash
# Find formula for slide type
python ../design-system/scripts/search-slides.py "problem agitation" -d copy

# Get emotion-appropriate formula
python ../design-system/scripts/search-slides.py "urgency cta" -d copy
```

## 速查表

| 需求 | 使用公式 |
|------|------------|
| 制造紧迫感 | Cost of Inaction, Scarcity |
| 建立信任 | Social Proof, Testimonial |
| 展示价值 | FAB, Value Stack |
| 驱动行动 | AIDA, CTA |
| 讲故事 | BAB, Story Arc |
| 呈现数据 | Proof Stack |
