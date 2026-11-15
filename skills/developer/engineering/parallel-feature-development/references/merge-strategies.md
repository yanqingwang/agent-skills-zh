> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/agent-teams/skills/parallel-feature-development/references/merge-strategies.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 集成与合并策略

整合并行工作流与解决冲突的模式。

## 集成模式

### Pattern 1: 直接集成

所有实现者都向同一个分支提交，集成自然发生。

```
feature/auth ← implementer-1 commits
             ← implementer-2 commits
             ← implementer-3 commits
```

**何时使用**：小团队（2-3 人）、严格的文件所有权（预期不会出现冲突）。

### Pattern 2: 子分支集成

每个实现者在各自的子分支上工作，由负责人按顺序合并。

```
feature/auth
  ├── feature/auth-login     ← implementer-1
  ├── feature/auth-register  ← implementer-2
  └── feature/auth-tests     ← implementer-3
```

合并顺序：遵循依赖图（先基础、再依赖方、最后集成）。

**何时使用**：较大团队（4 人以上）、关注点有重叠、需要评审关卡。

### Pattern 3: 主干开发与功能开关

所有实现者都在功能开关的保护下向主分支提交。

```
main ← all implementers commit
     ← feature flag gates new code
```

**何时使用**：CI/CD 环境、短生命周期功能、持续部署。

## 集成验证清单

所有实现者完成后：

1. **构建检查**：代码能否无错误地编译/打包？
2. **类型检查**：TypeScript/类型注解能否通过？
3. **lint 检查**：代码能否通过 lint 规则？
4. **单元测试**：所有单元测试能否通过？
5. **集成测试**：跨组件测试能否通过？
6. **接口验证**：所有接口契约是否与实现一致？

## 冲突解决

### 预防（最佳）

- 严格的文件所有权可消除大多数冲突
- 接口契约在实现开始前就界定好边界
- 共享类型文件由负责人拥有并按顺序修改

### 发现

- 若发生冲突，Git 合并会报告出来
- TypeScript/lint 错误表明接口不匹配
- 测试失败表明存在行为冲突

### 解决策略

1. **契约优先**：若代码与接口契约不符，错的是代码
2. **负责人仲裁**：由团队负责人决定保留哪个实现
3. **测试裁决**：能通过测试的实现才是正确的
4. **手动合并**：复杂冲突由负责人手动合并
