> **中文汉化版** · 上游：[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) · 原文件：`skills/morph-ppt/reference/styles/INDEX.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 风格索引

Agent 用这张表按主题快速选定参考风格。选定后读 `<directory>/style.md` 理解设计理念；需要实现参考时读 `build.sh`。

**重要提示**：

- 这些风格里的 build.sh 脚本**只供设计手法参考**（配色、形状、Morph 编排）
- 部分脚本存在文字重叠、排版错位等问题，**不要照抄坐标与尺寸**
- 生成时必须遵守 `pptx-design.md` 的设计原则（文字可读性、间距、对齐等）
- **学方法，不要抄代码**

---

**主色 hex 列**：bg / fg / accent，取自各风格的 `build.sh`。可先用它目测匹配用户给定的品牌色，再打开任何 `style.md`。`-` 表示该风格只有 `style.md`（没有可提取的构建脚本）。

## Dark 色系（dark）

| 目录                     | 风格名                   | 主色 hex（bg / fg / accent）   | 适用场景                                                        | 气质                                    |
| ------------------------ | ------------------------ | ------------------------------ | --------------------------------------------------------------- | --------------------------------------- |
| dark--liquid-flow        | 流体光感                 | `#0F0F2D / #6C63FF / #48E5C2`  | 品牌升级、创意发布、时尚秀场                                    | 流动、梦幻、前卫                        |
| dark--premium-navy       | 高级藏青与金             | `#0C1B33 / #C9A84C / #1E3A5F`  | 高端企业、年度战略、董事会汇报                                  | 权威、精致、高级                        |
| dark--investor-pitch     | 投资路演专业版           | `#1A1A2E / #0F3460 / #16213E`  | 投资路演、融资材料、商业计划                                    | 专业、可信、沉稳                        |
| dark--cosmic-neon        | 宇宙霓虹                 | `#050510 / #8A2BE2 / #00FFFF`  | 科学演讲、未来主题、物理、宇宙题材                              | 科幻、神秘、未来感、霓虹                |
| dark--editorial-story    | 杂志编辑叙事             | `#FFFFFF / #2C3E50 / #E74C3C`  | 品牌故事、编辑杂志、内容发布                                    | 叙事、艺术、高级                        |
| dark--tech-cosmos        | 科技宇宙                 | `-`                            | 技术演讲、架构评审、科学报告                                    | 未来感、科学、宇宙                      |
| dark--blueprint-grid     | 蓝图网格                 | `#1B3A5C / #4A90D9 / #FFFFFF`  | 技术规划、工程蓝图、系统架构                                    | 精确、专业、工程感                      |
| dark--diagonal-cut       | 工业斜切                 | `#1A1A1A / #FF6600 / #FFCC00`  | 工业、工程、建筑、制造                                          | 粗犷、有力、大胆                        |
| dark--spotlight-stage    | 聚光舞台                 | `#0A0A0A / #FFFFFF / #FFE0B2`  | 主题演讲、发布会、TED 风格演讲、晚会                            | 戏剧化、聚焦、舞台感                    |
| dark--cyber-future       | 赛博未来                 | `#0B0C10 / #66FCF1 / #1F2833`  | 未来主题、技术愿景、赛博朋克、AI/机器人                         | 未来感、赛博朋克、沉浸                  |
| dark--circle-digital     | 暗色数字机构             | `#0D0E11 / #171A20 / #22252E`  | 数字营销、创意机构、科技公司                                    | 现代、暗色酷感、数字                    |
| dark--architectural-plan | 建筑规划图               | `#FFFFFF / #18293B / #B5D5E3`  | 建筑设计、商业计划、地产开发                                    | 专业、结构化、建筑感                    |
| dark--luxury-minimal     | 奢华极简                 | `#111111 / #D4AF37 / #FFFFFF`  | 奢侈品牌、高端产品、高端企业                                    | 奢华、极简、精致                        |
| dark--space-odyssey      | 太空奥德赛               | `#0A0E27 / #1E3A5F / #4A5FFF`  | 太空/天文、科学教育、探索叙事                                   | 宇宙、鼓舞、史诗、探索                  |
| dark--neon-productivity  | 霓虹效率                 | `#0B0F1A / #2BE4A8 / #FFB020`  | 效率主题演讲、技术工作坊、励志、创业                            | 有活力、现代、鲜明                      |
| dark--midnight-blueprint | 午夜蓝图                 | `#080B2A / #181B55 / #131650`  | 建筑事务所、专业服务、高端地产                                  | 精致、建筑感、高级                      |
| dark--sage-grain         | 鼠尾草纹理               | `#1E2720 / #FFFFFF / #D9B88F`  | 创意机构、精品咨询、有机品牌                                    | 有机、精致、手作感                      |
| dark--obsidian-amber     | 黑曜石琥珀               | `-`                            | 金融、投资、奢侈品服务、高端咨询                                | 高级、精致、有力                        |
| dark--velvet-rose        | 天鹅绒玫瑰               | `-`                            | 奢侈品牌、高端时尚、高端零售                                    | 奢华、优雅、精致                        |
| dark--aurora-softedge    | 极光柔边                 | `-`                            | 设计作品集、创意展示、美术馆                                    | 极光感、梦幻、艺术                      |

