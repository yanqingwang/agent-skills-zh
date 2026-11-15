> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/dark--investor-pitch/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 08-investor-pitch（投资路演专业版）

## 风格概览

深蓝专业基调配红色强调，适合投资路演、融资演示、商业计划等场景

- **场景**：投资路演、融资演示、商业计划、创业展示
- **气质**：专业、可信、沉稳、进取
- **基调**：暗色调、冷色、专业的蓝红搭配
- **行业**：风险投资、科技、金融、企业服务

## 配色

| 名称            | Hex     | 用途           |
| --------------- | ------- | -------------- |
| Background      | #1A1A2E | background     |
| Card Background | #16213E | card           |
| Auxiliary       | #0F3460 | secondary      |
| Accent          | #E94560 | accent         |
| Primary Text    | #FFFFFF | text_primary   |
| Secondary Text  | #B8B8D1 | text_secondary |
| Muted Text      | #6B6B8D | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial Black     |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 深蓝专业基调
- 红色强调关键数据
- 数据可视化图表
- 几何线条装饰
- 清晰的信息层级
- Morph 切换动画

## 页面结构（6 页）

| 页码  | 类型        | 元素数量 | 描述                                                     |
| ----- | ----------- | -------- | -------------------------------------------------------- |
| S1    | hero        | 68       | 封面页：公司 Logo + 项目名 + 融资信息                    |
| S2    | problem     | 56       | 问题页：行业痛点 + 市场机会                              |
| S3    | solution    | 75       | 方案页：解决方案 + 产品展示                              |
| S4    | market      | 55       | 市场页：市场规模 + 竞争格局                              |
| S5    | financial   | 57       | 财务页：财务数据 + 增长预测                              |
| S6    | fundraising | 72       | 融资页：融资需求 + 联系方式                              |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，公司 Logo + 项目名 + 融资信息

不必通读，浏览 2-3 个代表页即可。
