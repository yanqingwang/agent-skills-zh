> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/ios.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# iOS 平台

面向原生 iOS / iPadOS 应用：SwiftUI、UIKit、React Native、Expo、Flutter，交付到 Apple 硬件。

在 native 上，访客模式会收窄表现力可以覆盖的范围。HIG 合规在任何模式下都管辖结构、导航与交互；品牌经由平台留出的那一层表达（tint、字体、动效、内容）。

## iOS 腔测试

一个娴熟的 iPhone 用户会信任这个应用，还是会在不合规格的控件前停顿？破绽是"从网站移植过来的"：重新发明的导航栏、自定义的返回手势、web 形状的按钮、依赖 hover 的交互。默认使用平台组件；偏离只为一个用户会感谢你的理由。

## 布局与结构

- **Safe area。** 在 safe-area insets 之内布局。刘海、灵动岛、Home 指示条或圆角之下不放任何控件。
- **系统导航。** 2–5 个顶层分区用 tab bar（分区，不是动作），层级用 navigation stack，自包含任务用 sheet。不要自定义全局导航，不要混合隐喻。
- **边缘滑动返回必须保持可用。** 左缘返回手势是肌肉记忆；绝不禁用或遮挡它。
- **Large titles** 用于顶层屏幕，滚动时收缩为 inline。深层详情屏保持 inline。

## 触控目标

- **44×44 pt 最小值**适用于每个可点按控件，相邻目标之间留出呼吸空间。

## 字体排印

- **Dynamic Type。** 使用系统文本样式（Large Title 到 Caption），让文字跟随用户的阅读字号。不硬编码 point 尺寸。
- **San Francisco 承载 UI。** 正文、标签与控件保持 SF Pro / SF Compact；品牌字体可以出现在展示时刻。
- **下限 11 pt**；Body 为 17 pt。

## 颜色与材质

- **语义化系统颜色**（label、secondaryLabel、systemBackground、separator、tint）。它们自动适配深色模式与增强对比；裸 hex 在那里会坏。
- **Dark Mode 是一等公民。** 两种外观都要设计与测试。
- **一个 tint 色**驱动可交互元素；装饰不是它的职责。
- 栏与 sheet 之后的模糊与半透明用**系统材质**；不要手搓玻璃拟态。

## 组件与控件

- **平台控件。** Switch、segmented control、stepper、系统 picker、action sheet、alert、context menu、swipe actions。为了风味重新发明它们是最常见的 native 腔。
- 图标用 **SF Symbols**：基线对齐、感知 Dynamic Type、有字重与缩放变体。不要混入 web 图标集。
- **有节制的模态。** 聚焦的可关闭子任务用 sheet，沉浸体验用 full-screen cover。清晰的 Cancel/Done；尊重下滑关闭，除非数据丢失需要一道确认。
- 设置形态的内容用 **grouped/inset lists**；不要定制卡片堆叠。

## 动效

- **系统过渡。** push 滑入，sheet 升起，dismiss 反演进入。与导航模型打架的自定义过渡让人失去方向。
- **尊重 Reduce Motion。** 视差与大滑入改为交叉淡变。

## 验证构建

- **截图来自 Simulator，绝不来自浏览器。** 先构建并运行，再用 `xcrun simctl io booted screenshot <path>` 截图（多个模拟器在跑时，把 `booted` 换成 `xcrun simctl list devices booted` 中目标设备的 UDID；显示名会撞，UDID 不会）。覆盖应用交付的每个设备类别，至少一台 iPhone，iPad 是目标时再加一台 iPad，并把文件写到审查流程期待的位置。
- **Dark Mode 与 Dynamic Type 属于这一轮检查。** `xcrun simctl ui booted appearance dark` 翻转外观，多个模拟器在跑时复用截图的 UDID；在一个较大的 Dynamic Type 档位做检查，能抓住固定布局藏起来的截断。
- **模拟器给广度；姿态、手势与性能需要真机。** 说明证据出自哪一个。
