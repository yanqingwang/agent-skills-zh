---
name: pixelfx
description: 使用 pixelfx 库以代码制作像素艺术特效与精灵动画，内置 244 个现成特效，由一个会蓄力、命中顿帧并收招的角色演绎（类别涵盖 fire、explosions、water、ice、lightning、sci-fi、melee、impacts、projectiles、spawn and death、arcane、holy、shadow、status、nature、weather、UI、pickups、transitions、critters），可直接放进游戏、重新着色、导出为精灵图（sprite sheet）或改编 remix，并配有"草稿-渲染-观察-打磨"的迭代流程，让新特效看上去如同手工绘制的动画。适用于：想要像素艺术 VFX、精灵动画或精灵图（sprite sheet），想要游戏打击感（game juice），想要某个具体特效（"给我的法师来个冰霜新星"、"金币拾取闪光"），想在 Godot、Unity、Phaser 或 canvas 游戏中使用或导出 pixelfx 特效，或想让像素特效更好看。
license: MIT
compatibility: Node 18 or newer. ffmpeg is optional (GIF and MP4 previews).
---

> **中文汉化版** · 上游：[patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) · 原文件：`skills/pixelfx/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# pixelfx

用代码实现的像素艺术特效。每个特效就是一个文件 `src/fx/<category>/<name>.js`，向两个缓冲区绘制：**color**（颜色：像素可为不透明、抖动或真正半透明）和 **light**（光照：叠加式辉光）。不依赖任何图片，因此特效可以实时播放、重新着色、镜像、更换随机种子，并渲染成适配任意引擎的精灵图（sprite sheet）。

其方法论来自 Hugo Duprez 的《[How to make (good) pixel art effects with Claude](https://www.spritefusion.com/blog/how-to-make-good-pixel-art-effects-with-claude)》：代码如黏土，相信你的眼睛，喂入你的参考素材。一次性提示词只能做出平庸的特效；先渲染、再观察、不断打磨的草稿才能做出好特效。

## 开始之前

1. 在 pixelfx 的代码检出中工作。如果工作目录里没有 `tools/render.mjs`，就把它克隆到项目旁边：`git clone https://github.com/patch-gg/pixelfx`。无需安装步骤：这些工具只依赖 Node。
2. 先验证它能跑：`node tools/render.mjs fire/torch` 会写出 `records/fire/torch/contact.png`。用你的图片读取工具打开那张 PNG。从现在起，你要通过这种联系表（contact sheet）来查看每一个特效。

## 1. 先找现成的特效

`node tools/list.mjs <words>` 会搜索 id、名称、标签与描述（例如 `node tools/list.mjs frost`、`node tools/list.mjs slash loop`）。`docs/CATALOG.md` 按类别列出全部特效。选定之前，先把候选渲染出来看一看。大多数需求其实就是某个现成特效配上不同选项：

- `palette`：主色阶（ramp），由暗到亮的十六进制色值字符串。可用 `src/core/color.js` 中的任意 `PAL` 色阶（fire ember lava smoke dust ice water electric volt poison holy heal arcane shadow blood earth stone gold leaf wood metal bone neon cyber matrix candy night），也可以自定义。蓝色火焰就是 `{"palette": PAL.ice}`。
- `seed` 换一个不同但等价的变体；`flip` 翻转为朝左；`angle` 旋转；`light`（0..1+）控制辉光强度；此外每个特效在 `meta.options` 中还有各自的旋钮（size、count、radius、text、height 等）。
- 不改代码就能试选项：`node tools/render.mjs fire/torch --opts '{"palette":["#102","#215","#43a","#8cf","#fff"]}'`。

## 2. 接入游戏

**JS 或 TS 编写的 Canvas / WebGL 游戏**（原生 canvas、Phaser、PixiJS、Kaplay、three.js）：直接使用代码。它没有任何依赖；复制 `src/core` 和你需要的特效文件，或直接依赖本仓库。

