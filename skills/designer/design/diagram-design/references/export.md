> **中文汉化版** · 上游：[unknown-upstream](https://github.com/unknown-upstream) · 原文件：`skills/designer/design/diagram-design/references/export.md` · License: MIT
> 翻译日期：2026-11-13 · 同步状态：上游 HEAD（2026-11-13 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 导出为 PNG / SVG

把生成的图表 HTML 文件转换成与之同目录的可移植 `.svg` 和/或 `.png`。**仅限手动触发：绝不在无人要求时自动运行。**

## 触发条件

在以下情况加载本文件：

- 用户调用 `/diagram-design:export-diagram <html-file>`（插件的斜杠命令，定义在仓库根目录的 `commands/export-diagram.md`）。
- 用户用自然语言要求把图表导出、保存、栅格化、转换或下载为 `.svg` 或 `.png` 形式。常见说法：
  - "把这个导出为 PNG"
  - "保存为 SVG"
  - "给我那张图表的 PNG"
  - "把它栅格化"
  - "转换成 png 和 svg"

斜杠命令是一个薄封装，把工作委托到这里：两条路径执行的都是下面同一套流程。

## 范围

两种格式都**只含图表**：即 `<svg>` 节点本身。编辑性包装（`-full` 变体中的页眉、摘要卡片、页脚）被有意舍弃：导出交付物就是图表本身，适合放进 Figma、幻灯片、社交卡片或博客配图。

仅 SVG 导出会把源 `<title>` 和 `<desc>` 连同图表一起保留。它们按图、按变体加前缀的 ID 保证多张图同页时，可访问名称是唯一的。

在同一个宿主文档中内联多个导出 SVG，还要求 `<defs>` ID 带命名空间（markers、patterns、gradients、filters、clip paths、masks、symbols）。导出流程会给这些 ID 加上源文件 slug 前缀，并改写匹配的 `url(#…)` / `href="#…"` 引用，这样一张浅色图与它的 `-dark` 孪生图不会悄悄共用箭头。仅有可访问名称的唯一性保证还不够。

如果用户明确要的是"包含卡片的整页截图"，那是另一个请求：改用用户的操作系统或浏览器做一次普通的整页截图。

## SVG 导出流程

**优先使用打包的辅助脚本。**在本 skill 目录下运行：

```
python3 scripts/export_svg.py <html-file> [<out.svg>] [--system-fonts]
```

`--system-fonts` 跳过 Google Fonts 的 `@import` 与自带的 `@font-face` 声明（第 5 步），使 SVG 不发起网络请求；当皮肤的字体来源是 `system` 时使用它（见 [style-guide.md § Font source](style-guide.md#font-source)）。图表 CSS 仍然会带上。

源文件读取或输出写入失败会返回退出码 2 并附错误诊断。viewport 必须包含四个有限的 SVG 数字且宽高为正；空 viewport 或被禁用的 viewport 会被拒绝。class-without-style 门检查的是非空的实际 `class` 属性；注释、可见文本、空 class 值和 `data-class` 元数据都不要求存在样式表。导出会选出一个仍然存活的 SVG，并携带仍然存活的 style 块；HTML 注释和脚本字面量不贡献图表或 CSS。选中的 SVG 在它自己的闭合标签处结束，因此嵌套的图标 `<svg>` 元素留在其中。选中 SVG 内部的注释保持原样，但 XML 禁止注释中出现 `--`，也禁止注释以 `-` 结尾：每个 `--` 变成 `- -`，结尾的 `-` 后面补一个空格。这个脚本是下述变换的唯一事实来源（CSS 迁移、defs ID 命名空间化、rgba 归一化，以及 class-without-style 门）。只有当辅助脚本不可用时才重新实现，且行为必须保持一致。

文本与属性中的数字字符引用按 HTML 规则解码，包括不带分号的十进制/ hexadecimal 形式，以及 `&#128;` → `€` 的映射。已转义的引用只解码一次；注释、CDATA 和原始 style/script 主体不经此归一化解码。XML 无法表示的字符会导致导出失败，而不是被悄悄删除。

### 手工算法（辅助脚本所做的事情）

1. 读取源 HTML 文件。
2. 提取**第一个**顶层 `<svg ...>...</svg>` 元素。跳过 HTML 注释、`<script>` 和 `<style>` 内容，然后统计 `<svg` 开标签与 `</svg>` 闭标签的数量（自闭合的 `<svg .../>` 不算开标签），计数归零时停止。把带引号的属性值整体读取，这样值内部的 `>` 或 `/>` 不会终结标签。非贪婪正则会在嵌套图标的 `</svg>` 处停下并截断图表。大多数生成的图表只有一个顶层 SVG；若有多个，第一个就是图表本身（gallery 文件是例外，见*边界情况*）。
3. 使其独立可用：
   - 确保开标签带有 `xmlns="http://www.w3.org/2000/svg"`。缺失则补上。SVG 命名空间必须属于根 SVG 元素；后代元素上的命名空间不算数。显式不兼容的根命名空间会被拒绝。
   - 确保存在 `viewBox`。本 skill 的模板总是包含它；如果缺失，警告用户而不是瞎猜。
   - 按书写原样保留 `role="img"`、`aria-labelledby`，以及首个子元素 `<title>` / `<desc>`。
   - 把仅 HTML 支持的属性语法改写为 XML：无值属性（`<g data-motion-item>`）变成 `data-motion-item=""`，未加引号的值加上双引号。标签与属性中已知的命名 HTML 字符引用变成等价的 XML 安全文本（例如 `&nbsp;` 变成不换行空格）。`&copy`、`&nbsp` 这类 HTML 遗留名即使不带分号也会解码，但属性值中下一个字符是字母、数字或 `=` 时除外，与浏览器行为一致。解码一次并转义 XML 分隔符；已转义的引用保持转义。注释、CDATA 和原始 style/script 内容按书写保留；style/script 开标签的属性与其他属性走同样的引用转换。
   - 让注释成为合法 XML。对 CDATA 之外的每个 `<!-- ... -->`，把每个 `--` 变成 `- -`，正文以 `-` 结尾时补一个空格。拒绝浏览器会在下一个 `-->` 之前提前闭合的注释（`<!-->`、`<!--->`，或包含 `--!>` 的注释）：其后的标记是活内容，改写注释会把它藏起来。
   - 在开 `<svg>` 标签上设置 `id="<slug>-root"`，其中 `<slug>` 是源文件去掉扩展名的 basename（例如 `example-loop.html` → `example-loop`）。这个 ID 为携带进来的 CSS 划定作用域，多个内联图形不会互相泄漏规则。替换既有 SVG 根 ID 时，把携带 CSS 中指向该根的完整 CSS ID token 一并改指向，包括转义写法的标识符；`.diagram#original` 这类复合选择器仍然绑定到根上，且不会因此多出祖先。后代 ID 和带引号的选择器值保持不变；未转义的点属于类选择器，不属于 ID token。
4. **把页面 CSS 带进 SVG。**类样式驱动的图表（loop 家族、process、medallion、data-flow 等）在页面 `<style>` 块里声明填充与字体，例如 `.station`、`.hub`、`.node-name` 等。不带这些规则提取裸 `<svg>` 会得到一片黑色方块。把页面的图表规则复制进 `<defs>` 内的一个 `<style>`，然后：
   - 在解析规则前，先解开 SVG 样式表文本中的 CDATA 段，再剥离真实的 CSS 注释，这样无论是 XML 分隔符还是注释都不会成为选择器的一部分。保留引号字符串和转义中看起来像注释的文本：`[data-label="net/*retained*/revenue"]` 必须仍然匹配原始属性值。CDATA 内容保持原始文本而不做 XML 解码；携带的副本在下面再做 XML 转义。原内嵌样式表留在 SVG 中。HTML 样式表里看起来像 CDATA 的文本保持字面，包括 SVG `foreignObject`、`desc` 或 `title` 元素内部的情形。HTML 中的嵌套 `<svg>` 会切回 SVG 样式表处理。
   - 图表规则连同其原始 `@media` 条件一起保留，包括嵌套条件；仅打印的绘制不得变成屏幕绘制。Keyframe 主体保持完整；普通标识符名（含带引号的）以及匹配的样式表/内联 `animation` 或 `animation-name` 绑定都加上 SVG 根 ID 前缀，内联图形之间不能共用动画名。内联 style 的字符引用在检查 CSS 名之前解码一次，写成 XML 时再转义一次；声明中的注释保留。自定义属性的 `{ … }` 值属于 token 数据，保持字面，包括其中的任何 `animation` 文本。带字面动画名的时长变量继续支持。转义/复杂名、由未解析变量给出的动画名、有歧义的简写关键字名、SVG 本地的动画样式表，以及绑定到已改名 keyframe 的嵌套普通规则动画声明，都会被明确拒绝而不是悄悄改指向。这些不支持的动画情况返回退出码 2 且不写出 SVG。包含普通规则的块级 at 规则（包括 `@layer` 和 `@container`）保留其分组与作用域绘制。不支持的仅声明块被丢弃并给出警告；规则之间的孤立闭括号被忽略，与浏览器 CSS 的恢复行为一致。
   - 把 `:root { … }` 自定义属性重新作用域到 `#<slug>-root` 上，让图形保有自己的 token。
   - 以 `<svg>` 元素开头的选择器改为从根开始：`svg .zone` 变成 `#<slug>-root .zone`，`svg text` 变成 `#<slug>-root text`。导出的根元素就是 `<svg>` 本身，所以 `#<slug>-root svg .zone` 会匹配不到任何东西。
   - 选择器列表只在顶层逗号处拆分。作用域化时保留带引号和转义的属性值、函数参数以及有意义的空白。
   - 其余保留的选择器都加上 `#<slug>-root ` 前缀（例如 `.station` → `#example-loop-root .station`）。
   - **丢弃**页面装饰：`*`、`html`、`body`、`main`、`h1`/`h2`/`h3`、`p`、`.frame`、`.eyebrow`、`.summary`、`.card(s)`、`.footer`、`.header`，以及裸的 `svg { min-width: … }` 布局规则。只有裸 `svg` 选择器属于布局；`svg .zone` 和 `svg text` 是图表规则（见上文）。这些不得跟随片段一起被带走。
   - 把被丢弃的 `body` 规则中的 `color` 和 `font-family` 迁移到 `#<slug>-root` 上。SVG 内容对两者都有继承：`stroke="currentColor"` 读 `color`，没有自己字体规则的文本读 `font-family`。
   - **XML 转义**携带的 CSS 文本（`&` → `&amp;`、`<` → `&lt;`）后再插入 SVG。规则体可能包含 XML 敏感字符（例如 `content: "R&D"`）；裸 `&` 会让独立文件解析失败。
5. 注入 Google Fonts 的 `@import`，让 SVG 在浏览器中以正确排版渲染。**把 `&` 分隔符 XML 转义为 `&amp;`**：独立 `.svg` 按严格 XML 解析，裸 `&` 会开启实体引用并使整个文件解析失败。（不要从 HTML `<link href>` 复制原始 URL；那种 & 形式只在 HTML 中合法。）合并进携带规则的同一个 `<defs>` `<style>`（不要添加第二个 `<defs>`）。如果需要新的 `<defs>`，插在既有的首个 `<title>` 和 `<desc>` 之后，保持首子元素可访问标题的契约：

     ```svg
     <defs>
       <style>@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Geist:wght@400;500;600&amp;family=Geist+Mono:wght@400;500;600&amp;family=Noto+Serif:ital@0;1&amp;family=Noto+Sans+KR:wght@400;500;600&amp;family=Noto+Serif+KR:wght@400&amp;family=Noto+Sans+TC:wght@400;500;600&amp;family=Noto+Serif+TC:wght@400&amp;display=swap');
       /* …scoped diagram rules… */
       </style>
       <!-- existing markers / patterns stay here -->
     </defs>
     ```

6. **给 `<defs>` ID 建立命名空间。**给每个可引用的 defs ID（`marker`、`pattern`、`linearGradient`、`radialGradient`、`filter`、`clipPath`、`mask`、`symbol`，以及可复用图形（`g`、`path`、`rect`、`circle`、`ellipse`、`line`、`polyline`、`polygon`、`text`、`image` 和 `use`））加上 `<slug>-` 前缀，并改写匹配的 `url(#…)` 和 `href="#…"` / `xlink:href="#…"` 引用。比较 ID 与片段值之前先做 XML 字符引用解码，等价的命名与数字引用保持关联。对绘制/引用属性、内联样式和样式表中可识别的本地 CSS URL 形式（字面 `url(...)`，大小写不敏感），比较片段同一性之前先解码 hex 转义，并在添加前缀时保留原转义写法；`url(#\70 aint)` 必须仍与命名空间化后的 `paint` 定义保持关联。URL 形态的元数据和带引号的 CSS 字符串内容保持字面。改指向内嵌样式规则中的 ID 选择器，声明中的颜色与无关 ID 保持不变。保留 URL 引号，并按大小写敏感匹配片段 ID（CSS `url` 关键字仍然大小写不敏感）。按**最长 ID 优先**改写，避免 `arrow-accent` 被较短的 `arrow` 规则截断。带引号的本地 URL（`url("#arrow")`、`url('#arrow')`，包括属性中 XML 转义过的引号）与不带引号的 URL 走同样的改写。无关的片段 ID 和非本地 URL 保持不变。示例：`example-loop.html` 里的 `id="arrow"` 变成 `id="example-loop-arrow"`，并配 `marker-end="url(#example-loop-arrow)"`。

7. 为严格的 SVG 1.1 消费者归一化颜色。本设计系统的 token 以 `rgba(...)` 书写（见 `style-guide.md`），在任何把颜色当 CSS 读取的地方都渲染正确：浏览器、Figma、Illustrator。PowerPoint 的 SVG 导入器不行：它把 `rgba(...)` 和 `transparent` 视为无法识别并涂成**不透明黑色**，把一层若有若无的色调变成吞掉内部标签的实心色块。只在 alpha 能被保留的前提下归一化呈现绘制：可以合并本地的呈现 opacity；当存在 CSS 或继承的 opacity，或元素及其子元素上有绘制覆盖而使拆分不安全时，保留 RGBA。无关的简单 CSS 规则不妨碍归一化。在写出文件前应用下面这套完整配方：

   ```python
   import re
   import math
   import html as html_entities
   import xml.etree.ElementTree as ET
   from typing import Callable


   CSS_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)


   XML_OPAQUE_OPEN_RE = re.compile(r"<!--|<!\[CDATA\[")


   START_TAG_RE = re.compile(
       r"<([A-Za-z][\w:.-]*)"
       r"((?:\s+[^\s\"'<>/=]+(?:\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s\"'=<>`]+))?)*)"
       r"(\s*/?)>"
   )


   TAG_ATTR_RE = re.compile(
       r"(\s+)([^\s\"'<>/=]+)(?:(\s*=\s*)(\"[^\"]*\"|'[^']*'|[^\s\"'=<>`]+))?"
   )


   STYLE_BLOCK_RE = re.compile(r"<style\b[^>]*>(.*?)</style\s*>", re.IGNORECASE | re.DOTALL)


   CSS_RULE_ATOM = r'''(?:/\*(?:[^*]|\*(?!/))*\*/|\\[\s\S]|"(?:\\[\s\S]|[^"\\])*"|'(?:\\[\s\S]|[^'\\])*'|/(?!\*)|[^{}"'\\/])'''


   RULE_RE = re.compile(rf"({CSS_RULE_ATOM}+)\{{({CSS_RULE_ATOM}*)\}}", re.DOTALL)


   RGBA_ATTR_RE = re.compile(
       r'(fill|stroke)="rgba\(\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*,\s*([+-]?\d*\.?\d+)\s*\)"'
   )


   def _rewrite_start_tags(svg: str, transform: Callable[[re.Match[str]], str]) -> str:
       """Transform actual start tags, preserving comments and CDATA sections."""
       out: list[str] = []
       pos = 0
       while True:
           opener = XML_OPAQUE_OPEN_RE.search(svg, pos)
           text_end = opener.start() if opener else len(svg)
           out.append(START_TAG_RE.sub(transform, svg[pos:text_end]))
           if opener is None:
               break
           closer = "-->" if opener.group(0) == "<!--" else "]]>"
           close_at = svg.find(closer, opener.end())
           stop = len(svg) if close_at == -1 else close_at + len(closer)
           out.append(svg[opener.start() : stop])
           pos = stop
           if close_at == -1:
               break
       return "".join(out)


   def _decoded_css_property_text(style: str) -> str:
       """Read opacity spellings conservatively without changing carried CSS."""
       style = CSS_COMMENT_RE.sub("", html_entities.unescape(style))

       def escape(match: re.Match[str]) -> str:
           hexadecimal, literal = match.groups()
           if hexadecimal is not None:
               value = int(hexadecimal, 16)
               return chr(value) if 0 < value <= 0x10FFFF and not 0xD800 <= value <= 0xDFFF else "\ufffd"
           return "" if literal in "\r\n\f" else literal

       return re.sub(r"\\(?:([0-9a-fA-F]{1,6})(?:\r\n|[ \t\r\n\f])?|([\s\S]))", escape, style)


   def _css_paint_may_target_descendants(selector: str, children: list[ET.Element]) -> bool:
       """Exclude provably unrelated simple selectors; preserve unknown CSS cascades."""
       for branch in selector.split(","):
           terminal = re.split(r"[\s>+~]+", branch.strip())[-1]
           # Unsupported selectors remain conservative, including escaped names,
           # attribute selectors and pseudo-classes that can affect descendant paint.
           if not re.fullmatch(r"(?:[A-Za-z][\w-]*|\*)?(?:[.#][\w-]+)*", terminal) or not terminal:
               return True
           tag = re.match(r"^[A-Za-z][\w-]*", terminal)
           classes = re.findall(r"\.([\w-]+)", terminal)
           ids = re.findall(r"#([\w-]+)", terminal)
           for child in children:
               if tag and child.tag.rsplit("}", 1)[-1] != tag.group(0):
                   continue
               if all(name in child.get("class", "").split() for name in classes) and all(
                   name == child.get("id") for name in ids
               ):
                   return True
       return False


   def normalize_rgba_presentation_attrs(svg: str) -> str:
       """Split rgba paint and combine its alpha with existing presentation opacity."""

       # A parent's paint and opacity may be inherited independently. Converting
       # its color alpha into opacity would also change children overriding paint.
       try:
           elements = list(ET.fromstring(svg).iter())
           descendants = {
               index: list(element.iter())[1:]
               for index, element in enumerate(elements) if len(element)
           }
       except ET.ParseError:
           return svg  # The existing final XML validator supplies the public error.
       opacity_counts = {"fill-opacity": 0, "stroke-opacity": 0}
       styles = list(STYLE_BLOCK_RE.findall(svg))

       def collect_opacity_context(match: re.Match[str]) -> str:
           for attr in TAG_ATTR_RE.finditer(match.group(2)):
               key, value = attr.group(2), attr.group(4)
               if key in opacity_counts:
                   opacity_counts[key] += 1
               elif key == "style" and value is not None:
                   styles.append(value[1:-1])
           return match.group(0)

       _rewrite_start_tags(svg, collect_opacity_context)
       css_opacity = {
           key for key in opacity_counts
           if any(re.search(rf"(?:^|[;{{])\s*{key}\s*:", _decoded_css_property_text(style), re.IGNORECASE)
                  for style in styles)
       }

       position = 0

       def normalize_tag(match: re.Match[str]) -> str:
           nonlocal position
           children = descendants.get(position, [])
           element = elements[position]
           position += 1
           name, attrs, end = match.groups()
           values = {
               attr.group(2): attr.group(4)[1:-1]
               for attr in TAG_ATTR_RE.finditer(attrs)
               if attr.group(4) is not None
           }
           updates: dict[str, str] = {}
           additions: list[str] = []
           for prop in ("fill", "stroke"):
               value = values.get(prop, "")
               if value == "transparent":
                   updates[prop] = "none"
                   continue
               rgba = RGBA_ATTR_RE.fullmatch(f'{prop}="{value}"')
               if rgba is None:
                   continue
               _, r, g, b, alpha = rgba.groups()
               opacity_name = f"{prop}-opacity"
               # Presentation opacity may be overridden by CSS or inherited from
               # another element. Preserve the color alpha when that cascade is
               # unresolved instead of replacing it with opaque RGB.
               # Converting a parent is safe when descendants inherit its paint.
               # Preserve alpha if a descendant overrides that paint, including
               # a conservatively detected stylesheet or inline declaration.
               inline_paint = re.search(
                   rf"(?:^|[;{{])\s*{prop}\s*:",
                   _decoded_css_property_text(element.get("style", "")), re.I,
               )
               descendant_paint = any(
                   prop in child.attrib
                   or re.search(rf"(?:^|[;{{])\s*{prop}\s*:",
                                _decoded_css_property_text(child.get("style", "")), re.I)
                   for child in children
               )
               stylesheet_paint = any(
                   re.search(rf"(?:^|[;{{])\s*{prop}\s*:", _decoded_css_property_text(rule.group(2)), re.I)
                   and _css_paint_may_target_descendants(rule.group(1), [element] + children)
                   for style in STYLE_BLOCK_RE.findall(svg)
                   for rule in RULE_RE.finditer(CSS_COMMENT_RE.sub("", style))
               )
               if inline_paint or descendant_paint or stylesheet_paint or opacity_name in css_opacity or opacity_counts[opacity_name] > int(opacity_name in values):
                   continue
               opacity = alpha if 0 <= float(alpha) <= 1 else "0" if float(alpha) < 0 else "1"
               if opacity_name in values:
                   try:
                       original = values[opacity_name].strip()
                       amount = float(original.rstrip("%")) / (100 if original.endswith("%") else 1)
                   except ValueError:
                       continue  # Keep paint intact when the opacity cannot be resolved here.
                   if not math.isfinite(amount):
                       continue
                   opacity = format(min(1, max(0, amount)) * max(0, min(1, float(alpha))), ".12g")
                   updates[opacity_name] = opacity
               else:
                   additions.append(f' {opacity_name}="{opacity}"')
               updates[prop] = "#{:02x}{:02x}{:02x}".format(*(max(0, min(255, int(c))) for c in (r, g, b)))

           def replace_attr(attr: re.Match[str]) -> str:
               space, key, _equals, _value = attr.groups()
               return f'{space}{key}="{updates[key]}"' if key in updates else attr.group(0)

           return f"<{name}{TAG_ATTR_RE.sub(replace_attr, attrs)}{''.join(additions)}{end}>"

       return _rewrite_start_tags(svg, normalize_tag)


   svg = normalize_rgba_presentation_attrs(svg)
   ```

通道和 alpha 被钳制在 CSS 范围 0–255 与 0–1 内，转换时越界的 rgba 值仍能保持浏览器的绘制效果。每个通道周围的 `\s*` 同时兼容带空格的 `rgba(45, 49, 66, 0.03)` 和模板常用的紧凑形式 `rgba(45,49,66,0.03)`；`\d*\.?\d+` 接受带或不带前导零的 alpha 值（已发布的 token 里 `0.03` 和 `.03` 都出现过）。匹配范围限定在 `fill="..."` / `stroke="..."` 呈现属性。类样式驱动的图表可能仍在内嵌 `<style>` 块里通过自定义属性（例如 `--accent-tint`）携带 `rgba(...)`；这种形式在浏览器和 Figma/Illustrator 中都正确，不属于本次呈现属性处理的范围。（品牌的调色板收录在 `style-guide.md` 中，原则上可以引入 `hsl()` 之类的第三种记法；目前所有已发布的 token 中都没有，所以本处理不覆盖它：将来真引入了再扩展正则。）

8. **门检查：**如果导出的 SVG 仍然含有 `class=` 却没有任何图表 CSS 规则，停下并修复 CSS 迁移步骤，否则该片段会渲染成黑色方块。仅含字体的 `<style>`（只有 Google Fonts `@import` 而无规则）**不**满足该门。
9. 前置 `<?xml version="1.0" encoding="UTF-8"?>\n`，使文件成为良构 XML。
10. 写到源文件旁边的 `<basename>.svg`（例如 `example-architecture.html` → `example-architecture.svg`）。如果用户提供了明确输出路径，以它为准。

### 需要向用户说明的注意事项

导入时不抓取远程字体的工具（离线的 Illustrator、部分 Figma 导入路径、较老的 SVG 查看器）会替换字体排版。SVG 在任何现代浏览器中都能正确渲染。要获得像素级的可移植性，推荐改用 PNG 导出。

## PNG 导出流程

渲染**原始 HTML**（不是提取出的 SVG），只对 `<svg>` 元素的包围盒截图。这样字体加载保持可靠（源 HTML 里已经接好），同时满足"只要图表"的规则。PNG 始终带**透明背景**（`omit_background=True`），因此可以放在任何幻灯片或文档颜色上而不带白色光晕。对启用了动效的 HTML，追加 `?motion=static`，等待 `document.fonts.ready`，并在截取前断言动效根已处于 `data-frame="static"`；绝不在任意的墙钟延迟处导出。

### 检测

开始之前，确认你将用于导出的 Python 解释器中安装了 Playwright。试运行：

```
python3 -c "import playwright"
```

如果失败，再试 `python -c "import playwright"`（Windows 上的常用命令）。下面的栅格化命令使用通过导入测试的那个解释器。如果两个导入都失败，把下面这段原话转达给用户并停止：

> Playwright 不可用。PNG 导出需要宿主环境预先配置经批准的 Playwright 安装以及兼容的浏览器；本 skill 绝不自动安装运行时依赖。
> 之后请再次让我导出。

不要自动安装。用户要的是一个功能，不是改动系统。

### 栅格化

保持用户的工程目录作为工作目录，使相对输入输出路径仍在那里解析。用通过检测的解释器、按已解析的 skill 目录下的绝对路径调用打包的渲染器：`python3 <skill-dir>/scripts/export_png.py <src.html> <out.png> [scale]` 或 `python <skill-dir>/scripts/export_png.py <src.html> <out.png> [scale]`。

如果 `networkidle` 等待超时（某个字体或样式表在代理后面卡住），辅助脚本会用 `window.stop()` 取消未完成的加载并以回退字体截取，同时向 stderr 打印警告：请把该警告转达给用户。其他错误照常传播并使导出失败。辅助脚本会请求完整的静态动效帧，等待字体就绪，并在动效根尚未达到 `data-frame="static"` 时拒绝；普通无脚本的图表不需要动效根。

默认 `device_scale_factor=2`，输出清晰。接受 `1`（紧凑素材）或 `3`（打印/retina 主视觉），作为第三个 CLI 参数传入。也接受 `1.25` 这类小数缩放，在文档记载的 1–4 范围内，用于精确像素尺寸。

辅助脚本的溢出释放对宽幅预设很重要。`min-width` 等于 viewBox 宽度（见 [`output-spec.md`](output-spec.md)），所以 `doc-wide` 或 `slide-16x9` 的 SVG 是 1200px 框架里的 1280px，它的 `.diagram-container` 滚动容器在屏幕上裁掉最后 80px。截图只覆盖 SVG 的盒子，不覆盖被祖先裁掉的部分，所以没有这个释放，PNG 会是完整尺寸但右边缘一片空白。这是模板中 `@media print` 规则在屏幕侧的对应物。

### 输出命名

`example-architecture.html` → `example-architecture.png`，写在源文件旁边。以用户明确提供的路径为准。栅格化器把源文件的绝对路径编码为 file URI，因此文件名中的字面 `#` 和 `%` 字符仍保持为文件名内容。

