---
name: notebooklm
description: 通过 notebooklm-py CLI 或类型化异步 Python API 安装、认证、排障并操作 Gemini Notebook。当用户提及 Gemini Notebook、notebooklm-py、notebooklm CLI 或其 Python API 时，用于笔记本（notebook）与来源（source）管理、有据对话（grounded chat）与研究（research），以及产物（artifact）的生成或下载。不要用于通用 Gemini API 或无关的内容创作。
---

> **中文汉化版** · 上游：[teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) · 原文件：`SKILL.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Gemini Notebook 自动化

在 Agent 工作流中使用 `notebooklm` CLI。优先使用 `--json` 与显式 ID，让每个操作都可审查、并在并发下安全。
仅当用户要求编写应用代码，或 CLI 无法表达该工作流时，才使用类型化的异步 Python API。
下文关于就绪状态、身份、
授权与凭证处理的规则对两种接口均适用。

## 安装与认证

需要 Python 3.10+。将包安装到用户现有的环境中；
除非用户要求，否则不要创建独立的环境：

```bash
pip install "notebooklm-py[browser]"
pip install "notebooklm-py[cookies]"  # optional browser-cookie extraction
```

如果系统 `pip` 报告 `externally-managed-environment`，不要使用 `--break-system-packages`。
若仅使用 CLI，可提供 `uv tool install "notebooklm-py[browser]"` 或等效的 `pipx`
命令；若用于应用代码，则使用用户当前激活的项目环境。

对于无人值守或无头（headless）场景，优先使用基于 profile 的持久 master-token 认证，而不是复制的
cookie 快照。安装 `pip install "notebooklm-py[headless]"`；一次性自动 OAuth
捕获还需要 `[browser]`。在可信的工作站上运行
`notebooklm login --master-token --account <email>`，然后将 `master_token.json`（而非
`storage_state.json`）部署到选定的 profile。`NOTEBOOKLM_HOME` 选择私有基础目录，
`NOTEBOOKLM_PROFILE` 选择其中的 profile；默认解析为
`~/.notebooklm/profiles/default/master_token.json`。

在 CI 中，`NOTEBOOKLM_MASTER_TOKEN_JSON` 是一种密钥传输约定，不是包直接读取的环境变量。
将其原样值写入所选 profile 的 `master_token.json`（权限模式 `0600`），随后将其从环境中清除（unset），
再运行 `notebooklm auth refresh` 以生成 `storage_state.json`。同级的 master token
可以自动重新生成已过期的文件式 cookie。内联的
`NOTEBOOKLM_AUTH_JSON` 只是短期回退手段；它会绕过上述恢复路径。

使用 PyPI 或 release 标签，不要使用未发布的 `main` 检出。如有可用的
[安装指南](https://github.com/teng-lin/notebooklm-py/blob/main/docs/installation.md)，请查阅。

在执行工作流之前，验证真实认证状态，而不是仅仅解析 cookie 文件：

```bash
notebooklm auth check --test --json
```

要求 `.status == "ok"` 且 `.checks.token_fetch == true`。如果验证失败：

- 在有显示器的环境下，运行 `notebooklm login` 并重新验证。
- 在无头环境中，安装 `[cookies]` 并使用
  `notebooklm login --browser-cookies <browser>`。当账户选择不明确时，先使用
  `notebooklm auth inspect --browser <browser>`。
- 如果此前有效的 cookie 已过期，尝试 `notebooklm auth refresh`；在重新登录浏览器之后，使用
  `notebooklm auth refresh --browser-cookies <browser>`。

正常的 `--test` 预检可能会修复并持久化刷新后的 cookie。当检查必须严格只读时（包括下文的
故障诊断工作流），请加 `--passive`。

`notebooklm status` 报告的是已选笔记本的上下文，而非认证状态。

将两种认证文件都视为持有者（bearer）凭证：绝不打印、记录日志或提交它们。master token 是一种持久的
全账户凭证，密码更改后仍然有效；请使用专用账户，将其保存在密钥库中并以 `0600` 权限存放于磁盘，
若泄露则显式吊销。

## 操作不变量

1. 发现与变更操作都使用 `--json`，然后保留返回的完整 UUID。重要的信封（envelope）字段包括：
   `create` 返回的 `.notebook.id`、`source add` 返回的 `.source.id`，以及异步生成器返回的
   `.task_id`。`generate mind-map` 则返回 `mind_map`、`note_id` 和 `kind`；
   两种 mind-map 类型都直接返回已完成的结果，没有任务 ID，也没有单独的 `artifact wait` 步骤。
2. 在自动化或并发工作中，每条笔记本作用域的命令都要传入 `-n/--notebook <id>`。
   不要依赖 `notebooklm use`。每次并发运行还应设置唯一的
   `NOTEBOOKLM_PROFILE=agent-<id>`，使上下文与 profile 写入相互隔离。新建的 profile 没有
   凭证：先在该 profile 中放入一份 `master_token.json` 副本并生成其 storage，然后再使用。
   绝不要在多个 Agent 之间共享同一个可写的 `storage_state.json`。
3. 添加来源后，保留每个 `.source.id`，然后在对话或生成之前对每个来源运行 `source wait`。
   add 返回的信封中没有状态字段。要求 wait 以退出码 0 结束且 `status == "ready"`；
   媒体特有的暂时性 `error` 行交给 waiter 处理。
4. 异步生成器返回任务/产物 ID 后，将其按位置参数传给
   `artifact wait`，并带上 `-n <notebook_id>`。用
   `-a <artifact_id> -n <notebook_id>` 下载那个确切的产物；绝不要选择当前可见的最新产物。
   mind-map 生成直接返回其已完成的结果，不需要 `artifact wait`。
5. 对于重叠的研究（research）运行，始终传入 `--run-id <research_run_id>`。
6. 只有当宿主环境确实存在后台机制时才使用它。将 wait 与依赖它的下载
   命令放在同一个顺序执行的任务中，且只在 wait 以退出码 0 结束后才下载。否则在前台
   运行，或向用户返回精确的、以 ID 锁定的命令。

## 授权边界

安全的检查操作，以及明确请求过的创建、添加来源、对话和提示词建议，可以直接运行。
在尝试恢复之前，先用只读命令诊断故障。

当某操作尚未被明确授权时，须在执行前立即获得确认：

- 破坏性命令，如删除笔记本/来源/笔记/产物/标签/profile、移除共享、登出（logout）、清空（clear）、
  取消研究以及 `ask --new`；
- `language set`，因为默认模式会更改账户全局的输出语言
  （优先使用生成命令的 `--language` 覆盖）；
- 生成或长时间的前台等待，可能耗时数分钟且受速率限制；
- 下载操作，会写入文件；
- `research wait --import-all`，会导入来源；
- `ask --save-as-note` 与 `history --save`，会创建笔记。

授权边界是用户意图，而不是 CLI 是否出现提示。获得授权后，在支持的地方传入
`--yes`/`-y`。大多数破坏性 JSON 命令在没有它时会拒绝执行而不提示，但
有些命令——包括 `ask --new --json` 和 `share remove --json`——会不经提示直接执行。绝不要
把“没有提示”当作同意。

`research cancel` 是发出即忘（fire-and-forget）的。在获得授权的取消之后，用
`notebooklm research status -n <notebook_id> --run-id <research_run_id> --json` 验证该次运行。

## 命令发现

使用已安装 CLI 的帮助作为与版本匹配的权威信息来源，而不是猜测参数：

```bash
notebooklm --help
notebooklm source --help
notebooklm research --help
notebooklm generate --help
notebooklm artifact --help
notebooklm download --help
```

同时查看 `notebooklm --version`，并在某个命令的帮助与本 Skill 不一致时，深入查看
确切命令的帮助，例如 `notebooklm generate audio --help`。

常用操作：

| 目标 | 命令 |
|---|---|
| 检查计算资源用量 | `notebooklm usage --json`；`notebooklm usage --categories` 查看各类别可用性与预估成本 |
| 列出或创建笔记本 | `notebooklm list --json`；`notebooklm create "Title" --json` |
| 添加并等待来源 | `notebooklm source add <input> -n <nb> --json`；`notebooklm source wait <src> -n <nb>` |
| URL 恢复 | `notebooklm source add <url> --fallback-fetch` |
| 对话 | `notebooklm ask "question" -n <nb> --json` |
| 研究 | `notebooklm source add-research "query" -n <nb> --mode fast --json`（也支持 `deep`） |
| 列出或等待产物 | `notebooklm artifact list -n <nb> --json`；`notebooklm artifact wait <id> -n <nb>` |
| 生成 | `notebooklm generate <type> ... -n <nb> --json` |
| 下载 | `notebooklm download <type> <path> -n <nb> -a <artifact>` |

完整命令面请查阅已安装命令的帮助，或（如可用）
[CLI 参考](https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md)。
应用代码请使用下文的基线，并（如可用）参考
[Python API 指南](https://github.com/teng-lin/notebooklm-py/blob/main/docs/python-api.md)。

## 标准的从来源到产物工作流

从 JSON 输出中保留 `{notebook_id}`、每个 `{source_id}` 以及 `{artifact_id}`：

对这个完整工作流的显式请求，即授权其常规的前置等待、所请求的生成以及所请求的输出文件。
只需确认该请求未覆盖的工作。

1. `notebooklm create "Research: topic" --json`
2. `notebooklm source add <input> -n {notebook_id} --json`，对每个输入执行。
3. 一旦前台等待获得授权，对每个记录下来的来源运行
   `notebooklm source wait {source_id} -n {notebook_id} --timeout 600`。
4. 一旦生成获得授权，生成所请求的类型。音频用：
   `notebooklm generate audio "instructions" -n {notebook_id} -s {source_id} --json`。
   对每个选中的来源重复 `-s`，并把 `.task_id` 记为 `{artifact_id}`。
5. 一旦前台等待获得授权，运行
   `notebooklm artifact wait {artifact_id} -n {notebook_id} --timeout 1200`。
6. 一旦输出写入获得授权，运行
   `notebooklm download audio ./podcast.m4a -a {artifact_id} -n {notebook_id}`。

若只做分析而不生成，则在每个来源都就绪之后，
用一个以 ID 锁定的对话命令替换第 4-6 步：

```bash
notebooklm ask "Summarize the key arguments" -n {notebook_id} --json
```

## 深度研究（Deep Research）

深度研究可能需要 15-30 分钟以上。以非阻塞方式启动，并把
`.poll_task_id // .task_id` 保留为 `{research_run_id}`：