```js
import { createFrame, clearFrame, createFx, composite } from "pixelfx";   // src/core/index.js
import * as frostNova from "pixelfx/fx/ice/frost-nova";                   // src/fx/ice/frost-nova.js

const frame = createFrame(320, 180);            // the game's pixel resolution; ox, oy scroll it with the camera
const img = new ImageData(320, 180);
const fx = createFx(frostNova, { x: hero.x, y: hero.y, flip: hero.facing < 0 });

// every tick
fx.update(dt);
clearFrame(frame);
fx.draw(frame, "back");    // what goes behind characters
drawCharacters();          // your own sprites, or draw them into frame.color yourself
fx.draw(frame, "front");
composite(frame, img.data, background);   // color over the background plus light; or null for transparent
ctx.putImageData(img, 0, 0);              // then scale the canvas up with image-rendering: pixelated
if (fx.done()) removeIt();               // one-shots end on their own; fx.stop() fades a loop out
```

多个特效可以共享同一个 frame。在 WebGL 引擎里，每帧把合成后的 RGBA 上传为纹理；或者把特效一次性渲染成精灵图（见下文），再像普通动画一样播放。

**任意引擎**（Godot、Unity、GameMaker、Defold、LÖVE、Bevy、Construct）：导出精灵图（sprite sheet）。`node tools/render.mjs ice/frost-nova --sheet` 会写出 `records/ice/frost-nova/frost-nova.png`（网格排布的透明帧）和 `frost-nova.json`（Aseprite 风格的帧数据，因此 Phaser 的图集加载器、Godot 与 Unity 的 Aseprite 导入器以及大多数工具都能直接读取；`meta.pixelfx` 中含有 fps、loop、帧尺寸、列数和 pivot）。把 pivot 设为 `meta.pixelfx.pivot`（特效的原点，例如脚部），以最近邻过滤、无压缩方式导入，并按 `meta.pixelfx.fps` 播放。辉光以带 alpha 的颜色形式烘焙进图集，在暗色场景中读起来就是叠加发光；在明亮场景中，可以渲染一个重新着色的版本，或把特效放在暗色图层上。

要导出整库：`node tools/render.mjs <category> --sheet` 一次渲染一整个类别。

**打击需要人物作为支撑。**单独一个特效看起来就像贴纸。带人物的特效自带一段 `act`（表演）：身体何时蓄力、何时顿帧、目标作何反应。无论游戏如何构建，都能用上它：

- 用自带的标准人物：以 `createAct(slash, { x, y })` 代替 `createFx`。调用 `act.update(dt)`、`act.draw(frame)`，并用 `act.shake` 让画面抖动。顿帧期间它会自己保持静止。`node tools/act.mjs <id> --sheet` 会把整套内容烘焙成精灵图。
- 用游戏自己的角色：读取时序信息，即精灵图 JSON 里的 `slash.act` 或 `meta.pixelfx.act`（`windup`、`recovery`，以及带 `t` 和 `freeze` 的 `hits`）。在特效出现前 `windup` 秒播放角色的攻击动画；每次命中时，把一切——特效和角色都包括——暂停更新 `freeze` 秒。宿主侧顿帧（hit-stop）对任何特效都有效，有 act 没 act 都行。

`src/fx/moves/` 收录了由特效串成的完整攻击，从蓄力到收招：如果用户要的是一招"招式"而非单个特效，从这里开始。

## 3. 制作新特效

先读 `docs/AUTHORING.md`：它是规范契约（meta、纯特效用 `draw(p, t, o)` 或模拟特效用 `create(o)`、局部坐标系、无缝循环、结束时清空画面），也是工具集、painter API 和质量标准。然后：