## 确定导出尺寸

PNG 的像素尺寸是 SVG 的 `viewBox` × `device_scale_factor`。栅格化器用有限的、非零的 viewBox 尺寸来确定截取视口，页面 CSS 无法放大或缩小承诺的输出。所以尺寸决策在画图时就已经做出（预设见 [`output-spec.md` §2](output-spec.md)），导出只选择倍数。

| 目标用途 | 缩放 | 1280×720 `viewBox` 的结果 |
|---|---|---|
| 文档、README、wiki | 2 | 2560×1440 |
| 幻灯片（投影） | 2 | 2560×1440 |
| 打印 / PDF 讲义 | 3 | 3840×2160 |
| 内嵌缩略图、邮件 | 1 | 1280×720 |

### 命中精确像素尺寸

当用户需要特定尺寸（恰好 1200×630 的 OG 卡片、1920×1080 的幻灯片图）时，计算缩放系数而不是猜：Playwright 接受小数值：

```
scale = target_width / viewBox_width
```

960 宽的 `viewBox` 目标 1200px 就是 `scale=1.25`。两条规则：

- **绝不缩到 1 以下**去凑小目标：那会让字体发虚。改为用更小的预设重画。
- **绝不缩过 4**：超过之后你是在放大一个为更小画布设计的布局；请改用 `slide-16x9` 或打印预设重画。

