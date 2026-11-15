> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/audit.native.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

对原生应用（`ios` / `android` / `adaptive`）运行系统化的**技术**质量检查并生成综合报告。不要修复问题；把问题记录下来，交给其他命令处理。

这是代码级审计，不是设计批评。从源码审计（SwiftUI / UIKit / Compose / React Native / Flutter）；浏览器工具和 `impeccable detect` 都不适用。按平台参照打分：[ios.md](ios.md) / [android.md](android.md)，`adaptive` 两者都要。Setup 没读的话，打分之前先读。报告骨架镜像 [audit.md](audit.md)；改动时保持两者同步。

## 诊断扫描

围绕 5 个维度运行综合检查。按下述标准给每个维度打 0-4 分。

### 1. 可访问性（VoiceOver / TalkBack）

**检查项**：
- **缺少标签**：交互元素没有无障碍标签、traits/role 或状态播报
- **阅读与焦点顺序**：遍历顺序不合逻辑、控件不可达、导航中焦点丢失
- **文本缩放**：固定 pt 尺寸让 Dynamic Type（iOS）失效，或用 px 而非 sp（Android）；大字号下裁切或重叠的布局
- **触控目标**：小于 44 pt（iOS）/ 48 dp（Android），或拥挤无间距
- **无视 Reduce Motion**：视差与大幅滑动没有交叉淡化的替代
- **对比度**：文本在浅色或深色任一外观下不达标

**评分 0-4**：0=屏幕阅读器不可用，1=重大缺口（控件无标签、无缩放），2=部分（标签存在、顺序或缩放出问题），3=良好（小缺口），4=优秀（有标签、有序、缩放干净、Reduce Motion 受到尊重）

### 2. 性能

**检查项**：
- **启动慢**：首帧之前在启动时做重活
- **列表未虚拟化**：长内容没有 FlatList / LazyColumn / List 回收
- **主线程卡顿**：滚动或手势路径中的同步工作，60/120 Hz 掉帧
- **浪费渲染**：不必要的重渲染（React Native）或重组（Compose）；缺少 memoization/keys
- **图片处理**：缩略图解码全尺寸图，没有缓存
- **应用体积**：JS bundle 或二进制臃肿、未使用的依赖

**评分 0-4**：0=处处卡顿，1=重大问题（列表未虚拟化、启动慢），2=部分，3=良好（可小幅改进），4=优秀（启动快、滚动顺、精瘦）

### 3. 外观与主题化

**检查项**：
- **硬编码颜色**：裸 hex 而非语义系统色（iOS）/ Material 颜色角色（Android）/ 设计 token
- **深色外观损坏**：缺少深色变体、深色下对比度差、简单反转
- **Dynamic Color**（Android 12+）：没有静态回退方案，或在合适之处被忽略
- **脱离平台的材质**：在应有系统材质或色调海拔（tonal elevation）之处手搓视觉材质

**评分 0-4**：0=全部硬编码，1=极少 token，2=部分（token 存在、使用不一致），3=良好（少量硬编码值），4=优秀（全程语义化、两种外观都是一等公民）

### 4. 平台符合性（关键）

按已加载的平台参照打分，包括其中的 slop 测试。**检查项**：
- **系统手势损坏**：边缘滑动返回被禁用（iOS）、predictive Back 被劫持（Android）
- **Inset 违例**：内容压到刘海、灵动岛、home indicator、状态栏或键盘之下
- **脱离平台的导航**：自定义全局导航、过载的标签栏、Android 上用 iOS 模式或反之
- **Web 形状的控件**：HTML 式按钮、自制开关、依赖悬停的示能
- **图标漂移**：图标集混用而不是 SF Symbols / Material Symbols
- **系统漂移**：与产品、平台或既有设计系统冲突的反复出现的捷径或装饰模式

**评分 0-4**：0=Web 搬运（毫无原生），1=重度违例（3-4 类），2=有一些（1-2 处明显），3=基本符合（问题轻微），4=完全原生（熟练用户信任每一屏）

### 5. 自适应

**检查项**：
- **手机布局拉伸**：平板/iPad 渲染放大的手机 UI，而不是使用 size classes / window size classes
- **方向损坏**：横屏裁切、被忽略或无理由锁定
- **键盘/IME 处理**：输入框被键盘遮住、没有 inset 调整
- **多任务**：iPad Split View / Android 多窗口破坏布局
- **折叠屏**：姿态变化时布局无感于铰链（Android）

