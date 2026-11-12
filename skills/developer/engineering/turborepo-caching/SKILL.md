---
name: turborepo-caching
description: 为高效的 monorepo 构建配置 Turborepo，支持本地与远程缓存。用于设置 Turborepo、优化构建流水线或实现分布式缓存时。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/developer-essentials/skills/turborepo-caching/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Turborepo 缓存

Turborepo 构建优化的生产级模式。

## 何时使用本 Skill

- 搭建新的 Turborepo 项目
- 配置构建流水线
- 实现远程缓存
- 优化 CI/CD 性能
- 从其他 monorepo 工具迁移
- 调试缓存未命中

## 核心概念

### 1. Turborepo 架构


```
Workspace Root/
├── apps/
│   ├── web/
│   │   └── package.json
│   └── docs/
│       └── package.json
├── packages/
│   ├── ui/
│   │   └── package.json
│   └── config/
│       └── package.json
├── turbo.json
└── package.json
```


### 2. 流水线概念

| 概念 | 说明 |
| -------------- | -------------------------------- |
| **dependsOn** | 必须先完成的任务 |
| **cache** | 是否缓存输出 |
| **outputs** | 要缓存的文件 |
| **inputs** | 影响缓存键的文件 |
| **persistent** | 长时间运行的任务（开发服务器） |

## 模板

### 模板 1：turbo.json 配置


```json
{
  "$schema": "https://turbo.build/schema.json",
  "globalDependencies": [".env", ".env.local"],
  "globalEnv": ["NODE_ENV", "VERCEL_URL"],
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**", "!.next/cache/**"],
      "env": ["API_URL", "NEXT_PUBLIC_*"]
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "inputs": ["src/**/*.tsx", "src/**/*.ts", "test/**/*.ts"]
    },
    "lint": {
      "outputs": [],
      "cache": true
    },
    "typecheck": {
      "dependsOn": ["^build"],
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "clean": {
      "cache": false
    }
  }
}
```


### 模板 2：包级流水线


```json
// apps/web/turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "extends": ["//"],
  "pipeline": {
    "build": {
      "outputs": [".next/**", "!.next/cache/**"],
      "env": ["NEXT_PUBLIC_API_URL", "NEXT_PUBLIC_ANALYTICS_ID"]
    },
    "test": {
      "outputs": ["coverage/**"],
      "inputs": ["src/**", "tests/**", "jest.config.js"]
    }
  }
}
```


### 模板 3：使用 Vercel 的远程缓存


```bash
# Login to Vercel
npx turbo login

# Link to Vercel project
npx turbo link

# Run with remote cache
turbo build --remote-only

# CI environment variables
TURBO_TOKEN=your-token
TURBO_TEAM=your-team
```



```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

env:
  TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}
  TURBO_TEAM: ${{ vars.TURBO_TEAM }}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: "npm"

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npx turbo build --filter='...[origin/main]'

      - name: Test
        run: npx turbo test --filter='...[origin/main]'
```


### 模板 4：自托管远程缓存


```typescript
// Custom remote cache server (Express)
import express from "express";
import { createReadStream, createWriteStream } from "fs";
import { mkdir } from "fs/promises";
import { join } from "path";

const app = express();
const CACHE_DIR = "./cache";

// Get artifact
app.get("/v8/artifacts/:hash", async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || "default";
  const filePath = join(CACHE_DIR, team, hash);

  try {
    const stream = createReadStream(filePath);
    stream.pipe(res);
  } catch {
    res.status(404).send("Not found");
  }
});

// Put artifact
app.put("/v8/artifacts/:hash", async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || "default";
  const dir = join(CACHE_DIR, team);
  const filePath = join(dir, hash);

  await mkdir(dir, { recursive: true });

  const stream = createWriteStream(filePath);
  req.pipe(stream);

  stream.on("finish", () => {
    res.json({
      urls: [`${req.protocol}://${req.get("host")}/v8/artifacts/${hash}`],
    });
  });
});