## Light 色系（light）

| 目录                        | 风格名                   | 主色 hex（bg / fg / accent）   | 适用场景                                                  | 气质                                |
| --------------------------- | ------------------------ | ------------------------------ | --------------------------------------------------------- | ----------------------------------- |
| light--minimal-corporate    | 极简企业报告             | `#FFFFFF / #E8EEF4 / #1E3A5F`  | 年报、工作总结、商业提案                                  | 专业、干净、沉稳                    |
| light--minimal-product      | 极简产品展示             | `#FAFAFA / #00B894 / #2D3436`  | 产品发布、技术展示、品牌介绍                              | 现代、极简、高级                    |
| light--project-proposal     | 项目提案                 | `#E8EEF4 / #1E3A5F / #D4A84B`  | 项目启动、商业提案、投标演示                              | 专业、可信、严谨                    |
| light--bold-type            | 粗体排印                 | `#F2F2F2 / #1A1A1A / #E8E8E8`  | 编辑排版、杂志风、品牌手册                                | 大胆、现代、编辑风                  |
| light--isometric-clean      | 等距清爽科技             | `#F0F4F8 / #E8ECF1 / #4A90D9`  | 科技产品、SaaS 平台、数据演示                             | 清新、现代、科技感                  |
| light--spring-launch        | 春日发布                 | `#E8F5E9 / #4CAF50 / #8BC34A`  | 春季发布、新品上市、季节营销                              | 清新、自然、有活力                  |
| light--training-interactive | 互动培训                 | `#FFF9E6 / #FF6B6B / #4ECDC4`  | 企业培训、在线课程、知识分享                              | 教学感、互动、亲切                  |
| light--watercolor-wash      | 水彩晕染                 | `#FFFDF7 / #7AADCF / #E8A87C`  | 艺术、文创、茶道、婚礼                                    | 柔和、诗意、艺术                    |
| light--firmwise-saas        | 稳健 SaaS                | `#EFF2F7 / #7B3FF2 / #FFFFFF`  | SaaS 平台、效率工具、B2B 软件                             | 干净、高效、可信                    |
| light--glassmorphism-vc     | 玻璃拟态 VC              | `-`                            | VC 基金、投资材料、金融科技、创业路演                     | 现代、高级、精致                    |
| light--fluid-gradient       | 流体渐变                 | `-`                            | AI/科技产品、SaaS 平台、现代软件                          | 流动、科技前沿、动感                |

## Warm 色系（warm）

