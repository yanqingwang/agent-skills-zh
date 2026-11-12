> **中文汉化版** · 上游：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 原文件：`plugins/mcp-server-dev/skills/build-mcp-app/references/payload-budgeting.md` · License: Apache-2.0
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 载荷预算

宿主会限制工具结果文本的大小。claude.ai 与 Claude Desktop 大约在 **150,000 字符**处截断；Claude Code 约 25k token。工具结果超过上限时，宿主会用一个文件指针字符串替换你的 JSON。widget 随后在 `ontoolresult` 里收到非 JSON 内容，`JSON.parse` 抛错，用户看到类似 *"Bad payload: SyntaxError: Unexpected token 'E'"* 的报错，完全看不出大小才是原因。

## 症状 → 原因

| 症状 | 可能原因 |
|---|---|
| widget 在 `content[0].text` 上报 JSON 解析错误 | 结果超过宿主上限；宿主换成了文件指针字符串 |
| 单个查询正常，"所有 X"就坏 | 行数 × 列数越过了上限 |
| MCP Inspector 里正常，Desktop 里坏 | Inspector 没有上限；Desktop 有 |

## 策略

把自己的载荷控制在约 130KB 内，按顺序降级：

1. `JSON.stringify(rows).length` 未超上限时，**整行返回**。
2. **裁剪列**，只留渲染规格实际引用的列。遍历规格时既找 `field: "..."` 键，也找表达式字符串里的 `datum.X` / `datum['X']`：如果规格通过 `calculate` transform 给某列起了别名，别名以 `field:` 出现，但源列只以 `datum.X` 出现，删掉它 widget 就会拿到 NaN。
3. **截断行**是最后手段，载荷里带上 `{ truncated: N }`，让 widget 能标注出来。

```ts
const MAX = 130_000;
let out = rows;
if (JSON.stringify(out).length > MAX) {
  const keep = referencedFields(spec); // field: + datum.X refs
  out = rows.map((r) => pick(r, keep));
  if (JSON.stringify(out).length > MAX) {
    const per = JSON.stringify(out[0] ?? {}).length || 1;
    out = out.slice(0, Math.floor(MAX / per));
  }
}
```

## 大体积资源走 `callServerTool`，不走结果

几何数据、图片字节，或任何 widget 需要、Claude 不需要的大块数据，应由单独的工具提供，widget 挂载后再调用：

```js
const topo = await app.callServerTool({ name: "get-topojson", arguments: { level } });
```

给这个辅助工具标上 `_meta.ui.visibility: ["app"]`，它就不会出现在 Claude 的工具列表里。
