---
name: writing-hookify-rules
description: 当用户要求 "create a hookify rule"（创建 hookify 规则）、"write a hook rule"（编写 hook 规则）、"configure hookify"（配置 hookify）、"add a hookify rule"（添加 hookify 规则），或需要 hookify 规则语法与模式方面的指导时，应使用本 Skill。
version: 0.1.0
---

> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/hookify/skills/writing-rules/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 编写 Hookify 规则

## 概述

Hookify 规则是带有 YAML frontmatter 的 markdown 文件，用于定义要监视的模式以及模式匹配时要显示的消息。规则存储在 `.claude/hookify.{rule-name}.local.md` 文件中。

## 规则文件格式

### 基本结构

```markdown
---
name: rule-identifier
enabled: true
event: bash|file|stop|prompt|all
pattern: regex-pattern-here
---

Message to show Claude when this rule triggers.
Can include markdown formatting, warnings, suggestions, etc.
```

### frontmatter 字段

**name**（必填）：规则的唯一标识符
- 使用 kebab-case：`warn-dangerous-rm`、`block-console-log`
- 要有描述性，且面向动作
- 以动词开头：warn、prevent、block、require、check

**enabled**（必填）：用于启用/停用的布尔值
- `true`：规则处于激活状态
- `false`：规则已停用（不会触发）
- 可以直接切换，无需删除规则

**event**（必填）：触发哪种 hook 事件
- `bash`：Bash 工具命令
- `file`：Edit、Write、MultiEdit 工具
- `stop`：当 Agent 想要停止时
- `prompt`：当用户提交提示词时
- `all`：所有事件

**action**（可选）：规则匹配时要执行的动作
- `warn`：显示消息但允许操作（默认）
- `block`：阻止操作（PreToolUse）或停止会话（Stop 事件）
- 若省略，默认为 `warn`

**pattern**（简单格式）：用于匹配的正则表达式模式
- 用于简单的单条件规则
- 针对 command（bash）或 new_text（file）进行匹配
- Python 正则表达式语法

**示例：**
```yaml
event: bash
pattern: rm\s+-rf
```

### 高级格式（多条件）

适用于包含多个条件的复杂规则：

```markdown
---
name: warn-env-file-edits
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$
  - field: new_text
    operator: contains
    pattern: API_KEY
---

You're adding an API key to a .env file. Ensure this file is in .gitignore!
```

**条件字段：**
- `field`：要检查的字段
  - 对于 bash：`command`
  - 对于 file：`file_path`、`new_text`、`old_text`、`content`
- `operator`：如何匹配
  - `regex_match`：正则表达式模式匹配
  - `contains`：子串检查
  - `equals`：精确匹配
  - `not_contains`：子串必须不存在
  - `starts_with`：前缀检查
  - `ends_with`：后缀检查
- `pattern`：要匹配的模式或字符串

**所有条件都必须匹配，规则才会触发。**

## 消息正文

frontmatter 之后的 markdown 内容会在规则触发时显示给 Claude。

**好的消息：**
- 说明检测到了什么
- 说明为什么有问题
- 给出替代方案或最佳实践建议
- 使用格式化提高清晰度（加粗、列表等）

**示例：**
```markdown
⚠️ **Console.log detected!**

You're adding console.log to production code.

**Why this matters:**
- Debug logs shouldn't ship to production
- Console.log can expose sensitive data
- Impacts browser performance

**Alternatives:**
- Use a proper logging library
- Remove before committing
- Use conditional debug builds
```

## 事件类型指南

### bash 事件

匹配 Bash 命令模式：

```markdown
---
event: bash
pattern: sudo\s+|rm\s+-rf|chmod\s+777
---

Dangerous command detected!
```

**常见模式：**
- 危险命令：`rm\s+-rf`、`dd\s+if=`、`mkfs`
- 提权操作：`sudo\s+`、`su\s+`
- 权限问题：`chmod\s+777`、`chown\s+root`

### file 事件

匹配 Edit/Write/MultiEdit 操作：

```markdown
---
event: file
pattern: console\.log\(|eval\(|innerHTML\s*=
---

Potentially problematic code pattern detected!
```

**针对不同字段匹配：**
```markdown
---
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.tsx?$
  - field: new_text
    operator: regex_match
    pattern: console\.log\(
---

Console.log in TypeScript file!
```

**常见模式：**
- 调试代码：`console\.log\(`、`debugger`、`print\(`
- 安全风险：`eval\(`、`innerHTML\s*=`、`dangerouslySetInnerHTML`
- 敏感文件：`\.env$`、`credentials`、`\.pem$`
- 生成文件：`node_modules/`、`dist/`、`build/`

### stop 事件

