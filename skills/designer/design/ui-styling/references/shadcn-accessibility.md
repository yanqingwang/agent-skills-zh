> **中文汉化版** · 上游：[nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) · 原文件：`.claude/skills/ui-styling/references/shadcn-accessibility.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# shadcn/ui 无障碍模式

ARIA 模式、键盘导航、屏幕阅读器支持与无障碍组件用法。

## 基础：Radix UI 原语

shadcn/ui 构建在 Radix UI 原语之上：无样式、无障碍的组件，遵循 WAI-ARIA 设计模式。

优势：
- 键盘导航开箱即用
- 屏幕阅读器播报
- 焦点管理
- ARIA 属性自动附加
- 已按无障碍标准测试

## 键盘导航

### 焦点管理

**焦点可见状态：**
```tsx
<Button className="focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
  Accessible Button
</Button>
```

**跳转正文：**
```tsx
<a href="#main-content" className="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2">
  Skip to content
</a>

<main id="main-content">
  {/* Content */}
</main>
```

### 对话框/模态框导航

对话框通过 Radix Dialog 原语自动捕获焦点：

```tsx
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog"

<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    {/* Focus trapped here */}
    <input />  {/* Auto-focused */}
    <Button>Action</Button>
    {/* Esc to close, Tab to navigate */}
  </DialogContent>
</Dialog>
```

特性：
- 焦点被限制在对话框内
- Esc 键关闭
- Tab 在可聚焦元素间循环
- 关闭后焦点回到触发器

### 下拉菜单/菜单导航

```tsx
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu"

<DropdownMenu>
  <DropdownMenuTrigger>Open</DropdownMenuTrigger>
  <DropdownMenuContent>
    <DropdownMenuItem>Profile</DropdownMenuItem>
    <DropdownMenuItem>Settings</DropdownMenuItem>
    <DropdownMenuItem>Logout</DropdownMenuItem>
  </DropdownMenuContent>
</DropdownMenu>
```

键盘快捷键：
- `Space/Enter`：打开菜单
- `Arrow Up/Down`：在条目间移动
- `Esc`：关闭菜单
- `Tab`：关闭并移动焦点

### 命令面板导航

```tsx
import { Command } from "@/components/ui/command"

<Command>
  <CommandInput placeholder="Search..." />
  <CommandList>
    <CommandGroup heading="Suggestions">
      <CommandItem>Calendar</CommandItem>
      <CommandItem>Search</CommandItem>
    </CommandGroup>
  </CommandList>
</Command>
```

特性：
- 输入即过滤
- 方向键移动
- Enter 选中
- Esc 关闭

## 屏幕阅读器支持

### 语义化 HTML

使用正确的 HTML 元素：

```tsx
// Good: Semantic HTML
<button>Click me</button>
<nav><a href="/">Home</a></nav>

// Avoid: Div soup
<div onClick={handler}>Click me</div>
```

### ARIA 标签

**为交互元素加标签：**
```tsx
<Button aria-label="Close dialog">
  <X className="h-4 w-4" />
</Button>

<Input aria-label="Email address" type="email" />
```

**描述元素：**
```tsx
<Button aria-describedby="delete-description">
  Delete Account
</Button>
<p id="delete-description" className="sr-only">
  This action permanently deletes your account and cannot be undone
</p>
```

### 仅屏幕阅读器可见的文本

用 `sr-only` 类标记仅屏幕阅读器可见的内容：

```tsx
<Button>
  <Trash className="h-4 w-4" />
  <span className="sr-only">Delete item</span>
</Button>

// CSS for sr-only
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

### 动态区域（Live Regions）

播报动态内容：

```tsx
<div aria-live="polite" aria-atomic="true">
  {message}
</div>

// For urgent updates
<div aria-live="assertive">
  {error}
</div>
```

Toast 组件内置 live region：
```tsx
const { toast } = useToast()

toast({
  title: "Success",
  description: "Profile updated"
})
// Announced to screen readers automatically
```

## 表单无障碍

### 标签与描述

**始终为输入框加标签：**
```tsx
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"

<div>
  <Label htmlFor="email">Email</Label>
  <Input id="email" type="email" />
</div>
```

**添加描述：**
```tsx
import { FormDescription, FormMessage } from "@/components/ui/form"

<FormItem>
  <FormLabel>Username</FormLabel>
  <FormControl>
    <Input {...field} />
  </FormControl>
  <FormDescription>
    Your public display name
  </FormDescription>
  <FormMessage />  {/* Error messages */}
</FormItem>
```

### 错误处理

向屏幕阅读器播报错误：

```tsx
<FormField
  control={form.control}
  name="email"
  render={({ field, fieldState }) => (
    <FormItem>
      <FormLabel>Email</FormLabel>
      <FormControl>
        <Input
          {...field}
          aria-invalid={!!fieldState.error}
          aria-describedby={fieldState.error ? "email-error" : undefined}
        />
      </FormControl>
      <FormMessage id="email-error" />
    </FormItem>
  )}
/>
```

### 必填字段

标明必填字段：

