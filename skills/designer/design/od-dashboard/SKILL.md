---
name: dashboard
description: |
  单文件 HTML 的管理 / 分析 dashboard。固定左侧栏，
  顶栏含用户/搜索，主区为 KPI 卡片网格和一两个图表。
  当需求要的是 "dashboard"、"admin"、"analytics" 或
  "control panel" 屏幕时使用。
triggers:
  - "dashboard"
  - "admin panel"
  - "analytics"
  - "control panel"
  - "后台"
  - "管理后台"
od:
  mode: prototype
  platform: desktop
  scenario: operations
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, components]
  craft:
    requires: [state-coverage, accessibility-baseline, laws-of-ux]
---

> **中文汉化版** · 上游：[nexu-io/open-design](https://github.com/nexu-io/open-design) · 原文件：`design-templates/dashboard/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Dashboard Skill

产出单屏的管理 / 分析 dashboard。

## 工作流

1. **阅读当前生效的 DESIGN.md**（已在上方注入）。颜色、字体、间距、
   组件样式全部来自它。不要发明新 token。
2. **分类**这个 dashboard 监控的对象（销售、流量、用量、事故、
   运维等），依据需求简报判断。生成具体、可信的指标名和数值，
   不要"指标 A / 指标 B"这类占位符。
3. **排布**必需的区域：
   - **左侧栏**（220–260px）：顶部放品牌标识，6–8 个带
     图标的导航链接，激活态使用 DS 强调色。
   - **顶栏**：左侧页面标题，右侧搜索输入框 +
     用户头像 / 状态。
   - **主区**：
     - 第 1 行：3–4 张 KPI 卡片（标签 + 大数字 + 对比上期的增量）。
     - 第 2 行：一张主图表（全宽或 2/3），用看起来真实的数字
       画成内联 SVG 的折线 / 柱状 / 面积图。
     - 第 3 行：一张次级图表或表格（最近事件、Top 条目等）。
4. **写**一个自包含的 HTML 文档：
   - 从 `<!doctype html>` 写到 `</html>`，CSS 放在一个内联 `<style>` 块里。
   - 整体布局用 CSS Grid；卡片内部用 Flexbox。
   - 语义化 HTML：`<aside>`、`<header>`、`<main>`、`<section>`。
   - 给每个逻辑区域标上 `data-od-id="slug"`，供评论模式使用。
5. **图表**：只用内联 SVG，不用 JS 库。折线图大约是 10 行
   `<polyline>` 加淡淡的面积填充。柱状图是 N 个 `<rect>`，用
   DS 强调色填充。坐标轴标签从轻（弱化的文字，更小的刻度）。
6. **自检**：
   - 每个颜色都来自 DESIGN.md 的 token。
   - 强调色最多用两次（侧栏激活态 + 一处图表高亮）。
   - 侧栏和顶栏固定（sticky）；主区独立滚动。
   - 密度匹配 DS 的气质——舒展的 DS 留白更多，高密的 DS
     （交易、加密货币类）收紧行距。

## 输出契约

放在 `<artifact>` 标签之间输出：

```
<artifact identifier="dashboard-slug" type="text/html" title="Dashboard Title">
<!doctype html>
<html>...</html>
</artifact>
```

artifact 前面写一句话，artifact 之后什么都不写。
