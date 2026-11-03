> **中文汉化版** · 上游：[K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 原文件：`skills/exploratory-data-analysis/references/microscopy_imaging_formats.md` · License: MIT
> 翻译日期：2026-11-03 · 同步状态：上游 HEAD（2026-11-03 快照）· AI 辅助翻译 + 人工校对
> 术语以 [GLOSSARY.md](../../../../../GLOSSARY.md) 为准；代码块、命令与 frontmatter 字段名保持原文。本文件为翻译作品，非上游官方中文版。

# 显微镜与科学成像格式

**审阅时间：** 2026-09-30
**可执行范围：** 仅限元数据的 PNG/JPEG 与 TIFF/OME-TIFF 检查。
仓库内工具绝不解码像素。

## 精确的能力矩阵

| 格式 | 仓库内自带检查 | 深度 |
|---|---|---|
| `.png`、`.jpg`、`.jpeg` | 可选，`pillow==12.3.0` | 宽、高、模式、帧数、格式与元数据条目数 |
| `.tif`、`.tiff` | 可选，`tifffile==2026.9.20` | 有界的页面与通用 series，形状/dtype，BigTIFF/OME 标记 |
| `.ome.tif`、`.ome.tiff` | 可选，`tifffile==2026.9.20` | 同等的结构元数据；OME-XML 的值不会被输出，也不做语义校验 |
| ND2/CZI/LIF 与其他厂商显微镜格式 | 不支持 | 仅作参考的厂商/Bio-Formats 流程 |
| DICOM/NIfTI/MRC | 不支持 | 仅作参考的医学/神经/电镜流程 |
| SVS/NDPI 与其他全切片格式 | 不支持 | 仅作参考的 WSI 流程 |
| OME-Zarr/Zarr | 不支持 | 目录/store 格式在常规文件边界之外 |

没有仓库内脚本支持“全部 Pillow 格式”或“全部 tifffile 格式”。
只接受上面登记的后缀。未知格式一律失败关闭。

## 仅元数据的安全模型

图像与元数据可能包含受保护的健康信息、登记号、
标本标签、GPS/EXIF 字段、用户批注、XML、外部
引用或对抗性文本。这些检查器：

- 只接受 `--root` 之内有界的本地常规文件；
- 拒绝 URL、路径穿越、符号链接、特殊文件，以及后缀/签名
  不匹配；
- 拒绝声明的元素数超过 100,000,000，以及过多的 TIFF
  页面/series；
- 把 Pillow 的解压炸弹警告当作致命错误；
- 绝不调用 `load()`、`asarray()`、`imread()`、图像编解码器或缩略图
  生成；
- 报告元数据计数与结构事实，而不是 EXIF/tag/OME-XML 的值；
- 绝不跟随元数据链接或嵌入的指令；以及
- 不声称做了完整的损坏、编解码器或语义校验。

仅元数据访问降低了解压风险，但它本身不是沙箱。请
把库版本钉住，并在风险需要时于隔离且资源受限的
进程中检查不可信图像。

## PNG 与 JPEG

Pillow 的 `Image.open()` 是惰性的：它识别容器，并读取足够的
头部信息来构造一个图像对象。仓库内的检查器会在不解码像素的
情况下关闭该对象。

### 谨慎解读

- PNG 可能是调色板、灰度、RGB/RGBA、8/16 位、多帧/APNG，或携带
  文本/profile chunk。
- JPEG 是有损的，通常不适合作为定量原始测量
  来源。反复保存会改变像素。
- 宽/高/模式不能确立位深保真度、校准、通道
  身份、线性度、饱和度或采集设置。
- 图像处理之后元数据可能已经过期。

对于定量 EDA，请保留采集原生的图像，并把
容器元数据与仪器记录做比对。不要从展示/导出的 JPEG 计算强度统计。

## TIFF

TIFF 是一个灵活的容器，而不是单一的像素组织方式。它可以包含
多页、tile/strip、金字塔、SubIFD、私有/厂商 tag、外部
存储以及多种压缩方案。仅凭 `.tif` 后缀并不意味
着符合显微镜或 OME 约定。

仓库内的 tifffile 检查器报告：

- 主页面与通用 series 的数量，上限为 1,000 与 128；
- 每个 series 的形状、轴、元素数，以及 dtype 类别/项大小；
- 经典 TIFF 还是 BigTIFF；以及
- tifffile 是否识别出 OME 元数据。

当前的公开 `tiff.series(kind="generic")` API 对本地页面分组，而不会
重建 OME/厂商维度，也不发现伴随文件。钉住的
`_multifile=False` 参数增加了一道上游内部防护；升级 tifffile 时
请重新核查它。形状与轴描述的是通用页面分组，不是经过验证的
OME XYZCT 维度。主页面加上声明的直接子 SubIFD 共用
1,000 条目的上限。嵌套金字塔不会被彻底校验。

读取器必然要在内部解析结构 tag 的值，但绝不输出
原始 tag 或 OME-XML。它不解码压缩片段、不校验每个 IFD、
不打开伴随存储，也不建立科学上正确的轴语义。

## OME-TIFF

OME-TIFF 在 TIFF 中存储一个或多个图像平面，并内嵌一段 OME-XML 元数据
块。多文件数据集可以使用基于 UUID 的引用。OME 规范
比文件名约定丰富得多。

在定量分析之前，请用 OME 感知的校验确认：

- OME-XML 的 schema/版本与 UUID/文件引用；
- X/Y/Z/C/T 的维度顺序与尺寸；
- `TiffData` 的平面到 IFD 映射；
- 物理像素尺寸与单位；
- 通道名称、波长、探测器/物镜设置，以及采集
  时间；以及
- 是否应当存在金字塔、标签、ROI 或伴随文件。

仓库内的检查器有意不输出 OME-XML，因为其中可能包含
标识符或类似提示词的文本。`is_ome_tiff=true` 不是校验结果。

## 仅作参考的厂商显微镜格式

ND2、CZI、LIF、VSI、专有全切片文件等格式需要
感知版本的厂商读取器或 Bio-Formats。能力因库、原生
依赖、文件生成版本与 series 类型而异。不要仅凭后缀就选择
读取器。

流程：

1. 保留原件，并记录仪器/软件版本。
2. 在隔离环境中用版本钉住的读取器打开一个小型的已批准文件。
3. 在加载像素之前，先清点 scene/series 与 XYZCT 轴。
4. 把维度、校准、通道、载物台位置与时间戳
   与采集记录做比对。
5. 给 tile/平面的读取设上界，绝不急切地实体化整张切片或五维
   图像。
6. 只有在有溯源信息并通过往返检查之后，才把派生副本转换为 OME-TIFF/OME-Zarr。

## 仅作参考的医学与全切片成像

### DICOM

DICOM 是带大量元数据、可能含 PHI 的临床标准。单个
`.dcm` 可能只是某个 study/series 中的一个实例。请遵循机构政策、
经批准的去标识化流程与 DICOM 感知的工具。不要打印患者、study、
series、登记号、日期、烧录批注或私有 tag 的值。

### NIfTI

请用神经影像工具校验维度、体素尺寸、affine/qform/sform、单位、方向、
缩放与时间轴。`.nii.gz` 是压缩格式，仓库内脚本不会
解压它。

### 全切片成像

SVS、NDPI 及相关格式是大型分块金字塔，可能包含带标识符的标签或
宏观图像。请使用 OpenSlide/tiffslide 或经过验证的厂商
读取器，检查关联图像，并对分块做有界采样。先按患者
划分，再生成分块，以防止泄漏。

## 成像 EDA 严谨性

1. 定义独立单元：像素、目标、视野、孔位、切片、标本、
   受试者或采集时段。
2. 区分生物学重复与技术重复，不要把同一标本的 tile 或
   细胞当作独立受试者。
3. 记录校准、单位、位深、探测器响应、曝光、增益、
   照明、物镜、通道、Z/T 间距与处理历史。
4. 审计缺失/损坏的平面、饱和、截断、背景、焦点、
   照明、配准、分割以及批次/场地效应。
5. 保留原始像素。不要自动重新缩放、去噪、扣背景、
   丢弃视野或移除目标。
6. 只在训练标本上拟合归一化、分割阈值、特征选择与模型；
   先按受试者/标本划分，再做分块。
7. 报告目标/视野/标本层级的敏感性，而不只是合并后的像素。
8. 不要从描述性的图像模式推断生物学机理、诊断或治疗效应。

## 钉住的可选快照

```bash
uv pip install \
  "pillow==12.3.0" \
  "tifffile==2026.9.20" \
  "numpy==2.5.3"
```

Pillow 12.3.0 发布于 2026-07-01，要求 Python 3.10+。
tifffile 2026.9.20 发布于 2026-09-21，要求 Python 3.12+。
仅元数据的检查器不会安装或调用 Imagecodecs。

## 权威来源

当前解析器 API 与格式指南审阅于 2026-09-30。历史方法学
引用保留下来作为来源背景。

- Pillow，[`Image` 模块与解压炸弹防护](https://pillow.readthedocs.io/en/stable/reference/Image.html)。
- [Pillow PyPI](https://pypi.org/project/pillow/)，版本 12.3.0，
  发布于 2026-07-01。
- tifffile，[当前 API 与通用 series 示例](https://www.cgohlke.com/docs/tifffile/)。
- [tifffile PyPI](https://pypi.org/project/tifffile/)，版本 2026.9.20，
  发布于 2026-09-21；上游指出解码压缩片段需要编解码器。
- 美国国会图书馆，[TIFF, Revision 6.0 格式描述](https://www.loc.gov/preservation/digital/formats/fdd/fdd000022.shtml)
  与 ITU 托管的 [TIFF 6.0 规范](https://www.itu.int/itudoc/itu-t/com16/tiff-fx/docs/tiff6.pdf)。
- OME，[OME-TIFF 规范](https://ome-model.readthedocs.io/en/stable/ome-tiff/specification.html)。
- OME，[OME 数据模型与文件格式](https://ome-model.readthedocs.io/en/stable/)。
- DICOM 标准委员会，[当前 DICOM 标准](https://www.dicomstandard.org/current)。
- OpenSlide，[受支持的格式与 Python API](https://openslide.org/api/python/)。
- National Academies（2019），[可复现性与溯源](https://doi.org/10.17226/25303)。