// Check artifact exists
app.head("/v8/artifacts/:hash", async (req, res) => {
  const { hash } = req.params;
  const team = req.query.teamId || "default";
  const filePath = join(CACHE_DIR, team, hash);

  try {
    await fs.access(filePath);
    res.status(200).end();
  } catch {
    res.status(404).end();
  }
});

app.listen(3000, "127.0.0.1");
```



```json
// turbo.json for the local cache demo
{
  "remoteCache": {
    "signature": false
  }
}
```



```bash
# This local demo does not authenticate the dummy token.
# Use only disposable artifacts on a trusted machine; do not expose the server.
turbo build --api="http://127.0.0.1:3000" --token="my-token" --team="my-team"
```


### 模板 5：过滤与范围限定


```bash
# Build specific package
turbo build --filter=@myorg/web

# Build package and its dependencies
turbo build --filter=@myorg/web...

# Build package and its dependents
turbo build --filter=...@myorg/ui

# Build changed packages since main
turbo build --filter='...[origin/main]'

# Build packages in directory
turbo build --filter='./apps/*'

# Combine filters
turbo build --filter=@myorg/web --filter=@myorg/docs

# Exclude package
turbo build --filter='!@myorg/docs'

# Include dependencies of changed
turbo build --filter='...[HEAD^1]...'
```


### 模板 6：高级流水线配置


```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "inputs": ["$TURBO_DEFAULT$", "!**/*.md", "!**/*.test.*"]
    },
    "test": {
      "dependsOn": ["^build"],
      "outputs": ["coverage/**"],
      "inputs": ["src/**", "tests/**", "*.config.*"],
      "env": ["CI", "NODE_ENV"]
    },
    "test:e2e": {
      "dependsOn": ["build"],
      "outputs": [],
      "cache": false
    },
    "deploy": {
      "dependsOn": ["build", "test", "lint"],
      "outputs": [],
      "cache": false
    },
    "db:generate": {
      "cache": false
    },
    "db:push": {
      "cache": false,
      "dependsOn": ["db:generate"]
    },
    "@myorg/web#build": {
      "dependsOn": ["^build", "@myorg/db#db:generate"],
      "outputs": [".next/**"],
      "env": ["NEXT_PUBLIC_*"]
    }
  }
}
```


### 模板 7：根 package.json 设置


```json
{
  "name": "my-turborepo",
  "private": true,
  "workspaces": ["apps/*", "packages/*"],
  "scripts": {
    "build": "turbo build",
    "dev": "turbo dev",
    "lint": "turbo lint",
    "test": "turbo test",
    "clean": "turbo clean && rm -rf node_modules",
    "format": "prettier --write \"**/*.{ts,tsx,md}\"",
    "changeset": "changeset",
    "version-packages": "changeset version",
    "release": "turbo build --filter=./packages/* && changeset publish"
  },
  "devDependencies": {
    "turbo": "^1.10.0",
    "prettier": "^3.0.0",
    "@changesets/cli": "^2.26.0"
  },
  "packageManager": "npm@10.0.0"
}
```


## 调试缓存


```bash
# Dry run to see what would run
turbo build --dry-run

# Verbose output with hashes
turbo build --verbosity=2

# Show task graph
turbo build --graph

# Force no cache
turbo build --force

# Show cache status
turbo build --summarize

# Debug specific task
TURBO_LOG_VERBOSITY=debug turbo build --filter=@myorg/web
```


## 最佳实践

### 该做的

- **定义显式的 inputs** - 避免缓存失效
- **使用 workspace 协议** - `"@myorg/ui": "workspace:*"`
- **启用远程缓存** - 在 CI 与本地之间共享
- **在 CI 中过滤** - 只构建受影响的包
- **缓存构建输出** - 而非源文件

### 不该做的

- **不要缓存开发服务器** - 使用 `persistent: true`
- **不要在 env 中放入机密** - 使用运行时环境变量
- **不要忽略 dependsOn** - 会导致竞态条件
- **不要过度过滤** - 可能遗漏依赖
