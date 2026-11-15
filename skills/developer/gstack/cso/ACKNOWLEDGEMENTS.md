> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/cso/ACKNOWLEDGEMENTS.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# CSO 研究与源版本

CSO v3 把受支持的静态证据、复现、提议的修复候选与当前源码闭环区分开来。该设计参考了 [Mozilla 对加固 Firefox 的叙述](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/) 与 [Codex Security 的 research-preview 说明](https://openai.com/index/codex-security-now-in-research-preview/)：应用上下文与可复现的验证塑造了工作流。它们的结果不是对 CSO 的度量。

`sections/audit-phases.md.tmpl` 中的领域指令标注了其所用的版本：

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/0x00_2025-Introduction/)，包括异常条件与修订后的供应链类别。
- [OWASP API Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)。
- 取自 [ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) 的部分控制项；requirement ID 必须携带其版本。
- [OWASP LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) 与 [Agentic Applications Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)，于 2026 年 9 月 9 日核查。审计记录实际使用的 artifact/版本，而不是从发布公告推断内容。
- [MCP security guidance dated 2026-07-28](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)。

执行细节遵循一手文档：[Bun compiled executables](https://bun.com/docs/bundler/executables)、[Docker contexts](https://docs.docker.com/engine/manage-resources/contexts/)、[container networking](https://docs.docker.com/engine/network/)、[Docker logging](https://docs.docker.com/engine/logging/configure/)、[npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/)、[uv CLI](https://docs.astral.sh/uv/reference/cli/) 与 [RubyGems commands](https://guides.rubygems.org/command-reference/#gem-fetch)。仅编译并不能压制 Bun 的配置或运行时注入变量。离线依赖准备必须在获取阶段排除本地 Python 构建，并把 Gemfile 求值推迟到离线执行时。

更早的 CSO 工作借鉴了 [Trail of Bits 的 skills](https://github.com/trailofbits/skills)（上下文构建与变体分析）、[Sentry 的 skills](https://github.com/getsentry/skills)（报告前的研究）以及更广泛的社区 security-skill 评审。v3 用明确的攻击者/控制/影响证据与独立挑战，取代了继承来的一揽子误报豁免与数值置信度门槛。

CSO 的准确率、召回率、搭建成功率与修复正确性都是发布度量，不是继承自厂商的基准声明。资格认定要求模型/预算配对一致、保留集断言、受支持的搭建失败计为未命中，以及零个误认证的修复。存在文档或适配器，不代表其运行时镜像或发布门已通过。
