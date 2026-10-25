#!/usr/bin/env python3
"""按 humanizer §8 深化 gstack 译稿：把 em dash 直译改为中文原生标点。

规则（安全度递减）：
  R1 加粗标签内 `**X——Y**`      → `**X：Y**`
  R2 标题 `## X——Y`             → `## X：Y`
  R3 成对短插入 `——X——`（≤22字）→ `（X）`
  R4 行内单个 `——`（解释/附加）→ `，`
只处理正文；代码块、frontmatter、声明块不动。用法：
  python3 scripts/deepen_zh.py <file...>   # 就地修改
"""
from __future__ import annotations

import re
import sys

R1 = re.compile(r"(\*\*[^*\n]{2,24})——([^*\n]{2,60}\*\*)")
R2 = re.compile(r"(^#{2,4} [^#\n]{2,34})——", re.M)
R3 = re.compile(r"——([^——\n]{1,22})——")


def split_prose(text: str):
    """返回 [(片段, 是否正文)] 列表，代码块与 frontmatter 标为非正文。"""
    parts = []
    # frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            parts.append((text[: end + 5], False))
            text = text[end + 5 :]
    # 声明块（翻译 banner，含 > 引用行）
    m = re.match(r"(^> \*\*中文汉化版\*\*.*?\n(?:>.*\n)+)", text, re.M)
    if m:
        parts.append((m.group(1), False))
        text = text[m.end() :]
    # 代码块
    chunks = re.split(r"(```.*?```)", text, flags=re.S)
    for c in chunks:
        parts.append((c, not c.startswith("```")))
    return parts


def deepen(text: str) -> tuple[str, int]:
    total = 0
    out = []
    for frag, is_prose in split_prose(text):
        if not is_prose:
            out.append(frag)
            continue
        n = len(R1.findall(frag)) + len(R2.findall(frag)) + len(R3.findall(frag))
        frag = R1.sub(r"\1：\2", frag)
        frag = R2.sub(r"\1：", frag)
        frag = R3.sub(r"（\1）", frag)
        rest = frag.count("——")
        n += rest
        frag = frag.replace("——", "，")
        total += n
        out.append(frag)
    return "".join(out), total


if __name__ == "__main__":
    for path in sys.argv[1:]:
        t = open(path).read()
        new, n = deepen(t)
        if n:
            open(path, "w").write(new)
        print(f"{path}: {n} 处改写")