```bash
notebooklm source add-research "query" -n {notebook_id} --mode deep --no-wait --json
```

只有在显式授权后才导入，并同时锁定两个 ID：

```bash
notebooklm research wait -n {notebook_id} --run-id {research_run_id} \
  --import-all --timeout 1800 --json
```

使用 `--import-all` 时，`--timeout` 是轮询与导入重试的每个阶段的预算，因此该示例
可能消耗约 3600 秒的宿主墙钟时间。

从 `.imported_sources[].id` 中保留新建来源的 ID，
并在后续对话或生成之前等待其就绪。

## Python API 基线

当完整的 API 指南不可用时，使用已安装的类型化 API 及其 docstring；不要凭空猜测
方法名。保持与 CLI 工作流相同的 ID 与就绪门槛：

```python
import asyncio

from notebooklm import NotebookLMClient


async def main(url: str) -> None:
    async with NotebookLMClient.from_storage() as client:
        notebook = await client.notebooks.create("Research: topic")
        source = await client.sources.add_url(notebook.id, url)
        await client.sources.wait_until_ready(notebook.id, source.id, timeout=600)

        answer = await client.chat.ask(
            notebook.id, "Summarize the key arguments", source_ids=[source.id]
        )
        print(answer.answer)

        task = await client.artifacts.generate_audio(
            notebook.id,
            source_ids=[source.id],
            instructions="Focus on the key arguments",
        )
        final = await client.artifacts.wait_for_completion(notebook.id, task.task_id, timeout=1200)
        if not final.is_complete:
            raise RuntimeError(f"Generation ended with {final.status}: {final.error}")
        await client.artifacts.download_audio(
            notebook.id, "./podcast.m4a", artifact_id=task.task_id
        )


asyncio.run(main("https://example.com"))
```

