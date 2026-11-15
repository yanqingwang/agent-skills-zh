> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/parallel-feature-development/references/file-ownership.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 文件所有权决策框架

将功能拆解为并行开发时，如何分配文件所有权。

## 所有权决策流程

### Step 1: 梳理所有文件

列出该功能需要创建或修改的每一个文件。

### Step 2: 识别自然聚类

按以下维度给文件分组：

- 目录邻近性（同一目录下的文件）
- 功能关联性（相互 import 的文件）
- 所属层（所有 UI 文件、所有 API 文件）

### Step 3: 把聚类分配给所有者

每个聚类成为一个实现者的所有权边界：

- 任何文件都不出现在多个聚类中
- 每个聚类内部内聚
- 跨聚类依赖降到最少

### Step 4: 定义接口点

在聚类发生交互的位置，定义：

- 共享类型定义（由负责人或指定实现者拥有）
- API 契约（函数签名、请求/响应结构）
- 事件契约（事件名称与载荷结构）

## 按项目类型的所有权

### React/Next.js 前端

```
implementer-1: src/components/{feature}/   (UI components)
implementer-2: src/hooks/{feature}/        (custom hooks, state)
implementer-3: src/api/{feature}/          (API client, types)
shared:        src/types/{feature}.ts      (owned by lead)
```

### Express/Fastify 后端

```
implementer-1: src/routes/{feature}.ts, src/controllers/{feature}.ts
implementer-2: src/services/{feature}.ts, src/validators/{feature}.ts
implementer-3: src/models/{feature}.ts, src/repositories/{feature}.ts
shared:        src/types/{feature}.ts      (owned by lead)
```

### 全栈（Next.js）

```
implementer-1: app/{feature}/page.tsx, app/{feature}/components/
implementer-2: app/api/{feature}/route.ts, lib/{feature}/
implementer-3: tests/{feature}/
shared:        types/{feature}.ts          (owned by lead)
```

### Python Django

```
implementer-1: {app}/views.py, {app}/urls.py, {app}/forms.py
implementer-2: {app}/models.py, {app}/serializers.py, {app}/managers.py
implementer-3: {app}/tests/
shared:        {app}/types.py              (owned by lead)
```

## 冲突解决

当两个实现者需要修改同一个文件时：

1. **首选：拆分文件**：把共享关注点抽取到独立的文件中
2. **无法拆分时：指定唯一所有者**：另一个实现者以变更请求方式提交修改
3. **最后手段：按顺序访问**：实现者 A 先完成，实现者 B 再接手
4. **绝不**：让双方同时修改同一个文件
