---
name: gsap-utils
description: GSAP 官方 gsap.utils Skill — clamp、mapRange、normalize、interpolate、random、snap、toArray、wrap、pipe。当用户询问 gsap.utils、clamp、mapRange、random、snap、toArray、wrap 或 GSAP 辅助工具函数时使用。
license: MIT
---

> **中文汉化版** · 上游：[greensock/gsap-skills](https://github.com/greensock/gsap-skills) · 原文件：`skills/gsap-utils/SKILL.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# gsap.utils

## 何时使用本 Skill

在编写或审查使用 **gsap.utils** 做数学计算、数组/集合处理、单位解析或动画取值映射的代码时适用（例如把滚动映射为某个值、随机化、吸附到网格，或归一化输入）。

**相关 Skill：** 构建动画时配合 **gsap-core**、**gsap-timeline** 与 **gsap-scrolltrigger** 使用；CustomEase 及其他缓动工具位于 **gsap-plugins**。

## 概述

**gsap.utils** 提供纯辅助函数；无需注册。可在补间 vars 中使用（如函数型值），可在 ScrollTrigger 或 Observer 回调中使用，也可在任何驱动 GSAP 的 JS 代码中使用。所有方法都位于 **gsap.utils** 上（如 `gsap.utils.clamp()`）。

**省略 value 参数：函数形式。** 许多工具函数把待转换的值作为**最后一个**参数。若省略该参数，工具函数会返回一个**函数**，稍后调用时再传入值。当需要以相同配置对多个值进行 clamp、map、normalize 或 snap 时（如在 mousemove 处理器或补间回调中），请使用函数形式。**例外：random()** — 请传入 **true** 作为最后一个参数以获得可复用的函数（不要省略 value）；参见 [random()](https://gsap.com/docs/v3/GSAP/UtilityMethods/random())。

```javascript
// With value: returns the result
gsap.utils.clamp(0, 100, 150); // 100

// Without value: returns a function you call with the value later
let c = gsap.utils.clamp(0, 100);
c(150);  // 100
c(-10);  // 0
```

## 钳制与区间映射

### clamp(min, max, value?)

把值约束在 min 与 max 之间。省略 **value** 则返回函数：`clamp(min, max)(value)`。

```javascript
gsap.utils.clamp(0, 100, 150); // 100
gsap.utils.clamp(0, 100, -10); // 0

let clampFn = gsap.utils.clamp(0, 100);
clampFn(150); // 100
```

### mapRange(inMin, inMax, outMin, outMax, value?)

把一个值从一个区间映射到另一个区间。用于把滚动位置、进度（0–1）或输入区间转换为动画区间。省略 **value** 则返回函数：`mapRange(inMin, inMax, outMin, outMax)(value)`。

```javascript
gsap.utils.mapRange(0, 100, 0, 500, 50);  // 250
gsap.utils.mapRange(0, 1, 0, 360, 0.5);   // 180 (progress to degrees)

let mapFn = gsap.utils.mapRange(0, 100, 0, 500);
mapFn(50);  // 250
```

### normalize(min, max, value?)

返回值在给定区间内归一化到 0–1 的结果。当目标区间为 0–1 时，它是区间映射的逆操作。省略 **value** 则返回函数：`normalize(min, max)(value)`。

```javascript
gsap.utils.normalize(0, 100, 50);   // 0.5
gsap.utils.normalize(100, 300, 200); // 0.5

let normFn = gsap.utils.normalize(0, 100);
normFn(50); // 0.5
```

### interpolate(start, end, progress?)

按给定进度（0–1）在两个值之间插值。支持数字、颜色以及键相匹配的对象。省略 **progress** 则返回函数：`interpolate(start, end)(progress)`。

```javascript
gsap.utils.interpolate(0, 100, 0.5);       // 50
gsap.utils.interpolate("#ff0000", "#0000ff", 0.5); // mid color
gsap.utils.interpolate({ x: 0, y: 0 }, { x: 100, y: 50 }, 0.5); // { x: 50, y: 25 }

let lerp = gsap.utils.interpolate(0, 100);
lerp(0.5); // 50
```

## 随机与吸附

### random(minimum, maximum[, snapIncrement, returnFunction]) / random(array[, returnFunction])

返回 **minimum**–**maximum** 范围内的随机数，或从**数组**中随机取出一个元素。可选的 **snapIncrement** 会把结果吸附到最近的倍数（如 `5` → 5 的倍数）。**要获得可复用的函数**，请将 **true** 作为最后一个参数（**returnFunction**）传入；返回的函数不接受参数，每次调用返回一个新的随机值。这是唯一一个以传入 `true`（而非省略 value）来获得函数形式的工具函数。

```javascript
// immediate value: number in range
gsap.utils.random(-100, 100);        // e.g. 42.7
gsap.utils.random(0, 500, 5);        // 0–500, snapped to nearest 5

// reusable function: pass true as last argument
let randomFn = gsap.utils.random(-200, 500, 10, true);
randomFn();  // random value in range, snapped to 10
randomFn();  // another random value

// array: pick one value at random
gsap.utils.random(["red", "blue", "green"]);  // "red", "blue", or "green"
let randomFromArray = gsap.utils.random([0, 100, 200], true);
randomFromArray();  // 0, 100, or 200
```

**补间 vars 中的字符串形式：** 使用 `"random(-100, 100)"`、`"random(-100, 100, 5)"` 或 `"random([0, 100, 200])"`；GSAP 会对每个目标分别求值。

```javascript
gsap.to(".box", { x: "random(-100, 100, 5)", duration: 1 });
gsap.to(".item", { backgroundColor: "random([red, blue, green])" });
```

### snap(snapTo, value?)

把值吸附到 **snapTo** 的最近倍数，或允许值数组中最近的值。省略 **value** 则返回函数：`snap(snapTo)(value)`（或 `snap(snapArray)(value)`）。

```javascript
gsap.utils.snap(10, 23);     // 20
gsap.utils.snap(0.25, 0.7);  // 0.75
gsap.utils.snap([0, 100, 200], 150); // 100 or 200 (nearest in array)

let snapFn = gsap.utils.snap(10);
snapFn(23); // 20
```

在补间中使用，可实现网格或步进式动画：

```javascript
gsap.to(".x", { x: 200, snap: { x: 20 } });
```

### shuffle(array)

返回一个元素相同但顺序随机的新数组。用于随机化顺序（例如为 “random” 模式的 stagger 提供打乱后的副本）。

```javascript
gsap.utils.shuffle([1, 2, 3, 4]); // e.g. [3, 1, 4, 2]
```

### distribute(config)

**返回一个函数**，根据每个目标在数组（或网格）中的位置为其分配值。高级 stagger 内部就使用它；只要需要把一组值铺开到多个元素上（如 scale、opacity、x、delay），都可以使用它。返回的函数接收 `(index, target, targets)` — 既可以手动调用，也可以把结果直接传入补间；GSAP 会按目标逐个调用它，并传入 index、元素和数组。

**配置项（均可选）：**

| 属性 | 类型 | 说明 |
|----------|------|-------------|
| `base` | Number | 起始值。默认 `0`。 |
| `amount` | Number | 分配到所有目标上的总量（加到 base 上）。例如 100 个目标时 `amount: 1` → 相邻目标之间相差 0.01。若要为每个目标设定固定步长，请改用 **each**。 |
| `each` | Number | 相邻目标之间累加的量（加到 base 上）。例如 4 个目标时 `each: 1` → 0, 1, 2, 3。若要把总量拆分，请改用 **amount**。 |
| `from` | Number \| String \| Array | 分布起点：索引，或 `"start"`、`"center"`、`"edges"`、`"random"`、`"end"`，或如 `[0.25, 0.75]` 的比例。默认 `0`。 |
| `grid` | String \| Array | 使用网格位置而非扁平索引：`[rows, columns]`（如 `[5, 10]`）或 `"auto"` 自动检测。省略则按扁平数组处理。 |
| `axis` | String | 网格模式下：限制在单一轴上（`"x"` 或 `"y"`）。 |
| `ease` | Ease | 沿缓动曲线分布值（如 `"power1.inOut"`）。默认 `"none"`。 |

**在补间中：** 将 `distribute(config)` 的结果作为属性值传入；GSAP 会以 `(index, target, targets)` 为每个目标调用该函数。

```javascript
// Scale: middle elements 0.5, outer edges 3 (amount 2.5 distributed from center)
gsap.to(".class", {
  scale: gsap.utils.distribute({
    base: 0.5,
    amount: 2.5,
    from: "center"
  })
});
```

**手动使用：** 以 `(index, target, targets)` 调用返回的函数，即可得到该索引对应的值。

```javascript
const distributor = gsap.utils.distribute({
  base: 50,
  amount: 100,
  from: "center",
  ease: "power1.inOut"
});
const targets = gsap.utils.toArray(".box");
const valueForIndex2 = distributor(2, targets[2], targets);
```

更多信息参见 [distribute()](https://gsap.com/docs/v3/GSAP/UtilityMethods/distribute/)。

## 单位与解析

### getUnit(value)

返回值的单位字符串（如 `"px"`、`"%"`、`"deg"`）。在归一化或转换值时使用。

```javascript
gsap.utils.getUnit("100px");   // "px"
gsap.utils.getUnit("50%");     // "%"
gsap.utils.getUnit(42);        // "" (unitless)
```

### unitize(value, unit)

为数字追加单位；若值已带单位则原样返回。在构建 CSS 值或补间终点值时使用。

```javascript
gsap.utils.unitize(100, "px");  // "100px"
gsap.utils.unitize("2rem", "px"); // "2rem" (unchanged)
```

### splitColor(color, returnHSL?)

把颜色字符串转换为数组：**[red, green, blue]**（0–255），或 **[red, green, blue, alpha]**（当 alpha 存在或需要时，RGBA 为 4 个元素）。将 **true** 作为第二个参数（**returnHSL**）传入，则改为返回 **[hue, saturation, lightness]** 或 **[hue, saturation, lightness, alpha]**（HSL/HSLA）。支持 `"rgb()"`、`"rgba()"`、`"hsl()"`、`"hsla()"`、十六进制和命名颜色（如 `"red"`）。在制作颜色分量动画或构建渐变时使用。参见 [splitColor()](https://gsap.com/docs/v3/GSAP/UtilityMethods/splitColor/)。

```javascript
gsap.utils.splitColor("red");                    // [255, 0, 0]
gsap.utils.splitColor("#6fb936");                // [111, 185, 54]
gsap.utils.splitColor("rgba(204, 153, 51, 0.5)"); // [204, 153, 51, 0.5] (4 elements)
gsap.utils.splitColor("#6fb936", true);          // [94, 55, 47] (HSL: hue, saturation, lightness)
```

## 数组与集合

### selector(scope)

返回一个限定作用域的选择器函数，只在给定元素（或 ref）内部查找元素。在组件中使用，使 `".box"` 这类选择器只匹配该组件的后代，而不是整个文档。接受 DOM 元素或 ref（如 React ref；会处理 `.current`）。

```javascript
const q = gsap.utils.selector(containerRef);
q(".box");        // array of .box elements inside container
gsap.to(q(".circle"), { x: 100 });
```

### toArray(value, scope?)

把值转换为数组：选择器字符串（限定在元素范围内）、NodeList、HTMLCollection、单个元素或数组。在向 GSAP 传入混合类型的输入（如 targets）且需要真正的数组时使用。

```javascript
gsap.utils.toArray(".item");           // array of elements
gsap.utils.toArray(".item", container); // scoped to container
gsap.utils.toArray(nodeList);          // [ ... ] from NodeList
```

### pipe(...functions)

组合函数：**pipe(f1, f2, f3)(value)** 返回 f3(f2(f1(value)))。在补间或回调中需要依次应用一串转换（如 normalize → mapRange → snap）时使用。

```javascript
const fn = gsap.utils.pipe(
  (v) => gsap.utils.normalize(0, 100, v),
  (v) => gsap.utils.snap(0.1, v)
);
fn(50); // normalized then snapped
```

### wrap(min, max, value?)

把值回绕到 min–max 区间内（含 min，不含 max）。用于无限滚动或循环取值。省略 **value** 则返回函数：`wrap(min, max)(value)`。

```javascript
gsap.utils.wrap(0, 360, 370);  // 10
gsap.utils.wrap(0, 360, -10);   // 350

let wrapFn = gsap.utils.wrap(0, 360);
wrapFn(370); // 10
```

### wrapYoyo(min, max, value?)

以 yoyo 方式把值回绕到区间内（在两端反弹）。用于区间内的往复取值。省略 **value** 则返回函数：`wrapYoyo(min, max)(value)`。

```javascript
gsap.utils.wrapYoyo(0, 100, 150); // 50 (bounces back)

let wrapY = gsap.utils.wrapYoyo(0, 100);
wrapY(150); // 50
```

## 最佳实践

- ✅ 当同一个区间/配置被多次使用时（如滚动处理器、补间回调），省略 value 参数以获得可复用的函数：`let mapFn = gsap.utils.mapRange(0, 1, 0, 360); mapFn(progress)`。
- ✅ 网格对齐或步进取值时使用 **snap**；当 GSAP 或你的代码需要从选择器或 NodeList 得到真正的数组时，使用 **toArray**。
- ✅ 在组件中使用 **gsap.utils.selector(scope)**，使选择器限定在容器或 ref 的作用域内。

## 禁止事项

- ❌ 不要假设 **mapRange** / **normalize** 会处理单位；它们只作用于数字。涉及单位时请使用 **getUnit** / **unitize**。
- ❌ 不要覆盖或依赖未在文档中说明的行为；坚持使用文档化的 API。

### 了解更多

https://gsap.com/docs/v3/HelperFunctions
