---
name: threejs-scene-setup
description: >
  搭建并调试一个原生 three.js r187 游戏或 3D 场景：import map、Scene、PerspectiveCamera
  与 WebGLRenderer、配合 Timer 的 setAnimationLoop、resize、OrbitControls 以及 WebGPURenderer。
  在遇到 "Failed to resolve module specifier three"、黑屏画布或画面不动时使用。不适用于 GLB
  加载（`threejs-gltf-loading`）、材质（`threejs-materials-lighting`）或 React Three Fiber。
---

> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/web-engines/threejs-scene-setup/SKILL.md` · License: Apache-2.0
> 翻译日期：2026-11-12 · 同步状态：上游 HEAD（2026-11-12 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# three.js 场景搭建

搭建每个 three.js 游戏都需要的基础：模块加载、场景、相机与渲染器、一个渲染循环、resize 处理，以及分辨率预算。以下模式针对 **r187**。先读取已安装的 `three` 版本；addons、默认值与弃用项每个版本都在变动。

## 何时使用

- 初始化一个 three.js 场景、修复黑屏或空白画布、让画布自适应、搭建循环、加入 `OrbitControls`，或在 `WebGLRenderer` 与 `WebGPURenderer` 之间做选择。
- `package.json` 依赖 `three`，或代码中出现 `import * as THREE from 'three'`。
- 不适用于模型与动画（`threejs-gltf-loading`）、表面外观、光照与阴影（`threejs-materials-lighting`），也不适用于 React Three Fiber（`@react-three/fiber`）组件，其 `<Canvas>` 自行管理渲染器与循环。2D 场景请用 `pixijs-rendering` 或 Phaser。

## 工作流程

1. **从 `package.json` 或 import map 中读取 `three`。** 现有项目沿用其版本，除非用户要求升级。
2. **用打包器或 import map 解析 `three` 与 `three/addons/`**；addons 位于 `three/addons/...` 之下。
3. **创建场景、相机与渲染器**，把相机从原点后移，并给像素比设置上限（模式 2）。
4. **先用一个不受光的 mesh 验证整条管线**（`MeshNormalMaterial`）。之后再切换到受光材质并加入灯光。
5. **一切都由 `renderer.setAnimationLoop` 驱动**，配合 `Timer` 与经过钳制的 delta。把游戏状态保存在普通对象里，每帧再拷贝到 mesh 上。这样 mesh 始终是视图，状态也能在没有 GPU 的情况下保存与测试。
6. **处理 resize**（aspect、投影矩阵、渲染器尺寸），并在开发时加入 `OrbitControls`。
7. **验证**，参见 [验证](#verify)。

## 模式

### 1. Import map（无打包器）


```html
<canvas id="c"></canvas>
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.187.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.187.0/examples/jsm/"
  }
}
</script>
<script type="module" src="./main.js"></script>
```


使用 Vite 或 webpack 时，执行 `npm i three`，同样的导入无需 map 即可解析。

### 2. 场景、相机与渲染器


```js
import * as THREE from 'three';

const canvas = document.querySelector('#c');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); // starting budget; profile on target hardware
renderer.setSize(window.innerWidth, window.innerHeight);

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x101018);

const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 100);
camera.position.set(3, 2, 5);
camera.lookAt(0, 0, 0);

const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
scene.add(cube);

Object.assign(window, { renderer, scene }); // for the smoke check and console debugging
```


### 3. 配合 Timer 的渲染循环


```js
const timer = new THREE.Timer();        // replaces the deprecated THREE.Clock (r183+)
timer.connect(document);                // optional: no huge delta after a hidden tab

renderer.setAnimationLoop(() => {
  timer.update();                      // use performance.now(), like visibility reset
  const dt = Math.min(Math.max(timer.getDelta(), 0), 0.1); // seconds; bound stalls and negative deltas
  cube.rotation.x += dt;                // frame-rate independent
  cube.rotation.y += dt * 0.7;
  renderer.render(scene, camera);
});
// renderer.setAnimationLoop(null); // stop the loop
// timer.dispose();                 // remove visibility listener when tearing down
```


当 timer 已连接时，调用不带参数的 `update()`。可见性重置会采样 `performance.now()`，因此在隐藏标签页刚恢复时传入循环的时间戳可能产生负的 delta。钳制同时也保护固定步长累加器；0.1 s 的上限会刻意丢弃卡顿之后的时间，请按游戏的追帧策略调整它。

### 4. resize 处理


```js
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();      // required after changing aspect
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```


### 5. OrbitControls


```js
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
// In the loop, before render: controls.update(); (required every frame with damping)
```


### 6. WebGPURenderer，仅在需要时使用

默认继续使用 `WebGLRenderer`。当项目需要 TSL 节点材质或计算着色器时再切换；在缺少 WebGPU 的环境下，`WebGPURenderer` 会回退到 WebGL 2 后端。


```js
// Official WebGPU examples map both "three" and "three/webgpu" to
// build/three.webgpu.js, plus "three/tsl" to build/three.tsl.js.
import * as THREE from 'three/webgpu';

const renderer = new THREE.WebGPURenderer({ antialias: true });
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5)); // starting budget; profile on target hardware
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);
await renderer.init();                  // required before direct render()/compute()

renderer.setAnimationLoop(() => renderer.render(scene, camera));
```


场景、相机、内置的 `Mesh*Material` 以及大多数 addons 都能沿用。自定义 GLSL（`ShaderMaterial`、`onBeforeCompile`）不行。

## 验证

1. `npm run build`（或用与 `three` 版本匹配的 `@types/three` 执行 `npx tsc --noEmit`）通过。
2. 在无头浏览器里做冒烟测试。保持开发服务器运行，并按模式 2 暴露 `window.renderer`，在 `npm i -D playwright` 和 `npx playwright install chromium` 之后运行 `node smoke.mjs <url>`。若没有浏览器自动化，请让用户打开页面，然后报告控制台输出，以及立方体是否可见、是否在转动。


```js
// smoke.mjs: fails on page errors; checks that frames are drawn and survive a context loss.
import { chromium } from 'playwright';

