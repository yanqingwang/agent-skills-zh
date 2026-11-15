> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/ui-styling/references/shadcn-theming.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# shadcn/ui 主题与定制

主题配置、CSS 变量、暗色模式与组件定制。

## 暗色模式设置

### Next.js App Router

**1. 安装 next-themes：**
```bash
npm install next-themes
```

**2. 创建 theme provider：**
```tsx
// components/theme-provider.tsx
"use client"

import * as React from "react"
import { ThemeProvider as NextThemesProvider } from "next-themes"

export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>
}
```

**3. 包裹应用：**
```tsx
// app/layout.tsx
import { ThemeProvider } from "@/components/theme-provider"

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

**4. 主题切换组件：**
```tsx
import { Moon, Sun } from "lucide-react"
import { useTheme } from "next-themes"
import { Button } from "@/components/ui/button"

export function ThemeToggle() {
  const { setTheme, theme } = useTheme()

  return (
    <Button
      variant="ghost"
      size="icon"
      onClick={() => setTheme(theme === "light" ? "dark" : "light")}
    >
      <Sun className="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
      <Moon className="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
      <span className="sr-only">Toggle theme</span>
    </Button>
  )
}
```

### Vite / 其他框架

使用类似的方式，配合 next-themes 或自行实现：

```javascript
// Store preference
function toggleDarkMode() {
  const isDark = document.documentElement.classList.toggle('dark')
  localStorage.setItem('theme', isDark ? 'dark' : 'light')
}

// Initialize on load
if (localStorage.theme === 'dark' ||
    (!('theme' in localStorage) &&
     window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark')
}
```

## CSS 变量体系

shadcn/ui 使用 CSS 变量做主题。变量定义在 `globals.css` 中：

```css
@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 222.2 84% 4.9%;
    --primary: 222.2 47.4% 11.2%;
    --primary-foreground: 210 40% 98%;
    --secondary: 210 40% 96.1%;
    --secondary-foreground: 222.2 47.4% 11.2%;
    --muted: 210 40% 96.1%;
    --muted-foreground: 215.4 16.3% 46.9%;
    --accent: 210 40% 96.1%;
    --accent-foreground: 222.2 47.4% 11.2%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 40% 98%;
    --border: 214.3 31.8% 91.4%;
    --input: 214.3 31.8% 91.4%;
    --ring: 222.2 84% 4.9%;
    --radius: 0.5rem;
  }

  .dark {
    --background: 222.2 84% 4.9%;
    --foreground: 210 40% 98%;
    --primary: 210 40% 98%;
    --primary-foreground: 222.2 47.4% 11.2%;
    --secondary: 217.2 32.6% 17.5%;
    --secondary-foreground: 210 40% 98%;
    --muted: 217.2 32.6% 17.5%;
    --muted-foreground: 215 20.2% 65.1%;
    --accent: 217.2 32.6% 17.5%;
    --accent-foreground: 210 40% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 40% 98%;
    --border: 217.2 32.6% 17.5%;
    --input: 217.2 32.6% 17.5%;
    --ring: 212.7 26.8% 83.9%;
  }
}
```

### 颜色格式

取值使用不带 `hsl()` 包装的 HSL 格式，便于更细的透明度控制：
```css
--primary: 222.2 47.4% 11.2%;  /* H S L */
```

在 Tailwind 中的用法：
```css
background: hsl(var(--primary));
background: hsl(var(--primary) / 0.5);  /* 50% opacity */
```

## Tailwind 配置

把 CSS 变量映射到 Tailwind 工具类：

```ts
// tailwind.config.ts
export default {
  darkMode: ["class"],
  theme: {
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
}
```

## 颜色定制

### 方法 1：更新 CSS 变量

在 `globals.css` 中修改 CSS 变量来调整颜色：

```css
:root {
  --primary: 262.1 83.3% 57.8%;  /* Purple */
  --primary-foreground: 210 20% 98%;
}

.dark {
  --primary: 263.4 70% 50.4%;  /* Darker purple */
  --primary-foreground: 210 20% 98%;
}
```

### 方法 2：主题生成器

使用 shadcn/ui 主题生成器：https://ui.shadcn.com/themes

选择基色，生成主题，复制 CSS 变量。

### 方法 3：多主题

用 data 属性创建主题变体：

```css
[data-theme="violet"] {
  --primary: 262.1 83.3% 57.8%;
  --primary-foreground: 210 20% 98%;
}

[data-theme="rose"] {
  --primary: 346.8 77.2% 49.8%;
  --primary-foreground: 355.7 100% 97.3%;
}
```

应用主题：
```tsx
<div data-theme="violet">
  <Button>Violet theme</Button>
</div>
```

## 组件定制

组件就在你的代码库里，直接修改即可。

### 定制变体

```tsx
// components/ui/button.tsx
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground",
        destructive: "bg-destructive text-destructive-foreground",
        outline: "border border-input bg-background",
        // Add custom variant
        gradient: "bg-gradient-to-r from-purple-500 to-pink-500 text-white",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        // Add custom size
        xl: "h-14 rounded-md px-10 text-lg",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)
```

用法：
```tsx
<Button variant="gradient" size="xl">Custom Button</Button>
```

### 定制样式

直接修改组件中的基础样式：

```tsx
// components/ui/card.tsx
const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow-lg",  // Modified
      className
    )}
    {...props}
  />
))
```

### 用 className 覆盖

传入额外的类来覆盖：

```tsx
<Card className="border-2 border-purple-500 shadow-2xl hover:scale-105 transition-transform">
  Custom styled card
</Card>
```

## 基础色预设

shadcn/ui 在 `init` 时提供基础色预设：

- **Slate**：冷灰调
- **Gray**：中性灰
- **Zinc**：暖灰
- **Neutral**：均衡灰
- **Stone**：大地灰

在初始化时选择，或之后更新 CSS 变量来更改。

## 风格变体

有两种组件风格可选：

- **Default**：更柔和、更圆润
- **New York**：更锐利、对比更强

在 `init` 时或在 `components.json` 中选择：

```json
{
  "style": "new-york",
  "tailwind": {
    "cssVariables": true
  }
}
```

## 圆角定制

全局控制圆角：

```css
:root {
  --radius: 0.5rem;  /* Default */
  --radius: 0rem;    /* Sharp corners */
  --radius: 1rem;    /* Rounded */
}
```

组件使用 radius 变量：
```tsx
className="rounded-lg"  /* Uses var(--radius) */
```

## 最佳实践

1. **使用 CSS 变量**：支持运行时切换主题
2. **前景色保持一致**：每种颜色都搭配恰当的前景色
3. **两种主题都测**：在亮色与暗色模式下验证组件
4. **语义化命名**：用 `destructive` 而非 `red`，用 `muted` 而非 `gray`
5. **可访问性**：保持足够的颜色对比（至少 WCAG AA）
6. **组件级覆盖**：一次性定制用 `className` prop
7. **提取模式**：为反复出现的定制创建自定义变体
