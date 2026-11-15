> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/light--spring-launch/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 07-spring-launch（春日发布）

## 风格概览

浅绿渐变配嫩绿与黄绿配色，采用自然曲线 + 花瓣式版式，适合春季发布会、新品上市、季节营销等清新自然场合

- **场景**：春季发布会、新品上市、季节营销、品牌活动
- **气质**：清新、自然、有活力、元气、希望感
- **色调**：绿色调、浅色系、自然色、清新渐变
- **行业**：消费品、环保、健康、美妆、食品

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #E8F5E9 | background     |
| Primary        | #4CAF50 | primary        |
| Secondary      | #8BC34A | secondary      |
| Accent         | #81C784 | accent         |
| Dark           | #1B5E20 | dark           |
| Primary Text   | #1B5E20 | text_primary   |
| Secondary Text | #388E3C | text_secondary |
| Muted Text     | #66BB6A | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial Black     |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 浅绿渐变配嫩绿与黄绿配色
- 自然曲线版式
- 花瓣装饰元素
- 四叶草式排布
- 纵向时间轴设计
- Morph 切换动画
- 标准化装饰元素

## 页面结构（6 页）

| 页码  | 类型       | 元素数量 | 描述                                                                 |
| ----- | ---------- | -------- | -------------------------------------------------------------------- |
| S1    | hero       | 45       | 封面页：曲线分割 + 花瓣装饰 + 中央卡片                               |
| S2    | highlights | 55       | 亮点页：四叶草式交错排布卡片                                         |
| S3    | features   | 55       | 特性页：左侧产品 + 纵向特性流                                        |
| S4    | pricing    | 55       | 定价页：三栏定价卡片                                                 |
| S5    | timeline   | 50       | 时间轴页：嫩芽生长式纵向时间轴                                       |
| S6    | cta        | 50       | CTA 页：顶部绿色区 + 行动按钮                                        |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，曲线分割 + 花瓣装饰 + 中央卡片
- **Slide 5（timeline）**：时间轴页，嫩芽生长式纵向时间轴

不必通读，浏览 2-3 个代表页即可。