const browser = await chromium.launch();
const page = await browser.newPage();
const errors = [];
page.on('pageerror', (e) => errors.push(e.message));
page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
await page.goto(process.argv[2]);
await page.waitForFunction(() => window.renderer?.info.render.calls > 0, null, { timeout: 15000 });
const state = await page.evaluate(() => ({
  drawCalls: window.renderer.info.render.calls,
  triangles: window.renderer.info.render.triangles,
  geometries: window.renderer.info.memory.geometries,
  canvas: [window.renderer.domElement.width, window.renderer.domElement.height],
}));
await page.screenshot({ path: 'smoke.png' });
await page.evaluate(async () => {           // WebGLRenderer only: lose and restore the context
  if (!window.renderer.forceContextLoss) return;
  window.renderer.forceContextLoss();
  await new Promise((r) => setTimeout(r, 200));
  window.renderer.forceContextRestore();
  await new Promise((r) => setTimeout(r, 500));
});
await page.screenshot({ path: 'smoke-restored.png' });
await browser.close();
console.log(JSON.stringify({ ...state, errors }, null, 2));
process.exit(errors.length ? 1 : 0);
```


预期 `drawCalls` 大于 0、画布尺寸不是 0 × 0，且没有报错。打开两张截图：第二张仍须显示场景，否则说明有东西占用了 GPU 对象，而恢复流程没有重建它们。

## 常见陷阱

- **`Failed to resolve module specifier "three"`** → 缺少 import map 或打包器。同时映射 `"three"` 与 `"three/addons/"`；addons 条目必须以 `/` 结尾。
- **画布全黑，且没有报错** → 相机位于物体内部或后方，或受光材质没有灯光。把相机后移，用 `MeshNormalMaterial` 测试。
- **resize 后画面被拉伸** → 只调整了渲染器尺寸，却没有更新 `camera.aspect` 和 `updateProjectionMatrix()`。
- **在 HiDPI 与手机上又慢又烫** → 像素比为 2 时绘制的像素是 1 的四倍，所以在 2× 屏幕上把上限设为 2 毫无作用。从 1.25 到 1.5 起步，并提供分辨率设置；自适应分辨率见参考文档。
- **标签页切回后模拟卡住** → 在 r186 和 r187 中，传给 `timer.update(time)` 的循环时间戳可能早于可见性重置，从而产生负的 delta。调用不带参数的 `update()`，并按模式 3 做钳制。
- **`THREE.Clock: This module has been deprecated`** → 自 r183 起；改用 `THREE.Timer`。
- **旧教程还在用 `<script src="three.min.js">` 或 `examples/js/...`** → `examples/js` 在 r148 移除，`build/three.min.js` 在 r161 移除。改用模块与 import map。
- **OrbitControls 像失灵了一样** → 开启 `enableDamping` 后，必须每帧调用 `controls.update()`。
- **GPU 重置或标签页开多了之后画布变黑** → WebGL 上下文丢失了。`WebGLRenderer` 会处理 `webglcontextlost` 并在恢复时重建自身状态；而保留了原始 GL 对象、或在丢失期间跳过循环的代码无法恢复。按「验证」一节用 `forceContextLoss()` / `forceContextRestore()` 测试。
- **`.render() called before the backend is initialized`**（WebGPURenderer）→ 在直接调用 `render()`/`compute()` 之前先 `await
  renderer.init()`，或只从 `setAnimationLoop` 渲染，它会先完成初始化。
- **`Material "ShaderMaterial" is not compatible`，或 `onBeforeCompile` 无效**（WebGPURenderer）→ 它只渲染节点材质。把效果移植到 TSL，或继续留在 `WebGLRenderer`。

## 参考资料

- 阅读 [`references/scene-graph.md`](references/scene-graph.md)，了解坐标约定、用 `Group` 做父子关系、`OrthographicCamera` 用于 2.5D、在关卡之间释放几何体 / 材质 / 纹理、停止循环、按需渲染以及自适应分辨率。

## 相关 Skill

- `threejs-materials-lighting`：光照、阴影、PBR 与环境贴图。
- `threejs-gltf-loading`：加载模型并播放其动画。
- `camera-systems`：跟随、环绕与第一人称相机设计。
- `fps-shooter`：基于这些 Skill 构建的 3D 游戏类型。

## 版本说明

最后核对：2026-11-11，基于 three r187（npm `three@0.187.0`，发布于 2026-10-30；`@types/three@0.187.0`）。

- `Timer.update()` 在 r186 与 r187 之间没有变化，因此关于负 delta 的说明依旧适用。
- r187 的 WebGPU 示例仍把 `three` 与 `three/webgpu` 映射到 `build/three.webgpu.js`。
- 来源：[r187 release notes](https://github.com/mrdoob/three.js/releases/tag/r187)、[Migration Guide](https://github.com/mrdoob/three.js/wiki/Migration-Guide)、[r187 Timer.js](https://github.com/mrdoob/three.js/blob/r187/src/core/Timer.js)、[r187 responsive rendering manual](https://github.com/mrdoob/three.js/blob/r187/manual/pages/responsive.html)、[WebGLRenderer.js context handling](https://github.com/mrdoob/three.js/blob/r187/src/renderers/WebGLRenderer.js)。
