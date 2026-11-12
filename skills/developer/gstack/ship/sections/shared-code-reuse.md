<!-- AUTO-GENERATED from shared-code-reuse.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/shared-code-reuse.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

**仅在持有完整结构证据时复用一条被跳过的共享代码建议：**

1. **读证据。** 读全部支撑调用方与 helper 目的地。确立第一方原创归属，
   并判断当前抽取是否值得；这一点 checker 定不了。保留
   `evidence_paths`/`helper_target`。
2. **跑 checker。** 在仓库根，把当前发现作为字面 JSON 从 stdin 传入。
   REVIEW_START 换成本次 pass 捕获的 token，示例路径/符号换成本实际
   证据。保留带引号的分隔符。

```bash
"$HOME/.claude/skills/gstack/bin/gstack-review-log" --check-shared-libs REVIEW_START <<'GSTACK_SHARED_LIBS_REUSE_JSON'
{"advisory":true,"severity":"INFORMATIONAL","evidence_paths":["src/caller-a.ts","src/caller-b.ts"],"helper_target":{"path":"src/shared.ts","symbol":"sharedHelper"}}
GSTACK_SHARED_LIBS_REUSE_JSON
```

3. **按结果行事。** 读 JSON。只有 `reusable: true` 允许抑制。False、
   命令失败或输出不可读都要求重新做源码评审并做新决策，绝不是抑制。
   不要自己提供快照、既往记录或覆盖。
4. **经 logger 持久化。** logger 会重算最终覆盖；绝不要自己提供证明。
   真实缺陷照常走 Fix-First，不受影响。

**可复用结果证明了什么（不要自己重构这些检查）：**
- 同一性：`sharedLibsFingerprint` 加真实的仓库、原始分支与当前快照。
  checker 读 REVIEW_START 但不消费/替换它。净化过的分支名不是同一性。
- 既往决策：completed/converged 评审、已验证的绑定、显式 Skip 与
  logger 记录版本的 `snapshot_covered_paths`；更旧的无版本覆盖需要新
  决策。
- 来源：`canReuseSharedLibsAdvisory` 要求每条支撑路径的原始文件与其
  blob 逐字节一致。排除 assume-unchanged、skip-worktree 与 sparse
  index 条目；符号链接/祖先目录、子模块、被忽略/仓库外或不可读文件；
  活跃/未知的 Git filter、编码与换行转换。
- 安全检视：禁用 fsmonitor 与可选锁；绝不使用外部 diff/textconv。
  未知证据 fail-closed。
