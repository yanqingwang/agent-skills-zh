> **中文汉化版** · 上游：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) · 原文件：`skills/obsidian-bases/references/FUNCTIONS_REFERENCE.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 函数参考

## 全局函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `date()` | `date(string): date` | 把字符串解析为日期。格式：`YYYY-MM-DD HH:mm:ss` |
| `duration()` | `duration(string): duration` | 解析时长字符串 |
| `now()` | `now(): date` | 当前日期和时间 |
| `today()` | `today(): date` | 当前日期（时间为 00:00:00） |
| `if()` | `if(condition, trueResult, falseResult?)` | 条件判断 |
| `min()` | `min(n1, n2, ...): number` | 最小数 |
| `max()` | `max(n1, n2, ...): number` | 最大数 |
| `number()` | `number(any): number` | 转换为数字 |
| `link()` | `link(path, display?): Link` | 创建链接 |
| `list()` | `list(element): List` | 不是列表时包装为列表 |
| `file()` | `file(path): file` | 获取文件对象 |
| `image()` | `image(path): image` | 创建用于渲染的图像 |
| `icon()` | `icon(name): icon` | 按名称获取 Lucide 图标 |
| `html()` | `html(string): html` | 渲染为 HTML |
| `escapeHTML()` | `escapeHTML(string): string` | 转义 HTML 字符 |

## 任意类型函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `isTruthy()` | `any.isTruthy(): boolean` | 强制转换为布尔值 |
| `isType()` | `any.isType(type): boolean` | 检查类型 |
| `toString()` | `any.toString(): string` | 转换为字符串 |

## 日期函数与字段

**字段：**`date.year`、`date.month`、`date.day`、`date.hour`、`date.minute`、`date.second`、`date.millisecond`

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `date()` | `date.date(): date` | 去除时间部分 |
| `format()` | `date.format(string): string` | 按 Moment.js 模式格式化 |
| `time()` | `date.time(): string` | 以字符串形式获取时间 |
| `relative()` | `date.relative(): string` | 人类可读的相对时间 |
| `isEmpty()` | `date.isEmpty(): boolean` | 对日期始终为 false |

## Duration 类型

两个日期相减，结果是 **Duration** 类型（不是数字）。Duration 有自己的属性和方法。

**Duration 字段：**
| 字段 | 类型 | 说明 |
|-------|------|-------------|
| `duration.days` | 数字 | 时长内的总天数 |
| `duration.hours` | 数字 | 时长内的总小时数 |
| `duration.minutes` | 数字 | 时长内的总分钟数 |
| `duration.seconds` | 数字 | 时长内的总秒数 |
| `duration.milliseconds` | 数字 | 时长内的总毫秒数 |

**重要：**Duration 不直接支持 `.round()`、`.floor()`、`.ceil()`。必须先取数值字段（如 `.days`），再套用数字函数。

```yaml
# CORRECT: Calculate days between dates
"(date(due_date) - today()).days"                    # Returns number of days
"(now() - file.ctime).days"                          # Days since created

# CORRECT: Round the numeric result if needed
"(date(due_date) - today()).days.round(0)"           # Rounded days
"(now() - file.ctime).hours.round(0)"                # Rounded hours

# WRONG - will cause error:
# "((date(due) - today()) / 86400000).round(0)"      # Duration doesn't support division then round
```

## 日期算术

```yaml
# Duration units: y/year/years, M/month/months, d/day/days,
#                 w/week/weeks, h/hour/hours, m/minute/minutes, s/second/seconds

# Add/subtract durations
"date + \"1M\""           # Add 1 month
"date - \"2h\""           # Subtract 2 hours
"now() + \"1 day\""       # Tomorrow
"today() + \"7d\""        # A week from today

# Subtract dates returns Duration type
"now() - file.ctime"                    # Returns Duration
"(now() - file.ctime).days"             # Get days as number
"(now() - file.ctime).hours"            # Get hours as number

