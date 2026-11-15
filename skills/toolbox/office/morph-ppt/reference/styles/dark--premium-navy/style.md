> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/dark--premium-navy/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 05-premium-navy（高级藏青与金）

## 风格概览

深藏青底色配金色与钢蓝点缀，营造高级的企业级视觉语言。

- **场景**：高端企业、年度战略、董事会报告
- **气质**：权威、精致、高级、可信
- **基调**：深藏青底 + 金色高光 + 钢蓝辅助

## 配色

| 名称          | Hex      | 用途                                                   |
| ------------- | -------- | ------------------------------------------------------ |
| 深藏青        | `0C1B33` | 背景                                                   |
| 浓郁金        | `C9A84C` | 金色横线、边框、圆点、数字点缀                         |
| 纯白          | `FFFFFF` | 标题文字                                               |
| 中藏青        | `1E3A5F` | 竖线、边框底色                                         |
| 钢蓝          | `8EACC1` | 点缀圆、描述文字                                       |
| 藏青强调      | `2C4F7C` | 卡片背景                                               |

## 字体排印

| 角色             | 字体           | 字号    | 颜色   |
| ---------------- | -------------- | ------- | ------ |
| 主标题           | Segoe UI Black | 60pt    | FFFFFF |
| 副标题           | Segoe UI Light | 24pt    | C9A84C |
| 卡片数字         | Segoe UI Black | 48pt    | C9A84C |
| 卡片标题         | Segoe UI Black | 22pt    | FFFFFF |
| 卡片描述         | Segoe UI Light | 14pt    | 8EACC1 |
| 数据数字         | Segoe UI Black | 54-64pt | FFFFFF |
| 辅助说明         | Segoe UI Light | 16-18pt | 8EACC1 |

## 设计手法

- **金色细线分隔**：金色横线（height=0.08cm）、藏青竖线（width=0.06cm），构建精致网格
- **半透明边框**：`roundRect` 作卡片底（透明度 0.12-0.45），金色与藏青交替
- **金色圆点点缀**：小 `ellipse` 作视觉锚点，金色透明度 0.6，白色透明度 0.3
- **暗底高对比**：白色标题 + 金色副标题，在深藏青上形成强层级
- **Morph 动画**：金线与边框跨页重新排布，边框变形为数据区背景

## 场景元素

共 8 个场景元素，每页位置不同：

| 名称             | preset    | fill   | opacity | 典型尺寸      | 描述                  |
| ---------------- | --------- | ------ | ------- | ------------- | --------------------------- |
| `!!bar-gold`     | rect      | C9A84C | 1.0     | 18cm x 0.08cm | 金色横线                    |
| `!!bar-navy`     | rect      | 1E3A5F | 1.0     | 0.06cm x 14cm | 藏青竖线                    |
| `!!frame-gold`   | roundRect | C9A84C | 0.15    | 8cm x 6cm     | 金色半透明边框              |
| `!!frame-navy`   | roundRect | 1E3A5F | 0.30    | 10cm x 6cm    | 藏青半透明边框              |
| `!!accent-gold`  | ellipse   | C9A84C | 0.20    | 3cm x 3cm     | 金色点缀圆                  |
| `!!accent-steel` | ellipse   | 8EACC1 | 0.15    | 4cm x 4cm     | 钢蓝点缀圆                  |
| `!!dot-gold`     | ellipse   | C9A84C | 0.60    | 1.5cm x 1.5cm | 金色小圆点                  |
| `!!dot-white`    | ellipse   | FFFFFF | 0.30    | 1cm x 1cm     | 白色小圆点                  |

## 页面结构

共 5 页，第 2-5 页设置 `transition=morph`：

| 页码    | 类型                  | 描述                                                                                                                 |
| ------- | --------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Slide 1 | Hero                  | 居中大标题白字 + 金色副标题，金线横贯中部                                                                            |
| Slide 2 | Statement             | 大字宣言，金线与边框重新排布                                                                                         |
| Slide 3 | 3-Column Pillars      | 金线作栏顶分隔线，三张 roundRect 卡片（透明度 0.12）并排，编号 + 标题 + 描述                                          |
| Slide 4 | Metrics / Performance | 金色边框放大为数据背景区，展示 $128M / 34% / #1 等指标                                                               |
| Slide 5 | CTA / 结尾            | 边框缩小为角落点缀，居中大标题 + 金色副标题                                                                          |

## 参考脚本

完整构建脚本见 `build.sh`。
**建议阅读以下页理解核心设计手法**：

- **Slide 1（Hero）**：8 个场景 actor 的初始布局，金线 + 边框 + 圆点的组合
- **Slide 3（Pillars）**：边框变形为卡片底，金线变成栏顶分隔线
- **Slide 4（Metrics）**：边框放大并变色为数据区背景的进阶技巧

不必通读，浏览 2-3 个代表页即可。
