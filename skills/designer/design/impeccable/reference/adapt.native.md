> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/adapt.native.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

> **Additional context needed**: 目标平台/设备与使用情境。

把一个既有的 **native** 设计（`ios` / `android` / `adaptive`）适配到另一个情境：另一种设备类别、方向、平台或来源。陷阱是把适配当成缩放。这份工作是为新情境重新构思体验，同时停留在 [ios.md](ios.md) / [android.md](android.md) 的平台惯例之内；如果 Setup 阶段还没有读过目标平台的参考文件，先读再规划。

## 评估适配难度

1. **Source context**: 它原本为谁设计，做了哪些假设？（只考虑手机？只考虑竖屏？只用某个平台的习惯用法？还是一个网站？）
2. **Target context**: 哪种设备类别（手机、平板、折叠屏）、方向、平台与使用姿态（路上单手操作，还是静息双手操作）？
3. **什么会坏掉：** 不适配目标的导航、只会拉伸而不会重构的布局、目标上不存在的手势或控件？

## 适配策略

### 手机 → 平板（iPad / 大屏）

- **重构，不要拉伸。** 放大版手机 UI 出现在平板上就是失败模式。用 size classes（iOS）/ window size classes（Android）切换结构。
- **导航改变形状：** iPad 上 tab bar 保留或变成侧边栏；Android 的 navigation bar 在加宽后变成 rail 或 drawer。
- **利用宽度：** split view / master-detail（列表与详情并排）、多列网格、手机上用 sheet 的地方改用 popover。
- **多任务是尺寸，不是边界情况：** iPad Split View 与 Android 多窗口会把手机宽度的窗口交到平板上；由 size class 驱动的布局两种都免费处理。

### 方向与折叠屏

- 横屏是重构（并排面板、控件重新布位），绝不裁切或加黑边。只有任务真正要求时才锁定方向。
- 折叠屏（Android）：经 window size classes 响应姿态与铰链；在折起、展开、桌面支架三种状态都测试。

### 平台 → 平台（iOS ↔ Android）

翻译习惯用法；绝不移植：

| iOS | Android |
|---|---|
| Tab bar | Navigation bar / rail / drawer |
| Edge-swipe back, back chevron | Predictive Back gesture / button |
| Switch, segmented control, system pickers | Material switch, chips, Material pickers |
| Action sheet | Bottom sheet / Material dialog |
| SF Symbols, SF Pro, Dynamic Type | Material Symbols, Roboto, sp scaling |
| Semantic system colors, materials | Material color roles, tonal elevation |
| System push/sheet transitions | Container transform, shared-axis, fade-through |

在目标的词汇里重建导航与控件；品牌的表达层（配色意图、字体点缀、动效性格）经目标的 theming 系统带过去。

### Web → native（移植网站或 Web 应用）

重新贴合，而不是重排。把 web 导航换成平台的模型，把 HTML 形状的控件换成平台控件，把 hover 交互换成触控优先的，把基于 px 的字体换成 Dynamic Type / sp。然后把结果交给完整的平台参考；那里的 slop 测试就是验收线。

## 实现与验证

- 结构由 **size classes / window size classes** 驱动，绝不基于设备型号判断。
- 在每种新配置下都尊重 safe areas 与 window insets（刘海、铰链、状态栏、键盘）。
- 先在模拟器上测广度，再到真机上求真相：每个交付平台至少一台手机加一台平板，两种方向，支持的则测分屏。

当适配在每个情境里都显得 native 时，交给 `/impeccable polish` 做最后一遍打磨。

**Avoid**:
- 把拉伸的手机布局交付到平板上
- 把一个平台的控件或导航移植到另一个平台
- 在小设备上隐藏核心功能（要紧的功能就让它能用）
- 用锁定方向来绕过一个布局 bug
- 只信模拟器（姿态、手势与性能需要真机）
