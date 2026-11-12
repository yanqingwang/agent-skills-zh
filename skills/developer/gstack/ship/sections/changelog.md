<!-- AUTO-GENERATED from changelog.md.tmpl — do not edit directly -->
<!-- Regenerate: bun run gen:skill-docs -->
> **中文汉化版** · 上游：[garrytan/gstack](https://github.com/garrytan/gstack) · 原文件：`ship/sections/changelog.md` · License: MIT
> 翻译日期：2026-10-26 · 同步状态：上游 HEAD（2026-10-26 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与生成注释保持原文。本文件为翻译作品，非上游官方中文版。

## Step 13：CHANGELOG（自动生成）

1. 读 `CHANGELOG.md` 头部，弄清格式。

2. **先枚举分支上的每个 commit：**
   ```bash
   git log origin/<base>..HEAD --oneline
   ```
   拷贝完整清单。数一数 commit 数。你要把它当检查清单用。

3. **读完整 diff**，理解每个 commit 实际改了什么：
   ```bash
   git diff origin/<base>
   ```

4. **动笔前先按主题分组。** 常见主题：
   - 新功能 / 新能力
   - 性能改进
   - bug 修复
   - 死代码清理
   - 基础设施 / 工具链 / 测试
   - 重构

5. **写 CHANGELOG 条目**，覆盖全部分组：
   - 分支上既有的 CHANGELOG 条目已覆盖部分 commit 时，用一个统一的新
     版本条目替换它们
   - 把变更归入适用小节：
     - `### Added`：新功能
     - `### Changed`：对既有功能的变更
     - `### Fixed`：bug 修复
     - `### Removed`：移除的功能
   - 写简洁、有描述性的 bullet
   - 插在所观察到文件头之后、第一个版本条目之前，日期为今天
   - 格式：`## [X.Y.Z.W] - YYYY-MM-DD`
   - **口吻：** 先说用户现在能**做**什么（以前做不到）。用平实语言，
     不写实现细节。绝不提 TODOS.md、内部跟踪或面向贡献者的细节。

6. **交叉检查：** 把你的 CHANGELOG 条目与第 2 步的 commit 清单对比。
   清单中每个面向用户的变更都必须出现；补上缺的。无用户可见影响的
   commit（merge、版本号 bump、修本分支早前引入的工作）不需要
   bullet。条目必须反映每个面向用户的主题。

**不要让用户描述变更。** 从 diff 与 commit 历史推断。

**NO_VERSION（Step 12）：** 跳过本步；不写 CHANGELOG 条目或版本头。

---
