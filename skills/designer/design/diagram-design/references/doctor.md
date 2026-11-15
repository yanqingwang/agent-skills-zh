> **中文汉化版** · 上游：[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) · 原文件：`skills/diagram-design/references/doctor.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 环境诊断（doctor）

当用户要求运行诊断、健康检查或首次运行排障，或调用 `/diagram-design:doctor` 或 `/doctor` 时，加载本文件。

目标是一份一次到位的报告：检查本地是否具备 Diagram Design 导入/导出与命令路由的就绪条件，不改动用户文件、不安装依赖。

Diagram Design 的安装位置要从本参考文件解析，而不是从用户当前工作目录解析。在普通项目目录里调用 doctor 是预期场景，绝不能当成"仓库路径错误"处理。

使用两种诊断模式：

- **已安装 Skill 模式**（默认）：检查运行时和解析出的 Skill 安装。不要求只有维护者仓库才有的文件。
- **维护者检出模式**：仅当解析出的安装根目录同时包含 `CONTRIBUTING.md`、`.github/workflows/ci.yml` 和 `scripts/verify-plugin-package.py` 时使用。此时加入下方的仓库完整性检查。

## 输入

可选旗标：

- `--strict`：在最终汇总里把警告当失败。
- `--json`：在人类可读汇总之外，额外打印机器可读的 JSON 报告。

不给旗标时按标准模式运行。

## 必做检查

按以下顺序全部执行，每项报告为 `pass`、`warn` 或 `fail`。

1. Python 运行时
- 先解析 `python3`，再解析 `python`。一个名字虽然在 PATH 上、却报不出自己的版本，不配赢得解析：落到下一个候选。（Windows 自带一个 `python3` App Execution Alias，那是 Microsoft Store 的占位 stub，不是解释器，而且它排在 python.org 安装之前。）一个完全无法启动的名字算同类废品，按检查失败上报，而不是终止整个运行。
- 要求版本 >= 3.10。
- 找不到任何 Python 解释器：`fail`。
- 版本低于 3.10：`fail`。

2. PNG 导出所需的 Playwright
- 检查当前 Python 解释器里 Playwright 是否可导入（`import playwright`）；不要求可选的包版本属性。
- 验证默认的 headless Chromium 能在该解释器里启动，探测后关闭。这包括只装受支持 headless-shell 的安装；默认 PNG 导出不要求完整 Chromium 可执行文件路径。浏览器启动限 5 秒，子进程探测限 10 秒，超时即终止自己拥有的探测进程树。Windows 的进程树清理和父进程收割各另有 2 秒限额；清理失败按警告上报。
- 缺失时标 `warn`，并报告宿主环境必须准备一个受认可的 Playwright 安装和兼容浏览器。
- 绝不自动安装依赖。

3. 预期脚本存在（仅维护者检出模式）
- 验证这些仓库脚本存在：
  - `scripts/verify-drawio-import.py`
  - `scripts/verify-mermaid-import.py`
  - `scripts/verify-excalidraw-import.py`
  - `scripts/verify-plantuml-import.py`
  - `scripts/verify-motion.py`
  - `scripts/lint-skin.py`
  - `scripts/verify-docs-sync.py`
- 维护者检出模式下脚本缺失为 `fail`。
- 已安装 Skill 模式下，报告维护者脚本不适用；它们的缺席不算警告或失败。

4. Plugin 接线面（仅维护者检出模式）
- 验证 Claude 命令文件存在并指向各自的参考文件：
  - `commands/export-diagram.md` -> `references/export.md`
  - `commands/import-drawio.md` -> `references/import-drawio.md`
  - `commands/import-mermaid.md` -> `references/import-mermaid.md`
  - `commands/import-excalidraw.md` -> `references/import-excalidraw.md`
  - `commands/import-plantuml.md` -> `references/import-plantuml.md`
  - `commands/profile.md` -> `references/profiles.md`
  - `commands/doctor.md` -> `references/doctor.md`
- 验证 Pi prompt 文件存在并指向各自的参考文件：
  - `prompts/export-diagram.md` -> `references/export.md`
  - `prompts/import-mermaid.md` -> `references/import-mermaid.md`
  - `prompts/import-excalidraw.md` -> `references/import-excalidraw.md`
  - `prompts/import-plantuml.md` -> `references/import-plantuml.md`
  - `prompts/profile.md` -> `references/profiles.md`
  - `prompts/doctor.md` -> `references/doctor.md`
- 文件缺失为 `fail`。
- 参考路由不匹配为 `fail`。
- 已安装 Skill 模式下，报告维护者命令/prompt 接线不适用；仓库路由树残缺或缺失不算失败。

5. 常见路径错误
- 验证解析出的安装根目录之下有 `SKILL.md`。不要相对用户当前项目去搜索它，也不要指导用户进入维护者仓库。
- 路径含空格而给出的命令示例没有加引号时，检测出这个 Windows 引号风险。
- 检测对本地已安装 Skill 路径的引用（如果命令输出里出现）指向不存在的位置。
- 这些都标 `warn`，并给出精确的修复建议。
- 解析出的 `SKILL.md` 缺失时，建议重装或更新 Diagram Design，而不是切换进仓库检出。

## 输出契约

始终打印：

1. 一行紧凑汇总：
- `Doctor summary: <PASS|WARN|FAIL> (<pass_count> pass, <warn_count> warn, <fail_count> fail)`

2. 一张清单，每个检查一行：
- `[PASS] Python 3.11.9 found at ...`
- `[WARN] Playwright not installed ...`
- `[FAIL] Missing scripts/verify-docs-sync.py`

3. 仅当存在 warn/fail 时，输出 `Next actions` 小节。

4. 带 `--json` 时，追加 JSON 对象，包含：
- `status`、`counts`、`checks[]`（`name`、`status`、`message`、可选 `fix`）、`timestamp`。

## 安全与行为规则

- 只做只读诊断：不改文件、不装包、不跑破坏性 git 命令。
- 任何命令意外失败：抓取 stderr，继续剩余检查。
- 绝不声称某个检查通过，除非本次运行里直接验证过。
- 优先给出明确、可直接复制粘贴的修复命令。

## 示例结果

```text
Doctor summary: WARN (6 pass, 2 warn, 0 fail)
[PASS] Python 3.11.9 found at /usr/bin/python3
[WARN] Playwright package not found in active interpreter
[PASS] scripts/verify-drawio-import.py present
...

Next actions
- Provision an approved PNG export renderer, then re-run the doctor check
- Re-run: /diagram-design:doctor --strict
```