```tsx
<Label htmlFor="name">
  Name <span className="text-destructive">*</span>
  <span className="sr-only">(required)</span>
</Label>
<Input id="name" required />
```

### Fieldset 与 Legend

把相关字段分组：

```tsx
<fieldset>
  <legend className="text-lg font-semibold mb-4">
    Contact Information
  </legend>
  <div className="space-y-4">
    <FormField name="email" />
    <FormField name="phone" />
  </div>
</fieldset>
```

## 组件专属模式

### Accordion

```tsx
import { Accordion } from "@/components/ui/accordion"

<Accordion type="single" collapsible>
  <AccordionItem value="item-1">
    <AccordionTrigger>
      {/* Includes aria-expanded, aria-controls automatically */}
      Is it accessible?
    </AccordionTrigger>
    <AccordionContent>
      {/* Hidden when collapsed, announced when expanded */}
      Yes. Follows WAI-ARIA design pattern.
    </AccordionContent>
  </AccordionItem>
</Accordion>
```

### Tabs

```tsx
import { Tabs } from "@/components/ui/tabs"

<Tabs defaultValue="account">
  <TabsList role="tablist">
    {/* Arrow keys navigate, Space/Enter activates */}
    <TabsTrigger value="account">Account</TabsTrigger>
    <TabsTrigger value="password">Password</TabsTrigger>
  </TabsList>
  <TabsContent value="account">
    {/* Hidden unless selected, aria-labelledby links to trigger */}
    Account content
  </TabsContent>
</Tabs>
```

### Select

```tsx
import { Select } from "@/components/ui/select"

<Select>
  <SelectTrigger aria-label="Choose theme">
    <SelectValue placeholder="Theme" />
  </SelectTrigger>
  <SelectContent>
    {/* Keyboard navigable, announced to screen readers */}
    <SelectItem value="light">Light</SelectItem>
    <SelectItem value="dark">Dark</SelectItem>
  </SelectContent>
</Select>
```

### Checkbox 与 Radio

```tsx
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"

<div className="flex items-center space-x-2">
  <Checkbox id="terms" aria-describedby="terms-description" />
  <Label htmlFor="terms">Accept terms</Label>
</div>
<p id="terms-description" className="text-sm text-muted-foreground">
  You agree to our Terms of Service and Privacy Policy
</p>
```

### Alert

```tsx
import { Alert } from "@/components/ui/alert"

<Alert role="alert">
  {/* Announced immediately to screen readers */}
  <AlertTitle>Error</AlertTitle>
  <AlertDescription>
    Your session has expired
  </AlertDescription>
</Alert>
```

## 颜色对比度

确保文字与背景的对比度足够。

**WCAG 要求：**
- **AA**：普通文本 4.5:1，大号文本 3:1
- **AAA**：普通文本 7:1，大号文本 4.5:1

**检查默认值：**
```tsx
// Good: High contrast
<p className="text-gray-900 dark:text-gray-100">Text</p>

// Avoid: Low contrast
<p className="text-gray-400 dark:text-gray-600">Hard to read</p>
```

**弱化文本：**
```tsx
// Use semantic muted foreground
<p className="text-muted-foreground">
  Secondary text with accessible contrast
</p>
```

## 焦点指示器

始终提供可见的焦点指示器：

**默认焦点环：**
```tsx
<Button className="focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2">
  Button
</Button>
```

**自定义焦点样式：**
```tsx
<a href="#" className="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary focus-visible:underline">
  Link
</a>
```

**不要移除焦点样式：**
```tsx
// Avoid
<button className="focus:outline-none">Bad</button>

// Use focus-visible instead
<button className="focus-visible:ring-2">Good</button>
```

## 动效与动画

尊重"减少动态效果"偏好：

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

在组件中：
```tsx
<div className="transition-all motion-reduce:transition-none">
  Respects user preference
</div>
```

## 测试清单

- [ ] 所有交互元素可键盘操作
- [ ] 焦点指示器可见
- [ ] 屏幕阅读器正确播报所有内容
- [ ] 表单错误已播报并正确关联
- [ ] 颜色对比度达到 WCAG AA
- [ ] 使用了语义化 HTML
- [ ] 纯图标按钮提供 ARIA 标签
- [ ] 模态框/对话框焦点捕获正常
- [ ] 下拉框/选择器可键盘操作
- [ ] 动态区域播报更新
- [ ] 尊重"减少动态效果"偏好
- [ ] 浏览器放大到 200% 仍可用
- [ ] Tab 顺序合理
- [ ] 导航提供跳转链接

## 工具

**测试工具：**
- Lighthouse 无障碍审计
- axe DevTools 浏览器扩展
- NVDA/JAWS 屏幕阅读器
- 纯键盘导航测试
- 颜色对比度检查器（Contrast Ratio、WebAIM）

**自动化测试：**
```bash
npm install -D @axe-core/react
```

```tsx
import { useEffect } from 'react'

if (process.env.NODE_ENV === 'development') {
  import('@axe-core/react').then((axe) => {
    axe.default(React, ReactDOM, 1000)
  })
}
```
