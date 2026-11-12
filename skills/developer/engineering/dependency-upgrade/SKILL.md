---
name: dependency-upgrade
description: 通过兼容性分析、分阶段灰度与全面测试来管理依赖的主版本升级。在升级框架版本、更新主要依赖，或处理库中的破坏性变更时使用。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/framework-migration/skills/dependency-upgrade/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 依赖升级

掌握依赖主版本升级、兼容性分析、分阶段升级策略与全面的测试方法。

## 何时使用本 Skill

- 升级框架的主版本
- 更新存在安全漏洞的依赖
- 现代化遗留依赖
- 解决依赖冲突
- 规划渐进式升级路径
- 测试兼容性矩阵
- 自动化依赖更新

## 语义化版本回顾


```
MAJOR.MINOR.PATCH (e.g., 2.3.1)

MAJOR: Breaking changes
MINOR: New features, backward compatible
PATCH: Bug fixes, backward compatible

^2.3.1 = >=2.3.1 <3.0.0 (minor updates)
~2.3.1 = >=2.3.1 <2.4.0 (patch updates)
2.3.1 = exact version
```


## 依赖分析

### 审计依赖


```bash
# npm
npm outdated
npm audit
npm audit fix

# yarn
yarn outdated
yarn audit

# Check for major updates
npx npm-check-updates
npx npm-check-updates -u  # Update package.json
```


### 分析依赖树


```bash
# See why a package is installed
npm ls package-name
yarn why package-name

# Find duplicate packages
npm dedupe
yarn dedupe

# Visualize dependencies
npx madge --image graph.png src/
```


## 兼容性矩阵


```javascript
// compatibility-matrix.js
const compatibilityMatrix = {
  react: {
    "16.x": {
      "react-dom": "^16.0.0",
      "react-router-dom": "^5.0.0",
      "@testing-library/react": "^11.0.0",
    },
    "17.x": {
      "react-dom": "^17.0.0",
      "react-router-dom": "^5.0.0 || ^6.0.0",
      "@testing-library/react": "^12.0.0",
    },
    "18.x": {
      "react-dom": "^18.0.0",
      "react-router-dom": "^6.0.0",
      "@testing-library/react": "^13.0.0",
    },
  },
};

function checkCompatibility(packages) {
  // Validate package versions against matrix
}
```


## 分阶段升级策略

### 阶段 1：规划


```bash
# 1. Identify current versions
npm list --depth=0

# 2. Check for breaking changes
# Read CHANGELOG.md and MIGRATION.md

# 3. Create upgrade plan
echo "Upgrade order:
1. TypeScript
2. React
3. React Router
4. Testing libraries
5. Build tools" > UPGRADE_PLAN.md
```


### 阶段 2：增量更新


```bash
# Don't upgrade everything at once!

# Step 1: Update TypeScript
npm install typescript@latest

# Test
npm run test
npm run build

# Step 2: Update React (one major version at a time)
npm install react@17 react-dom@17

# Test again
npm run test

# Step 3: Continue with other packages
npm install react-router-dom@6

# And so on...
```


### 阶段 3：验证


```javascript
// tests/compatibility.test.js
describe("Dependency Compatibility", () => {
  it("should have compatible React versions", () => {
    const reactVersion = require("react/package.json").version;
    const reactDomVersion = require("react-dom/package.json").version;

    expect(reactVersion).toBe(reactDomVersion);
  });

  it("should not have peer dependency warnings", () => {
    // Run npm ls and check for warnings
  });
});
```


## 破坏性变更处理

### 识别破坏性变更


```bash
# Check the changelog directly
curl https://raw.githubusercontent.com/facebook/react/master/CHANGELOG.md
```


### 使用 Codemod 自动修复


```bash
# Run jscodeshift with transform URL
npx jscodeshift -t <transform-url> <path>

# Example: Rename unsafe lifecycle methods
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js src/

# For TypeScript files
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js --parser=tsx src/

# Dry run to preview changes
npx jscodeshift -t https://raw.githubusercontent.com/reactjs/react-codemod/master/transforms/rename-unsafe-lifecycles.js --dry src/
```


### 自定义迁移脚本


```javascript
// migration-script.js
const fs = require("fs");
const glob = require("glob");

glob("src/**/*.tsx", (err, files) => {
  files.forEach((file) => {
    let content = fs.readFileSync(file, "utf8");

    // Replace old API with new API
    content = content.replace(
      /componentWillMount/g,
      "UNSAFE_componentWillMount",
    );

    // Update imports
    content = content.replace(
      /import { Component } from 'react'/g,
      "import React, { Component } from 'react'",
    );

    fs.writeFileSync(file, content);
  });
});
```


## 测试策略

### 单元测试


```javascript
// Ensure tests pass before and after upgrade
npm run test

// Update test utilities if needed
npm install @testing-library/react@latest
```


### 集成测试


```javascript
// tests/integration/app.test.js
describe("App Integration", () => {
  it("should render without crashing", () => {
    render(<App />);
  });

  it("should handle navigation", () => {
    const { getByText } = render(<App />);
    fireEvent.click(getByText("Navigate"));
    expect(screen.getByText("New Page")).toBeInTheDocument();
  });
});
```


### 视觉回归测试


```javascript
// visual-regression.test.js
describe("Visual Regression", () => {
  it("should match snapshot", () => {
    const { container } = render(<App />);
    expect(container.firstChild).toMatchSnapshot();
  });
});
```


### E2E 测试


```javascript
// cypress/e2e/app.cy.js
describe("E2E Tests", () => {
  it("should complete user flow", () => {
    cy.visit("/");
    cy.get('[data-testid="login"]').click();
    cy.get('input[name="email"]').type("user@example.com");
    cy.get('button[type="submit"]').click();
    cy.url().should("include", "/dashboard");
  });
});
```


## 自动化依赖更新

### Renovate 配置


```json
// renovate.json
{
  "extends": ["config:base"],
  "packageRules": [
    {
      "matchUpdateTypes": ["minor", "patch"],
      "automerge": true
    },
    {
      "matchUpdateTypes": ["major"],
      "automerge": false,
      "labels": ["major-update"]
    }
  ],
  "schedule": ["before 3am on Monday"],
  "timezone": "America/New_York"
}
```


### Dependabot 配置


```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    reviewers:
      - "team-leads"
    commit-message:
      prefix: "chore"
      include: "scope"
```


## 回滚计划


```javascript
// rollback.sh
#!/bin/bash

# Save current state
git stash
git checkout -b upgrade-branch

# Attempt upgrade
npm install package@latest

# Run tests
if npm run test; then
  echo "Upgrade successful"
  git add package.json package-lock.json
  git commit -m "chore: upgrade package"
else
  echo "Upgrade failed, rolling back"
  git checkout main
  git branch -D upgrade-branch
  npm install  # Restore from package-lock.json
fi
```


## 常见升级模式

### 锁文件管理


```bash
# npm
npm install --package-lock-only  # Update lock file only
npm ci  # Clean install from lock file

# yarn
yarn install --frozen-lockfile  # CI mode
yarn upgrade-interactive  # Interactive upgrades
```


### 对等依赖解析


```bash
# npm 7+: strict peer dependencies
npm install --legacy-peer-deps  # Ignore peer deps

# npm 8+: override peer dependencies
npm install --force
```


### Workspace 升级


```bash
# Update all workspace packages
npm install --workspaces

# Update specific workspace
npm install package@latest --workspace=packages/app
```
