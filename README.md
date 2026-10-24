# Agent Skills 中文汉化库（agent-skills-zh）

> 将 GitHub 上最受欢迎的 Agent Skills（星标 10 万+ 级别）系统性汉化为中文，服务中文 AI 编程用户。
> **本仓库只做翻译，不做原创**——原创人物视角 Skills 另见独立仓库（原则 #7）。

**上游星标快照日期：2026-10-24** · 完整数据见 [data/upstream-inventory.md](data/upstream-inventory.md)

## 来源仓库（第一批）

| 上游仓库 | 星标 | License | 本仓库收录 |
|---|---:|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 304k | MIT | 5 个 Skill |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 302k | MIT | 2 个 Skill |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 110k | MIT | 2 个 Skill + 1 个 Agent |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 102k | MIT | 1 个 Skill |
| multica-ai/andrej-karpathy-skills (223k) | — | **无 License** | ❌ 不收录（原则 #2） |

## 分类索引

由 [scripts/classify.py](scripts/classify.py) 按 [data/manifest.json](data/manifest.json) 自动生成 → [data/category-index.md](data/category-index.md)

- **工程方法论**：TDD、系统化调试、写计划、完成前验证、规格拆解
- **质量与审查**：代码审查、审查者 Agent
- **头脑风暴与构思**：brainstorming、idea-refine
- **上下文工程**：context-engineering
- **设计品味**：taste-skill

## 使用方法

将 `skills/<上游名>/<skill-name>/` **整个目录**复制到你所用 Harness 的技能目录（如 Claude Code 的 `~/.claude/skills/`、DSH 的技能目录），或按各上游原版安装方式替换为中文版目录。

目录内文件分三类（原则 #11，详见 [PRINCIPLES.md](PRINCIPLES.md)）：

| 类型 | 文件 | 处理 |
|---|---|---|
| 翻译件 | `SKILL.md`（含 description） | 已译中文，头部带来源与同步声明 |
| 原样复制件 | 脚本/样式/数据（.sh .py .mjs .cjs .ts .css .json .yaml .html）与上游散文引用（.md） | 逐字节与上游一致；散文件翻译排后续 issue |
| 排除件 | 上游 install.sh、plugin manifest、QA 产物 | 不收录，清单见 data/manifest.json `verbatim_excluded` |

## 合规与致谢

- 所有上游均为 MIT License：版权声明与许可原文保留于 [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md)
- 本仓库为翻译作品，注明"基于上游 X 翻译修改"，不代表上游官方中文版，除非上游 README 明确链接本仓库
- 术语统一见 [GLOSSARY.md](GLOSSARY.md)；翻译原则见 [PRINCIPLES.md](PRINCIPLES.md)

## 同步策略

`.github/workflows/sync-check.yml` 每日比对各上游 HEAD commit 与 `data/sync-state.json`：
上游有变更 → 自动开 issue 列出待重译文件 → 人工翻译后更新快照。每个翻译文件头部标注同步日期。

## 与上游的关系（引流策略）

向上游申请的方式：先开 issue 询问维护者，获同意后在其 README 提"中文版"一行链接指向本仓库。
**绝不把汉化正文直接 PR 进上游**（原则 #1）。