`NotebookLMClient.from_storage()` 是异步上下文管理器，不需要 await。客户端
在同一个事件循环上可重入，但不是线程安全的；每个事件循环创建一个客户端。公开的命名空间
包括 `notebooks`、`sources`、`chat`、`research`、`artifacts`、`mind_maps`、`notes`、`settings`、
`sharing`、`labels` 和 `collections`。在执行改变状态、长时间运行或写文件的调用之前，
先套用上文的授权边界。

## 生成说明

可用的生成器包括 `audio`、`video`、`slide-deck`、`infographic`、`report`、`mind-map`、
`data-table`、`quiz` 和 `flashcards`。请查看 `notebooklm generate <type> --help`，因为
格式、样式、来源选择、语言和重试支持因类型而异。

请牢记这些不那么显而易见的区别：

- Mind map（`--kind interactive`，默认）内部是异步的 Studio 产物，但
  CLI 会轮询至完成并返回 `{mind_map, note_id, kind}`；不要运行 `artifact wait`。
- Mind map（`--kind note-backed`）是服务端同步的。两种类型都接受 `--instructions`；
  interactive 类型会可靠地应用它，而服务端可能对 note-backed 地图忽略它。
- `generate video --format cinematic` 会忽略 `--style`，需要 Google AI Ultra，
  且可能耗时约 30-40 分钟。
