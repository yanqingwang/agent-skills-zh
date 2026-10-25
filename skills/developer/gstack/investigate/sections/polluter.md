<!-- AUTO-GENERATED from polluter.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`investigate/sections/polluter.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## 污染者配方

污染者是一个较早的测试泄漏了受害者依赖的状态：受害者单独跑通过，
在整个套件或某个分片里失败。

1. **从 CI 日志拿文件顺序。** 分片 runner 按执行顺序打印文件清单。
   取失败分片中受害者之前跑过的文件（`gh run view <run-id> --log`，
   或本地分片清单
   `bun --no-env-file --config=/dev/null run scripts/ship-measure.ts free --shard <I>`，它复现 `bun run test` 用的确切打包）。
2. **确认依赖关系。** 受害者单独跑通过；受害者跟在较早文件之后跑
   失败（`<affected-files>` 是较早文件加受害者，按分片顺序逗号连接）：
   ```bash
   bun --no-env-file --config=/dev/null run scripts/ship-measure.ts free --files <failing-test-file> --reruns 3
   bun --no-env-file --config=/dev/null run scripts/ship-measure.ts free --files <affected-files> --reruns 3
   ```
3. **二分较早文件。** 把较早列表对半砍，留下仍让受害者失败的一半，
   重复直到只剩一个文件。每步是一次 `--files` 运行；每步都记录当前
   列表。
4. **点名泄漏物。** 读污染者，找出活得比它久的状态：环境变量、
   `process.cwd()`、`process.exitCode`、模块级缓存或单例、没卸载的
   mock 或 spy、还在监听的服务器或 watcher、共享路径下的临时文件、
   home 目录下的 learnings 或状态文件（free lane 的 home 守卫会报告
   这些）、全局定时器。
5. **修污染者，不修受害者。** 在状态产生处恢复或隔离它
   （`afterEach`、`mkdtemp`、私有 env）；给受害者加依赖顺序的
   `beforeEach` 只是把泄漏藏给下一个受害者。
6. **报告：** `POLLUTER: <file> leaked <what> into <victim>; fixed by
   <change>`，附二分日志。污染者在 main 上时，受害者的失败与本 PR
   无关（按 flake 配方的证据节路由）。
