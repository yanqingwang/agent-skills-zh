> **中文汉化版** · 上游：[pbakaus/impeccable](https://github.com/pbakaus/impeccable) · 原文件：`.claude/skills/impeccable/reference/hooks.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# /impeccable hooks

管理当前项目的**设计检测 hook**。

hook 在直接编辑设计相关文件（`.tsx`、`.jsx`、`.html`、`.vue`、`.svelte`、`.astro`、`.css`、`.scss`、`.sass`、`.less`、`.ts`、`.js`）时运行 impeccable 设计检测器。Claude Code、Codex、Cursor 和 GitHub Copilot 用 post-tool-use hook，在编辑之后把一条简短的系统提醒推入 agent 上下文：有发现就给纠正提示，有待处理问题就再催一次，干净的 UI 类文件给一条简短确认，除非 quiet 模式开着（config 里的 `hook.quiet`）。纯 `.ts` 和 `.js` 文件照样扫描，但检测器没发现就保持安静。Grok Build 触发同样的 PostToolUse 扫描来标记被改过的文件，然后在 Stop 的 `additionalContext` 里浮出发现。不要期待 Grok 的每次编辑提醒：Grok 丢弃那段 stdout。在 Hermes Agent 上，每次编辑的发现直接出现在 `write_file` 或 `patch` 工具结果里，就是它的 `impeccable` 字段。

检测器规则分两档。每次编辑的 hook 只浮出即时档：机械、无歧义、值得打断一次编辑的问题，例如坏图、内容溢出、对比度与可读性失败、渐变文字、发光阴影、设计系统漂移。其余一切（文案节奏、色板与字体品味、布局节奏）推迟到 `Stop` hook 事件上的深度一轮：它对会话中触碰过的每个 UI 文件跑完整规则集，把剩下的发现一次性浮出，并与每次编辑那轮已报告过的去重。再没东西可报的会话安静收尾。在 `.impeccable/config.json` 里设 `hook.perEditRules` 为 `"all"` 可恢复每次编辑跑完整规则集。Stop 深度一轮为 Claude Code、Codex 和 Grok Build（它们派发原生 `Stop` hook 事件）以及 Hermes Agent（其插件从 `pre_verify` 发出）接线。Cursor 没有（它的 `stop` hook 只能用一条后续用户消息作答），GitHub Copilot 的 stop 类事件不把上下文回传给模型，所以它们保持每次编辑跑完整检测器。Grok 在 `end_turn` 之后还会触发一次只观察的 Stop，`reason: "shutdown"`：跳过那一次，只扫 `end_turn`。

每个 hook 都是一次机械扫描。扫描器抓不到的直觉反应住在 [craft-floor.md](craft-floor.md) 里，skill 在编辑 UI 之前加载它，所以无论有没有接 hook，它们都生效。没有自动 hook 的会话会从 `impeccable context` 收到一条 `MANUAL_DETECTOR_REQUIRED` 指令，要求最后跑一次检测器。

本命令通过编辑 `.impeccable/config.json`（统一的 Impeccable 配置；hook 运行时设置在其 `hook` 键下，共享的检测器忽略项在 `detector` 键下）**按项目**开关 hook。开发者个人层面的覆写，包括 CLI 记录的安装同意决定（`hook.consent`），住在 gitignore 掉的 `.impeccable/config.local.json` 里。设 `hook.enabled: false` 关掉 hook，设 `hook.quiet: true` 静音干净/待办的确认回执，把 `hook.auditLog` 设为文件路径可获得 NDJSON 日志。旧环境变量 `IMPECCABLE_HOOK_DISABLED`、`IMPECCABLE_HOOK_QUIET`、`IMPECCABLE_HOOK_LOG` 仍然生效，且在设置时覆盖这些 config 值。

项目使用 Blade、Twig、ERB 或 Handlebars 文件时，在 **`detector.extensions`** 下声明服务端模板扩展；否则 hook 会跳过它们，因为它们不在内建扩展列表里。一个扩展一条目，`{ "ext": ".blade.php", "engine": "html" }`。`engine` 选择分析器（标记模板用 `html`，类 JS/TS/CSS 文件用 `text`），默认 `html`。匹配按文件名结尾，所以 `.blade.php`、`.html.erb` 这样的双扩展名可用。config 只做增量；内建列表始终生效。

手动的 `.claude/skills/impeccable/scripts/impeccable detect` 扫描默认使用同一份项目过滤配置：`detector.ignoreRules`、`detector.ignoreFiles`、`detector.ignoreValues` 和 `detector.designSystem.enabled`。`hook.enabled` 只控制 hook 的自动执行，不管手动 CLI 扫描。要一次无视项目 config/上下文的裸检测器运行，用 `.claude/skills/impeccable/scripts/impeccable detect --no-config ...`。要直接对这些检测器忽略项做 CLI CRUD，用 `.claude/skills/impeccable/scripts/impeccable ignores ...`。

支持的 Harness：Claude Code（项目级安装用 `.claude/settings.local.json`；用户级安装用 `$CLAUDE_CONFIG_DIR/settings.json`，默认 `~/.claude/settings.json`；被挪进共享 `.claude/settings.json` 的项目 hook 也原地生效），Codex（项目里的 `.codex/hooks.json`），Cursor（项目里的 `.cursor/hooks.json`），Grok Build（项目里的 `.grok/hooks/impeccable.json`；要求 `/hooks-trust` 或 `--trust`），GitHub Copilot（项目里的 `.github/hooks/impeccable.json`，一份团队共享、入库提交的文件，Copilot CLI 和云端 agent 都读它），以及 Hermes Agent（`~/.hermes/plugins/` 里的 `impeccable-design-hook` 插件；用户用 `hermes plugins enable impeccable-design-hook` 启用一次；项目级安装的启动器只在 Hermes 信任的项目里运行，经 `hermes skills trust`）。对 Copilot CLI，`.github/hooks/impeccable.json` 提交进仓库默认分支后，仓库级 hook 即触发。

在 **Cursor** 上，hook 挂在 `Write` 工具（每次 agent 文件编辑）的 `postToolUse` 上，以 `additional_context` 返回提醒，Cursor 把它加在工具结果之后。更早建的项目跑的是一个 `preToolUse` 门（`hook-before-edit`），在坏写入落地前拦住；那条门仍然有效，直到 `hooks on`、`impeccable update` 或 `impeccable doctor --fix` 把条目挪到 `postToolUse`。

Gemini 在 `.gemini/settings.json` 里装 session 和 completion hook，合并进已有的设置（容忍注释；带注释的文件在重写前备份为 `settings.json.bak`，不是合法 JSON 的文件不动）。它不装每次编辑的检测器 hook。`BeforeTool` hook 只重写运行 `build-phase` 的 shell 命令，且只在 macOS 和 Linux 上；Windows 上（Gemini 经 PowerShell 跑 hook）没有 session id 到达 shell，comp 构建无法绑定会话，完成提醒保持沉默。

没有项目级 Claude skill 时，`hooks on` 会在 `CLAUDE_CONFIG_DIR`（默认 `~/.claude`）里找 `skills/impeccable/scripts/impeccable`，用已安装启动器的绝对路径把 hook 写进那个账号的 `settings.json`。相对账号目录按调用者的工作目录解析。显式账号目录是排他的：绝不用另一个账号的默认 skill 和设置顶替。status 和 context 读同一份账号设置。没有任何设计 Harness 可接线时，`hooks on` 直说，报告被跳过的无效设置或缺失的 skill 查找路径，并给出下一步。

status 检查每个 manifest 里当前的事件条目和匹配器，支持的地方包括 Stop 那一轮。项目设置文件（或其用户设置文件）之一含有当前条目，Claude Code 即算接线。旧命令、残缺 manifest 或文件缺失都报告为未接线。config 里启用但没有任何设计 Harness 接线时，status 直说，并给出修复命令 `impeccable hooks on`。已安装且已启用的 Hermes 设计 hook 插件也算接线；`on` 会承认它而不改插件配置。接线确认 manifest 条目；Harness 的信任要求和会话重载仍然适用。

项目的 `config.local.json` 里 `hook.consent` 为 `"accepted"` 且 hook 已启用时，`impeccable context` 会为已安装的 Harness skill 恢复缺失或过期的条目，并用一行报告修复。共享 config 里的同意不授权这次写入。自动修复保留无关的设置和 hook，不碰畸形 manifest。没有本地同意时，context 不写任何 manifest，保留 `MANUAL_DETECTOR_REQUIRED`，点名缺失或过期的 Harness 接线。被显式禁用的 hook 保持禁用。

## 路由

第一个参数是动作。默认 `status`。

| 动作 | 它做什么 |
|---|---|
| `status` | 打印当前状态、共享/本地 config 路径、被忽略的规则 / 文件 / 值、env 覆盖，以及每个 Harness 实际的 manifest 接线。 |
| `on` | 在 `.impeccable/config.json` 里设 `enabled: true`，把本地 hook 同意记录为 accepted，并在 skill 已安装时安装/修复各 provider 的 hook manifest。 |
| `off` | 在 `.impeccable/config.json` 里设 `enabled: false`。 |
| `ignore-rule <id>` | 把 `<id>` 追加进 `detector.ignoreRules`；`overused-font` 要求 `--all-values`。在整个项目压制该规则。 |
| `ignore-file <glob>` | 把 `<glob>` 追加进 `detector.ignoreFiles`。对匹配文件压制**全部**规则。 |
| `ignore-value <id> <value> [--shared] [--reason "..."]` | 把一条规则/值压制追加进共享的 `.impeccable/config.json`。 |
| `ignore-value <id> <value> --local [--reason "..."]` | 把一条私有的规则/值压制追加进 `.impeccable/config.local.json`。 |
| `ignore-value <id> "*" --file <glob> [--file <glob>...]` | 只在匹配文件里关掉一条规则，其余地方保持生效。重复 `--file`，或用 `--file=<glob>` / `--files=<glob>`。不带 `--file` 的裸 `"*"` 会被拒绝：真想全项目生效就用 `ignore-rule <id>`。 |
| `reset` | 删除项目 config、去重缓存和 Cursor 待处理队列，并从 `on` 安装过的每个 provider manifest 里移除 hook 条目，入库提交的 Copilot 文件也在内（`on` 从不写的团队共享 `settings.json` 绝不触碰）。 |

## 流程

1. 从用户参数解析动作。没给动作时默认 `status`。
2. 调用管理脚本，把用户的输出原样转达：

   ```bash
   .claude/skills/impeccable/scripts/impeccable hooks <action> [args...]
   ```

3. 动作为 `off` 时，补一句一行说明："完成。在你运行 `/impeccable hooks on` 之前，本项目的新编辑不会再触发设计 hook。"
4. 动作为 `on` 时，报告命令安装或修复了什么。没找到任何已安装的 skill 目录、或设置被跳过时，如实转达该结果，不要声称 hook 会运行。否则提示：Harness 必须先加载更新后的设置（并满足任何信任要求）才会运行。在 Hermes Agent 上，`on` 无法安装或启用插件：如果 `impeccable context` 报过 `MANUAL_DETECTOR_REQUIRED`，改让用户运行 `npx impeccable install`，然后 `hermes plugins enable impeccable-design-hook`。
5. 动作为 `ignore-value`、`ignore-file` 或 `ignore-rule` 时，只打印脚本输出。默认作用域是共享的 `.impeccable/config.json`；只在用户明确要求私有例外时加 `--local`。
6. 动作为 `status` 时，只打印脚本输出。除非用户追问，不加评论。

## 分诊发现

hook 自己绝不写忽略配置；每个例外都经 `impeccable hooks` 走。把每条发现分诊为三种结局之一：

- **真实设计问题**：修它。绝不为了跳过修复或把被拦的写入硬推过去而加忽略。
- **有把握的误报或获准的例外**：自己持久化最窄的忽略，并在回复里披露。门槛是你能点名的证据：有意的 demo 或 fixture、记录坏设计的文档、字面或符合领域语义的运动（一颗弹跳的球）、或用户已确认过的选择。把证据写进 `--reason`，格式 `"<谁决定的：证据>"`；只有用户真的确认过才写"用户确认"。
- **拿不准**：让发现留着，用一行说明原因。只有真的无法决定时才问用户。

自助只到 `ignore-value` 为止。`ignore-file` 和 `ignore-rule` 压制面太大，不能凭你自己的判断加；先问用户。

优先最窄的例外：

- 发现行给出 `ignore-value <rule> <value>` 对时，带上你的 `--reason` 传给 `impeccable hooks ignore-value`。这默认写进共享的 `.impeccable/config.json`。
- 对值级发现如 `overused-font` 和 `bounce-easing`，用 `ignore-value` 压那个具体值。不要对一款具体字体用 `ignore-rule overused-font`。
- 发现没有值级命令时，如 `side-tab`，把那一条规则按文件限定：`ignore-value <id> "*" --file <path>`。先跑 `.claude/skills/impeccable/scripts/impeccable detect <path>` 看那里实际触发什么。
- 只有当整个文件都不在设计评审范围之内时才动 `ignore-file <path>`：一个 fixture、一份生成产物、一个故意的 slop demo。它会永久压制该文件的全部规则，包括还没写出来的规则。一个只有一个吵闹规则的真实 UI 表面，想要的是上面的文件级值忽略。
- 只在用户要求把整条规则全项目压制时才用 `ignore-rule <id>`。要广泛压制 overused-font，只在用户要求一般性忽略滥用字体时才用 `ignore-rule overused-font --all-values`。
- 默认优先 config 忽略（上面的命令）；它们把压制放在一个可评审的地方。只有当豁免必须随一个离开仓库的单文件走（生成/导出的独立文档、邮件里的 HTML 文件）时才用行内注释。受支持的标记是 `impeccable-disable <rule>`（整个文件）或 `impeccable-disable-line` / `impeccable-disable-next-line`（单行），任意注释语法均可，`:` 或 `--` 之后可带原因。检测器默认认可它；`--no-inline-ignores` 或 `--no-config` 绕过它。

值级例外示例：

```bash
.claude/skills/impeccable/scripts/impeccable hooks ignore-value overused-font Inter --shared --reason "User confirmed Inter is intentional"
```

自助例外示例，证据点名：

```bash
.claude/skills/impeccable/scripts/impeccable hooks ignore-value bounce-easing bounce-ball --shared --reason "Agent: literal ball-bounce animation, bounce easing is the subject"
```

整规则字体例外示例：

```bash
.claude/skills/impeccable/scripts/impeccable hooks ignore-rule overused-font --all-values --reason "User asked to ignore overused fonts generally"
```

单文件单规则例外示例，该文件其余部分仍值得评审：

```bash
.claude/skills/impeccable/scripts/impeccable hooks ignore-value design-system-font-size "*" --file "src/overlay/widget.js" --reason "Injected widget builds its own type scale; DESIGN.md's ramp describes the site"
```

整文件例外示例，该文件完全在范围之外：

```bash
.claude/skills/impeccable/scripts/impeccable hooks ignore-file "src/legacy/Card.tsx"
```

## 约束

- 绝不从本命令手改 `.impeccable/config.json` 或 `.impeccable/config.local.json`。始终经 `impeccable hooks` 走，写入才有校验、文件形状才一致。唯一例外：`detector.extensions` 没有管理动作，用户要求覆盖一套模板栈时，直接编辑 `.impeccable/config.json` 里这一个字段，文件其余部分不动。
- 不要在这条流程里编辑 `impeccable hook` 和 `impeccable hook-before-edit` 背后的启动器或二进制。那是 skill 的管线。
- 用户问 hook 该信到什么程度时，如实说：它带着 agent 的环境和网络访问不加沙箱地运行引擎（`.github/hooks/impeccable.json` 提交后，Copilot 云端 agent 里也一样），且启动器在首次运行前对照 `.claude/skills/impeccable/scripts/engine-checksums.txt` 校验下载的引擎；**绝不**说它是沙箱化的。
- hook 绝不阻塞编辑；它发出编辑后的提醒。（还在旧 `preToolUse` 门上的 Cursor 项目可以拦写入，直到 manifest 迁移。）禁用即停止提醒。
- hook 随 Impeccable skill 打包。项目级安装用 `.claude/settings.local.json`、`.codex/hooks.json`、`.cursor/hooks.json`、`.github/hooks/impeccable.json` 和 `.gemini/settings.json`；用户级 Claude 安装用当前账号的 `$CLAUDE_CONFIG_DIR/settings.json`（默认 `~/.claude/settings.json`）。Codex 上，用户首次须经 `/hooks` 批准 hook。Cursor 上，确认 Settings -> Hooks 下 hook 已启用。GitHub Copilot 上，`.github/hooks/impeccable.json` 提交进仓库默认分支后 CLI 才加载它，云端 agent 直接从仓库读。

## 失败模式

- `.impeccable/config.json` 或 `.impeccable/config.local.json` 不可读或畸形时，hook 忽略该文件，用剩余的有效 config/默认值。`impeccable hooks status` 会把畸形文件显示为已忽略。
- 用户要求全局"禁用 hook"时，先给 `/impeccable hooks off`（对本项目持久；向 config 写入 `hook.enabled: false`）。旧环境变量 `IMPECCABLE_HOOK_DISABLED=1` 也可作为跟随 shell 的一次性覆写。
