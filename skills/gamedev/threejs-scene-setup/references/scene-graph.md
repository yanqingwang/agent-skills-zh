> **中文汉化版** · 上游：[gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) · 原文件：`skills/web-engines/threejs-scene-setup/references/scene-graph.md` · License: Apache-2.0
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# three.js 场景图、相机与资源清理（r150+）

scene-setup skill 背后的底层细节：坐标约定、`Object3D`
层级结构、正交相机、资源释放，以及分辨率预算。

目录：

- 坐标与约定
- Object3D 层级结构
- PerspectiveCamera 与 OrthographicCamera 的对比
- 释放资源（避免内存泄漏）
- 停止与重启渲染循环
- 按需渲染
- 自适应分辨率

## 坐标与约定

- 右手坐标系：**+X 向右，+Y 向上，+Z 朝向观察者**。新建的
  `PerspectiveCamera` 朝 **-Z** 方向看。
- 旋转用**弧度**表示（`PerspectiveCamera` 的 `fov` 例外，单位是度）。
  如果你习惯用度思考，请用 `THREE.MathUtils.degToRad(deg)` 换算。
- 单位可以任选，但必须保持一致。glTF 模型以米为单位制作；选定一个
  比例后在整个项目中坚持使用。

## Object3D 层级结构

一切可见对象（`Mesh`、`Group`、`Camera`、`Light`）都继承自 `Object3D`，都拥有
`position`、`rotation`、`quaternion` 和 `scale`。子对象继承父对象的
变换。

```js
import * as THREE from 'three';

const turret = new THREE.Group();         // empty transform node
turret.add(barrelMesh);                   // child, positioned relative to turret
scene.add(turret);
turret.rotation.y = Math.PI / 4;          // rotates the whole group

barrelMesh.removeFromParent();            // detach (r129+)
scene.add(barrelMesh);                    // re-parent to the scene root
```

实用的遍历/查找辅助方法：

```js
scene.getObjectByName('Player');          // first descendant with that .name
root.traverse((obj) => { /* visit every descendant */ });
obj.getWorldPosition(new THREE.Vector3()); // world-space position
```

不要缩放物理/玩法对象的父级：非单位缩放会沿子级层层叠加，
让世界坐标计算（射线检测、距离）容易出错。

## PerspectiveCamera 与 OrthographicCamera 的对比

- **PerspectiveCamera(fov, aspect, near, far)**：物体随距离增加而缩小。
  3D 场景的默认选择。`near`/`far` 在场景允许的前提下尽量收紧；far/near
  比值过大会毁掉深度精度（z-fighting）。
- **OrthographicCamera(left, right, top, bottom, near, far)**：没有透视效果；
  适合 2.5D、等距（isometric）或类 CAD 视图。视锥体尺寸要按宽高比来定：

```js
const aspect = window.innerWidth / window.innerHeight;
const d = 5;
const cam = new THREE.OrthographicCamera(-d * aspect, d * aspect, d, -d, 0.1, 100);
// On resize, recompute left/right from the new aspect, then updateProjectionMatrix().
```

修改任何投影属性（`aspect`、`fov`、视锥体范围、`zoom`）之后，
都要调用 `camera.updateProjectionMatrix()`。

## 释放资源（避免内存泄漏）

three.js 不会替你垃圾回收 GPU 显存。把对象从场景中移除
不会释放任何 GPU 资源；你必须显式 dispose 几何体、材质和
纹理。

```js
// Disposes everything under obj. Skip geometries/materials/textures that other
// objects still share, or they will be re-uploaded (or break) on the next frame.
function disposeObject(obj) {
  obj.traverse((node) => {
    if (node.geometry) node.geometry.dispose();
    const materials = Array.isArray(node.material) ? node.material : [node.material];
    for (const mat of materials) {
      if (!mat) continue;
      for (const key of Object.keys(mat)) {
        const value = mat[key];
        if (value && value.isTexture) value.dispose(); // map, normalMap, etc.
      }
      mat.dispose();
    }
    if (node.isSkinnedMesh) node.skeleton.dispose();    // bone texture
    node.dispose();   // Object3D.dispose() (r186+): shadow maps, instancing buffers
  });
  obj.removeFromParent();
}
```

自 r186 起，每个对象都带 `Object3D.dispose()`（更早的版本只有灯光、
`InstancedMesh` 和 `BatchedMesh` 才有；旧版本请用 `node.dispose?.()` 做防护）。
基类方法不释放几何体、材质或纹理；这些仍需手动处理
（`BatchedMesh` 是例外：它自己持有并 dispose 自己的几何体）。

渲染目标也要 dispose（`renderTarget.dispose()`），整体拆除时还要
dispose 渲染器（`renderer.dispose()`）。切换关卡时，先 dispose 旧关卡的
子树再加载下一关，否则显存会随每次切换持续增长。

## 停止与重启渲染循环

`renderer.setAnimationLoop(fn)` 启动循环；`setAnimationLoop(null)` 停止它
（例如标签页经 Page Visibility API 隐藏时，或菜单打开时）。WebXR 也要求
使用这种循环；`requestAnimationFrame` 无法驱动 XR
帧。

## 按需渲染

静态场景或编辑器不需要持续循环。只在发生变化时渲染
（输入、controls 的 `change` 事件、补间动画的一步）：

```js
let needsRender = true;
controls.addEventListener('change', () => { needsRender = true; });
renderer.setAnimationLoop(() => {
  controls.update();          // keeps damping alive; fires 'change' while moving
  if (!needsRender) return;
  needsRender = false;
  renderer.render(scene, camera);
});
```

对非动画内容，这能大幅降低 GPU 与电量消耗。

## 自适应分辨率

像素比就是填充率预算：同样 CSS 尺寸下，比值为 2 时绘制的像素是 1 的四倍。
瓶颈在 GPU 时调低它有用；瓶颈在模拟运算时则没用。

运行时自适应方法：

- 在资源加载完毕、着色器预热完成后，测量数秒的帧时间。忽略
  标签页隐藏的时间段和加载卡顿。
- 如果 GPU 持续超出预算，按 0.25 的步长下调比值，降到设定的下限
  （例如 1）。绝不能高于设备比值或用户自己设置的值。
- 再次上调前，先等待冷却期，并使用单独的、更高的恢复阈值，
  否则比值会来回震荡。
- 显示器或 `devicePixelRatio` 变化时，重新应用选定的比值，并按渲染器
  同步调整渲染目标和后处理缓冲区的尺寸。
