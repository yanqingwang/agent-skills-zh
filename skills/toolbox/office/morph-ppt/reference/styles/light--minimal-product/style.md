> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/light--minimal-product/style.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 05-minimal-product（极简产品展示）

## 风格概览

浅灰背景配深灰主色与绿色点缀的极简风格，采用居中聚焦 + 极简留白版式，适合产品发布、技术展示、商务演示等场合

- **场景**：产品发布、技术展示、品牌介绍、商务演示
- **气质**：专业、现代、极简、高级、科技感
- **色调**：冷色调、低饱和、高对比
- **行业**：科技、电子、软件、互联网、金融

## 配色

| 名称           | Hex     | 用途           |
| -------------- | ------- | -------------- |
| Background     | #FAFAFA | background     |
| Primary        | #2D3436 | primary        |
| Accent         | #00B894 | accent         |
| Secondary      | #636E72 | secondary      |
| Primary Text   | #2D3436 | text_primary   |
| Secondary Text | #636E72 | text_secondary |
| Muted Text     | #B2BEC3 | text_muted     |

## 字体排印

| 元素     | 字体            |
| -------- | --------------- |
| title_en | Arial           |
| title_cn | Microsoft YaHei |
| body     | Microsoft YaHei |
| data     | Arial Black     |

## 设计手法

- 浅灰背景配深灰主色与绿色点缀
- 居中聚焦版式
- 极简留白设计
- 细线装饰
- 高对比设计
- Morph 切换动画
- 标准化装饰元素

## 页面结构（6 页）

| 页码  | 类型       | 元素数量 | 描述                                                                    |
| ----- | ---------- | -------- | ----------------------------------------------------------------------- |
| S1    | hero       | 45       | 封面页：居中标题 + 底部细线 + 品牌信息                                  |
| S2    | product    | 50       | 产品页：中央产品展示 + 左右特性亮点                                     |
| S3    | features   | 55       | 特性页：两排特性卡片                                                    |
| S4    | compare    | 50       | 对比页：中央 VS 分隔 + 左右对比                                         |
| S5    | highlights | 50       | 亮点页：中央超大数字 + 数据卡片                                         |
| S6    | cta        | 45       | CTA 页：中央大按钮 + 联系方式                                           |

## 参考脚本

完整构建脚本见 `build.sh`。

**建议阅读以下页理解核心设计手法**：

- **Slide 1（hero）**：封面页，居中标题 + 底部细线 + 品牌信息

不必通读，浏览 2-3 个代表页即可。
