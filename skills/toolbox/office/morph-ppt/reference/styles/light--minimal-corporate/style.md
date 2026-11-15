> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/light--minimal-corporate/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 02-minimal-corporate（极简企业报告）

## 风格概览

纯白底配深蓝与金点缀，采用左侧色块分割 + 纵向信息流版式，适合年报、工作总结、商业提案等场合

- **场景**：年报、工作总结、项目汇报、商业提案
- **气质**：专业、简洁、清晰、精致、沉稳
- **色调**：浅色调、暖色调、低对比
- **行业**：金融、咨询、企业、政府、教育

## 配色

| 名称            | Hex     | 用途           |
| --------------- | ------- | -------------- |
| Background      | #FFFFFF | background     |
| Card Background | #E8EEF4 | card           |
| Primary         | #1E3A5F | primary        |
| Secondary       | #D4A84B | secondary      |
| Primary Text    | #333333 | text_primary   |
| Secondary Text  | #666666 | text_secondary |
| Muted Text      | #999999 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial Black     |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial           |

## 设计手法

- 纯白背景，大量留白
- 深蓝与金的专业配色
- 简洁线条装饰
- 几何色块点缀
- 非对称网格版式
- 左侧色块分割版式
- 已修复坐标冲突

## 页面结构（6 页）

| 页码  | 类型       | 元素数量 | 描述                                                                              |
| ----- | ---------- | -------- | --------------------------------------------------------------------------------- |
| S1    | hero       | 50       | 封面页：左侧深蓝竖条 + 大标题 + 信息卡片                                          |
| S2    | statement  | 45       | 宣言页：左侧内容 + 右侧装饰区，已修复坐标冲突                                     |
| S3    | grid       | 60       | 网格页：非对称网格（上 2 下 4）                                                   |
| S4    | case       | 50       | 案例页：左右双卡对比                                                              |
| S5    | comparison | 50       | 对比页：中央 VS 分隔                                                              |
| S6    | thanks     | 40       | 致谢页：左侧致谢 + 右侧联系方式                                                   |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，左侧深蓝竖条 + 大标题 + 信息卡片

不必通读，浏览 2-3 个代表页即可。
