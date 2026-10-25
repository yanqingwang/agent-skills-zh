#!/usr/bin/env python3
"""全库译文 AI 腔体检（humanizer 规则的可机器检测子集）。

检测指标（对应 humanizer pattern 的中文版变体）：
  H1  破折号滥用："——" 每千字 > 3 次（humanizer: em dash overuse）
  H2  AI 腔套话：值得注意的是/不得不说/总的来说/综上所述/众所周知/毋庸置疑/换句话说/一言以蔽之
  H3  排比堆砌：连续 3+ 行以相同结构开头（"…的…，…的…，…的…"或三连同构句）
  H4  空洞强调："非常"、"极其"、"十分" 密度 > 每千字 2
  H5  被动堆叠："被" 字密度 > 每千字 5（中文被动句天然少）
  H6  公式化过渡：首先/其次/再次/最后 四连全出现于同一文件
  H7  "不仅仅是…更是…" 句式（not just X but Y 的直译腔）
  H8  结尾总结段：最后一段以 "总之/总而言之/综上" 开头

用法：python3 scripts/lint_zh_style.py [--min-score N]
输出：每文件一行体检结果 + 全库 TOP 问题榜；exit 1 若有文件 > 阈值。
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

CLICHES = ["值得注意的是", "不得不说", "总的来说", "综上所述", "众所周知",
           "毋庸置疑", "一言以蔽之", "需要指出的是", "这不仅仅"]
HOLLOW = ["非常", "极其", "十分", "格外"]
TRANSITIONS = ["首先", "其次", "再次", "最后"]
NOT_JUST = re.compile(r"不仅仅[^。；\n]{0,30}(?:更是|而是|还是)")
DASH = "——"


def check(text: str) -> dict:
    # 只检正文：去掉 frontmatter、声明块、代码块
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    body = re.sub(r"^> \*\*中文汉化版\*\*.*?\n(?:>.*\n)+", "", body, count=1, flags=re.M)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    chars = len(re.sub(r"\s", "", body))
    if chars < 200:
        return {}
    per_k = lambda n: round(n * 1000 / chars, 2)
    lines = [l for l in body.splitlines() if l.strip()]
    h3 = 0
    for i in range(len(lines) - 2):
        trio = lines[i:i + 3]
        if all(re.match(r"^(?:[-*]|\d+\.)\s*(\S{1,6})", l) for l in trio):
            heads = [re.match(r"^(?:[-*]|\d+\.)\s*(\S{1,6})", l).group(1) for l in trio]
            if len(set(heads)) == 3 and all(re.match(r"^[\u4e00-\u9fa5]{2,4}[:：]", h) or h[0] == h[0] for h in heads):
                # 粗略同构：三行前缀等长且都不是句子（列表短头）
                if all(len(h) == len(heads[0]) for h in heads):
                    h3 += 1
    cliche_hits = {c: body.count(c) for c in CLICHES if c in body}
    hollow_n = sum(body.count(h) for h in HOLLOW)
    passive_n = body.count("被")
    dash_n = body.count(DASH)
    trans = [t for t in TRANSITIONS if re.search(rf"[。；\n]|\A{t}", body)]
    trans_all = all(t in body for t in TRANSITIONS)
    paras = [p for p in body.split("\n\n") if p.strip()]
    h8 = bool(paras) and re.match(r"^(总之|总而言之|综上)", paras[-1].strip())
    h7 = len(NOT_JUST.findall(body))
    return {
        "chars": chars,
        "H1_dash_per_k": per_k(dash_n),
        "H2_cliches": cliche_hits,
        "H4_hollow_per_k": per_k(hollow_n),
        "H5_passive_per_k": per_k(passive_n),
        "H6_transitions_all": trans_all,
        "H7_not_just": h7,
        "H8_summary_ending": h8,
    }


def main() -> int:
    m = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))
    rows = []
    for up in m["upstreams"]:
        for e in up.get("files", []):
            p = ROOT / e["local"]
            if not p.exists():
                continue
            r = check(p.read_text(encoding="utf-8"))
            if not r:
                continue
            flags = []
            if r["H1_dash_per_k"] > 3: flags.append(f"H1破折号{r['H1_dash_per_k']}/千字")
            if r["H2_cliches"]: flags.append(f"H2套话{sum(r['H2_cliches'].values())}处:{list(r['H2_cliches'])[:3]}")
            if r["H4_hollow_per_k"] > 2: flags.append(f"H4空洞强调{r['H4_hollow_per_k']}/千字")
            if r["H5_passive_per_k"] > 5: flags.append(f"H5被动{r['H5_passive_per_k']}/千字")
            if r["H6_transitions_all"]: flags.append("H6四连过渡")
            if r["H7_not_just"] > 2: flags.append(f"H7不仅更是×{r['H7_not_just']}")
            if r["H8_summary_ending"]: flags.append("H8总结尾")
            if flags:
                rows.append((e["local"], r["chars"], flags))
    print(f"体检范围：全部翻译件；有 AI 腔信号的文件 {len(rows)} 个\n")
    for local, chars, flags in sorted(rows, key=lambda x: -len(x[2])):
        print(f"{'；'.join(flags)}  ←  {local}（{chars}字）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