| 目录                     | 风格名             | 主色 hex（bg / fg / accent）   | 适用场景                                                          | 气质                             |
| ------------------------ | ------------------ | ------------------------------ | ----------------------------------------------------------------- | -------------------------------- |
| warm--earth-organic      | 大地与鼠尾草       | `#F5F0E8 / #8B6F47 / #A8C686`  | 环保、可持续、有机品牌                                            | 温暖、真诚、自然                 |
| warm--minimal-brand      | 极简品牌           | `-`                            | 品牌介绍、产品发布、高端品牌展示                                  | 温暖、精致、极简                 |
| warm--brand-refresh      | 品牌焕新           | `#F5F0E8 / #162040 / #1A6BFF`  | 品牌发布、企业形象更新、创意提案                                  | 时尚、多彩、现代                 |
| warm--creative-marketing | 创意营销           | `-`                            | 营销活动、广告创意、海报式 PPT                                    | 大胆、冲击力、表现力             |
| warm--playful-organic    | 童趣自然           | `#FFF8E7 / #3D3B3C / #FFFFFF`  | 生活方式、宠物/动物主题、儿童教育、故事讲述                       | 温暖、俏皮、友好                 |
| warm--sunset-mosaic      | 落日马赛克         | `-`                            | 工程、基础设施、B2B 企业、建筑                                    | 专业、温暖、踏实                 |
| warm--coral-culture      | 珊瑚文化           | `-`                            | 企业文化材料、HR 演示、团队展示                                   | 温暖、文化感、以人为本           |
| warm--monument-editorial | 纪念碑编辑风       | `-`                            | 建筑、奢侈品牌、编辑杂志、工作室品牌                              | 纪念感、精致、排印导向           |
| warm--vital-bloom        | 元气绽放           | `-`                            | 健康应用、瑜伽馆、正念生活、有机品牌                              | 有机、有活力、健康               |
| warm--bloom-academy      | 绽放学园           | `-`                            | 教育、在线学习、儿童内容、趣味品牌                                | 俏皮、教学感、友好               |

## Vivid 色系（vivid）

| 目录                     | 风格名                  | 主色 hex（bg / fg / accent）   | 适用场景                                              | 气质                            |
| ------------------------ | ----------------------- | ------------------------------ | ----------------------------------------------------- | ------------------------------- |
| vivid--candy-stripe      | 彩虹糖果条纹            | `#FFFFFF / #FF5252 / #FF7B39`  | 活动庆典、节日、儿童教育                              | 欢乐、活泼、彩虹                |
| vivid--playful-marketing | 青春活力营销            | `#FFFFFF / #FF6B6B / #4ECDC4`  | 营销活动、新品推广、促销活动                          | 年轻、活力、热情                |
| vivid--energy-neon       | 能量霓虹                | `#E8E8E8 / #00FF41 / #111111`  | 会议、能源峰会、科技活动、编辑风                      | 有能量、冲击力、现代            |
| vivid--pink-editorial    | 粉调编辑风              | `#160B33 / #7B2D52 / #C85080`  | 年报、数据新闻、编辑展示                              | 当代、编辑风、大胆              |
| vivid--bauhaus-electric  | 包豪斯电光              | `-`                            | 创意机构、设计工作室、大胆品牌                        | 大胆、有能量、电光感            |

## 黑白（bw）

| 目录              | 风格名        | 主色 hex（bg / fg / accent）   | 适用场景                                                     | 气质                           |
| ----------------- | ------------- | ------------------------------ | ------------------------------------------------------------ | ------------------------------ |
| bw--mono-line     | 极简线条      | `#FFFFFF / #1A1A1A / #C8C8C8`  | 极简企业、学术报告、咨询提案                                 | 冷静、克制、专业               |
| bw--swiss-bauhaus | 瑞士包豪斯    | `#E63322 / #1C1C1C / #F5F5F5`  | 设计机构、建筑事务所、艺术展览                               | 理性、严谨、经典               |
| bw--brutalist-raw | 粗野主义原色  | `#FFFFFF / #000000 / #FF0000`  | 先锋艺术展、实验设计、独立品牌                               | 反叛、粗犷、冲击力             |
| bw--swiss-system  | 瑞士体系      | `#FFFFFF / #000000 / #FF0000`  | 企业、金融、咨询、专业服务                                   | 干净、系统化、大胆             |

