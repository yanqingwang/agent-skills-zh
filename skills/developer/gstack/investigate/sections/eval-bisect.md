<!-- AUTO-GENERATED from eval-bisect.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`investigate/sections/eval-bisect.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Eval 二分配方

一个带评审或带评分的指标在两个版本之间回归了。二分的是输入，不是
commit；付费 judge 放到最后花。

1. **只保留实质不同的版本。** `git log --oneline <good>..<bad> -- <prompt 与
   resolver 路径>`；展开后 prompt 字节完全相同的 commit 合并掉（在每个
   版本用真实 builder 构建 prompt 并比对哈希；渲染出相同字节的模板
   编辑不是候选）。
2. **先用便宜的缓存评分器。** 用确定性或廉价的检查（结构 judge、
   token 计数、最低档的质量 judge）给每个实质版本打分，结果按
   `(revision, case)` 缓存在 `.gstack/tmp/eval-bisect/` 下。按便宜分
   做二分；只在便宜评分器与上报回归不一致的那两个版本上花付费
   judge。
3. **分离式运行。** 付费 case 经文档化的分离 runner 发起
   （`bun run eval:bg:pr`），轮询日志找
   `### gstack-detach EXIT=<code> ###`，并持有 eval 锁。绝不重试付费
   case；启动失败在报告里记为启动失败，不是第二个样本。
4. **报告。** 首个坏版本及其 prompt diff、每个版本的便宜分与付费分
   （标出缓存命中）、预注册的评审面板规模与每次尝试、以及没有跑的
   case。
