> **中文汉化版** · 上游：[Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) · 原文件：`0-autoresearch-skill/references/progress-reporting.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 进度报告：研究演示

当研究产出值得分享的东西时，做一份有说服力的演示 — 不是状态倾倒，而是一个配有可视化的研究故事。

## 何时报告

由你判断进度是否重要到值得报告。考虑在以下时机报告：

- 一次外循环反思之后，发现了显著的模式
- 优化轨迹显示出清晰且持续的改善
- 一次转向之后 — 解释方向为什么改变
- 就重大决策请求人工介入之前
- 研究收尾、写论文之前

最高频率：每个 /loop tick 或心跳周期一次。最低标准：只要你手上有让人感兴趣的东西。

## 什么是好的研究演示

好的进度报告读起来像一场研究讲座，而不是一条数据库查询。它应该：

1. **讲一个故事**：我们为什么开始、尝试了什么、发现了什么、这意味着什么
2. **展示，而不只是讲述**：包含图表、表格、对比 — 而不只是文字
3. **有取舍**：突出有意思的发现，不要事无巨细地罗列每一次实验
4. **以方向收尾**：接下来会发生什么，为什么

## 推荐章节

按当前研究中真正有说服力的内容来调整。跳过不相关的章节。补上研究所需的章节。

### 1. 研究问题与动机
- 我们在研究什么，它为什么重要？
- 一段话，写给不熟悉这个项目的人看

### 2. 方法
- 我们的方法是什么？我们在优化什么？
- 一句话讲清双循环架构

### 3. 优化轨迹（Karpathy 图）
- X 轴：实验序号或墙钟时间
- Y 轴：代理指标数值
- 用一条水平线显示基线
- 标注显著跃升，以及是什么改动引发的
- 这通常是最有说服力的一张图 — 尽可能总是带上它

### 4. 关键发现
- 2-3 个最重要的结果，附支撑证据
- 包含图表、指标表、对比图
- 解释结果为何重要（WHY），而不只是结果是什么（WHAT）

### 5. 我们尝试过什么（决策地图）
- 对假设树的有取舍的呈现
- 聚焦推理过程：为什么选这个方向，它教会了我们什么
- 成功与有信息量的失败都要有

### 6. 当前理解
- findings.md 的叙述，但要有说服力地呈现
- 对我们看到的模式，最好的解释是什么？

### 7. 下一步
- 计划了哪些实验，为什么
- 还有哪些悬而未决的问题
- 哪些决策需要人工介入

## 优化轨迹图

这是 autoresearch 的标志性视觉元素 — 一张展示指标随实验改进的图表。

最小实现（基于 SVG，无依赖）：

```python
def generate_trajectory_svg(trajectory_data, width=800, height=400):
    """Generate an SVG optimization trajectory chart.

    trajectory_data: list of {"run": int, "metric": float, "label": str}
    """
    if not trajectory_data:
        return "<p>No experiments yet.</p>"

    metrics = [d["metric"] for d in trajectory_data]
    min_m, max_m = min(metrics), max(metrics)
    margin = (max_m - min_m) * 0.1 or 0.1
    y_min, y_max = min_m - margin, max_m + margin

    padding = 60
    plot_w = width - 2 * padding
    plot_h = height - 2 * padding
    n = len(trajectory_data)

    def x_pos(i):
        return padding + (i / max(n - 1, 1)) * plot_w

    def y_pos(v):
        return padding + plot_h - ((v - y_min) / (y_max - y_min)) * plot_h

    # Build SVG
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
    svg += f'<rect width="{width}" height="{height}" fill="#1a1a2e" rx="8"/>'

    # Grid lines
    for i in range(5):
        y = padding + i * plot_h / 4
        val = y_max - i * (y_max - y_min) / 4
        svg += f'<line x1="{padding}" y1="{y}" x2="{width-padding}" y2="{y}" stroke="#333" stroke-dasharray="4"/>'
        svg += f'<text x="{padding-8}" y="{y+4}" fill="#888" text-anchor="end" font-size="11">{val:.3f}</text>'

    # Baseline line
    baseline = trajectory_data[0]["metric"]
    by = y_pos(baseline)
    svg += f'<line x1="{padding}" y1="{by}" x2="{width-padding}" y2="{by}" stroke="#ff6b6b" stroke-dasharray="6" opacity="0.7"/>'
    svg += f'<text x="{width-padding+5}" y="{by+4}" fill="#ff6b6b" font-size="10">baseline</text>'

    # Data line
    points = " ".join(f"{x_pos(i)},{y_pos(d['metric'])}" for i, d in enumerate(trajectory_data))
    svg += f'<polyline points="{points}" fill="none" stroke="#4ecdc4" stroke-width="2"/>'

    # Data points
    for i, d in enumerate(trajectory_data):
        cx, cy = x_pos(i), y_pos(d["metric"])
        svg += f'<circle cx="{cx}" cy="{cy}" r="4" fill="#4ecdc4"/>'

    # Title
    svg += f'<text x="{width/2}" y="24" fill="#eee" text-anchor="middle" font-size="14" font-weight="bold">Optimization Trajectory</text>'
    svg += f'<text x="{width/2}" y="{height-10}" fill="#888" text-anchor="middle" font-size="11">Experiment Run</text>'
    svg += '</svg>'
    return svg
```

把 SVG 输出直接嵌入 HTML 报告。用简短标注标出显著的跃升点。

## HTML 演示模板

以 [templates/progress-presentation.html](../templates/progress-presentation.html) 为起点。它提供了：

- 干净的暗色主题样式，适合研究演示
- 响应式布局
- 与推荐结构相匹配的章节骨架
- 轨迹图的占位

用你的实际研究数据替换占位内容。按研究需要增删或重排章节。模板是脚手架，不是限制。

### Claude Code

生成 HTML，然后展示给人看：

```bash
open to_human/progress-001.html
```

### OpenClaw

生成 PDF 版本。可选方案：
- 用 Python 的 `weasyprint` 把 HTML 转成 PDF
- 用 `matplotlib` 直接把图表生成为 PDF
- 搭一条简单的 markdown → PDF 流水线

在 HEARTBEAT.md 里记下 PDF 路径，让人知道去哪里看。

## 演示质量要点

- **每节一个洞察** — 不要堆叠
- **所有图表都要标注坐标轴与单位**
- **颜色保持一致** — 改进用一种颜色，基线用另一种
- **有意义的地方加上置信区间或误差棒**
- **尽早展示轨迹** — 它是那个让读者相信“这在起作用”的钩子
- **以清晰的下一步收尾** — 让人不用问就知道接下来会发生什么