如果目标宽高比与 `viewBox` 的宽高比不一致，说明这一点并提出按匹配的预设重画。把成品图表填充或裁剪去适配某个画框不是导出操作，那会破坏 40px 安全边距。

## 边界情况

- **源文件是 `assets/index.html`**（gallery，一个文件里有多个 SVG）：拒绝导出，询问用户具体指哪个图表文件。不要猜。
- **找不到 `<svg>` 块**：源文件不是图表文件。告诉用户；什么都不要写。
- **周围的 HTML 对用户很重要**：他们想要图里有卡片/页眉。告诉他们本 skill 只导出图表，并推荐基于浏览器的整页截图（或单独的 PDF 打印）。
- **源文件在运行时缺字体**：Playwright 会替换字体，截图会走样。检查源 HTML 的 `<head>` 里是否有 `<link href="...fonts.googleapis.com...">` 标签。若缺失，说明该文件不是当前模板生成的：修源文件，而不是在导出环节绕过。

## 本命令绝不做的事

- 修改源 HTML。
- 添加导出按钮或 `<script>` 标签。静态图表保持无脚本；已启用动效的源可以保留 [`animation.md`](animation.md) 中限定作用域的控制器，但导出绝不注入另一个控制器。
- 在生成 HTML 时自动顺带产出 `.svg` 或 `.png`。每次调用都必须手动触发。
- 通过 `foreignObject` 把 HTML 包装（卡片、页眉）嵌进 SVG。跨渲染器太脆弱。

