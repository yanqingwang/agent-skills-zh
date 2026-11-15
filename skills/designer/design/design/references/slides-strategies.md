> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/design/references/slides-strategies.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 幻灯片策略

15 种经过验证的演示文稿结构，附情绪曲线。

## 策略选择

| 策略 | 页数 | 目标 | 受众 |
|----------|--------|------|----------|
| YC Seed Deck | 10-12 | 融集种子资金 | 风投机构 |
| Guy Kawasaki | 10 | 20 分钟内完成推介 | 投资人 |
| Series A | 12-15 | 融集 A 轮 | 成长期风投 |
| Product Demo | 5-8 | 展示价值 | 潜在客户 |
| Sales Pitch | 7-10 | 达成交易 | 意向线索 |
| Nancy Duarte Sparkline | 不定 | 转变认知 | 通用 |
| Problem-Solution-Benefit | 3-5 | 快速说服 | 时间紧张者 |
| QBR | 10-15 | 向干系人汇报 | 管理层 |
| Team All-Hands | 8-12 | 对齐团队 | 员工 |
| Conference Talk | 15-25 | 建立思想影响力 | 与会者 |
| Workshop | 20-40 | 传授技能 | 学员 |
| Case Study | 8-12 | 证明价值 | 潜在客户 |
| Competitive Analysis | 6-10 | 战略决策 | 内部 |
| Board Meeting | 15-20 | 向董事会汇报 | 董事 |
| Webinar | 20-30 | 获取线索 | 报名者 |

## 常见结构

### YC Seed Deck（10 页）
1. 标题/钩子
2. 问题
3. 解决方案
4. 增长数据
5. 市场
6. 产品
7. 商业模式
8. 团队
9. 财务
10. 融资诉求

**情绪曲线：**好奇→受挫→希望→信心→信任→紧迫感

### Sales Pitch（9 页）
1. 个性化钩子
2. 对方的问题
3. 不行动的代价
4. 你的解决方案
5. 证明/案例
6. 差异点
7. 定价/ROI
8. 异议处理
9. 行动号召 + 下一步

**情绪曲线：**联结→受挫→恐惧→希望→信任→信心→紧迫感

### Product Demo（6 页）
1. 钩子/问题
2. 方案概览
3. 现场演示/截图
4. 关键特性
5. 收益/定价
6. 行动号召

**情绪曲线：**好奇→受挫→希望→信心→紧迫感

## Duarte Sparkline 模式

在"现状"（What Is，当前的痛点）与"可能"（What Could Be，更好的未来）之间交替：

```
What Is → What Could Be → What Is → What Could Be → New Bliss
(pain)     (hope)         (pain)     (hope)         (resolution)
```

在 1/3 与 2/3 的位置打破节奏，制造参与高峰。

## 搜索命令

```bash
# Find strategy by goal
python ../design-system/scripts/search-slides.py "investor pitch" -d strategy

# Get emotion arc
python ../design-system/scripts/search-slides.py "series a funding" -d strategy --json
```

## 按语境匹配策略

| 语境 | 推荐策略 |
|---------|---------------------|
| 融资 | YC Seed, Series A, Guy Kawasaki |
| 卖产品 | Sales Pitch, Product Demo |
| 内部汇报 | QBR, All-Hands, Board Meeting |
| 公开演讲 | Conference Talk, Workshop |
| 证明价值 | Case Study, Competitive Analysis |
| 获取线索 | Webinar |
