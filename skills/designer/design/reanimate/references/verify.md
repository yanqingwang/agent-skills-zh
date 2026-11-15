> **中文汉化版** · 上游：[NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) · 原文件：`skills/designer/design/reanimate/references/verify.md` · License: MIT
> 翻译日期：2026-11-15 · 同步状态：上游 HEAD（2026-11-15 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 验证克隆

一轮是：用与参考相同的方式抓克隆 → `compare.ts` → `sheet.ts compare` → 对每个被跟踪元素跑 `easing.ts --compare-track` → 把结果读全 → 改一个根因 → 下一轮。保留每一轮的目录（`clone-1`、`compare-1`、`clone-2`…），报告里才能展示进展。

## compare.ts 告诉你什么

`report.md` / `report.json`：

- **offset**：匹配到参考第 0 帧的克隆帧（在前十帧上自动对齐）。offset 大说明克隆起步偏晚或偏早；去修触发时序或 `--wait-before`，别靠对齐把它藏起来。
- **mean mismatch** 和 **worst frames**：每帧有差异的像素比例。pixel-faithful 工作直接读它。motion-faithful 把它当趋势读：静止时应当低，只在两者状态不同处才冒尖。
- **motion window**：两组各自的首次/末次可见变化帧，以及峰值。**timing error** 是 start、end、duration 和 peak 的秒数差。这是主要的动效指标，与配色和文案无关。
- **activity curve**：逐帧变化量的条形。形状相同 = 缓动和 stagger 相同；若克隆的条形前置、参考的均匀，说明克隆用了更强的 ease-out，以此类推。
- `diff/NNNN.png`：像素有差异处标红。`sheet.ts compare --diff` 把参考、克隆和 diff 并排摆放，每行附差异值。

`easing.ts --compare-track other.json` 打印两条 track 之间该属性随时间的 `maxAbsDiff` / `meanAbsDiff`（单位 CSS px 或 opacity），以及克隆拟合最好的缓动，用来和参考的对比。

## 通过标准

Motion-faithful（逐规格行）：

- start 和 end 的时序误差 ≤ 0.08 s（25 fps 下两帧）；duration 误差 ≤ 0.08 s
- 缓动：拟合最好的家族相同（out / in / in-out / linear / spring），且把参考的最佳拟合套到克隆 track 上 RMSE ≤ 0.05，或 `meanAbsDiff` ≤ 行程距离的 5 %
- stagger 顺序和间隔在 0.04 s 以内
- 相对元素尺寸的行程距离在参考的 10 % 以内，方向相同
- 参考里静止的元素在克隆里不动，反过来也一样
- 对比帧表：同一时间戳上视觉状态相同，文案/配色不同可接受

Pixel-faithful 另加：

- mean mismatch ≤ 2 %，没有哪帧超过 5 %（设 `--threshold 0.02`）；静止帧 ≤ 0.5 %
- 字体已加载且一致（核对两次抓取的 `inspect.json › fonts`），`nodes` 里配色和尺寸相等
- 同样的素材、同样的尺寸

Mixed：克隆区域用 `--region` 限定后按上面某一档通过；新增部分放到帧表上展示并说明。

Canvas、WebGL、3D（用 `--clock virtual --gl` 抓取，见 `references/webgl.md`）：

- `gl.ts compare --ref ref --clone clone-N`：参考里每个动态通道在克隆里都有一个同类型通道，start 和 end 相差在 0.08 s 内，平均误差 ≤ 参考量程的 5 %（名字不同时用 `--map`）；canvas 属性、renderer 设置和绘制结构（primitive、顶点数、blend 状态、节奏）相同，或差异有解释
- 每个 `clock` 通道的时钟速率相同（`gl.ts channels`）
- 像素同上。若克隆移植了参考的生成器，带种子的随机给出同样的粒子，按清晰的差异来判。若没有，用 `compare.ts --blur 4` 判断，并把清晰数值一并报在旁边

