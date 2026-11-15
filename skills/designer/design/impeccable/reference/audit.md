> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/impeccable/reference/audit.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

运行系统化的**技术**质量检查并生成综合报告。不要修复问题；把问题记录下来，交给其他命令处理。

这是代码级审计，不是设计批评。检查实现中可测量、可验证的部分。

**仅限 Web。** 原生平台（`ios` / `android` / `adaptive`）改走 [audit.native.md](audit.native.md)；项目是原生的就立即切换过去。

## 诊断扫描

围绕 5 个维度运行综合检查。按下述标准给每个维度打 0-4 分。

### 1. 可访问性（A11y）

**检查项**：
- **对比度问题**：文本对比度 < 4.5:1，大文本 < 3:1（AAA 为 7:1）
- **动效敏感**：`prefers-reduced-motion` 需要有意的替代方案，保留状态变化与层级；标记破坏有用反馈的全局 `0.01ms` 一刀切、超阈值的闪烁，以及阻碍聚焦、阅读或完成任务的动效
- **缺少 ARIA**：交互元素缺少正确的 role、标签或状态
- **键盘导航**：缺少焦点指示器、Tab 顺序混乱、键盘陷阱
- **语义化 HTML**：标题层级不当、缺少 landmark、用 div 代替 button
- **替代文本**：图片描述缺失或低质
- **表单问题**：输入框无标签、错误提示差、缺少必填标识

**评分 0-4**：0=不可访问（不满足 WCAG A），1=重大缺口（几乎没有 ARIA 标签、无键盘导航），2=部分（有一些 a11y 努力、缺口显著），3=良好（基本满足 WCAG AA、有小缺口），4=优秀（完全满足 WCAG AA、接近 AAA）

### 2. 性能

**检查项**：
- **布局抖动**：循环中读写布局属性
- **昂贵动画**：随意动画布局属性、无界的 blur/filter/shadow 效果，或明显掉帧的效果
- **缺少优化**：图片未懒加载、素材未优化
- **will-change 滥用**：`will-change` 大范围应用或静止时仍保留（它是针对已知昂贵动画的定向提示，不是基线要求）
- **包体积**：不必要的导入、未使用的依赖
- **渲染性能**：不必要的重渲染、缺少 memoization

**评分 0-4**：0=严重问题（布局抖动、全无优化），1=重大问题（无懒加载、昂贵动画），2=部分（有一些优化、仍有缺口），3=良好（基本已优化、可小幅改进），4=优秀（快、精、优化到位）

### 3. 主题化

**检查项**：
- **硬编码颜色**：颜色未使用设计 token
- **深色模式损坏**：缺少深色变体、深色主题下对比度差
- **token 不一致**：用错 token、混用 token 类型
- **主题切换问题**：主题切换时值不更新

**评分 0-4**：0=无主题化（全部硬编码），1=极少 token（大多硬编码），2=部分（token 存在但使用不一致），3=良好（token 已用、少量硬编码值），4=优秀（完整 token 体系、深色模式完美工作）

### 4. 响应式设计

**检查项**：
- **固定宽度**：硬编码宽度在移动端破版
- **触控目标**：交互元素小于 44x44px。WCAG AA（SC 2.5.8）要求至少 24x24 CSS px，除非有例外：间距、等效控件、行内文本、用户代理样式或必要尺寸。当以目标包围盒为中心的 24 CSS px 圆不与任何其他目标重叠、也不与任何其他过小目标的圆重叠时，靠间距即可通过
- **触控交互损坏**：自定义滑杆、拖拽面、可滚动控制条的主手势在触屏下失效、吞掉页面滚动或在滚动中丢失拖拽、或手势被打断后卡死。代码特征：只有鼠标事件处理、pointer-event 拖拽面上没有 `touch-action`、取消时没有任何东西清除拖拽状态、捕获丢失或失焦。浏览器工具能合成触控时实际演练该手势（渲染出的视口只能证明布局，证明不了手势），然后说明证据来源（模拟视口、合成触控、哪个引擎、物理设备）与未测部分
- **横向滚动**：窄视口下内容溢出
- **文本缩放**：文本放大时布局破版
- **缺少断点**：没有移动端/平板变体

在声明了 RTL 的页面上，以下各项都是"核实渲染结果"的信号，本身不是缺陷；只在渲染确实错误时标记：
- **物理方向属性**：`margin-left/right`、`padding-left/right`、`text-align: left/right`、`float: left/right`、`border-left/right`，而逻辑等价属性（`margin-inline-start/end`、`padding-inline-start/end`、`text-align: start/end`、`float: inline-start/end`、`border-inline-start/end`）本应可用。形如 `[dir="rtl"] .x { margin-right:1rem }` 的方向限定覆盖，只有在同时清除冲突的基础属性（如 `margin-left: 0`）时才正确；否则两个 margin 都会生效
- **定位元素上的物理定位**：用 `left:` 或 `right:` 而不是 `inset-inline-start` / `inset-inline-end`。注意：`left:50%; transform:translateX(-50%)` 是方向无关的居中模式，在 LTR 和 RTL 下都正确；在那里把 `left` 换成 `inset-inline-start` 反而破坏居中，因为 `translateX` 是物理属性，不会镜像
- **方向性图标与素材**：箭头、chevron、导航图标指向与阅读顺序相反的方向。纯 RTL 页面可能直接交付了画对方向的素材而不带 `[dir="rtl"]` 翻转；核实渲染出的图标，而不是把缺少 `transform: scaleX(-1)` 想当然地当缺陷

