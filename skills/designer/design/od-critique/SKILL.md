---
name: critique
description: |
  对项目中的任意 HTML 产物运行 5 维度专家设计评审：Philosophy / Visual
  hierarchy / Detail / Functionality / Innovation，每项按 0–10 打分。
  输出一份单文件自包含 HTML 报告，内含雷达图、有证据支撑的评分，以及
  Keep / Fix / Quick-wins 三个清单。当需求中出现 "design review"、
  "design critique"、"5 维度评审"、"design audit" 或 "what's wrong
  with my design" 时使用。
triggers:
  - "critique"
  - "design review"
  - "design audit"
  - "5 维度评审"
  - "5-dim review"
  - "audit my design"
  - "review my deck"
  - "review my landing page"
  - "评审"
  - "复盘"
od:
  mode: prototype
  platform: desktop
  scenario: design
  upstream: "https://github.com/alchaincyf/huashu-design"
  preview:
    type: html
    entry: index.html
  design_system:
    requires: false
  example_prompt: "Run a 5-dimension critique on the magazine-web-ppt deck I just generated — score philosophy / hierarchy / detail / function / innovation, give me Keep / Fix / Quick-wins."
---

> **中文汉化版** · 上游：[nexu-io/open-design](https://github.com/nexu-io/open-design) · 原文件：`design-templates/critique/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Critique Skill · 5 维度专家评审

生成一份单文件 HTML "design review report"，对任意产物按 5 个维度打分并给出可执行的修改建议。借鉴 *huashu-design* 的专家评审流程。

## 何时使用

- 在 Agent（或用户）生成产物（演示文稿 / 原型 / 落地页）之后，用户询问 "what's wrong with this?" 或 "review this" 时
- 作为 Agent 在输出**之前**可对自身产出运行的自检循环
- 用于比较同一设计的两个变体

## 产出内容

一份单文件自包含 `<artifact type="text/html">` 评审报告，包含：

1. **页眉**：评审了哪个产物、日期、评审人（"OD · Critique skill"）、一句话结论
2. **雷达图**（内联 SVG，不依赖库）展示 5 项评分
3. **五张维度卡片**，每张包含：
   - 评分 0–10（附区间：0–4 *Broken* · 5–6 *Functional* · 7–8 *Strong* · 9–10 *Exceptional*）
   - 一段证据文字（引用具体的元素 / 文件 / 行）
   - 一条 Keep / Fix / Quick-win 要点
4. **底部合并的行动清单**：
   - **Keep**：运转正常、不要改动的部分
   - **Fix**：视觉代价高的 P0 / P1 问题
   - **Quick wins**：5–15 分钟即可完成、收益远超投入的调整

## 5 个维度

> 每个维度彼此独立：一份演示文稿可以在 Innovation 上拿 9/10，却在 Hierarchy 上只有 4/10，报告应当直说。不要把有意思的短板平均掉。

### 1. Philosophy consistency · 哲学一致性

> 产物是否选定了一个明确的*方向*，并在每一次微观决策（chrome / kicker / spacing / accent）中始终贯彻？

**需寻找的证据：**
- 是否有一个明确声明的设计方向（例如 Monocle / WIRED / Kinfolk），还是三种风格硬凑在一起？
- chrome / kicker 的用语是否保持同一调性，还是第 3 页写着 "Vol.04 · Spring"、第 7 页却是 "BUT WAIT 🔥"？
- accent / serif / mono 是否全程遵循同一套规则？

**0–4** 三种风格互相打架。**5–6** 有统一方向，但半数元素跑偏。**7–8** 整体连贯，边缘页面偶有偏差。**9–10** 每个元素都在为同一个论点说话。

### 2. Visual hierarchy · 视觉层级

> 一个陌生人能否在无人提示的情况下，看出先读什么、再读什么、最后读什么？

**需寻找的证据：**
- 每一页上最大的字号是否明显对应最重要的内容？
- mono / serif / sans 的分工是否契合信息的*角色*（meta / body / display）？
- 是否有一堆"抢眼"元素互相竞争？还是存在清晰的主 / 次 / 第三层级？

**0–4** 所有元素都在喊。**5–6** 层级在 hero 页成立，到正文就崩。**7–8** 层级清晰，偶有冲突。**9–10** 视线移动毫无阻力。

### 3. Detail execution · 细节执行

> 那 90/10 的细活：对齐、行距、大字号下的字距、图像裁切、页脚 / chrome 的打磨、边界情况下的间距。

**需寻找的证据：**
- 大数字页面：数字是落在基线上，还是悬空？
- 左右两栏顶部在 `grid-2-7-5` 中是否对齐？
- `frame-img` + 图注的比例在各页是否一致？
- mono 标签：字距是否统一？大写规则是否一致？
- 有没有孤立的 `<br>` 造成只有一个字符的行？

**0–4** 胶带和线头都看得见。**5–6** 多数页面干净，1–2 处粗糙。**7–8** 打磨到位，行家能挑出 2–3 处疏漏。**9–10** 达到杂志级水准，手工排印的字体师看了也会点头。

### 4. Functionality · 功能性

> 产物在既定用途上是否真的*能用*？点击热区、导航、演示距离下的可读性、代码块的复制粘贴、以及必要时的移动端回退。

**需寻找的证据：**
- 演示文稿：键盘 / 滚轮 / 触摸导航是否都可用？Iframe 滚动回退呢？
- 落地页：CTA 是否在首屏？电话号码在移动端能否点按？
- 操作手册：代码块可复制、使用 mono 字体、没有智能引号？
- 关键信息在大屏演示时能否从 4m 外看清？

**0–4** 看着还行，却没完成本职任务。**5–6** 主流程可用，边界情况失效。**7–8** 日常使用足够稳健。**9–10** 做了防御式设计，从容应对 iframe / fullscreen / paste / print。

### 5. Innovation · 创新性

> 它是否越过了平庸线？有没有某个元素让人忍不住凑近？

**需寻找的证据：**
- 有没有一处并非必需、却*出人意料*的布局 / 动效 / 字体处理？
- 还是 100% 稳妥，看起来像任何一家代理商都能做的演示文稿 / 落地页？
- 这份创新是*水到渠成*（契合方向），还是生硬嫁接（在 Kinfolk 慢生活风格的演示文稿里硬塞一段 WebGL）？

**0–4** 泛泛的 AI 流水线水准。**5–6** 合格但记不住。**7–8** 有一个记得住的亮点，其余扎实。**9–10** 多处手法让人想直接搬走，但每一处都明显服务于核心论点。

## 评分准则（打分前先读）

- **始终附上证据**："scored 4 because hero page mixes Playfair display with Inter sans on the same line" 胜过 "feels inconsistent"。没有证据支撑的分数不予采纳。
- **不要往上平均**：如果第 3 页有问题导致 Hierarchy 只给 5 分，不要因为第 1、2 页不错就抬到 7 分。分数取*持续处于的最差区间*。
- **不要放水抬分**：7 分意味着*强*，而不是*尚可*。如果每项都在 7 分以上，说明你没在认真做评审。
- **Innovation 可以打低分**：对生产交付物而言，5/10 完全没问题。不要惩罚*恰到好处*的保守。

## 工作流程

### 步骤 1：获取产物

三种模式：

1. **项目文件**：用户说 "review the index.html I just made"，从项目文件夹里打开它。
2. **粘贴的 HTML**：用户在对话里粘贴了代码，从消息中读取。
3. **本轮由你生成**：你刚在上面产出了一个产物，想做自我评审，重新读取你自己的 `<artifact>`。

如果存在多个 HTML 文件，问清楚评审哪一个（不要全部评审）。

### 步骤 2：读够内容再打分

通读整个 `<style>`，再挑 6–8 个有代表性的内容块细读。**不要只看 frontmatter 就打分。** 评分依据的是*已落地*的设计，而非声明的意图。

### 步骤 3：带证据打分

针对 5 个维度中的每一个，写出分数，以及一段 30–80 词、点名具体元素的证据文字。用上行号、类名、页码。

示例：

```
Dimension: Detail execution
Score: 6 / 10
Evidence: Stat-cards on page 3 align cleanly (grid-6, 3×2), but on
page 8 the right column foot sits 2vh higher than the left because
.callout has 3vh top margin while the figure doesn't. Image captions
use mono on page 5 but sans on page 7 — pick one.
```


### 步骤 4：整理行动清单

把 5 段证据汇总成：

- **Keep**（3–5 条）：运转正常、用户在下一轮迭代中务必不要破坏的具体内容。按类 / 页 / 元素引用。
- **Fix**（3–6 条）：必做项，按*每分钟投入所省下的视觉代价*排序。每条 ≤ 1 句。
- **Quick wins**（3–5 条）：每条耗时 5–15 分钟，信噪比高（例如 "swap `display:flex` for `grid` on page 4 to fix the column drift"）。

### 步骤 5：产出报告 HTML

构建单个文件：

- 页眉：产物名称 + 评审人署名 + 日期
- 大幅雷达图（SVG）
- 5 张维度卡片，采用 1 列或 2 列网格
- 底部三个行动清单，带复选框样式

如果存在生效的 DESIGN.md token，就沿用；否则默认用中性浅色主题（米白背景、近黑文字、雷达填充用一种强调色）。

## 输出约定


```
<artifact identifier="critique-<artifact-slug>" type="text/html" title="Critique · <Artifact Title>">
<!doctype html>
<html>...</html>
</artifact>
```


在产物前写一句话（"Reviewed X across 5 dimensions, see report below."），并在 `</artifact>` 之后**立即停止**，不要在对话里复述报告；用户会自行阅读产物。

## 硬性规则

- **每次都要给出 5 项评分**：不允许只做部分报告（例如只评 3 个维度）。
- **每项分数都要有证据**：不许出现 "feels off" / "needs work"。如果无法引用具体元素，这个分数就不成立。
- **不要放水抬分**：总体均值超过 8 就值得怀疑，记得自查。
- **不要在同一轮里评审自己的产物**：用户需要先看到它。仅在明确要求时才做自我评审（"now critique what you just made"）。
- **只用单文件 HTML**：不引入外部 CSS/JS，一切都内联。
- **雷达图必不可少**：它让报告有辨识度，也让用户一眼就能看出薄弱的维度。