导出器保留 `@font-face`，并在 `@supports`、`@media`、`@layer`、`@container` 这类块级 at 规则内部为普通规则保留作用域，不展平其条件。只含 keyframe 或 font face 的分组也会保留，包括嵌套分组，让分组之外的引用保有其定义。仅声明的不支持块被丢弃并给出警告，而不是中止导出。系统字体模式继续省略自定义 font-face 声明。括号包裹的 CSS 函数（包括未加引号的 data URL）内部的分号仍是值文本，不会终结语句。

CSS 分组规则只扫描一次并原样保留，不递归重扫嵌套主体。嵌套超过 1,024 层 CSS 块的导出会在写出前以明确的诊断失败（CLI 退出码 2）。

包含普通绘制规则的 `@scope` 组会在写出前以明确的退出码 2 诊断被拒绝；仅定义的 scope 保留其 keyframe 和 font face。`@layer` 顺序语句与其 layer 块一起保持源顺序，包括在分组规则内部，级联优先级因此得以保留。
导出器把注释里的可选 defs 保持命名空间化，以便日后取消注释启用。只有可引用的 defs 元素类型的 ID 会被改名；活的标题等元素保留其 ID 和无障碍引用。

动画属性名在 CSS 转义解码之后比较，书写原样保留。页面样式和内联属性保持与命名空间化 keyframe 的绑定，包括 `anim\61 tion` 和带厂商前缀的属性。嵌套动画声明和 SVG 本地的动画样式表仍然不支持并会明确失败，包括转义的属性名。