# Complex duration arithmetic
"now() + (duration('1d') * 2)"
```

## 字符串函数

**字段：**`string.length`

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `contains()` | `string.contains(value): boolean` | 是否包含子串 |
| `containsAll()` | `string.containsAll(...values): boolean` | 所有子串都存在 |
| `containsAny()` | `string.containsAny(...values): boolean` | 任一子串存在 |
| `startsWith()` | `string.startsWith(query): boolean` | 以 query 开头 |
| `endsWith()` | `string.endsWith(query): boolean` | 以 query 结尾 |
| `isEmpty()` | `string.isEmpty(): boolean` | 为空或不存在 |
| `lower()` | `string.lower(): string` | 转为小写 |
| `title()` | `string.title(): string` | 转为标题式大小写 |
| `trim()` | `string.trim(): string` | 去除空白字符 |
| `replace()` | `string.replace(pattern, replacement): string` | 替换匹配模式 |
| `repeat()` | `string.repeat(count): string` | 重复字符串 |
| `reverse()` | `string.reverse(): string` | 反转字符串 |
| `slice()` | `string.slice(start, end?): string` | 取子串 |
| `split()` | `string.split(separator, n?): list` | 拆分为列表 |

## 数字函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `abs()` | `number.abs(): number` | 绝对值 |
| `ceil()` | `number.ceil(): number` | 向上取整 |
| `floor()` | `number.floor(): number` | 向下取整 |
| `round()` | `number.round(digits?): number` | 按指定位数四舍五入 |
| `toFixed()` | `number.toFixed(precision): string` | 定点表示法 |
| `isEmpty()` | `number.isEmpty(): boolean` | 不存在 |

## 列表函数

**字段：**`list.length`

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `contains()` | `list.contains(value): boolean` | 元素存在 |
| `containsAll()` | `list.containsAll(...values): boolean` | 所有元素都存在 |
| `containsAny()` | `list.containsAny(...values): boolean` | 任一元素存在 |
| `filter()` | `list.filter(expression): list` | 按条件过滤（使用 `value`、`index`） |
| `map()` | `list.map(expression): list` | 转换元素（使用 `value`、`index`） |
| `reduce()` | `list.reduce(expression, initial): any` | 归约为单个值（使用 `value`、`index`、`acc`） |
| `flat()` | `list.flat(): list` | 展平嵌套列表 |
| `join()` | `list.join(separator): string` | 拼接为字符串 |
| `reverse()` | `list.reverse(): list` | 反转顺序 |
| `slice()` | `list.slice(start, end?): list` | 取子列表 |
| `sort()` | `list.sort(): list` | 升序排序 |
| `unique()` | `list.unique(): list` | 去除重复项 |
| `isEmpty()` | `list.isEmpty(): boolean` | 无元素 |

## 文件函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `asLink()` | `file.asLink(display?): Link` | 转换为链接 |
| `hasLink()` | `file.hasLink(otherFile): boolean` | 是否有指向文件的链接 |
| `hasTag()` | `file.hasTag(...tags): boolean` | 是否带有任一标签 |
| `hasProperty()` | `file.hasProperty(name): boolean` | 是否含有属性 |
| `inFolder()` | `file.inFolder(folder): boolean` | 位于文件夹或子文件夹中 |

## 链接函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `asFile()` | `link.asFile(): file` | 获取文件对象 |
| `linksTo()` | `link.linksTo(file): boolean` | 是否链接到该文件 |

## 对象函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `isEmpty()` | `object.isEmpty(): boolean` | 无属性 |
| `keys()` | `object.keys(): list` | 键的列表 |
| `values()` | `object.values(): list` | 值的列表 |

## 正则表达式函数

| 函数 | 签名 | 说明 |
|----------|-----------|-------------|
| `matches()` | `regexp.matches(string): boolean` | 测试是否匹配 |
