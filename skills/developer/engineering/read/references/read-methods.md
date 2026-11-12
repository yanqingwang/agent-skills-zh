> **中文汉化版** · 上游：[tw93/Waza](https://github.com/tw93/Waza) · 原文件：`skills/read/references/read-methods.md` · License: MIT
> 翻译日期：2026-10-25 · 同步状态：上游 HEAD（2026-10-25 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# Read 方法参考

## 辅助脚本目录

内置抓取器、飞书和微信辅助脚本共用同一目录,解析一次即可。把 `<skill-base-dir>` 替换为已安装的 Read Skill 或 Waza 调度器目录:

```bash
READ_SCRIPT_DIR=""
for candidate in \
  "<skill-base-dir>/scripts" \
  "<skill-base-dir>/skills/read/scripts"; do
  if [ -f "$candidate/fetch.sh" ]; then
    READ_SCRIPT_DIR="$candidate"
    break
  fi
done
if [ -z "$READ_SCRIPT_DIR" ]; then
  echo "read helper scripts not found under the installed skill base; reinstall Waza" >&2
  exit 1
fi
```

## 内置抓取器

```bash
bash "$READ_SCRIPT_DIR/fetch.sh" "{url}"
```

提取顺序与内容检查都由该脚本负责:先请求源站点并在本地提取。失败时,查看它输出的结构化 stderr。仅当用户已选择加入第三方提取且 URL 为公开 URL 时,才运行:

```bash
bash "$READ_SCRIPT_DIR/fetch.sh" --use-proxy "{url}"
```

不要把需要认证、内部或其他敏感 URL 发给第三方提取服务或阅读器插件。已安装的插件只是同一隐私边界下的可选阅读器,不代表获得自动披露 URL 的许可。如果阅读器返回 JSON,先提取其中包含 Markdown 的字段,再回答或保存。

## DeepSeek 搜索与抓取

需要在 shell 配置文件中导出来自 DeepSeek 平台的 `DEEPSEEK_API_KEY`。没有它,脚本以退出码 2 退出,不发送任何内容。

```bash
python3 "$READ_SCRIPT_DIR/deepseek.py" search "{query}" --count 10
python3 "$READ_SCRIPT_DIR/deepseek.py" fetch "{url}"
```

- `search` 输出带编号的结果,包含 URL、站点、日期、`authority`(0-4,3 及以上为高度权威)和 `score`(0-3,1.5 及以上为强匹配),并附 600-800 字的摘要。摘要是 DeepSeek 建立索引时的快照,引用其中的事实前先读原页面。
- 查询为 1-128 个字符,支持 `site:`、`lang:`、`after:` 等操作符。`--content` 附加页面正文;`--json` 返回原始响应。
- 每个成功请求都会计费;失败、空结果和超时请求不计费。批量运行前先规划好查询集合。

## GitHub URL

GitHub 文件 URL(`github.com/user/repo/blob/...`)会渲染出很重的 HTML。代理级联经常返回不完整或充满导航元素的内容。优先使用:

```bash
# Raw file content (fastest)
curl -sL "https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}"

# Via gh CLI (works with private repos)
gh api repos/{user}/{repo}/contents/{path} --jq '.content' | base64 -d
```

内置抓取器只作为公开 GitHub 页面的兜底,且仅限非 raw 文件视图的情况(例如 issue 讨论、README 渲染页)。私有内容一律走带认证的 `gh` 路径。

## PDF 转 Markdown

### 远程 PDF URL

从源站点下载到会话临时目录,然后在本地提取:

```bash
READ_PDF_DIR=$(mktemp -d)
curl -fL "{pdf_url}" -o "$READ_PDF_DIR/input.pdf"
pdftotext -layout "$READ_PDF_DIR/input.pdf" -
```

本地提取失败时,第三方 PDF 阅读器只能用于用户已选择加入的公开 URL,且遵循与内置抓取器相同的边界。绝不把失败当作同意。

### 本地 PDF 文件

```bash
# Best quality (requires: pip install marker-pdf)
marker_single /path/to/file.pdf --output_dir "${READ_OUTPUT_DIR:-/tmp/waza-read}"

# Fast, text-heavy PDFs (requires: brew install poppler)
pdftotext -layout /path/to/file.pdf - | sed 's/\f/\n---\n/g'

# Python fallback (requires pypdf)
python3 -c "
import pypdf, sys
r = pypdf.PdfReader(sys.argv[1])
print('\n\n'.join(p.extract_text() for p in r.pages))
" /path/to/file.pdf
```

在意版式(论文、表格)时用 `marker`;追求速度时用 `pdftotext`。

## 飞书 / Lark 文档

使用[辅助脚本目录](#helper-directory)中的 `READ_SCRIPT_DIR`。

需要 `requests` 和飞书应用凭证:

```bash
pip install requests  # one-time setup
export FEISHU_APP_ID=your_app_id
export FEISHU_APP_SECRET=your_app_secret
python3 "$READ_SCRIPT_DIR/fetch_feishu.py" "{url}"
```

支持:docx 和 wiki 页面。本脚本不支持旧版 `/docs/` 页面;先把它们转换为 docx,或者在不经 API 即可访问文档时使用公开页面兜底。应用需要 `docx:document:readonly` 和 `wiki:wiki:readonly` 权限。
输出:YAML frontmatter(title, document_id, url)+ Markdown 正文。

不要一上来就让每个用户安装 `lark-cli`。当 API 辅助脚本因缺少应用凭证而失败,或用户明确偏好 OAuth 登录而非 `FEISHU_APP_ID` / `FEISHU_APP_SECRET` 时,把它作为用户登录的兜底:

```bash
npm install -g @larksuite/cli  # one-time setup if lark-cli is absent
lark-cli auth login            # one-time login
lark-cli docs +fetch --doc "{url}" --format json
```

`lark-cli docs +fetch` 返回的是结构化文档 JSON,不是最终 Markdown。回答前先提取并转换有用内容;不要直接返回原始 JSON。

## 微信公众号

先用[内置抓取器](#built-in-fetcher),包括其针对第三方提取的选择加入边界。

如果提取失败,用内置的 Playwright 脚本在本地浏览器中读取源页面(需一次性安装约 300 MB):

```bash
pip install playwright beautifulsoup4 lxml && playwright install chromium
python3 "$READ_SCRIPT_DIR/fetch_weixin.py" "{url}"
```