1. **用一句话说清**，并附上美术方向：它是什么、如何运动、用什么调色板、节奏如何。"冰霜新星：水晶从脚底向外呈环形迸发，中心闪过一道白光，碎片旋转飞散，地面留霜并渐渐消退。"
2. **在库里找参考**：`node tools/list.mjs <words>`，然后读最接近的两三个特效文件，借用它们的技法（`src/core/sim.js` 里的 `Particles` 和 `Bits` 用来做火花、烟尘和碎屑，`p.disc` 用来做半透明体积，`cycle` 用来做无缝粒子，`tileFbm` 滚动用来做火焰和水）。也看看 [Hugo Duprez 的特效](https://www.spritefusion.com/pixel-art-vfx)里最接近的那几个：它们就是质量标杆。如果他的特效在同样的屏幕尺寸下细节更多、光更足、更有生气，你的就还没完成。
3. **起草。**`node tools/new.mjs <category>/<name>`（循环特效加 `--loop`）会生成一个能运行的文件。当方向还不确定时，写 3 到 5 个真正不同的草稿（`<name>-a.js` .. `-e.js`），全部渲染出来（`node tools/render.mjs "<category>/<name>-*"`），选定前逐张看每张联系表。如果用户在场，把最强的两三个展示给他们（`--gif` 可生成便于分享的动画）。
4. **看、评、改。**渲染，打开 `records/<id>/contact.png`，像挑剔的像素艺术家那样评判。修掉最严重的问题，再渲染。至少三轮；拿得出手的门面特效要更多轮。`--all` 显示全部帧，`--mp4` 以全速展示动态。
5. **演出来**，只要有人物参与：添加 `export const act`（见 `docs/AUTHORING.md` 中的 "Acts" 一节），在 t = 0 之前蓄力，出手帧切换姿势，命中时顿帧，随后收招。`node tools/act.mjs <id>` 显示连续的 12 fps 步进：动态要从这些步进图和 `--mp4` 来判断，不要靠联系表的采样帧。
6. **检查。**`node tools/check.mjs <id>` 能抓出画布外绘制、结束不清空的一次性特效、循环接缝、未设定种子的随机数和过慢的帧；对 act 还能抓出关键帧乱序、未知姿势字段以及手部瞬移。修到完全通过为止。删掉没保留的草稿。

要看什么问题，以及常见的修法：

| 你看到的现象 | 通常修法 |
|---|---|
| 1x 下糊成一团 | 减少颜色，轮廓清晰，一个视觉焦点，更大的形状 |
| 斑点：形状内部有孤立的噪点像素 | 少用噪声阈值，用 `at()` 量化，小形状上不要加噪声 |
| 飘忽、没有打击感 | 快进慢出（`ease.outQuart`/`outExpo`），加 1 到 2 帧的白色主帧（hero frame），缩短总时长 |
| 僵硬或机械 | 让每个粒子都有差异（大小、速度、延迟、寿命），加次级运动（火花、烟、碎屑） |
| 发灰发白 | 减少辉光（k 0.2 到 0.5），边缘色阶加深，白色只留给最热的核心 |
| 平淡无光 | 从一侧打光：左上更亮、右下一档更暗；底部加一档更暗的色阶 |
| 平滑渐变、有矢量感 | 颜色上用硬色阶；柔和只留给光照和半透明烟雾 |
| 该是烟雾的地方出现棋盘格 | 用 `SMOKE`、`VAPOUR` 或 `DUST` 粒子，或 `p.disc`：真正半透明、顶部受光 |
| 循环回卷时有接缝 | 用 `cycle`、`loopNoise(phase)`、整格 `tileNoise` 滚动、`sin(phase * TAU * n)` |
| 一次性特效结束时突兀跳掉 | 在 t = duration 之前让它缩小、抖动淡出或散落退场 |
| 特效很棒，人物却像死的 | 给它加 act：蓄力、出手姿势、命中顿帧、有反应的目标、收招 |
| 动作显得没有重量 | 朝出招反方向蓄力，更长的顿帧（最长 0.2 秒），更大的剪影变化，加抖动 |
| 命中时机不同步 | 把命中关键帧对齐到特效自身的常量，而不是目测的时间 |
| 他握武器的样子很别扭 | 手肘保持弯曲，长杆放在胸前；挥击时刀刃要滞后于手；手臂伸展约 15 px 且不拉伸，所以要让身体上前一步 |
| 双臂交叉或姿势显得扁平 | 他应朝向观众四分之三侧面：张开双臂时近手在左（`fx < 0`）、远手在右，并加 `turn: 1`；`yaw` 能让他真正转身 |

方向性特效朝右，地面特效站在 y = 0 上，人物特效包裹 `o.actor`（一个 24 x 38 内置标准人物的遮罩与像素），并且任何地方都不使用 `Math.random`。通用母题没问题；绝不要复刻某个具体游戏的精灵、角色或标志。

## 4. 用原生代码替代 JS

如果游戏跑不了 JS，而精灵图又不够用（比如特效要跟随移动目标，或需要在运行时按实例着色），就把特效移植过去。纯特效是时间的函数；模拟类特效则在 `src/core/sim.js` 中逐步推进粒子。保留双缓冲的思路、用于抖动 alpha 的 4x4 Bayer 阈值，以及调色板色阶查表。把 JS 原版和你的移植版并排渲染，确认两者一致。