## Mixed 色系（mixed）

| 目录                        | 风格名               | 主色 hex（bg / fg / accent）   | 适用场景                                                | 气质                              |
| --------------------------- | -------------------- | ------------------------------ | ------------------------------------------------------- | --------------------------------- |
| mixed--duotone-split        | 双色调分割           | `#FFFFFF / #2D3436 / #E17055`  | 品牌发布、建筑设计、高端展示                            | 大胆、建筑感、极简                |
| mixed--chromatic-aberration | 色差故障             | `#050814 / #0A1030 / #00F5E4`  | 科技创业、AI 平台、创意技术                             | 未来感、故障艺术、赛博            |
| mixed--bauhaus-blocks       | 包豪斯色块           | `#F0EBE0 / #1D5C38 / #F4C040`  | 创意工作室、设计作品集、品牌代理                        | 大胆、现代主义、几何              |
| mixed--spectral-grid        | 光谱网格             | `-`                            | 创意科技、创新展示、设计大会                            | 鲜活、创新、实验                  |

---

## 按使用场景速查

| 使用场景                                 | 推荐风格                                                                                                                                                                               |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **科技 / AI / SaaS**                     | dark--tech-cosmos, dark--cyber-future, light--isometric-clean, mixed--chromatic-aberration, light--firmwise-saas, light--fluid-gradient                                                |
| **投资 / 路演 / 融资**                   | dark--investor-pitch, dark--premium-navy, light--project-proposal, light--glassmorphism-vc, dark--obsidian-amber                                                                       |
| **企业 / 商务 / 报告**                   | light--minimal-corporate, light--minimal-product, dark--premium-navy, vivid--pink-editorial, warm--sunset-mosaic, warm--coral-culture                                                  |
| **品牌 / 发布 / 营销**                   | warm--brand-refresh, warm--creative-marketing, vivid--playful-marketing, warm--minimal-brand, vivid--bauhaus-electric                                                                  |
| **设计 / 建筑 / 艺术**                   | bw--swiss-bauhaus, bw--brutalist-raw, dark--architectural-plan, mixed--duotone-split, dark--midnight-blueprint, mixed--bauhaus-blocks, dark--aurora-softedge, warm--monument-editorial |
| **教育 / 培训 / 课件**                   | light--training-interactive, warm--playful-organic, vivid--candy-stripe, warm--bloom-academy                                                                                           |
| **主题演讲 / 发布会 / 晚会**             | dark--spotlight-stage, dark--liquid-flow, vivid--energy-neon                                                                                                                           |
| **创意机构 / 工作室**                    | dark--sage-grain, mixed--bauhaus-blocks, dark--circle-digital, vivid--bauhaus-electric, mixed--spectral-grid                                                                           |
| **开发者 / 技术**                        | dark--cyber-future, dark--blueprint-grid, dark--tech-cosmos                                                                                                                            |
| **环保 / 自然 / 有机**                   | warm--earth-organic, warm--minimal-brand, light--spring-launch                                                                                                                         |
| **文创 / 杂志 / 故事**                   | dark--editorial-story, light--watercolor-wash, light--bold-type, warm--monument-editorial                                                                                              |
| **科幻 / 太空 / 未来**                   | dark--space-odyssey, dark--cosmic-neon, dark--cyber-future                                                                                                                             |
| **奢侈 / 高端**                          | dark--luxury-minimal, dark--premium-navy, warm--minimal-brand, dark--velvet-rose                                                                                                       |
| **效率 / 励志**                          | dark--neon-productivity, dark--cyber-future                                                                                                                                            |
| **健康 / 生活方式**                      | warm--vital-bloom, warm--playful-organic, light--spring-launch                                                                                                                         |
| **金融 / 投资**                          | dark--obsidian-amber, dark--investor-pitch, light--glassmorphism-vc                                                                                                                    |
