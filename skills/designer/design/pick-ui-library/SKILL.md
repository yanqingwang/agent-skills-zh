---
name: pick-ui-library
description: 从一个经过筛选、立场明确的清单里，为给定的前端任务挑对库：数字动画、OTP 输入框、图表、命令菜单、虚拟化、拖拽、toast、状态、样式等等。仅在显式调用时运行，不会自行触发（Only runs when explicitly invoked; it does not trigger on its own）。
disable-model-invocation: true
---

> **中文汉化版** · 上游：[emilkowalski/skills](https://github.com/emilkowalski/skills) · 原文件：`skills/pick-ui-library/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 挑对库

## 初始回应

当本 Skill 首次被调用且没有具体问题时，只回应以下内容：

> 我已准备好为你的任务挑对库，我的推荐来自 Emil Kowalski 的精选清单。

在用户提问之前，不要提供任何其他信息。

这是一个查询型 Skill。被带着任务调用时（"我需要 toast"、"拖拽该用什么？"），把任务匹配到下面的精选清单并推荐对应的库。这些都是深思熟虑、由品味驱动的选择，不要替换成清单之外的备选，除非用户主动要求，或任务确实不在覆盖范围内。

## 使用方法

1. **识别任务**，而不是用户点名的库。"我需要显示一个下拉菜单"是 UI 基础组件任务（base-ui），哪怕他们问的是别的东西。
2. **先检查已安装了什么。** 先看 `package.json`。如果项目已经在用清单里的某个库，就用它。如果用的是竞品（例如 react-window 而不是 Virtuoso），照样给出推荐，但没人要求就不要乱动依赖。
3. **推荐一个库**，用一句话说明它的用途；如果请求本身包含安装/接线，就装好接好。清单有明确答案时，不要摆出一堆可选项。
4. 如果任务不在清单覆盖范围内，明确说出来，并凭自己的知识推荐，但要说清楚你已经离开了精选清单。

## 清单

### UI 组件与基础组件

| 任务 | 库 |
| --- | --- |
| 无样式、无障碍的 UI 组件（对话框、popover、菜单、select 等） | [base-ui](https://base-ui.com) |
| 命令菜单（⌘K 面板） | [cmdk](https://cmdk.paco.me) |
| Toast / 通知 | [Sonner](https://sonner.emilkowal.ski) |
| 一次性密码 / 验证码输入框 | [input-otp](https://input-otp.rodz.dev) |
| 可定制的 GUI / 控制面板 | [Leva](https://github.com/pmndrs/leva)，备选 [dialkit](https://joshpuckett.me/dialkit) |

### 动效与视觉

| 任务 | 库 |
| --- | --- |
| 通用动画（spring、layout 动画、进出场） | [motion](https://motion.dev)（Framer Motion） |
| 数字动画（计数器、价格、统计） | [NumberFlow](https://number-flow.barvian.me) |
| 文本动画组件 | [torph](https://torph.lochie.me/) |
| 3D 地球 | [Cobe](https://cobe.vercel.app) |
| 动态 OG 图片（HTML/CSS → SVG/PNG） | [Satori](https://github.com/vercel/satori) |
| 语法高亮 | [shiki](https://shiki.style) |

需要 spring、layout 动画、退场动画或手势驱动的值时，才用 motion。简单的 hover 或淡入淡出用不着它，普通 CSS transition 才是对的工具。

### 图表

| 任务 | 库 |
| --- | --- |
| 实时 / 流式图表 | [Liveline](https://github.com/benjitaylor/liveline) |
| 通用图表（静态或交互式 dashboard） | [recharts](https://recharts.org) |

分界线：数据点实时到达、图表随时间滚动，用 Liveline。其余一切用 recharts。

### 交互与性能

| 任务 | 库 |
| --- | --- |
| 拖拽 | [dnd kit](https://dndkit.com) |
| 虚拟化（长列表、大表格） | [Virtuoso](https://virtuoso.dev) |

### 状态与样式

| 任务 | 库 |
| --- | --- |
| 状态管理 | [zustand](https://zustand.docs.pmnd.rs) |
| 有条件地拼接 `className` 字符串 | [clsx](https://github.com/lukeed/clsx) |
| Tailwind 的类型安全、变体驱动样式 | [cva](https://cva.style) |
| 主题切换 / 暗色模式（加载时不闪烁） | [next-themes](https://github.com/pacocoursey/next-themes) |

样式上的分界：clsx 用于临时性的条件类名；cva 用于组件有真正的变体（尺寸、意图、状态）、值得一个类型化 API 的情况。两者可以组合使用，cva 内部就接受 clsx 风格的输入。

## 要留意的常见错配

- **手写 toast 或用 modal 库拼 toast** → Sonner 就是为这个而生的。
- **基于 `<div>` 的下拉菜单/对话框，靠手动处理焦点** → 用 base-ui，它负责无障碍、焦点圈定和关闭。
- **靠重渲染文本做数字动画** → NumberFlow 能正确处理数字位的过渡。
- **直接渲染上千行的列表** → 先用 Virtuoso，别急着上分页之类的权宜之计。
- **每个组件一个 `useState`、靠 props 结网传递共享状态** → 用 zustand。
- **模板字符串 className 里三层嵌套的三元表达式** → 用 clsx（如果是变体形状就用 cva）。
