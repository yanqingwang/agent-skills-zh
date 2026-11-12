---
name: open-code-review
description: >
  使用 alibaba/open-code-review 提供的 `ocr` CLI 对 Git 变更执行 AI 驱动的代码审查。当用户要求审查代码、审查 PR、审查已暂存/未暂存的变更、审查某个 commit，或比较分支以排查代码质量问题时使用。生成行级审查评论，并可在用户要求时自动应用修复。配置适当的审查规则后，可检测多类问题，包括缺陷、安全漏洞、性能问题和代码质量隐患。
license: Apache-2.0
compatibility: >
  Requires the `ocr` CLI installed (via `npm install -g
  @alibaba-group/open-code-review` or GitHub release binary). Requires a
  configured supported LLM provider before first run (protocols: Anthropic,
  OpenAI Chat Completions, OpenAI Responses, AWS Bedrock).
metadata:
  author: alibaba
  homepage: https://github.com/alibaba/open-code-review
  version: "1.0.0"
---

> **中文汉化版** · 上游：[alibaba/open-code-review](https://github.com/alibaba/open-code-review) · 原文件：`skills/open-code-review/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Open Code Review

用于调用 [open-code-review](https://github.com/alibaba/open-code-review)（`ocr`）的 Skill。这是一个开源的 AI 代码审查 CLI，读取 Git diff 并生成结构化的行级审查评论。

## 工作流

### 第 1 步：收集业务上下文

分析审查目标（commit、分支或变更），提取简洁的业务上下文。通过 `--background` 传入该上下文，以提升审查质量。

### 第 2 步：运行代码审查

**不要预先检查 `ocr` 是否已安装**，跳过 `command -v ocr` 或 `ocr --version` 之类的探测。假定该 CLI 可用并直接运行审查，这样在常见路径上省去一次工具调用。仅当审查因 `command not found` 失败时，才按「故障排查」一节安装它。

带上适当的标志运行 OCR 命令。若有业务上下文，**务必通过 `--background` 传入**：


```bash
ocr review --audience agent --background "business context here" [user-args]
```


**参数处理：**

- **背景上下文**（推荐）：使用 `--background "context"` 或 `-b "context"` 提供业务上下文，以获得更好的审查质量
- **默认**（无用户参数）：审查已暂存、未暂存和未跟踪的变更（工作区模式）
- **指定 commit**：使用 `--commit` 或 `-c` 针对其父提交审查单个 commit
- **分支比较**：使用 `--from <ref>` 和 `--to <ref>` 审查两个 ref 之间的 diff
- **超时**：每个审查组的有效超时 = `--timeout` × 审查轮数。默认 `--timeout 15`，配合默认强度 `medium`（2 轮）得到 30 分钟；`low`/`high` 分别得到 15/45 分钟。
- **并发**：默认并发为 8 个文件 worker；若触发速率限制，用 `--concurrency <n>` 降低
- **预览模式**：使用 `--preview` 或 `-p` 预览将要审查哪些文件，而不运行 LLM
- **输出文件**：使用 `--output <path>` 将完整结果写入文件，而非 stdout。若命令因 `unknown flag: --output` 失败，不要改用纯 stdout 继续审查。询问用户是否升级（`npm i -g @alibaba-group/open-code-review@latest`），并等待答复后再继续。用户确认且升级成功后，带 `--output` 重新运行。
- **安装**：若找不到 `ocr` 命令，运行 `npm i -g @alibaba-group/open-code-review` 安装

**常见调用模式：**

| 用户说 | 要运行的命令 |
|-----------|---------------|
| "审查我的变更" / "审查工作副本" | `ocr review --audience agent -b "context"` |
| "审查这个 PR" / "审查功能分支" | `ocr review --audience agent -b "context" --from main --to <branch>` |
| "审查 commit abc123" | `ocr review --audience agent -b "context" --commit abc123` |
| "会审查哪些内容？"（试运行） | `ocr review --preview` |

**输出模式：**

- 始终使用 `--audience agent` 以屏蔽进度 UI，只输出最终摘要
- **防止输出截断**：对于大型审查或受限的工具环境，传入 `--output /tmp/ocr_out.txt`，并通过文件读取工具完整查看该文件，而不是把 stdout 通过管道送给 `tail` 或 `head`，那会丢掉较早的审查评论。

**失败时**：若 `ocr review` 以非零码退出（例如 LLM 连接错误），不要盲目重试，请先查阅下面的「故障排查」一节找到对应的修复方法，再重新运行。

### 第 3 步：报告

OCR 输出在每条评论上包含结构化的 `severity`（critical / high / medium / low）和 `category`（bug / security / performance / maintainability / test / style / documentation / other）。按严重程度分组呈现结果，丢弃可能是误报或吹毛求疵的 `low` 级别项。

### 第 4 步：修复

应用修复前，先确认用户是否要求自动修复：

- 若用户明确要求「审查并修复」或类似表述，则继续自动修复
- 若用户只要求「审查」而无修复意图，则在应用任何变更前请求许可

修复问题与建议时：

- 聚焦 critical、high 和 medium 级别的项
- 在安全且定义明确时，直接把修复应用到代码
- 对于需要人工介入的复杂修复，清楚说明需要做什么
- 在提交前始终与用户确认修复

## 输出格式

OCR 输出中的每条评论包含：

- `path`：文件路径
- `content`：审查评论文本
- `start_line` / `end_line`：行范围（两者均为 0 表示定位失败）
- `category`：问题类别（bug, security, performance, maintainability, test, style, documentation, other）
- `severity`：问题严重程度（critical, high, medium, low）
- `suggestion_code`：可选的修复建议
- `existing_code`：可选的原始代码片段
- `thinking`：可选的 LLM 推理过程

使用以下模板按严重程度分组呈现结果：


```markdown
## Code Review Results

**Files reviewed**: N
**Issues found**: X critical, Y high, Z medium

### Critical

- **`path/to/file.java:42`** [bug] — Brief description
  > Recommendation: How to fix

### High

- **`path/to/file.java:26`** [bug] — Brief description
  > Recommendation: How to fix

### Medium

- **`path/to/file.ts:88`** [performance] — Brief description
  > Recommendation: How to fix (if applicable)
```


若过滤后不再有 critical、high 或 medium 级别的问题，则声明：「审查完成，在 N 个文件中未发现 critical、high 或 medium 级别的问题。」

**处理定位错误的评论：**

当 `start_line` 和 `end_line` 均为 `0` 时，说明该评论未能在文件中定位到准确位置。此时：

1. 阅读评论内容以理解问题
2. 检查评论中提到的目标文件
3. 根据评论的上下文定位相关的代码段
4. 把修复或建议应用到正确的位置

## 自定义审查规则

若用户想要项目专属规则，OCR 按以下优先级顺序解析：

1. `--rule <path>` 标志（最高）
2. `<repo>/.opencodereview/rule.json`
3. `~/.opencodereview/rule.json`
4. 内置系统默认值（最低）

默认情况下，第一个匹配的用户规则会替换内置系统规则。当希望同时保留匹配的系统规则和用户规则时，在规则条目上设置 `merge_system_rule: true`。

规则文件格式：


```json
{
  "rules": [
    {
      "path": "**/*.java",
      "rule": "All new methods must validate required parameters for null",
      "merge_system_rule": true
    },
    {
      "path": "**/*mapper*.xml",
      "rule": "Check SQL for injection risks and missing closing tags"
    }
  ]
}
```


要在审查前预览某个文件适用哪条规则：


```bash
ocr rules check src/main/java/com/example/Foo.java
```


## 高级审查选项

除上述常用标志外，`ocr review` 还提供几组控制项。运行 `ocr review --help` 查看完整列表。

**范围限定**

- `--exclude '<patterns>'`：以逗号分隔的 gitignore 风格模式（例如 `--exclude '**/generated/*,**/testdata/*'`），与 `rule.json` 中的排除项合并。
- `--background-file <path>`：从 Markdown 文件读取审查上下文。优先级高于 `--background`。

**输出**

- `--format text|json|sarif`：`text`（默认）面向人类阅读；`json` 生成机器可读的发现项；`sarif` 用于代码扫描集成，例如 GitHub Code Scanning。

**模型**

- `--provider <name>` / `--model <name>`：仅对本次运行覆盖已配置的 provider/model（例如用不同模型复查某个 diff；模型由用户指定，`ocr llm providers` 列出内置项）。

**预算**

- `--max-tokens <n>`：每组提示词的上限；默认为配置值或模板默认值（`200000`）。
- `--max-tokens-budget <n>`：为本次运行限制输入 + 输出的 token 总量。在每轮 LLM 调用前检查：已超预算的组会获得最后一轮以提交发现项，不再派发新的组，部分结果仍会发布，被跳过的文件报告为 `failed(budget)`。
- `--no-filter`：保留所有审查评论，跳过 LLM 的后置过滤调用。

## 注意事项

- **必须先配置 LLM**：若无可用 LLM，`ocr review` 会明确报错。出现这种情况时，参见下面的「故障排查」一节。
- **工作目录很重要**：`ocr review` 作用于当前目录下的 Git 仓库。使用 `--repo /path/to/repo` 可从其他位置运行。
- **工作区模式会审查未跟踪文件**：直接运行 `ocr review` 会包含已暂存、未暂存*以及*未跟踪的变更。若想收窄范围，请有选择地暂存。
- **大型 diff 可能触及 token 上限**：`MAX_TOKENS` 设定提示词预算（审查模板中为 `200000`；`ocr scan` 使用 `58888`）；会话上下文会被压缩以控制在该提示词预算内。模型输出另由 `MAX_COMPLETION_TOKENS`（`16384`）单独设限。单个文件的 diff 若单独超过 `MAX_TOKENS` 约 80%，会在调用 LLM 之前被跳过。
- **计划阶段由两个阈值之一触发**：当某组中最大的变更文件达到 `PLAN_MODE_LINE_THRESHOLD`（默认 `50`）**或**组内存在 2+ 个文件、其合计变更行数达到 `PLAN_MODE_GROUP_LINE_THRESHOLD`（默认 `100`）时，该组会在主审查前额外运行一次风险分析阶段。这会增加延迟，但能提升质量。
- **不要传 `--audience human`**：它会流式输出进度 UI，污染结果。始终使用 `--audience agent`。
- **评论语言跟随配置**：`language` 配置控制审查评论的语言，默认为 `English`，可接受任意语言名称（例如 `English` 或 `中文`）。
- **避免输出截断**：大型审查运行会产生冗长输出。切勿把命令输出通过管道送给 `tail` 或 `head`，那会丢掉前面章节的审查评论。使用 `--output <path>` 并完整读取；在较旧的 CLI 上，遵循上面的「输出文件」指引。
- **恢复中断的审查**：失败或中断的范围/commit 审查可用 `ocr review --resume <id>` 继续，使用相同的 `--from`/`--to` 或 `--commit` 目标（失败时该 id 会以 `retry with: --resume <id>` 打印，或用 `ocr session list` 查找）。工作区模式不支持恢复。

## 验证

审查完成后，通过以下检查确认成功：

1. 命令以退出码 0 结束
2. 已生成评论（或出现「未生成评论」消息）
3. 警告（若有）显示在 stderr 中

若出现错误，查看 stderr 警告，了解哪些文件失败及原因。

## 故障排查

**`ocr: command not found`**

安装该 CLI：


```bash
npm install -g @alibaba-group/open-code-review
```


**`unknown flag: --output`**

该 CLI 版本低于 v1.10.0。不要改用纯 stdout 继续审查。询问用户是否升级（`npm i -g @alibaba-group/open-code-review@latest`），并等待答复后再继续。用户确认且升级成功后，带 `--output` 重新运行。

**`ocr review` 因 LLM 连接错误失败**

提示用户配置 LLM provider。

交互式配置（推荐）：


```bash
ocr config provider
```


手动配置（备选）：


```bash
ocr config set llm.url https://api.anthropic.com/v1/messages
ocr config set llm.auth_token <api-key>
ocr config set llm.model claude-opus-4-6
ocr config set llm.use_anthropic true
```


用 `ocr llm test` 验证连通性。到此为止，请用户提供凭证，切勿编造或硬编码 API key。

## 参考资料

- 完整文档：https://github.com/alibaba/open-code-review
- NPM 包：https://www.npmjs.com/package/@alibaba-group/open-code-review
- 问题跟踪：https://github.com/alibaba/open-code-review/issues