## 读失败 → 常见修法

| 症状 | 常见原因 | 修法 |
|---|---|---|
| 整体按同一 offset 平移，形状一致 | 触发延迟或缺了 delay | 加/调初始 delay；检查 `--wait-before` |
| 克隆更短且前置 | 缓动太猛（expo 对 quint），或时长取了可见窗口而非声明值 | 用 `easing.ts` 拟合的 `durationMs`，设成声明时长 |
| 克隆按时结束但起步晚 | delay 太长、duration 太短 | 两个一起修 |
| 克隆里条形均匀，参考里尖峰 | 参考是 ease-out，却用了 linear 或 ease-in-out | 换缓动家族 |
| 静止帧差异高 | 布局/样式差异、字体回退、裁剪不同 | 修抓取裁剪；pixel-faithful 加载字体、修尺寸 |
| 参考过冲，克隆没有 | spring 对 bezier | 用 spring（Framer `type: "spring"`，GSAP `back.out`/`elastic`，CSS 用带采样 spring 的 `linear()`） |
| stagger 间隔不对 | 逐项 delay 算错 | `delay = base + index × step`；核对 index 来源 |
| 参考静止处克隆有活动 | 有元素不该动却动了，或鼠标位置触发了 hover 态 | 把鼠标移开，去掉多余的过渡 |
| 只有最后几帧不同 | 填充模式或结束状态（缺 `forwards`），或最终值取整不同 | 设 `animation-fill-mode: forwards` / `fill: "forwards"` |
| 滚动触发：克隆起步偏早/偏晚 | IntersectionObserver 的 threshold / rootMargin 不同 | 按 `track.json` 里参考的入点（动效开始处的 `y`）对齐 threshold |

## 什么时候停

- 每条规格行都达标、最新帧表逐状态看起来一致时停。带着数字说出来。
- 某行连做 5 轮没进展，或剩余差异不在你能控制的范围（字体许可、用户可能无权复制的着色器或模型、第三方嵌入、你做了近似的物理）时停。报出该行、最后一组数字和原因。绝不悄悄放宽阈值；若觉得用户能接受更松的标准，说清是哪一条、为什么。
- 若参考自身在两次抓取间不一致（随机内容、A/B 变体、依赖网络的懒加载），先用 `--clock virtual`（同一 seed）抓一次：这样消掉时序和随机性，两次抓取完全一致。仍然有差异的部分（A/B 变体、服务端随机）就是噪声底；评判克隆前，先把参考和它自己比一次量出来。

| 症状（canvas） | 常见原因 | 修法 |
|---|---|---|
| 形状相同，配色处处略偏 | 色彩管理：`outputColorSpace`、纹理色彩空间、tone mapping、three.js 版本 | 从 `gl.ts summary` 抄 renderer 设置；版本一致 |
| 边缘更硬或更软 | `antialias`、像素比、`premultipliedAlpha` | 抄 context 属性和像素比 |
| 动效对上但看起来更跳或更顺 | 渲染节奏（参考每隔一帧才画）或逐帧滞后速率不同 | 在 `gl.ts compare` 里比每帧 draw 数；对齐节奏和 `k` |
| 粒子位置不同、密度相同 | 随机顺序或 seed 不同 | 移植生成器的调用顺序，或用 `--blur` 验证 |
| 克隆里缺某个通道 | 值被烘进着色器，或 uniform 名字不同 | `--map ref=clone`，或把它暴露成 uniform |

## 报告块

```markdown
## Verification (round N of M)
| element / property | timing err (start/end/dur) | easing (ref → clone) | mismatch mean / worst | result |
| h1 translateY+opacity | +0.00 / −0.04 / −0.04 s | easeOutExpo 700 → easeOutExpo 700 | 0.3 % / 1.1 % | pass |
Sheets: .reanimate/<name>/compare-N/sheets/compare-01.png …
Residuals: <none | row, numbers, reason>
```
