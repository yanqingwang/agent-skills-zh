---
name: ui-styling
description: 借助 shadcn/ui 组件（构建于 Radix UI + Tailwind 之上）、Tailwind CSS 工具类优先（utility-first）样式以及基于 canvas 的视觉设计，创建美观且无障碍的用户界面。当需要构建用户界面、实现设计系统、创建响应式布局、添加无障碍组件（对话框、下拉菜单、表单、表格）、自定义主题与配色、实现深色模式、生成视觉设计与海报，或在多个应用间建立一致的样式模式时使用。
argument-hint: "[component or layout]"
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---

> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/ui-styling/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# UI Styling Skill（UI 样式）

一个综合性 Skill，用于结合 shadcn/ui 组件、Tailwind CSS 工具类样式与基于 canvas 的视觉设计系统，创建美观且无障碍的用户界面。

## 参考资料

- shadcn/ui：https://ui.shadcn.com/llms.txt
- Tailwind CSS：https://tailwindcss.com/docs

## 何时应用本 Skill

适用场景：
- 使用基于 React 的框架（Next.js、Vite、Remix、Astro）构建 UI
- 实现无障碍组件（对话框、表单、表格、导航）
- 采用工具类优先（utility-first）的 CSS 方案进行样式设计
- 创建响应式、移动优先的布局
- 实现深色模式与主题定制
- 构建使用一致 token 的设计系统
- 生成视觉设计、海报或品牌物料
- 借助即时视觉反馈进行快速原型开发
- 添加复杂 UI 模式（数据表格、图表、命令面板）

## 核心技术栈

### 组件层：shadcn/ui
- 借助 Radix UI primitives（原语）提供开箱即用的无障碍组件
- 复制粘贴式分发模式（组件直接存在于你的代码库中）
- TypeScript 优先，具备完整的类型安全
- 可组合的 primitives，支撑复杂 UI
- 基于 CLI 的安装与管理

### 样式层：Tailwind CSS
- 工具类优先（utility-first）的 CSS 框架
- 构建期处理，零运行时开销
- 移动优先的响应式设计
- 一致的设计 token（颜色、间距、字体排印）
- 自动清除无用代码（dead code elimination）

### 视觉设计层：Canvas
- 博物馆级的视觉构图
- 以设计哲学驱动的方法
- 精致的视觉传达
- 极少文字，最大视觉冲击力
- 系统化的模式与精炼的美学

## 脚本路径

本 Skill 及其 `references/` 中的脚本路径均相对于包含本 SKILL.md 的目录，而非相对于项目：`scripts/<file>` 指本 Skill 自己的 `scripts/` 文件夹，`../<skill>/scripts/<file>` 指与之并列安装的同级子 Skill。请从该目录构建完整路径（Skill 加载时 Claude Code 会将其报告为该 Skill 的基准目录），并将工作目录保持在项目根目录——脚本会以项目根为基准读写 `docs/brand-guidelines.md`、`assets/design-tokens.json`、`src/` 等项目文件。

## 快速开始

### 组件 + 样式配置

**安装 shadcn/ui 与 Tailwind：**
```bash
npx shadcn@latest init
```

CLI 会交互式询问框架、TypeScript、路径与主题偏好。此步骤会同时配置 shadcn/ui 和 Tailwind CSS。

**添加组件：**
```bash
npx shadcn@latest add button card dialog form
```

