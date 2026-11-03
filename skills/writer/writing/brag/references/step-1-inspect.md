> **中文汉化版** · 上游：[latent-spaces/brag](https://github.com/latent-spaces/brag) · 原文件：`skills/brag/references/step-1-inspect.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 第 1 步：检查项目

阅读项目目录，弄清楚你要拿什么来 brag。

## 该看哪些东西

按以下优先级阅读：

1. **`index.html`** — 主要来源。完整读一遍这个文件。提取：页面标题、hero 主标题、
   tagline、所有章节标题、CTA 文案、用户证言文案、导航项。这就是这个应用的声音与故事。

2. **`styles.css`** 或同类文件 — 提取：主色调色板（找 CSS 自定义属性 / `:root` 变量）、
   字体族、背景色、强调色。这些将成为 brag 视频的视觉识别。

3. **`README.md`** — 如果存在，提取：项目名称、一句话描述、列出的功能。

4. **`package.json`** — 如果存在，提取：`name`、`description`。

5. **子目录文件** — 如果这是多页面应用，扫描路由文件、组件文件或页面文件。
   提取关键功能名称与界面描述。

6. **用户流程 / 主路径** — 别只扫营销页面。brag 最有力的素材通常是产品
   *被使用*的样子，而不是产品对自己的营销宣传。看看：
   - **路由**（`app/`、`pages/`、路由文件）— 落地页之外的各个界面。
   - **关键功能组件** — 上传表单、编辑器、结果视图、仪表盘。
   - **状态机、store 或步骤组件** — 一次会话是怎么推进的。
   - **README 的 "how it works" 或 "usage" 章节** — 项目自己对流程的描述。
   - **示例或 demo 目录** — 团队测试时用过的示例输入与输出。

   找出*使用*产品的 2–3 个节拍：**入口 → 关键动作 → 结果。**

7. **`public/` 或 `assets/`** — 记下其中的图片、logo、图标。这些可以在合成中被引用。

## 9 个问题的量规

读完之后，九个问题都要回答。进入第 2 步之前先把这些写下来。

```
1. What is the app?
   One sentence. What does it actually do (or claim to do)?

2. What is the funniest or most impressive claim?
   The one line from the site that earns a reaction.

3. What is the visual hook?
   The strongest CSS visual: a color palette moment, a UI element, a diagram, a card.

4. What should be shown from the actual UI?
   Which section of the site has the most video-worthy content?
   (Hero? Feature section? Testimonial? The UI mockup?)

5. What is the shortest satisfying video?
   Would 15 seconds work? 20? What's the minimum to land the joke/claim?

6. What tone fits best?
   If the user specified a preset, use it.
   If the user gave freeform direction, preserve it and map it to the nearest preset.
   If the user did not specify, infer both:
   - Tone preset: one of the known presets
   - Creative direction: a short custom phrase for this project
   Examples:
   - Absurd product → preset: yc-parody; direction: fake startup launch
   - Earnest product → preset: polished; direction: quiet premium product film
   - Chaotic product → preset: chaotic; direction: overproduced social ad

7. What should the audio feel like?
   Decide the audio role and music direction before picking exact SFX files.
   Bias toward a polished audio layer: include music and tasteful SFX unless
   the user disabled them, assets are missing, or silence is clearly the
   strongest creative choice.
   Examples:
   - Warm corporate bed; SFX chosen later to match real UI motion
   - Low music bed with final fade; one dry logo hit if the composition supports it
   - Dense chaotic music; Hyperframes may align text/card reveals to beats
   - Cinematic bed with a low swell, restrained motion-matched accents, and subtle audio-reactive glow/presence if it supports the visual style

8. What should the share caption say?
   Draft one sentence. This becomes share-copy.txt.

9. What's the user flow worth showing?
   The 2–3 beats a real user goes through: entry → key action → result.
   Not the landing page's section list — the working app.
   Examples:
   - Upload long video → see it processing with progress → see 3 vertical clips ready
   - Type a message → assistant types back → user clicks "mark resolved"
   - Swipe right on Thunder's profile → match animation → chat opens
   If the project is a landing-page-only static site with no app, write
   "none — landing-page only" and rely on the strongest visual (Q3) instead.
```

## 颜色提取

读 CSS 时，找这类自定义属性：

```css
:root {
  --primary: oklch(...);
  --bg: oklch(...);
  --accent: ...;
}
```

如果没有自定义属性，就去扫 background、color 和 border 规则里用得最多的颜色。

记下：
- 背景色（精确值）
- 主文本色
- 强调色/品牌色
- 任何渐变或特殊处理

这些颜色会被记录进 `composition-brief.md`，并延续到合成的视觉风格
（见 `hyperframes` skill 的 `references/look.md`）。

## 字体提取

找这些：
- `:root` 或 `body` 中的 `font-family` 声明
- `<head>` 中的 Google Fonts `<link>`（字体族名在 URL 的查询串里）
- `@import` 语句

分别记下标题用的展示字体与正文用的正文字体。

## 该跳过什么

不要读：
- 生成的构建产物（`dist/`、`.next/`、`build/`）
- 锁文件（`package-lock.json`、`yarn.lock`）
- 测试文件
- `.git/`
- 环境变量与密钥文件（`.env`、`.env.*`）
- 凭据与密钥材料（`.pem`、`.key`、`id_rsa`、service-account JSON，
  以及 `secrets/` 或 `credentials/` 目录下的任何东西）
- 常用于存放 token 的本地配置
- 项目 `.gitignore` 因上述理由排除的任何文件

## 规则：本步骤不外泄任何机密

这一步读到的任何东西，最终都可能出现在用户公开发布的视频画面上。绝不要把机密、
API key、token、内部主机名或 URL、真实客户或用户姓名、邮箱地址，或任何个人
数据带进 `brag-plan.md`、`composition-brief.md`、合成产物、渲染出的视频或分享文案。
如果产品的真实 UI 中含有这类数据，请替换成合理的虚构替身，并在计划中说明这一点。
