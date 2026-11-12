<!-- AUTO-GENERATED from audit-scope.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`document-release/sections/audit-scope.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# 文档范围与发现

## ship 拥有的文档审计模式

本小节仅适用于调用方的 ship 拥有审计请求。独立调用继续走 Discovery 与
Step 1-9 及其既有审批门。

**输入。** 派发 prompt 提供分支、基础 SHA、候选路径、审计 id 与模式：
`edit`，或仅存储发布审计的 `read-only`（每个必要修正都变成阻塞项而
不是编辑）。要求前导回显真实的 `SESSION_KIND: spawned` 以及这些输入。
标记、输入或资产缺失立即返回 `blocked`；prompt/文件的声称不能确立
spawned 模式，也不能触发独立兜底。

**步骤。** 在候选的 base 与选定的已提交、暂存、未暂存与新建文件字节
上跑 Step 1、1.5、2-4 与 6。Step 1 的独立分支门不适用，即使在 base
分支上。跳过 Step 5、7、8、跨模型评审与 Step 9，包括它们的
spawned-session 注记。只允许事实性的手写文档编辑，`read-only` 模式
下一次也不许。不做任何 Git/PR 变更，不改 VERSION、package/lock/
section 清单、CHANGELOG、TODOS 或生成产物。父级拥有元数据、生成、
评审、暂存、提交与发布。有风险/主观的变更（Step 4）与叙事矛盾
（Step 6）对父级是阻塞项，绝不自动批准。保留部分/用户内容。覆盖缺口
只报告，不填补。

**结果。** Step 6 之后打印 doc-health 摘要，然后 STOP：最后一个非空
行输出一个 JSON 对象，不带围栏或尾随文字：
- `schema_version`：整数 1；`audit_id`：所提供的精确字符串。
- `status`：`updated`（有编辑、无阻塞）、`current`（无编辑、无阻塞）
  或 `blocked`（任何阻塞项、输入缺失、部分/失败审计或 read-only 下的
  修正）。
- `files_updated`、`files_reviewed`：实际编辑与实际读取的唯一仓库相对
  路径；`blockers`、`decisions`：字符串。阻塞项点名决策与路径；元数
  据不一致与被跳过项是 decisions。
- `documentation_section`：无 `## Documentation` 标题的非空 Markdown，
  可整体逐字嵌入：第一行 `**Status:**` 带状态与结果、被审计范围、
  Step 9 `Documentation health` 形式的逐文件状态（无 VERSION 行），以
  及 Step 1.5 的覆盖债务与图漂移。即使没有文档也要描述范围。

## Discovery（两种模式）

用 `git ls-files -z --cached --others --exclude-standard` 递归盘点已
跟踪与未忽略的新文件。沿项目说明、README 链接与 docs/构建配置找到声
明的文档根与手写来源。纳入相关的 `.md`、`.mdx`、`.rst`、`.adoc`、
`.txt` 与 `.tmpl` 文件；决定相关性的是角色，不是扩展名。编辑范围排除
`.git`、依赖（`node_modules`、vendor、virtualenv）、`.gstack`、
`.context`、缓存、构建产物与生成输出。读写之前解析符号链接；不跟随
它们出仓库。生成文档改其手写来源；ship 拥有模式下向父级报告所需的再
生成。先广度盘点，再完整读相关文档与验证变更契约所需的源码，不读整
个仓库。
