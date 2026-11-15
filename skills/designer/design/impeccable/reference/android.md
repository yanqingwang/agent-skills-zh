> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/android.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Android 平台

面向原生 Android 应用：Jetpack Compose、Android Views、React Native、Expo、Flutter，交付到 Android 硬件。

在 native 上，访客模式会收窄表现力可以覆盖的范围。Material Design 3 在任何模式下都管辖结构、导航与交互；品牌经由 Material 的 theming 表达（color roles、type scale、shape、motion）。一个 Material 用到所有地方、同时交付 iPhone 的跨平台应用，在 iOS 硬件上仍然欠 iOS 它的系统保证：safe-area insets、Reduce Motion、边缘滑动返回。

## Android 腔测试

一个娴熟的 Android 用户会信任这个应用，还是会在不合规格的组件上绊倒？最常见的破绽是一个穿着 Android 皮肤的应用：照抄 iPhone 的纯底部导航、无视系统返回手势的返回箭头、Cupertino 形状的开关与对话框。Material 3 就是规则手册；遵循它的组件，并经它为品牌做主题。

## 布局与结构

- **Material 导航，匹配尺寸。** 窄宽度用 navigation bar（底部，3–5 个目的地）；加宽后用 navigation rail 或 drawer。绝不在平板上原样交付手机的底部栏。
- **系统 Back 永远有效。** 尊重 predictive Back 手势与返回按钮；绝不困住用户或劫持手势。
- **Edge-to-edge 配 window insets。** 应用状态栏、导航栏、屏幕切口与 IME insets，让内容绝不藏在系统栏或键盘后面。
- **顶部应用栏承载屏幕上下文**；屏幕只有一个主操作时，配一颗 FAB。

## 触控目标

- **48×48 dp 最小值**适用于每个触控目标，彼此至少间隔 8 dp。

## 字体排印

- **Material type scale。** Display、Headline、Title、Body、Label 角色（各分 large/medium/small）。文字映射到角色；绝不逐屏手挑字号。
- **Roboto 是系统字体**；品牌字体经 type scale 接入，保持正文、标签与控件的可读与一致。
- **用 sp 单位，绝不用固定 px**，让文字跟随系统的字号设置。

## 颜色与主题

- **Material color roles**（primary、on-primary、surface、surface-variant、secondary-container、outline、error）。角色 token 自动解析明暗与对比变体；裸 hex 在那里会坏。
- **Dynamic Color（Material You）**在合适时使用：在 Android 12+ 上从用户壁纸派生配色方案，并配静态回退。
- **深色主题是一等方案。** 设计并测试它；绝不是一个快速反相。
- **Tonal elevation。** 通过标准表面色调层级表达抬升（必要时加阴影）；不用任意的投影。

## 组件与动效

- **Material 组件。** 按钮（filled / tonal / outlined / text）、FAB、switch、chip、snackbar、bottom sheet、Material dialog、navigation bar/rail/drawer。绝不移植 iOS 控件或发明等价物。
- **一颗 FAB，一个主操作。** 绝不堆叠 FAB，也不把一颗花在次要任务上。
- **短暂反馈用 snackbar**（有用时可带动作，那个场景绝不用 toast）；只有必须打断的决策才用对话框。
- **Material 动效模式。** Container transform、shared-axis、fade-through，配标准缓动与时长；尊重系统"移除动画"设置，改为交叉淡变或瞬时切换。

## 验证构建

- **截图来自模拟器或连接的设备，绝不来自浏览器。** 先构建并安装，再用 `adb exec-out screencap -p > <path>` 截图（多台设备连接时用 `adb -s <serial>` 选定设备）。覆盖应用交付的每个设备类别，至少一台手机，平板是目标时再加一台平板，并把文件写到审查流程期待的位置。
- **深色主题与字号缩放属于这一轮检查。** `adb shell cmd uimode night yes` 翻转主题；`adb shell settings put system font_scale 1.3`（先用 `adb shell cmd uimode night` 与 `adb shell settings get system font_scale` 读取两项设置，之后再恢复）能抓住固定布局藏起来的被裁切标签；多个目标连接时，截图用的 `-s <serial>` 也要加到这些命令上。
- **模拟器给广度；手势、刷新率与性能需要真机。** 说明证据出自哪一个。
