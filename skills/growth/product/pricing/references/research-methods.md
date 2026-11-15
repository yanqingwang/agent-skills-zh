> **中文汉化版** · 上游：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) · 原文件：`skills/pricing/references/research-methods.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 定价研究方法

## 目录
- Van Westendorp 价格敏感度测试（四个问题、如何分析、调研技巧、示例输出）
- MaxDiff 分析（工作原理、示例调研问题、结果分析、用 MaxDiff 做包装定价）
- 支付意愿调研
- 使用量-价值相关性分析

## Van Westendorp 价格敏感度测试

Van Westendorp 调研用于找出你的产品可接受的价格区间。

### 四个问题

向每位受访者提问：
1. "在什么价格下，你会认为 [产品] 贵到你根本不会考虑购买？"（太贵）
2. "在什么价格下，你会认为 [产品] 便宜到让你怀疑它的质量？"（太便宜）
3. "在什么价格下，你会认为 [产品] 开始有点贵，但你仍可能考虑？"（贵/偏高一侧）
4. "在什么价格下，你会认为 [产品] 划算，是物有所值的好买卖？"（便宜/划算）

### 如何分析

1. 校验响应：统一货币、计费周期和产品描述。标记缺失值、非数值，或阈值排序不一致（`too cheap ≤ cheap ≤ expensive ≤ too expensive`）的情况；记录每一例排除项，不要悄悄改答案。
2. 以候选价格作为 x 轴、受访者占比作为 y 轴绘图。两条便宜曲线随价格上升而下降；两条贵曲线随价格上升而上升。在每个候选价格 `p` 上，按下表取值：

   | 曲线 | 要绘制的占比 | 方向 |
   |-------|---------------|-----------|
   | 太便宜 | 太便宜阈值大于等于 `p` 的受访者 | 递减 |
   | 便宜 / 划算 | 便宜阈值大于等于 `p` 的受访者 | 递减 |
   | 贵 | 贵阈值小于等于 `p` 的受访者 | 递增 |
   | 太贵 | 太贵阈值小于等于 `p` 的受访者 | 递增 |

   对并列值采用一致的端点约定并记录下来。不要对四个问题都套用递增的累积分布：那会反转便宜曲线的含义。[Sawtooth 的示例](https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter)展示了太便宜占比随价格上升而下降的情况。
3. 找出交点：
   - **边际廉价点（PMC）：** "太便宜"与"贵"相交
   - **边际昂贵点（PME）：** "太贵"与"便宜"相交
   - **最优价格点（OPP）：** "太便宜"与"太贵"相交
   - **无差异价格点（IDP）：** "贵"与"便宜"相交

**可接受价格区间：** PMC 到 PME
**值得测试的候选价：** OPP 和 IDP 可以帮助缩小候选清单，但它们并不能划定经济学意义上的最优区间。

这四个问题衡量的是价格感知，不是购买概率。在预测需求之前，先做补充的购买意向研究（比如 Newton-Miller-Smith 扩展，并明确其假设前提）、选择实验（choice study）或真实的价格测试。比较收入、毛利和留存；可接受价格更高并不意味着需求不变。参见 [Sawtooth 对该方法及其局限的说明](https://sawtoothsoftware.com/resources/blog/posts/van-westendorp-pricing-sensitivity-meter)。

### 调研技巧
- 需要受访者 100-300 人才能得到可靠数据
- 按用户画像分层（支付意愿不同）
- 使用贴近真实的产品描述
- 考虑加入购买意向问题

### 示例输出

```
Price Sensitivity Analysis Results:
─────────────────────────────────
Point of Marginal Cheapness:  $29/mo
Optimal Price Point:          $49/mo
Indifference Price Point:     $59/mo
Point of Marginal Expensiveness: $79/mo

Candidate test prices: $49 and $59/mo
Current price: $39/mo
Price changes: +25.6% and +51.3%
Demand, conversion and churn impact: not measured by these four questions
Next step: validate purchase behavior and unit economics before rollout
```

---

## MaxDiff 分析（Best-Worst Scaling）

MaxDiff 用于找出客户最看重哪些功能，为包装定价（packaging）决策提供依据。

### 工作原理

1. 列出你可以提供的 8-15 项功能
2. 每次向受访者展示 4-5 项功能
3. 提问："哪一项最重要？哪一项最不重要？"
4. 在多组题目中重复，直到所有功能都被两两比较过
5. 统计分析产出重要性得分

### 示例调研问题

```
Which feature is MOST important to you?
Which feature is LEAST important to you?

□ Unlimited projects
□ Custom branding
□ Priority support
□ API access
□ Advanced analytics
```

### 结果分析

功能按效用得分排序：
- 高效用 = 必备项（放进基础档）
- 中等效用 = 差异化项（用于拉开档位差距）
- 低效用 = 锦上添花项（放进高级档，或砍掉）

### 用 MaxDiff 做包装定价

| 效用得分 | 包装定价决策 |
|---------------|-------------------|
| 前 20% | 所有档位都含（table stakes） |
| 20-50% | 用于拉开档位差异 |
| 50-80% | 仅更高档位提供 |
| 后 20% | 考虑砍掉，或作为高级附加项 |

---

## 支付意愿调研

**直接法（简单但有偏差）：**
"你愿意为 [产品] 付多少钱？"

**更好：Gabor-Granger 方法：**
"在 [$X] 的价位上，你会购买 [产品] 吗？"（是/否）
在不同受访者之间变化价格，绘制需求曲线。

**更好：联合分析（Conjoint analysis）：**
展示不同价格下的产品组合
由受访者选择偏好选项
统计分析揭示每个功能的价格敏感度

---

## 使用量-价值相关性分析

### 1. 埋点采集使用数据
追踪客户如何使用你的产品：
- 功能使用频率
- 体量指标（用户数、记录数、API 调用量）
- 结果指标（带来的收入、节省的时间）

### 2. 与客户成功做相关分析
- 哪些使用模式能预测留存？
- 哪些使用模式能预测扩张？
- 哪些客户付得最多，为什么？

### 3. 识别价值阈值
- 使用量到什么程度，客户才算"上手了"？
- 使用量到什么程度，他们会扩张？
- 使用量到什么程度，应该提价？

### 示例分析

```
Usage-Value Correlation Analysis:
─────────────────────────────────
Segment: High-LTV customers (>$10k ARR)
Average monthly active users: 15
Average projects: 8
Average integrations: 4

Segment: Churned customers
Average monthly active users: 3
Average projects: 2
Average integrations: 0

Insight: Value correlates with team adoption (users)
        and depth of use (integrations)

Recommendation: Price per user, gate integrations to higher tiers
```
