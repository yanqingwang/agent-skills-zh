<!-- AUTO-GENERATED from detector-install-offer.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
<!-- Derived in part from nothing third-party: gstack's own consent flow for downloading impeccable's engine (Apache-2.0, see NOTICE.md). -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`design-html/sections/detector-install-offer.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

# 设计检测器：一次性安装提议

仅在 Setup 探针打印了 `DESIGN_DETECTOR_INSTALL_OFFER` 时读本节。它与
`/design-review` 问的是同一个问题；哪个设计 Skill 先跑就由哪个来问，
答案会被记住。

**安装提议（一个问题，只问一次）。** 探针打印了
`DESIGN_DETECTOR_INSTALL_OFFER: version=<v> platform=<p> bytes=<n> dest=<path>`
时，说明用户从未回答过。现在问，先于任何其他步骤，且仅在交互会话中：
`SESSION_KIND: spawned` 或无头运行下，绝不安装也绝不发问；按"暂不"作答
继续。Conductor 中把简报渲染为文字并 STOP。用本 Skill 的
AskUserQuestion 格式：

```
D<N> — Install impeccable's design detector engine?
Project/branch/task: <one line from the current work>
ELI10: impeccable is a separate Apache-2.0 tool (Paul Bakaus). Its engine is one <n>-byte program that checks pages and CSS for 61 mechanical design mistakes. gstack can download that one file (version <v>, from github.com/pbakaus/impeccable releases) into <dest>, check it against a checksum recorded in gstack, and log the download in ~/.gstack/security/egress.jsonl. No impeccable skill, no editor hook; the engine never touches the network when gstack runs it. Without it this skill works as it does today.
Stakes if we pick wrong: yes puts a third-party binary on this machine; no leaves machine-catchable design mistakes to judgment alone.
Recommendation: A because the download is pinned, logged, and reversible (delete <dest>).
Note: options differ in kind, not coverage — no completeness score.
Pros / cons:
A) Install the engine now (recommended)
  ✅ Every design review opens with 61 deterministic checks, tagged by rule id
  ✅ One checksum-verified file under your home directory, logged, removable with rm
  ❌ A third-party binary you did not build runs over your project files in scans
B) Not now
  ✅ Nothing changes on this machine; the question returns next time a design skill runs
  ❌ Design reviews keep relying on judgment alone for mistakes a machine can catch
C) Never ask again
  ✅ Design skills stay silent about impeccable (reversible: gstack-config set design_detector_install_prompted false)
  ❌ An engine you install later is still used, but gstack never reminds you
D) Turn the detector off
  ✅ No probe, scan, or handoff line in any design skill (gstack-config set design_detector off)
  ❌ An engine installed later is ignored until design_detector is back to auto
Net: a pinned, logged 16 MB download for machine-checked findings, versus every design check staying a judgment call.
```

选 **A** 时，运行安装并读其第一行（`IMPECCABLE_INSTALLED: <path>` 加
新的探针行；或 `IMPECCABLE_INSTALL_REFUSED: <reason>`，此后本 Skill
不带扫描继续）：

```bash
bun --no-env-file --config=/dev/null run $HOME/.claude/skills/gstack/bin/gstack-design-detect.ts install --host claude
```

选 **B** 不带扫描继续。选 **C** 运行
`~/.claude/skills/gstack/bin/gstack-config set design_detector_install_prompted true`。
选 **D** 运行
`~/.claude/skills/gstack/bin/gstack-config set design_detector off`。
绝不自己传 `--sha256` 或 `--base`：它们是给维护者和镜像用的。用户若
还想要 `/impeccable` Skill 及其 hook，由他们自己跑
`npx impeccable install`；gstack 绝不代劳。
