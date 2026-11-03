> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/references/step-4-deliver.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 第 4 步：校验、渲染与交付

## 校验

```bash
cd <output-dir>/composition
npx hyperframes check   # brag's single pre-render gate — fix every error it reports
```

把错误全部修掉。`check` 是 brag 唯一的渲染前门槛 — 跑一遍，它报出来的每一条都要修，包括 WCAG 对比度不达标（这类按错误拦截，不是警告）。每条对比度结论都会附一个建议的合规颜色，所以要么照着改，要么在同一色系里调整后重跑 `check` — 大多数修复不需要截图。真实文本没有逐元素跳过对比度的口子；唯一的绕行是 `check --no-contrast`，它跳过的是整个 WCAG 检查（全有或全无），不是用来接受某一个临界的元素。确切的对比度阈值、布局相关的豁免以及报告细节，以当前 hyperframes-cli 的 `check` 指南为准。`check` 的布局检查为"所有文字都要可读"这条创作法则兜底 — 报出的溢出都要修。

对比度的覆盖情况也要看。如果合成里有肉眼可见的 DOM 文字，检查却报 `0/0 text checks` 或者检查元素数为零，那它的对比度其实没被验证过，哪怕 `check` 打印 "passed"。查看 `npx hyperframes check --json` 和抽样帧，弄清哪些被跳过了。如果原因是用了不支持的 `oklch()` 颜色，就把受影响的颜色换成等效的 sRGB hex 或 `rgb()` 值，确认调色板仍然吻合，再重跑 `check`。只有在预期文字确实被审计、对比度问题都已解决时才继续；`--no-contrast` 不满足这道门槛。

渲染前想做视觉上的直觉检查，可以选择抓取关键帧：

```bash
npx hyperframes snapshot   # PNG key frames
```

## 预览

```bash
npx hyperframes preview
```

告诉用户预览已经跑起来了，把 localhost 地址给他们。请他们在渲染前先看一眼。

如果用户认可，或者要求渲染：

## 渲染

```bash
npx hyperframes render --output ../brag.mp4
```

输出落在 `<output-dir>/brag.mp4`（比合成目录高一级）。

想要更快迭代的渲染：

```bash
npx hyperframes render --quality draft --output ../brag.mp4
```

最终交付用：

```bash
npx hyperframes render --quality delivery --output ../brag.mp4
```

## 挑选海报帧

海报是视频播放前显示的那张静帧 — 空闲或未播放时谁先看到的就是它。别用原始首帧或随手挑的时间戳；那些位置常常落在淡入淡出、转场中途、空白的片头背景，或者渲染了一半的文字上。

这个合成是你自己做的，所以最强的那一刻在哪、什么时候到，你心里已经有数 — 钩子那行、主角亮相那刻，或者最后的 logo。挑那个节拍里一个**已经稳定**的点：文字动画完全进到位，而且还没退出去（分镜时序会告诉你安全窗口在哪）。然后用 ffmpeg 把这一帧按全分辨率抽出来。从 `<output-dir>/composition` 执行：

```bash
# use the timestamp of your strongest settled beat, e.g. 3.2s
ffmpeg -ss 3.2 -i ../brag.mp4 -frames:v 1 -q:v 2 ../brag.jpg
```

目标是抽出一帧单独看也能发（"把东西亮出来"这条法则 — 任何一帧定格都该能分享）。如果抽到的帧落在转场中或动画中途，把时间戳挪动零点几秒再抽一次。

### 把海报烘焙为第 0 帧

裸的 `.mp4` 没有 `poster` 属性 — 每个播放器和平台都自己挑静帧缩略图，而且几乎都会抓 **frame 0**。Slack、Twitter/X 和 Discord 在服务端重新生成缩略图，无视内嵌的封面元数据，所以在各处可靠控制静帧图像的唯一办法，是让第 0 帧*就是*海报。

只把**第一帧**的像素替换成 `brag.jpg`，其他帧和全部时序原样不动 — 时长不变、帧数不变、音频直接带过。30fps 下海报会显示 1/30 秒然后片头开始，播放时基本察觉不到，但每个抓缩略图的东西看到的就是它。从 `<output-dir>` 执行：

```bash
ffmpeg -y -i brag.mp4 -i brag.jpg \
  -filter_complex "[0:v][1:v]overlay=0:0:enable='eq(n,0)'[v]" \
  -map "[v]" -map "0:a?" -c:v libx264 -crf 18 -preset slow -pix_fmt yuv420p \
  -c:a copy -movflags +faststart brag.poster.mp4 \
  && mv brag.poster.mp4 brag.mp4
```

海报（`brag.jpg`）和视频尺寸一致，因为它是从同一次渲染里抽出来的，所以 overlay 能精确对齐。把 `brag.jpg` 留在旁边 — 它是那些支持上传自定义缩略图的平台的素材（Instagram、TikTok、YouTube、Facebook 和 LinkedIn 发帖编辑器），而 `poster="brag.jpg"` 是给任何嵌入这个 brag 的 `<video>` 用的图片（画廊卡片、用户的站点）。

## 撰写分享文案

写 `<output-dir>/share-copy.txt`。

分享文案应当：
- 最多一到三句
- 能直接发到 Twitter/X、LinkedIn 或 Discord
- 针对这个项目 — 不要"迫不及待想分享"这类通用话术
- 语气与 brag 视频一致

`share-copy.txt` 是唯一的正式文案。不要在这个文件里放多平台变体、长篇发布说明或 Product Hunt 文案。

如果确实需要变体，写到一个单独的可选文件里：

```text
<output-dir>/share-copy-variants.md
```

### 按 tone 写分享文案

**`default`:**
```
Made [App Name]. It's [what it does, in the project's own absurd terms].
[The best line from the product.]
```

**`polished`:**
```
Introducing [App Name]: [clean one-liner from the site].
Built with [stack if notable].
```

**`yc-parody`:**
```
We built [App Name] to solve [problem stated completely seriously].
[Deadpan feature or stat.]
```

**`chaotic`:**
```
[ALL CAPS CLAIM].
[App Name] is [wildly overstated description].
Link below.
```

**`deadpan`:**
```
I made [App Name].
It [what it does].
```

**`cinematic`:**
```
[App Name].
[Tagline from the site, verbatim or lightly adapted.]
```

**`app-store`:**
```
[App Name] is now live.
[Feature 1], [Feature 2], and [Feature 3] — all in one place.
```

### 示例：Taxi for Taxis

```
Every day, taxis carry us. But who carries the taxis?
Taxi for Taxis: the ride-hailing app for ride-hailing assets.
Available in 12 metros.
```

## 最终输出结构

这一步走完，`<output-dir>/` 应该包含：

```
<output-dir>/
  brag.mp4                — the rendered video
  brag.jpg                — the poster (best frame, for <video poster>)
  brag-plan.md            — the plan and storyboard
  composition-brief.md    — the Hyperframes handoff brief
  share-copy.txt          — the share caption
  composition/            — the Hyperframes project
    index.html
    ...
```

## 告知用户

全部完成后，告诉用户：
- 视频在哪（`<output-dir>/brag.mp4`）
- 分享文案在哪
- 用一句话说明这个视频在创意上做了什么
- 可选：提议重录某个场景、换个 tone，或换个切入角度