**RTL 范围**：只在 `<html>` 或 `<body>` 元素声明了 `dir="rtl"` 的页面上标记物理方向属性。仅有 `lang` 属性不设定方向（浏览器从 `dir` 取方向，从不从 `lang` 取），但带 RTL 文字 `lang`（`ar`、`fa`、`ur`、`ps`、`ckb`、`he`、`yi`、`ug`、`sd`、`dv`）而无显式 `dir` 时，值得记录为信号。

**评分 0-4**：0=仅桌面（移动端破版），1=重大问题（有一些断点、大量失败），2=部分（移动端可用、毛边多），3=良好（响应式、有轻微触控目标或溢出问题），4=优秀（流式、全视口、触控目标正确、手势在触屏下可用）。声明了 RTL 的页面，渲染层面的 RTL 失败遍地时减 1 分

### 5. 实现完整性（关键）

运行随包检测器并逐项在上下文中核实其发现。寻找反复出现的实现捷径、设计系统漂移、误导性或装饰性内容，以及换成无关产品也能成立的结构。确定性发现与视觉判断分开，并指出误报。

**桌面应用**（Electron、NW.js、CEF、WebView2）：以本地 DevTools 端口启动应用（`--remote-debugging-port=9222`，WebView2 用 `WEBVIEW2_ADDITIONAL_BROWSER_ARGUMENTS=--remote-debugging-port=9222`；保持在 127.0.0.1，绝不外露），先种入要审计的状态，让窗口留在屏幕上（隐藏窗口会跳过像素对比读取），然后运行 `.claude/skills/impeccable/scripts/impeccable detect --cdp 9222 --target <页面 URL 或标题的一部分> --json`。它返回与 URL 扫描相同的 JSON，并让窗口保持原样。截屏走 Harness 的 CDP 工具，结束时同样让窗口保持原样。macOS（WKWebView）与 Linux（WebKitGTK）上的 Tauri 不暴露 CDP：扫描源码，并说明渲染检查没有运行。

**评分 0-4**：0=系统性漂移，1=重大反复失败，2=若干已核实问题，3=轻微孤立问题，4=连贯且有意图

## 生成报告

### 审计健康分

| # | 维度 | 得分 | 关键发现 |
|---|-----------|-------|-------------|
| 1 | 可访问性 | ? | [最关键的 a11y 问题或 "--"] |
| 2 | 性能 | ? | |
| 3 | 主题化 | ? | |
| 4 | 响应式设计 | ? | |
| 5 | 实现完整性 | ? | |
| **总计** | | **??/20** | **[评分档]** |

**评分档**：18-20 优秀（小幅打磨），14-17 良好（补齐弱项维度），10-13 可接受（需要大量工作），6-9 差（需要大改），0-5 危急（根本性问题）

### 实现完整性判定
**从这里开始。** 通过/不通过：实现是否表达了一个连贯的、产品专属的系统？引用已核实的证据和检测器发现。

### 执行摘要
- 审计健康分：**??/20**（[评分档]）
- 发现问题总数（按严重度计数：P0/P1/P2/P3）
- 前 3-5 个关键问题
- 建议的下一步

### 按严重度排列的详细发现

给每个问题标 **P0-P3 严重度**：
- **P0 阻断**：阻止任务完成。立即修复
- **P1 重大**：显著困难或 WCAG AA 违例。发布前修复
- **P2 轻微**：令人恼火、存在变通。下一轮修复
- **P3 打磨**：修了更好，对真实用户无影响。有空再修

每个问题记录：
- **[P?] 问题名**
- **位置**：组件、文件、行
- **类别**：可访问性 / 性能 / 主题化 / 响应式 / 实现完整性
- **影响**：对用户的影响
- **WCAG/标准**：违反了哪条标准（如适用）
- **建议**：如何修复
- **建议命令**：用哪个命令（优先从这些里选：/impeccable adapt、/impeccable animate、/impeccable audit、/impeccable bolder、/impeccable clarify、/impeccable colorize、/impeccable critique、/impeccable delight、/impeccable distill、/impeccable document、/impeccable harden、/impeccable layout、/impeccable onboard、/impeccable optimize、/impeccable overdrive、/impeccable polish、/impeccable quieter、/impeccable shape、/impeccable typeset）

### 模式与系统性问题

指出反复出现、指向系统性缺口而非一次性失误的问题：
- "15+ 个组件出现硬编码颜色，应使用设计 token"
- "移动端体验全程触控目标过小（<44px）"

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
