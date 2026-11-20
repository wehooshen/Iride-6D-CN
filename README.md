# Iride 6D（简体中文版）

[![在线浏览器体验](https://img.shields.io/badge/%E2%96%B6%20%E5%9C%A8%E7%BA%BF%E4%BD%93%E9%AA%8C-Iride%206D-ff8c00?style=for-the-badge)](https://wehooshen.github.io/Iride-6D/)
[![Release](https://img.shields.io/github/v/release/wehooshen/Iride-6D?style=for-the-badge&label=release&color=2a2a2f)](https://github.com/wehooshen/Iride-6D/releases/latest)
[![Build](https://img.shields.io/github/actions/workflow/status/wehooshen/Iride-6D/build.yml?style=for-the-badge&label=%E6%B5%8B%E8%AF%95%E4%B8%8E%E5%9B%BA%E4%BB%B6%E6%9E%84%E5%BB%BA)](https://github.com/wehooshen/Iride-6D/actions/workflows/build.yml)

**面向 Canon EOS 6D（佳能原厂固件 1.1.6）的定制固件**：基于为 Iride 定制修改的 [Magic Lantern](https://www.magiclantern.fm/) 核心与 Iride 独立模块。
提供流畅的全屏动画界面，内置**天文摄影**、**进阶摄影**、拟真**胶卷模拟**与**配置方案**四大核心专区，并支持一键恢复 6D 原始状态。界面内置**简体中文**（默认）、**英文**与**意大利语**（可在 **选项 › 语言 / Language** 中随时切换），内置按需裁剪的思源黑体（Noto Sans SC）4 级抗锯齿位图字库，在 6D 真机、PC 模拟器与浏览器中均可清晰显示中文。

*本项目基于上游 [GodEater58/Iride-6D](https://github.com/GodEater58/Iride-6D) 完整汉化。*

> ⚠️ **实验性软件提示：** 已在实机 EOS 6D 上验证胶卷模拟与自定义文件命名，其余功能通过同源 C 模拟器（211+ 项自动化测试）并针对 6D 1.1.6 固件编译验证。使用风险自负。本项目与佳能（Canon）无任何关联。

<p align="center"><a href="https://wehooshen.github.io/Iride-6D/"><img src="docs/screenshots/animazioni-v16.gif" width="540" alt="启动、主页、胶卷架与弹窗动画"></a><br>
<b><a href="https://wehooshen.github.io/Iride-6D/">▶ 在浏览器中体验</a></b>：运行与 EOS 6D 真机完全一致的 C 代码（WebAssembly），支持键盘或机身按键操作。</p>

<details>
<summary><b>全部界面截图</b>（点击展开）</summary>


| ![主页](docs/screenshots/01_home-v16.png) | ![天文](docs/screenshots/02_astro-v16.png) | ![胶卷](docs/screenshots/14_rullini-v16.png) |
| ![极轴校准](docs/screenshots/06_polare-v16.png) | ![观星日历](docs/screenshots/07_cielo-v16.png) | ![夜间红光主题](docs/screenshots/21_cielo_notte-v16.png) |
| ![星点对焦](docs/screenshots/05_stelle-v16.png) | ![摄影](docs/screenshots/08_foto-v16.png) | ![恢复 6D 默认](docs/screenshots/19_torna_6d-v16.png) |
| ![自动星点对焦](docs/screenshots/05b_fuoco_auto-v16.png) | ![拍月曝光](docs/screenshots/25_luna_foto-v16.png) | ![银河指向](docs/screenshots/26_dove_puntare-v16.png) |
| ![间隔定时拍摄](docs/screenshots/04_intervallometro-v16.png) | ![地点与时区](docs/screenshots/18d_opzioni_luogo-v16.png) | ![INFO 帮助说明](docs/screenshots/05c_aiuto-v16.png) |
| ![暗光实时取景](docs/screenshots/11b_lv_al_buio-v16.png) | ![地球照曝光](docs/screenshots/25b_luna_cinerea-v16.png) | ![6D 机身自检](docs/screenshots/24_prova-v16.png) |
| ![配置方案](docs/screenshots/17_profili-v16.png) | ![选项](docs/screenshots/18_opzioni-v16.png) | ![ND 减光镜](docs/screenshots/12_filtri_nd-v16.png) |
| ![白平衡](docs/screenshots/27_bianco-v16.png) | ![摄影菜单](docs/screenshots/08b_foto_bianco-v16.png) | ![拍后暗场建议](docs/screenshots/04e_dark_fine_sessione-v16.png) |
| ![我的胶片](docs/screenshots/14e_rullini_mie-v16.png) | ![自定义配方](docs/screenshots/14f_tua_pellicola-v16.png) | ![长曝降噪提醒](docs/screenshots/04d_intervallometro_lenr-v16.png) |
| ![英文主页](docs/screenshots/en_home-v16.png) | ![英文间隔拍摄](docs/screenshots/en_intervallometro-v16.png) | |

</details>

<p align="center"><img src="docs/screenshots/menu-v16.gif" width="540" alt="天文菜单与右侧实时预览"></p>

## 版本历程

<p align="center"><a href="https://godeater58.github.io/Iride-6D/cronistoria.html"><img src="docs/screenshots/cronistoria-v16.png" width="620" alt="Iride 6D 从 0.1 到 1.6 的演进历程"></a><br>
<b><a href="https://godeater58.github.io/Iride-6D/cronistoria.html">从 0.1 到 1.6 的演进历程</a></b>：记录每个版本的新增特性、问题修复与自动化测试增长。</p>

## 核心功能

| 专区 | 功能介绍 |
|---|---|
| 🌌 **天文** | 基于 NPF 法则与天区赤纬计算银河最长不拖线快门（一键设置快门、光圈、ISO、白平衡）· 间隔定时拍摄（内置银河、深空、星轨、延时、日转夜、暗场、平场、偏置场预设），支持静音快门、抖动偏移暂停、电量/存储卡/温度监测与 CSV 拍摄日志（附 [tools/astrostack](tools/astrostack/) 会话读取器与堆栈方案生成器）· **亮场拍完后自动建议同温暗场** · 检测到机身长曝降噪 (LENR) 开启时自动提醒 · 实时取景 HFR 星点测焦与 V 型曲线自动对焦 · 拍月曝光（结合月相与仰角的 Looney 11 法则，支持地球照）· 逐小时银河指向图 · 极轴校准刻度盘与北天星图（北斗七星/仙后座）· 未来 7 晚观星日历（月相、天文黑夜、银河窗口、极限星等与本周最佳夜）· 堆栈用文件前缀（LGHT/DARK/FLAT/BIAS） |
| 📷 **摄影** | HDR 包围曝光 · 景深合成（Focus Stacking）· 双原生 ISO（Dual ISO）· 自动向右曝光（ETTR）· 移动侦测与陷阱对焦 · 实时取景辅助工具（峰值对焦、斑马纹、直方图、伪色、对焦放大、点测光与暗光提亮）· ND 减光镜快门换算与自动 B 门倒计时 · **独立白平衡界面**（补齐 6D 缺失的 WB 独立按键，支持佳能预设与色温标尺，可设为拍摄界面按 SET 直达） |
| 🎞️ **胶卷** | 16 款经典胶片模拟（彩色负片、反转片、黑白、电影卷）· **4 个自定义胶片配方槽**（可调 ISO、照片风格、反差、白平衡、颗粒、暗角，支持导出 TXT 配方卡分享）· 迫冲/减冲 · 12/24/36 张计数 · 暂停与恢复 · 实时取景状态栏计数器 · 存储卡拍摄记录 · 仅 RAW 模式提醒 · 配套 [LightCraft / Lightroom XMP 预设](presets/) |
| 💾 **配置方案** | 5 个自定义配置槽，内置 5 套开箱预设：人像 (Av f/2.8)、风光 (Av f/8 ISO 100)、街拍 (Av f/5.6 ISO Auto)、运动 (Tv 1/1000)、夜景 (M 1/30 f/4 ISO 3200)；若镜头光圈未达预设值将自动贴合镜头极限 |
| 🔁 **恢复 6D 默认** | 一键将相机恢复至开启 Iride 前的原始状态：照片风格与微调滑块、ISO、快门、光圈、白平衡、回放设置、Iride 改动的 Magic Lantern 开关及文件前缀 |
| 🌍 **地点与时区** | 内置 57 座全球城市，支持自由调整经纬度，覆盖全球时区并支持自动夏令时（已对照 IANA 数据库校验） |
| ✨ **交互界面** | 内置按需裁剪的简体中文 4 级抗锯齿位图字库（Noto Sans SC）与比例小字体（Inter Medium）· 圆角卡片与手绘图标 · 全屏 INFO 帮助说明 · 双缓冲无闪烁动画 · 支持简体中文 / 英语 / 意大利语切换 · 夜间护眼红光主题 · 开机自动启动，按删除键（或顶屏背光键）呼出 · 按键诊断与机身自检 |

### 定制修改版 Magic Lantern 核心

自 1.4 版起，发布包不仅包含模块 `iride.mo`，还包含针对 Iride 优化的 Magic Lantern 核心（`autoexec.bin`，补丁见 [`module/magiclantern.patch`](module/magiclantern.patch)）：

| 核心改动 | 作用 |
|---|---|
| **模块全屏模式** | Iride 打开期间阻止佳能原生界面重绘，彻底消除底层菜单闪烁叠加 |
| **核心保活佳能对话框** | 实时取景下由 ML 自动保活；半按快门即时关闭菜单无需等待重绘 |
| **事件同步信号** | ML 主动通知界面就绪与重绘时机，打开无固定延迟、按需刷新更流畅 |

核心新接口采用弱符号（weak symbol）链接：`iride.mo` 也可在官方版 Magic Lantern 下运行，仅缺少上述全屏无闪烁优化。所有代码均从存储卡运行，**不修改相机内部 ROM**。

### 顶屏背光键说明

EOS 6D 的肩屏背光键在回放模式下会上报 `0x20` 事件，但在拍摄模式下是否上报取决于具体机身状态。可在 **选项 → 按键诊断** 中查看近期按键事件，记录同步保存在 `ML/LOGS/IRIDEKEY.TXT`。

### 胶卷模拟与 RAW 后期

<p align="center"><img src="docs/screenshots/rullini_tutti-v06.png" width="720" alt="16 款经典胶卷"></p>

6D 机身仅将胶片风格应用于 **JPEG**（以及 CR2 内嵌预览图），在 LightCraft / Lightroom 中打开纯 RAW 时色调会恢复中性。
推荐两种用法：
1. 拍摄 **RAW+L**（若处于纯 RAW 模式，Iride 会标红提醒）；
2. 在电脑后期使用配套的 **[16 套 XMP 胶片预设](presets/)**，为 RAW 赋予同款胶片质感。

<p align="center"><img src="docs/screenshots/caricamento-v16.gif" width="540" alt="装卷动画"></p>
<p align="center"><img src="docs/screenshots/riavvolgimento-v16.gif" width="540" alt="倒卷动画"></p>

所有天文算法均在机身离线实时计算，并对照 [astropy](https://www.astropy.org/) 校验：北极星时角误差 < 0.4 秒、太阳 < 0.004°、月球 < 0.24°、日落/天文黑夜与月出月落误差均在 1 分钟以内。

## 安装方法

1. 确认 EOS 6D 已刷入 **佳能原厂固件 1.1.6**（参考 [Magic Lantern – 6D](https://builds.magiclantern.fm/6D.html)）。本仓库不含佳能原厂固件。
2. 从 **Releases** 下载 `Iride6D-<版本号>-SD.zip`（升级用户覆盖 `autoexec.bin` 与 `ML/modules/iride.mo` 即可）。
3. 在 6D 机身内格式化 SD 卡，将压缩包内所有文件解压到 SD 卡根目录。
4. 模式转盘切至 **M 档**，进入佳能菜单 → 固件版本 → 更新固件，启动 Magic Lantern 安装程序并按提示重启。
5. 开机后自动进入 Iride 主页（可在「选项」中关闭）。平时按 **删除键（垃圾桶）** 打开 Iride；在 Iride 界面内按删除键可切入 Magic Lantern 菜单，再按关闭。

完整说明见 [docs/LEGGIMI.txt](docs/LEGGIMI.txt)，首次真机测试请参考 **[6D 实机验证清单](docs/PROVA_6D.md)**。若机身出现卡死，拔插电池即可恢复。

## 自行编译与字库更新

### 1. 更新翻译与中文字库（修改中文文案后执行）

```bash
python3 tools/i18n/gen.py            # 生成 module/iride/lang_en.inc 与 lang_zh.inc
python3 tools/font/make_font_zh.py   # 按需裁剪并生成 module/iride/font_zh.inc
```

### 2. 编译 6D 1.1.6 固件包（Linux / WSL）

```bash
sudo apt install gcc-arm-none-eabi binutils-arm-none-eabi libnewlib-arm-none-eabi python3-docutils zip
git clone https://github.com/reticulatedpines/magiclantern_simplified ml
cd ml && git checkout ed3e7c0dfacfdeaf3349dee73edf9e3621217462   # 6D 官方构建 (2025-06-20)
cp -r ../module/iride modules/
git apply ../module/magiclantern.patch
cd platform/6D.116 && make -j8      # 输出 -> build/magiclantern.zip
```

GitHub Actions（`.github/workflows/build.yml`）会在每次推送时自动执行全部模拟器测试并编译 6D 固件包。

### 3. 本地模拟器测试与 Web Demo

```bash
# 运行 PC 模拟器与全部自动化测试（含简体中文越界与翻译完整度测试）
cd simulator && mkdir -p out
gcc -std=gnu99 -Ishim -o preview preview.c -lm && ./preview
python3 check_tz.py
python3 check_formats.py

# 构建浏览器 WebAssembly 演示版
sudo apt install emscripten
sh simulator/web/build.sh            # 输出 -> site/iride.js 与 site/iride.wasm
cd site && python3 -m http.server    # 访问 http://localhost:8000
```

## 目录结构

```text
module/iride/       Iride 模块源码（含 lang_en.inc、lang_zh.inc、font_small.inc、font_zh.inc）
tools/i18n/         英文 (en.py) 与简体中文 (zh.py) 词典及代码生成器 (gen.py)
tools/font/         小字体生成器 (make_font.py) 与按需裁剪中文字库生成器 (make_font_zh.py)
tools/astrostack/   CSV 拍摄会话读取器与 AstroStack 堆栈规划脚本
module/*.patch      Magic Lantern 6D 核心补丁（全屏模式与构建集成）
simulator/          PC 模拟器、自动化测试套件与截图渲染器
simulator/web/      浏览器演示版（WebAssembly）
site/               GitHub Pages 演示站点
presets/            16 款胶片 XMP 预设与自定义配方转换器
docs/               使用说明、实机测试清单与截图
```

## 致谢与许可

- 基于 [Magic Lantern](https://www.magiclantern.fm/)（[源码](https://github.com/reticulatedpines/magiclantern_simplified)），GPL v2 许可。
- 上游项目：[GodEater58/Iride-6D](https://github.com/GodEater58/Iride-6D)。
- 中文字库基于 **Noto Sans SC（思源黑体）**，遵循 SIL Open Font License 1.1。
- NPF 公式参考 [Lightstalking](https://www.lightstalking.com/npf-rule/)。
- 本项目遵循 **GPL v2** 协议，详见 [LICENSE](LICENSE)。

Canon 与 EOS 为佳能株式会社注册商标。本项目与佳能公司无任何关联。