**评分 0-4**：0=只有一种屏幕尺寸，1=重大破版（横屏或平板坏掉），2=部分，3=良好（轻微边界情况），4=优秀（跨尺寸、方向与窗口化自适应）

## 生成报告

### 审计健康分

| # | 维度 | 得分 | 关键发现 |
|---|-----------|-------|-------------|
| 1 | 可访问性 | ? | [最关键的问题或 "--"] |
| 2 | 性能 | ? | |
| 3 | 外观与主题化 | ? | |
| 4 | 平台符合性 | ? | |
| 5 | 自适应 | ? | |
| **总计** | | **??/20** | **[评分档]** |

**评分档**：18-20 优秀（小幅打磨），14-17 良好（补齐弱项维度），10-13 可接受（需要大量工作），6-9 差（需要大改），0-5 危急（根本性问题）

### 平台符合性判定
**从这里开始。** 通过/不通过：读起来是原生应用还是搬运的网站？列出具体违例。要毫不留情地诚实。

### 执行摘要
- 审计健康分：**??/20**（[评分档]）
- 发现问题总数（按严重度计数：P0/P1/P2/P3）
- 前 3-5 个关键问题
- 建议的下一步

### 按严重度排列的详细发现

给每个问题标 **P0-P3 严重度**：
- **P0 阻断**：阻止任务完成。立即修复
- **P1 重大**：显著困难或平台指南违例。发布前修复
- **P2 轻微**：令人恼火、存在变通。下一轮修复
- **P3 打磨**：修了更好，对真实用户无影响。有空再修

每个问题记录：
- **[P?] 问题名**
- **位置**：屏幕、文件、行
- **类别**：可访问性 / 性能 / 主题化 / 符合性 / 自适应
- **影响**：对用户的影响
- **指南**：违反的 HIG / Material 规则（如适用）
- **建议**：如何修复
- **建议命令**：用哪个命令（优先从这些里选：/impeccable adapt、/impeccable animate、/impeccable audit、/impeccable bolder、/impeccable clarify、/impeccable colorize、/impeccable critique、/impeccable delight、/impeccable distill、/impeccable document、/impeccable harden、/impeccable layout、/impeccable onboard、/impeccable optimize、/impeccable overdrive、/impeccable polish、/impeccable quieter、/impeccable shape、/impeccable typeset）

### 模式与系统性问题

指出反复出现、指向系统性缺口而非一次性失误的问题：
- "15+ 个屏幕出现硬编码颜色，应使用语义色"
- "标签栏与列表行全程触控目标低于 44 pt"

### 正面发现

记录做得好的部分：值得保持和复制的实践。

## 建议行动

按优先级列出建议命令（P0 在前，然后 P1、P2）：

1. **[P?] `/command-name`**：简述（来自审计发现的具体上下文）
2. **[P?] `/command-name`**：简述（具体上下文）

**规则**：只能推荐这些命令：/impeccable adapt、/impeccable animate、/impeccable audit、/impeccable bolder、/impeccable clarify、/impeccable colorize、/impeccable critique、/impeccable delight、/impeccable distill、/impeccable document、/impeccable harden、/impeccable layout、/impeccable onboard、/impeccable optimize、/impeccable overdrive、/impeccable polish、/impeccable quieter、/impeccable shape、/impeccable typeset。把发现映射到最合适的命令。若推荐了任何修复，最后以 `/impeccable polish` 收尾。

呈现摘要之后，告诉用户：

> 你可以让我逐条运行这些命令、一次性全部运行，或按你偏好的任意顺序运行。
>
> 修复后重新运行 `/impeccable audit`，就能看到分数提升。

P3 要少：一大串小问题会淹没真正要紧的那些。

**避免**：
- 报告问题却不解释影响（这事为什么重要？）
- 给出泛泛的建议（要具体、可执行）
- 跳过正面发现（做得好的要肯定）
- 忘了排优先级（不可能所有事都是 P0）
- 报告未经核实的误报

## 保存报告

报告交付之后，另存一份让发现活过这次对话：把从得分表到建议行动的部分写入临时文件，然后运行 `.claude/skills/impeccable/scripts/impeccable audit-storage write "<解析后的目标，整个项目则用 .>" <temp-file>` 并删除临时文件。辅助命令会打印写入路径，你用一行提及；`REPORTS OFF:` 表示项目选择不保存，什么都不要提。保存绝不替代交付：用户先在聊天里读到报告。
