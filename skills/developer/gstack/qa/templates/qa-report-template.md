> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`skills/developer/gstack/qa/templates/qa-report-template.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# QA 报告：{APP_NAME}

| 字段 | 值 |
|-------|-------|
| **日期** | {DATE} |
| **URL** | {URL} |
| **分支** | {BRANCH} |
| **提交** | {COMMIT_SHA} ({COMMIT_DATE}) |
| **PR** | {PR_NUMBER} ({PR_URL}) 或 "—" |
| **档位** | Quick / Standard / Exhaustive |
| **范围** | {SCOPE or "Full app"} |
| **探测预算 / 受守卫命令时长** | {CONFIGURED LIMIT / SUM OF MEASURED COMMAND SPANS} |
| **访问页面数** | {COUNT} |
| **截图数** | {COUNT} |
| **框架** | {DETECTED or "Unknown"} |
| **手机** | {Chromium device profiles emulated, or "—"}；仍需真机测试（/ios-qa）：{what, or "—"} |

## 健康分：{SCORE}/100

| 类别 | 得分 |
|----------|-------|
| Console | {0-100} |
| Links | {0-100} |
| Visual | {0-100} |
| Functional | {0-100} |
| UX | {0-100} |
| Performance | {0-100} |
| Accessibility | {0-100} |

## Top 3 待修复项

1. **{ISSUE-NNN}: {title}** — {one-line description}
2. **{ISSUE-NNN}: {title}** — {one-line description}
3. **{ISSUE-NNN}: {title}** — {one-line description}

## Console 健康

| 错误 | 次数 | 首次出现 |
|-------|-------|------------|
| {error message} | {N} | {URL} |

## 摘要

| 严重级别 | 数量 |
|----------|-------|
| Critical | 0 |
| High | 0 |
| Medium | 0 |
| Low | 0 |
| **合计** | **0** |

## 问题

### ISSUE-001: {Short title}

| 字段 | 值 |
|-------|-------|
| **严重级别** | critical / high / medium / low |
| **类别** | visual / functional / ux / content / performance / console / accessibility |
| **URL** | {page URL} |

**描述：** {What is wrong, expected vs actual.}

**复现步骤：**

1. 打开 {URL}
   ![Step 1](screenshots/issue-001-step-1.jpg)
2. {Action}
3. **观察：** {what goes wrong}
   ![Result](screenshots/issue-001-result.jpg)

---

## 已应用的修复（如适用）

| 问题 | 修复状态 | 提交 | 变更文件 |
|-------|-----------|--------|---------------|
| ISSUE-NNN | verified / best-effort / reverted / deferred | {SHA} | {files} |

### 修复前/修复后证据

#### ISSUE-NNN: {title}
**修复前：** ![Before](screenshots/issue-NNN-result.jpg) — Phase 5 的证据（静态 bug 用 `issue-NNN.png`）
**修复后：** ![After](screenshots/issue-NNN-after.jpg)

---

## 回归测试

| 问题 | 测试文件 | 状态 | 描述 |
|-------|-----------|--------|-------------|
| ISSUE-NNN | path/to/test | committed / deferred / skipped | description |

### 延后的测试

#### ISSUE-NNN: {title}
**前置条件：** {setup state that triggers the bug}
**操作：** {what the user does}
**预期：** {correct behavior}
**延后原因：** {reason}

---

## 发布就绪度

| 指标 | 值 |
|--------|-------|
| 健康分 | {before} → {after} ({delta}) |
| 发现问题数 | N |
| 已应用修复 | N（verified: X，best-effort: Y，reverted: Z） |
| 已延后 | N |

**PR 摘要：** "QA found N issues, fixed M, health score X → Y."

---

## 回归（如适用）

| 指标 | 基线 | 当前 | 变化 |
|--------|----------|---------|-------|
| 健康分 | {N} | {N} | {+/-N} |
| 问题数 | {N} | {N} | {+/-N} |

**基线后已修复：** {list}
**基线后新增：** {list}
