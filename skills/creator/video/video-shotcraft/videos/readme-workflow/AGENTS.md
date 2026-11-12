> **中文汉化版** · 上游：[Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) · 原文件：`videos/readme-workflow/AGENTS.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# HyperFrames 合成项目

## Skills：优先使用

**在编写或修改合成（composition）之前，务必先调用相关 skill。** Skills 中固化了框架专属的模式（例如 `window.__timelines` 注册、`data-*` 属性语义、shader 兼容的 CSS 规则），这些内容不在通用的 web 文档里。跳过它们会产出损坏的合成。

**要用 HyperFrames 做点什么？** 从 `/hyperframes` 开始。它会告诉你 HyperFrames 能做什么、你的意图该由哪个 skill 或 workflow 处理（做视频、TTS / BGM、准备素材、编写 / 动画、渲染、安装 blocks），先确认你的 brief（意图层），再把每个"帮我做个……"的请求（一段视频、一套 deck、一次合成移植）路由到正确的 workflow。先读它，尤其是在没有项目上下文帮你定位时。它路由到以下 workflow：

- `/product-launch-video`：任意**网站** URL，或一份 brief / 脚本 → 产品发布 / SaaS / 促销视频，或以该站点自己截取的画面为主角的站点导览 / 展示。
- `/faceless-explainer`：任意文本（主题 / 文章 / 笔记），**无 URL、无网站抓取** → 60-90 秒无人出镜讲解视频。
- `/embedded-captions`：已有的口播视频（MP4）→ 同一段素材加上字幕 / 副标题（字幕栏 + 内嵌，或纯电影式内嵌）；素材本身不做改动。
- `/talking-head-recut`：已有的口播 / 访谈 / 播客视频（MP4）→ 同一段素材**包装上设计好的图形叠加**（动态标题、下三分之一条、数据标注、引语摘录、侧边面板、画中画），与转录文本同步；底下的画面原样播放。（普通字幕 / 副标题 → `/embedded-captions`。）
- `/pr-to-video`：一个 GitHub PR（URL / `owner/repo#N` / "这个 PR"）→ 30-90 秒代码变更讲解（更新日志 / 功能揭晓 / 修复 / 重构）。
- `/motion-graphics`：一支短（通常 10 秒以内）、以设计为主导的**动态图形**，动效即信息，无旁白：动态文字、统计数字 / 数字滚动、图表、logo 定版、下三分之一条 / 叠加元素，或动态推文 / 标题 / 截屏高亮；渲染为 MP4 或透明叠加层。更长 / 带旁白 / 定制 → `/general-video`。
- `/music-to-video`：一条**音乐曲目**（音频文件、可抽取音频的视频，或根据氛围 brief 生成的音乐）→ 卡点视频（歌词 / 幻灯片 / 动感促销）。音乐驱动节奏；用户提供的图片 / 视频会剪到同一个节拍网格上。
- `/slideshow`：**演示文稿 / 路演 deck / 交互式 deck**，即离散的幻灯片、分步揭示、分支跳转、热点导航、演示者模式。产出是可导航的 deck，不是渲染出来的视频。
- `/general-video`：其他任何视频的兜底（标题卡、更长的品牌 / 集锦宣传片、多场景蒙太奇、静态循环、定制合成），也是 **companion mode** 的所在：用完整的 HyperFrames 工具箱共同创作；即最初的 hyperframes 创作流程，长度不限。

**要移植一个现有合成？** `/remotion-to-hyperframes` 把 Remotion（React）合成转换成 HyperFrames HTML，属于源码迁移，与上面的创建工作流是两回事。

领域 skills（`/hyperframes-core`、`/hyperframes-animation`、`/hyperframes-keyframes`、`/hyperframes-creative`、`/hyperframes-cli`、`/media-use`、`/hyperframes-audio`、`/hyperframes-registry`、`/figma`）与完整能力图谱都在 `/hyperframes` 内。哪个 skill 处理哪个意图，以它为唯一事实来源。

**要改变真实素材或图片的观感或呈现方式？** 编辑之前先加载 `/media-use` 并阅读它的 `references/media-treatments.md`，即使请求只是说更暗、更平、更无聊、复古、私密，或者"让揭晓效果更酷"。它约束的是素材如何被处理，而不是媒体能否被使用。使用规范的媒体处理手法与 seek 安全的动效；不要即兴手搓等效的 CSS/SVG 滤镜或叠加层。

> **Tailwind v4 项目**（`hyperframes init --tailwind`）：见 `/hyperframes-core` → `references/tailwind.md`。

