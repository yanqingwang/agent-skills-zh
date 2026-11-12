> **中文汉化版** · 上游：[obra/superpowers](https://github.com/obra/superpowers) · 原文件：`skills/systematic-debugging/defense-in-depth.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 纵深防御式校验

## 概述

修一个由无效数据引起的 bug 时，在一处加上校验就觉得够了。但这一处检查会被不同的代码路径、重构或 mock 绕过。

**核心原则：** 在数据经过的每一层都做校验。让这个 bug 在结构上不可能发生。

## 为什么要多层

单点校验："我们修好了这个 bug"
多层校验："我们让这个 bug 不可能发生"

不同的层抓住不同的情况：
- 入口校验抓住大多数 bug
- 业务逻辑抓住边界情况
- 环境守卫防止特定上下文里的危险操作
- 调试日志在其他层都失效时派上用场

## 四个层

### 第 1 层：入口点校验
**目的：** 在 API 边界拒绝明显无效的输入

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory cannot be empty');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory does not exist: ${workingDirectory}`);
  }
  if (!statSync(workingDirectory).isDirectory()) {
    throw new Error(`workingDirectory is not a directory: ${workingDirectory}`);
  }
  // ... proceed
}
```

### 第 2 层：业务逻辑校验
**目的：** 确保数据对这个操作来说说得通

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('projectDir required for workspace initialization');
  }
  // ... proceed
}
```

### 第 3 层：环境守卫
**目的：** 在特定上下文中阻止危险操作

```typescript
async function gitInit(directory: string) {
  // In tests, refuse git init outside temp directories
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `Refusing git init outside temp dir during tests: ${directory}`
      );
    }
  }
  // ... proceed
}
```

### 第 4 层：调试埋点
**目的：** 捕获上下文，供事后取证

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('About to git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  // ... proceed
}
```

## 套用这个模式

找到一个 bug 之后：

1. **追踪数据流** - 坏值从哪里产生？在哪里被使用？
2. **列出所有检查点** - 把数据经过的每个点都列出来
3. **在每一层加校验** - 入口、业务、环境、调试
4. **测试每一层** - 试着绕过第 1 层，验证第 2 层能接住

## 来自调试会话的例子

Bug：空的 `projectDir` 导致 `git init` 跑进了源代码目录

**数据流：**
1. 测试 setup → 空字符串
2. `Project.create(name, '')`
3. `WorkspaceManager.createWorkspace('')`
4. `git init` 运行在 `process.cwd()`

**加上的四层：**
- 第 1 层：`Project.create()` 校验非空/存在/可写
- 第 2 层：`WorkspaceManager` 校验 projectDir 非空
- 第 3 层：`WorktreeManager` 在测试中拒绝 tmpdir 之外的 git init
- 第 4 层：git init 之前记录堆栈跟踪日志

**结果：** 1847 个测试全部通过，这个 bug 再也无法复现

## 关键认识

四层全都有必要。测试过程中，每一层都抓住了其他层漏掉的 bug：
- 不同的代码路径绕过了入口校验
- mock 绕过了业务逻辑检查
- 不同平台上的边界情况需要环境守卫
- 调试日志定位出了结构性误用

**不要停在一个校验点上。** 每一层都加检查。