- Slide-deck 没有方向参数。在描述中要求竖屏输出（例如
  `9:16 portrait`）；幻灯片修订无法改变成品的方向。
- 自定义报告：将提示词作为位置参数 description 传入并使用 `--format custom`；
  `--append` 仅适用于内置报告格式。

当提示词过长或不便用 shell 引号表达时，可在 `ask`、
`source add-research` 和受支持的生成器上使用 `--prompt-file PATH`。该文件只包含提示词文本；
上传来源文档请改用 `source add`。

## 输出与引用

请以结构化方式使用 JSON，而不要解析人类可读输出。常见的生命周期取值为：

- sources：`unknown`/`preparing`/`processing` -> `ready` 或 `error`；仅在 `ready` 时继续；
- artifacts：`pending`/`in_progress` -> `completed`、`failed` 或 `removed`；`not_found` 可能只是
  短暂的列表延迟。仅在 `completed` 时继续或下载。

对话 JSON 包含 `answer`、`conversation_id` 和 `references[].source_id`。引用的
`start_char`/`end_char` 是相对结构化来源文档的 UTF-16 偏移量，而不是相对扁平的
`SourceFulltext.content`。在 Python 中，使用
`from notebooklm import resolve_chat_reference_passage`，然后调用
`await resolve_chat_reference_passage(client, notebook_id, reference)`；它会使用精确的文档
区间，必要时回退到 `find_citation_context()`。

## 故障处理

出现故障时，先运行安全的只读诊断：

```bash
notebooklm auth check --test --passive --json
notebooklm list --json
notebooklm source list -n {notebook_id} --json
notebooklm artifact list -n {notebook_id} --json
notebooklm research status -n {notebook_id} --run-id {research_run_id} --json
```

只检查与失败工作流相关的命令。诊断期间不要改变任何状态。

- 退出码 0 表示成功。预期内的命令失败使用退出码 1。`source wait` 超时使用退出码 2；
  `artifact wait` 与 `research wait` 超时使用退出码 1。
- 先按退出码分支判断。常规已处理的 JSON 失败使用 `{error, code, message}`，而 wait
  命令返回领域信封，如 `{"status": "timeout", "error": "..."}`。
- 认证失败时，重新验证 `checks.token_fetch`；仅当它不为 `true` 时才登录。
- 等待超时时，报告该情况并检查确切的来源、产物或研究运行。
- 生成受 Google 速率限制。保留任务 ID、检查状态，且仅在用户授权时重试；
  不要无限循环。对于已存在的失败 Studio 产物，先查看
  `notebooklm artifact retry <artifact_id> -n {notebook_id} --help`，再决定是否原地重试。
- 协议错误时，记录已安装版本、确切命令、相关 ID 和脱敏后的错误信息。
  在有网络访问时检查项目的 issue 跟踪器；
  没有时不要凭空发明变通方案。

进度更新保持简短，并包含相关的返回 ID。绝不暴露凭证内容。

## Skill 安装

如果本文件已位于某个 Agent Skill 目录内，则该 Skill 本身已安装。否则：

- `notebooklm skill install` 安装或更新受支持的本地 Skill 目标。
- `notebooklm skill package` 构建可上传的归档，用于沙箱化的 Agent 环境。
- `notebooklm skill status --json` 报告已安装版本及 `content_mismatch`。