在 Agent 想要停止时匹配（完成度检查）：

```markdown
---
event: stop
pattern: .*
---

Before stopping, verify:
- [ ] Tests were run
- [ ] Build succeeded
- [ ] Documentation updated
```

**用途：**
- 提醒必需步骤
- 完成度检查清单
- 流程强制执行

### prompt 事件

匹配用户提示词内容（高级）：

```markdown
---
event: prompt
conditions:
  - field: user_prompt
    operator: contains
    pattern: deploy to production
---

Production deployment checklist:
- [ ] Tests passing?
- [ ] Reviewed by team?
- [ ] Monitoring ready?
```

## 模式编写技巧

### 正则表达式基础

**字面字符：** 大多数字符匹配其自身
- `rm` 匹配 "rm"
- `console.log` 匹配 "console.log"

**特殊字符需要转义：**
- `.`（任意字符）→ `\.`（字面点号）
- `(` `)` → `\(` `\)`（字面圆括号）
- `[` `]` → `\[` `\]`（字面方括号）

**常见元字符：**
- `\s` - 空白字符（空格、制表符、换行符）
- `\d` - 数字（0-9）
- `\w` - 单词字符（a-z、A-Z、0-9、_）
- `.` - 任意字符
- `+` - 一个或多个
- `*` - 零个或多个
- `?` - 零个或一个
- `|` - 或

**示例：**
```
rm\s+-rf         Matches: rm -rf, rm  -rf
console\.log\(   Matches: console.log(
(eval|exec)\(    Matches: eval( or exec(
chmod\s+777      Matches: chmod 777, chmod  777
API_KEY\s*=      Matches: API_KEY=, API_KEY =
```

### 测试模式

使用前先测试正则表达式模式：

```bash
python3 -c "import re; print(re.search(r'your_pattern', 'test text'))"
```

或使用在线正则测试器（regex101.com，选择 Python 方言）。

### 常见陷阱

**过于宽泛：**
```yaml
pattern: log    # Matches "log", "login", "dialog", "catalog"
```
更好：`console\.log\(|logger\.`

**过于具体：**
```yaml
pattern: rm -rf /tmp  # Only matches exact path
```
更好：`rm\s+-rf`

**转义问题：**
- YAML 带引号字符串：`"pattern"` 需要双反斜杠 `\\s`
- YAML 不带引号：`pattern: \s` 原样可用
- **建议**：在 YAML 中使用不带引号的模式

## 文件组织

**位置：** 所有规则放在 `.claude/` 目录
**命名：** `.claude/hookify.{descriptive-name}.local.md`
**Gitignore：** 将 `.claude/*.local.md` 加入 `.gitignore`

**好名字：**
- `hookify.dangerous-rm.local.md`
- `hookify.console-log.local.md`
- `hookify.require-tests.local.md`
- `hookify.sensitive-files.local.md`

**坏名字：**
- `hookify.rule1.local.md`（没有描述性）
- `hookify.md`（缺少 .local）
- `danger.local.md`（缺少 hookify 前缀）

## 工作流

### 创建规则

1. 确定不想要的行为
2. 确定涉及哪个工具（Bash、Edit 等）
3. 选择事件类型（bash、file、stop 等）
4. 编写正则表达式模式
5. 在项目根目录创建 `.claude/hookify.{name}.local.md` 文件
6. 立即测试，规则会在下一次工具调用时动态读取

### 调整规则

1. 编辑 `.local.md` 文件
2. 调整模式或消息
3. 立即测试，更改在下一次工具调用时生效

### 停用规则

**临时：** 在 frontmatter 中设置 `enabled: false`
**永久：** 删除 `.local.md` 文件

## 示例

完整示例见 `${CLAUDE_PLUGIN_ROOT}/examples/`：
- `dangerous-rm.local.md` - 阻止危险的 rm 命令
- `console-log-warning.local.md` - 对 console.log 发出警告
- `sensitive-files-warning.local.md` - 对编辑 .env 文件发出警告

## 快速参考

**最小可用规则：**
```markdown
---
name: my-rule
enabled: true
event: bash
pattern: dangerous_command
---

Warning message here
```

**带条件的规则：**
```markdown
---
name: my-rule
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.ts$
  - field: new_text
    operator: contains
    pattern: any
---

Warning message
```

**事件类型：**
- `bash` - Bash 命令
- `file` - 文件编辑
- `stop` - 完成度检查
- `prompt` - 用户输入
- `all` - 所有事件

**字段选项：**
- Bash：`command`
- File：`file_path`、`new_text`、`old_text`、`content`
- Prompt：`user_prompt`

**操作符：**
- `regex_match`、`contains`、`equals`、`not_contains`、`starts_with`、`ends_with`
