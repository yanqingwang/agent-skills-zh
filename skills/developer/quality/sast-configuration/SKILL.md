---
name: sast-configuration
description: 为应用代码中的自动化漏洞检测配置静态应用安全测试（SAST）工具。在搭建安全扫描、实施 DevSecOps 实践，或自动化代码漏洞检测时使用本 Skill。
---

> **中文汉化版** · 上游：[wshobson/agents](https://github.com/wshobson/agents) · 原文件：`plugins/security-scanning/skills/sast-configuration/SKILL.md` · License: MIT
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# SAST 配置

静态应用安全测试（SAST）工具的安装、配置与自定义规则创建，用于跨多种编程语言实现全面的安全扫描。

## 概述

本 Skill 为安装与配置 SAST 工具（包括 Semgrep、SonarQube 与 CodeQL）提供全面指导。当你需要完成以下工作时使用本 Skill：

- 在 CI/CD 流水线中搭建 SAST 扫描
- 为你的代码库创建自定义安全规则
- 配置质量门禁与合规策略
- 优化扫描性能并减少误报
- 集成多个 SAST 工具实现纵深防御

## 核心能力

### 1. Semgrep 配置

- 通过模式匹配创建自定义规则
- 针对特定语言的安全规则（Python、JavaScript、Go、Java 等）
- CI/CD 集成（GitHub Actions、GitLab CI、Jenkins）
- 误报调优与规则优化
- 组织级策略强制执行

### 2. SonarQube 设置

- 质量门禁配置
- 安全热点分析
- 代码覆盖率与技术债跟踪
- 针对各语言的自定义质量配置
- 与 LDAP/SAML 的企业级集成

### 3. CodeQL 分析

- 与 GitHub Advanced Security 集成
- 自定义查询开发
- 漏洞变体分析
- 安全研究工作流
- SARIF 结果处理

## 快速开始

### 初始评估

1. 识别代码库中的主要编程语言
2. 确定合规要求（PCI-DSS、SOC 2 等）
3. 根据语言支持与集成需求选择 SAST 工具
4. 查看基线扫描，了解当前安全态势

### 基础设置

```bash
# Semgrep quick start
pip install semgrep
semgrep --config=auto --error

# SonarQube with Docker
docker run -d --name sonarqube -p 9000:9000 sonarqube:10.8-community

# CodeQL CLI setup
gh extension install github/gh-codeql
codeql database create mydb --language=python
```

## 集成模式

### CI/CD 流水线集成

```yaml
# GitHub Actions example
- name: Run Semgrep
  uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/security-audit
      p/owasp-top-ten
```

### 提交前 Hook

```bash
# .pre-commit-config.yaml
- repo: https://github.com/returntocorp/semgrep
  rev: v1.45.0
  hooks:
    - id: semgrep
      args: ['--config=auto', '--error']
```

## 最佳实践

1. **从基线开始**
   - 运行初始扫描以建立安全基线
   - 优先处理严重和高危级别的发现
   - 制定修复路线图

2. **渐进式采用**
   - 从侧重安全的规则入手
   - 逐步加入代码质量规则
   - 仅对严重问题实施阻断

3. **误报管理**
   - 记录合理的抑制项
   - 为已知安全模式建立允许列表
   - 定期复查被抑制的发现

4. **性能优化**
   - 排除测试文件与生成代码
   - 对大型代码库使用增量扫描
   - 在 CI/CD 中缓存扫描结果

5. **团队赋能**
   - 为开发者提供安全培训
   - 为常见模式编写内部文档
   - 建立安全大使计划

## 常见用例

### 新项目设置

```bash
# Semgrep: install, then run an auto-config scan that exits non-zero on findings
pip install semgrep
semgrep --config=auto --error

# SonarQube: start a community server for local evaluation, then analyze with sonar-scanner.
# SONAR_ES_BOOTSTRAP_CHECKS_DISABLE skips the Elasticsearch host checks for a local try-out;
# a real deployment needs vm.max_map_count>=524288 and fs.file-max>=131072 on the host instead.
docker run -d --name sonarqube -e SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true -p 9000:9000 sonarqube:10.8-community
```

### 自定义规则开发

```yaml
rules:
  - id: hardcoded-jwt-secret
    pattern: jwt.encode($DATA, "...", ...)
    message: JWT secret should not be hardcoded
    severity: ERROR
```

### 合规扫描

```bash
# PCI-DSS focused scan
semgrep --config p/pci-dss --json -o pci-scan-results.json
```

## 故障排查

### 误报率高

- 复查并调节规则灵敏度
- 添加路径过滤以排除测试文件
- 对噪声较多的模式使用 nostmt 元数据
- 创建组织专属的规则例外

### 性能问题

- 启用增量扫描
- 跨模块并行执行扫描
- 优化规则模式以提升效率
- 缓存依赖与扫描结果

### 集成失败

- 核验 API token 与凭据
- 检查网络连通性与代理设置
- 复查 SARIF 输出格式的兼容性
- 校验 CI/CD runner 权限

## 相关 Skill

- [STRIDE 分析模式](../stride-analysis-patterns/SKILL.md)
- [威胁缓解映射](../threat-mitigation-mapping/SKILL.md)

## 工具对比

| 工具      | 最适用场景           | 语言支持     | 成本            | 集成度        |
| --------- | ------------------------ | ---------------- | --------------- | ------------- |
| Semgrep   | 自定义规则、快速扫描 | 30+ 种语言   | 免费/企业版      | 极佳          |
| SonarQube | 代码质量 + 安全      | 25+ 种语言   | 免费/商业版      | 良好          |
| CodeQL    | 深度分析、研究       | 10+ 种语言   | 免费（开源）     | GitHub 原生   |

## 后续步骤

1. 完成 SAST 工具的初始安装配置
2. 运行基线安全扫描
3. 为组织专属模式创建自定义规则
4. 集成到 CI/CD 流水线
5. 建立安全门禁策略
6. 就发现项与修复方法培训开发团队
