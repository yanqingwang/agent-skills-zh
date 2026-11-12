> **中文汉化版** · 上游：[obra/superpowers](https://github.com/obra/superpowers) · 原文件：`skills/test-driven-development/writing-good-tests.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 写好测试

**何时加载本参考：** 编写或修改测试、添加 mock，或为测试添加清理/辅助方法时。

## 概述

测试的存在是为了捕获某个特定的破坏。两条原则统领这里的一切：

```
1. Every test names the break it catches
2. Every test exercises the real thing
```

严格的 TDD（测试驱动开发）会自然产出这两者：先写测试、亲眼看它对真实代码失败，就已经证明它能够失败；只有当真实依赖确实缓慢或属于外部系统时，才允许引入 mock。

## 原则 1：说出破坏点

写测试体之前，先回答：**什么样的生产代码改动应该让这个测试失败？那个改动是 bug，还是一次有意的决定？** 一个测试靠捕获走错的分支、缺失的副作用、错误的参数、边界情况或被破坏的契约，来赢得自己的位置。

**独立推导期望值。** 使用字面量和人工核验过的 fixture；带字面量 `want` 值的表驱动测试是首选形态。由被测代码（或其辅助函数）计算出来的期望值，无论那段代码怎么写都会通过：

```typescript
// ❌ Mirror assertion: the same builder computes both sides — always true
const expected = buildSearchQuery({ tag: 'urgent' });
expect(buildSearchQuery({ tag: 'urgent' })).toBe(expected);

// ✅ Hand-derived literal
expect(buildSearchQuery({ tag: 'urgent' })).toBe('tag:"urgent"');
```

**不做变更探测器。** 如果只有有意决定才能让测试失败（常量的取值、消息的确切措辞、私有结构），那它会在重设计时误报，却放过真正的 bug。去测试依赖于该决定的行为：不是 `expect(MAX_RETRIES).toBe(5)`，而是"一次失败的调用会被重试 5 次，第 6 次尝试永远不会发生"。

**测行为，不测文本。** 断言某个脚本、Skill 或配置包含某行确切文本，只能证明"源码就是源码"。让脚本在受控输入下运行，然后断言输出、副作用或退出码。指示 Agent 的文档，由消费它的 Agent 的行为来测试（superpowers:writing-skills）；写给人的散文段落则根本不配得到测试。

**测你自己的代码，不测框架。** 测试你的代码在其边界上立下的契约：你注册的路由、你发出的查询、你产出的载荷。上游的内部机制由它们的维护者负责写测试（经典反例：断言你的路由器会调用已注册的处理器，那是框架的测试，不是你的）。当上游行为真正让你感到意外时，写一个窄范围的特征测试（characterization test），并写明所依赖的假设。同样的边界也适用于你代码内部：构造函数、getter、常量和纯转发逻辑，只有当它们做校验、规范化、设默认值、推导、强制约束或产生副作用时才配得到测试；否则，就断言依赖它们的第一个消费者可见结果。

### 闸门函数

```
BEFORE writing the test body:
  Name the production change that would make this test fail.

  Cannot name one            → redesign around an observable behavior
  "The source text changed"  → run the artifact and assert its effects
  Only intentional decisions → change detector; test the behavior
                               that depends on the decision

  Confirm the expected value is derived without the code under test.
  IF it reuses the code's logic or helpers:
    Replace it with a literal or hand-checked fixture
```

## 原则 2：测试真实的东西

**mock 不配得到断言。** 针对 mock 的断言，mock 在场就通过，mock 缺席就失败，它对组件本身只字未提。断言真实组件的行为；如果你检查的对象就是 mock，要么去掉 mock，要么删掉这条断言。

```typescript
// ✅ Real behavior
expect(screen.getByRole('navigation')).toBeInTheDocument();

// ❌ Mock existence
expect(screen.getByTestId('sidebar-mock')).toBeInTheDocument();
```

**你的人类搭档的纠正：** "我们是在测试 mock 的行为吗？"

**在正确的层级打 mock。** 替换真实方法之前，先弄清它的每一个副作用；mock 缓慢或外部的那一层，让测试依赖的部分保持真实。拿不准时，先对真实实现跑一遍测试，观察实际需要发生什么。

```typescript
// ❌ The mock swallows the config write that duplicate detection reads
vi.mock('ToolCatalog', () => ({
  discoverAndCacheTools: vi.fn().mockResolvedValue(undefined)
}));

// ✅ Mock only the slow server startup; the config write stays real
vi.mock('MCPServerManager');
```

**让测试替身（double）足够具体。** 当参数、调用次数或调用顺序属于契约的一部分时，要对它们断言；一个来者不拒的 fake 什么都验证不了。给每个分支（成功、出错、畸形输入）各配一套 fixture 或 spy，让走错的分支无法满足期望。

**完整镜像真实数据。** mock 要按现实中的完整结构来造（所有已文档化的字段），而不是只造你的测试会读的那几个字段。只造一半的 mock 会静默失败：当下游代码读到被省略的字段时，测试照常通过，集成却已经断了。

**生产类只承载生产方法。** 只有测试才需要的清理逻辑，放进测试工具（test utilities）里，绝不要作为 `destroy()` 挂到生产类上。问自己：这个方法是不是只有测试在调用？这个类是不是拥有这个资源的生命周期？答案不对 → 放进测试工具。

**优先用真实组件，而不是复杂 mock。** 当 mock 的搭建代码盖过测试逻辑、mock 缺少真实组件拥有的方法，或 mock 一变测试就坏时，改用真实组件的集成测试。**你的人类搭档的问题：** "这里我们真的需要用 mock 吗？"

### 闸门函数

```
BEFORE adding a mock or test helper:
  List the real method's side effects; keep the ones the test
  depends on real — mock the slow/external level below them.

  Mock responses mirror the complete real structure.

  A method only tests call lives in test utilities, not production.

  About to assert on the mock itself?
    Unmock it or delete the assertion.
```

## 测试随实现一起发布上线

TDD 循环（失败测试、最小实现、重构）就是"完成"的含义。只发布该行为所需的测试，一个不多：琐碎代码和写给人的散文段落不配得到测试，而为了满足流程写出来的测试，会永远消耗维护成本。

## 突变检查

收尾之前，在脑中突变生产代码；每一种现实可能的突变，都应至少让一个测试失败：

- 错误的常量或参数
- 错误的分支处理器
- 缺失的状态变更或副作用
- 空返回或默认返回
- 缺失对零值、空值、nil、未授权或畸形输入的校验

没有任何测试能捕获的突变，说明该行为没有被保护，或者说该测试是同义反复。

## 快速参考

| 当你…… | 应当 |
|-------------|-----|
| 写任何测试 | 说出它捕获的破坏：是 bug，不是有意的决定 |
| 构造期望值 | 手工推导，绝不用被测代码 |
| 测试脚本或文档 | 运行它 / 压测它的消费者；绝不 grep 它的文本 |
| 想测试依赖项 | 测试你自己的边界契约，而不是它们的文档化机制 |
| 想对 mock 元素断言 | 测试真实组件，或去掉 mock |
| 准备 mock 某个方法 | 先弄清它的副作用；mock 缓慢/外部的那一层 |
| 构造 mock 响应 | 完整镜像真实结构 |
| 需要只有测试在用的清理逻辑 | 放进测试工具函数 |
| 看到 mock 搭建代码膨胀 | 换成真实组件的集成测试 |
| 完成一个测试文件 | 执行突变检查 |

## 危险信号

- 准备与断言共享同一个对象，相等是必然的
- 测试只能因 panic、崩溃或选择器缺失而失败
- 每次有意改动测试都失败，意外的破坏却从不触发失败
- 期望值藏在循环、构造器或辅助函数背后
- 测试 grep 源码文本，或断言某个已删除的符号保持被删除
- 把你的代码删光、只剩框架时，这个测试依然"成立"
- 测试只为覆盖率而存在，不检查任何副作用或结果
- 某条断言检查的是 `*-mock` 测试 ID，或移除 mock 后测试就失败
- 某个方法只有测试文件在调用
- mock 搭建占了大半个测试，或你说不清为什么需要这个 mock
- 抱着"以防万一"的心态打 mock
