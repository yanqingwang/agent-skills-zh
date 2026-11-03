# 散文引用件汉化规范（translated_prose）

> 本文件规范 `references/*.md` 等**人读行为规范**的汉化。原则 #11 更新：散文引用件不再一律原样复制，
> 已汉化者登记进 manifest 的 `translated_prose` 清单，走"上游变更 → 重译工单"路径，不被自动覆盖。

## 判定：哪些该汉化

| 类型 | 处理 | 例子 |
|---|---|---|
| 人读的行为规范、流程说明、检查清单、写作指南 | **汉化** | `references/knowledge-map.md`、`references/feynman.md`、`references/citation_styles.md` |
| 机器解析的数据/词表/格式定义 | **不汉化**（原样） | `languages/python.md`（语法解析表）、`locales/zh.md`（本地化词条）、`assets/*.csv` |
| 模板骨架（字段名即功能标识） | 字段名不译，说明文字译 | `assets/manuscript_scaffold.md`（占位符保留英文） |
| 素材、示例数据 | 不汉化 | `assets/music/cues/*.md` |

## 翻译规则

1. **frontmatter**：散文件通常无 frontmatter；有则键结构保持一致
2. **声明块**：每个已汉化散文文件在文件开头加声明块（三行格式同 SKILL.md）：

   ```
   > **中文汉化版** · 上游：[<repo>](<repo url>) · 原文件：`<upstream path>` · License: <license>
   > 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
   > 术语以 [GLOSSARY.md](<相对路径>) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。
   ```

   GLOSSARY.md 相对路径按文件所在深度计算（`skills/<角色>/<类别>/<skill>/references/x.md` → `../../../../../GLOSSARY.md`）
3. **代码块与行内代码**：逐字节保留不译
4. **功能性标记**：占位符（`[topic]`、`{name}`）、枚举值、字段名、库名、命令、路径、ID、URL 保留英文
5. **结构**：标题层级、列表、表格与源一一对应，不增删章节
6. **术语**：按 [GLOSSARY.md](GLOSSARY.md)；学科术语按业界惯例（如 literature review→文献综述、power analysis→功效分析）

## 同步机制

- 已汉化散文登记在 manifest 的 `translated_prose`（从 `verbatim` 移出）
- `scripts/sync_daily.py` 对 `translated_prose` 与 SKILL.md 同等对待：上游 blob 变更 → 开重译工单
- `scripts/fetch_verbatim.py` 只处理 `verbatim`，不触碰已汉化散文
- 重译工单销单条件：文件声明块的同步日期 ≥ 首次发现日期