**结合工具类样式使用组件：**
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export function Dashboard() {
  return (
    <div className="container mx-auto p-6 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
      <Card className="hover:shadow-lg transition-shadow">
        <CardHeader>
          <CardTitle className="text-2xl font-bold">Analytics</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-muted-foreground">View your metrics</p>
          <Button variant="default" className="w-full">
            View Details
          </Button>
        </CardContent>
      </Card>
    </div>
  )
}
```

### 替代方案：仅使用 Tailwind 的配置

**Vite 项目：**
```bash
npm install -D tailwindcss @tailwindcss/vite
```

```javascript
// vite.config.ts
import tailwindcss from '@tailwindcss/vite'
export default { plugins: [tailwindcss()] }
```

```css
/* src/index.css */
@import "tailwindcss";
```

## 组件库指南

**全面的组件目录，涵盖使用模式、安装方式与组合示例。**

参见：`references/shadcn-components.md`

涵盖：
- 表单与输入组件（Button、Input、Select、Checkbox、Date Picker、表单校验）
- 布局与导航（Card、Tabs、Accordion、Navigation Menu）
- 浮层与对话框（Dialog、Drawer、Popover、Toast、Command）
- 反馈与状态（Alert、Progress、Skeleton）
- 展示类组件（Table、Data Table、Avatar、Badge）

## 主题与定制

**主题配置、CSS 变量、深色模式实现与组件定制。**

参见：`references/shadcn-theming.md`

涵盖：
- 使用 next-themes 搭建深色模式
- CSS 变量体系
- 颜色定制与配色方案
- 组件变体（variant）定制
- 主题切换的实现

## 无障碍模式

**ARIA 模式、键盘导航、屏幕阅读器支持与无障碍组件的使用。**

参见：`references/shadcn-accessibility.md`

涵盖：
- Radix UI 的无障碍特性
- 键盘导航模式
- 焦点管理
- 屏幕阅读器播报
- 表单校验的无障碍处理

## Tailwind 工具类

**布局、间距、字体排印、颜色、边框与阴影的核心工具类。**

参见：`references/tailwind-utilities.md`

涵盖：
- 布局工具类（Flexbox、Grid、定位）
- 间距体系（padding、margin、gap）
- 字体排印（字号、字重、对齐、行高）
- 颜色与背景
- 边框与阴影
- 用于自定义样式的任意值（arbitrary values）

## 响应式设计

**移动优先断点、响应式工具类与自适应布局。**

参见：`references/tailwind-responsive.md`

涵盖：
- 移动优先的思路
- 断点体系（sm、md、lg、xl、2xl）
- 响应式工具类模式
- 容器查询
- 最大宽度查询
- 自定义断点

## Tailwind 定制

**配置文件结构、自定义工具类、插件与主题扩展。**

参见：`references/tailwind-customization.md`

涵盖：
- 用于自定义 token 的 @theme 指令
- 自定义颜色与字体
- 间距与断点扩展
- 自定义工具类的创建
- 自定义变体（variant）
- 分层组织（@layer base、components、utilities）
- 用于抽取组件的 @apply 指令

## 视觉设计系统

**基于 canvas 的设计哲学、视觉传达原则与精致构图。**

参见：`references/canvas-design-system.md`

涵盖：
- 设计哲学导向的方法
- 视觉传达优先于文字
- 系统化的模式与构图
- 色彩、形态与空间设计
- 极简文字的融入
- 博物馆级的执行水准
- 多页面设计系统

## 实用脚本

**用于组件安装与配置生成的 Python 自动化脚本。**

### shadcn_add.py
添加 shadcn/ui 组件，并自动处理依赖：
```bash
python scripts/shadcn_add.py button card dialog
```

### tailwind_config_gen.py
生成带自定义主题的 tailwind.config.js：
```bash
python scripts/tailwind_config_gen.py --colors brand:blue --fonts display:Inter
```

当同级目录下已存在任何 `tailwind.config.js`、`.cjs`、`.mjs` 或 `.ts` 文件时，生成器会拒绝创建或替换配置。请先查看其报告的现有配置，仅当确认覆盖是有意为之时才传入 `--force`：
```bash
python scripts/tailwind_config_gen.py --colors brand:blue --force
```

## 最佳实践

1. **组件组合**：用简单、可组合的 primitives 构建复杂 UI
2. **工具类优先的样式**：直接使用 Tailwind 类名；只有在真正重复时才抽取组件
3. **移动优先的响应式**：从移动端样式起步，再逐层叠加响应式变体
4. **无障碍优先**：充分利用 Radix UI primitives，添加焦点状态，使用语义化 HTML
5. **设计 token**：使用一致的间距刻度、配色方案与字体排印体系
6. **深色模式一致性**：为所有主题化元素应用 dark 变体
7. **性能**：利用自动 CSS 清除（purging），避免动态类名
8. **TypeScript**：使用完整的类型安全，获得更好的 DX
9. **视觉层级**：让构图引导注意力，有意识地运用间距与色彩
10. **专家级工艺**：每个细节都很重要——把 UI 当作一门手艺来打磨

## 参考导航

**组件库**
- `references/shadcn-components.md` - 完整组件目录
- `references/shadcn-theming.md` - 主题与定制
- `references/shadcn-accessibility.md` - 无障碍模式

**样式体系**
- `references/tailwind-utilities.md` - 核心工具类
- `references/tailwind-responsive.md` - 响应式设计
- `references/tailwind-customization.md` - 配置与扩展

**视觉设计**
- `references/canvas-design-system.md` - 设计哲学与 canvas 工作流

**自动化**
- `scripts/shadcn_add.py` - 组件安装
- `scripts/tailwind_config_gen.py` - 配置生成

## 常见模式

**带校验的表单：**
```tsx
import { useForm } from "react-hook-form"
import { zodResolver } from "@hookform/resolvers/zod"
import * as z from "zod"
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
})

export function LoginForm() {
  const form = useForm({
    resolver: zodResolver(schema),
    defaultValues: { email: "", password: "" }
  })

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(console.log)} className="space-y-6">
        <FormField control={form.control} name="email" render={({ field }) => (
          <FormItem>
            <FormLabel>Email</FormLabel>
            <FormControl>
              <Input type="email" {...field} />
            </FormControl>
            <FormMessage />
          </FormItem>
        )} />
        <Button type="submit" className="w-full">Sign In</Button>
      </form>
    </Form>
  )
}
```

**带深色模式的响应式布局：**
```tsx
<div className="min-h-screen bg-white dark:bg-gray-900">
  <div className="container mx-auto px-4 py-8">
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <Card className="bg-white dark:bg-gray-800 border-gray-200 dark:border-gray-700">
        <CardContent className="p-6">
          <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
            Content
          </h3>
        </CardContent>
      </Card>
    </div>
  </div>
</div>
```

## 资源

- shadcn/ui 文档：https://ui.shadcn.com
- Tailwind CSS 文档：https://tailwindcss.com
- Radix UI：https://radix-ui.com
- Tailwind UI：https://tailwindui.com
- Headless UI：https://headlessui.com
- v0（AI UI 生成器）：https://v0.dev