> **在用 HyperFrames 插件？** 从那个已安装的 bundle 加载 skills，并遵循其 `hyperframes/references/plugin-installation.md` 的执行规则。更新走插件管理器，不要用下面的独立命令。
>
> **独立 skill 缺失或过期？** 运行 `npx hyperframes skills update <name>` 安装 / 刷新你所需的那个 skill（`/hyperframes` 路由器会在进入 workflow 前自动执行），或不带子命令直接运行 `npx hyperframes skills update` 刷新核心集加所有已安装内容；两者都不会拉取全集。重启 agent 会话，让新安装的 skills 加载。

## 命令

```bash
npm run dev          # human-operated foreground preview (blocks until stopped)
npx hyperframes preview --background  # agent-safe persistent Studio preview
npx hyperframes preview --status      # verify the persistent preview is listening
npx hyperframes preview --stop        # stop it when review is finished
npm run check        # lint + runtime + layout + motion + contrast (one command)
npm run render       # render to MP4
npm run publish      # publish and get a shareable link
npx hyperframes lint --verbose  # include info-level findings
npx hyperframes lint --json     # machine-readable output for CI
npx hyperframes docs <topic> # reference docs in terminal
```

> **Agent 必须用 `npx hyperframes preview --background` 做 Studio 交接。** 不要依赖在 `npm run dev` 外面套一层 shell/工具的 `run_in_background`：那个前台进程仍归发起会话所有，浏览器还开着它却可能已经消失，刷新时只会得到 `ERR_CONNECTION_TIMED_OUT`。用 `preview --status` 验证，评审期间保持其存活，评审之后用 `preview --stop` 显式停止。

> **从桌面应用回来之后。** 一旦本项目在 HyperFrames 桌面应用里被打开过，在这里做下一次改动前先运行 `npx hyperframes catch-up`：它会列出用户在应用里向 Framey 提了什么、之后哪些文件有改动。

> **固定 CLI 版本。** 这些脚本把 `hyperframes@X.Y.Z` 钉在精确版本上，让本项目随时间推移重渲染出一致结果。几周后，这个 pin 就落后于那之后发布的修复了。要升级：`npx hyperframes@latest upgrade --project . --check`（查看差异），然后 `npx hyperframes@latest upgrade --project .` 改写各处 pin。始终用未钉住的（unpinned）命令：钉住版本的脚本只会拿旧版本对自身重复执行。

## 文档

**快速参考**请用本地 CLI 文档命令（无需联网）：

```bash
npx hyperframes docs <topic>
```

主题：`data-attributes`、`gsap`、`compositions`、`rendering`、`examples`、`troubleshooting`

**完整文档**请通过机器可读索引发现页面，不要凭空猜测 URL：

```
https://hyperframes.heygen.com/llms.txt
```

## 项目结构

- `index.html`：主合成（根 timeline）
- `compositions/`：子合成，通过 `data-composition-src` 引用
- `meta.json`：项目元数据（id、name）
- `transcript.json`：whisper 词级转录（若已生成）

## Lint：每次改动后必须运行

创建或编辑任何 `.html` 合成之后，在认定任务完成之前**务必**运行完整检查：

```bash
npm run check
```

展示结果前修复所有 error。渲染前应复查所有 warning。

## 关键规则

1. 每个计时元素都需要 `data-start` 和一段时长。`data-start` 是把它标记为计时元素的标志；`data-track-index` 只是可选的 Studio 显示轨道，渲染从不读取它
2. 给计时的视觉元素加上 `class="clip"`。框架依据 `data-start` 而不是类名来控制可见性，但共享的 `.clip` CSS 才是让场景获得全幅盒子的关键，缺了它 `lint` 会告警
3. 在 `window.__timelines` 上为每个合成注册一个 paused 的根 timeline：
   ```js
   window.__timelines = window.__timelines || {};
   window.__timelines["composition-id"] = gsap.timeline({ paused: true });
   ```
   手动添加到这个根上的场景 timeline 不得处于 paused 状态。子 timeline 一旦 paused，根被 seek 时它就不会推进。运行时激活的是已注册的 composition 同级节点，而不是任意嵌套的场景 timeline。
4. 有声音的视频把声音留在 `<video>` 上（`data-has-audio="true"`，不加 `muted`）。音乐、配音、替换音频、J/L cut，或在 Studio 里分离出来的音频，用单独的 `<audio>`。无声素材与 b-roll：加 `muted`。
5. 子合成用 `data-composition-src="compositions/file.html"` 引用其他 HTML 文件
6. 只写确定性逻辑：不碰 `Date.now()`，不碰 `Math.random()`，不发网络请求
