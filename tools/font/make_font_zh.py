#!/usr/bin/env python3
"""生成 module/iride/font_zh.inc：按需裁剪的 Iride 6D 简体中文 4 级抗锯齿位图字库。

扫描 tools/i18n/zh.py（及附加界面字面量）中所有非 ASCII 字符，
使用思源黑体 (Noto Sans SC, SIL Open Font License 1.1) 生成对应 4 种字号的 2-bit 位图：
  0: FONT_SMALL     (13 px, 对齐 Inter Medium 13 px)
  1: FONT_MED       (17 px, 对齐 argnor23.rbf)
  2: FONT_MED_LARGE (21 px, 对齐 argnor28.rbf)
  3: FONT_LARGE     (24 px, 对齐 argnor32.rbf)

用法：python3 tools/font/make_font_zh.py [字体文件路径]
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "module", "iride", "font_zh.inc")

DEFAULT_FONTS = [
    r"C:\Windows\Fonts\NotoSansSC-VF.ttf",
    r"C:\Windows\Fonts\msyh.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansSC-Medium.otf",
    "/usr/share/fonts/noto-cjk/NotoSansCJK-Medium.ttc",
]

# (像素字号, 相对 txt(font, fg, x, y, s) 中 y 的目标视觉中心行)
SIZES = [
    (13, 5.5),   # FONT_SMALL
    (17, 9.5),   # FONT_MED (argnor23: 'A' rows 2..16, center 9)
    (21, 11.5),  # FONT_MED_LARGE (argnor28: 'A' rows 2..20, center 11)
    (24, 13.5),  # FONT_LARGE (argnor32: 'A' rows 3..23, center 13)
]

# 代码中不经 zh.py 但可能直接显示的中文字符（如语言名称、后台状态条）
EXTRA_CHARS = "简体中文按删除键停止"


def pick_font():
    if len(sys.argv) > 1:
        return sys.argv[1]
    for p in DEFAULT_FONTS:
        if os.path.exists(p):
            return p
    sys.exit("未找到可用的中文字体，请通过参数传入 TTF/OTF/TTC 字体路径。")


def load_chars():
    sys.path.insert(0, os.path.join(ROOT, "tools", "i18n"))
    from zh import ZH  # noqa: E402
    s = {ch for v in ZH.values() for ch in v if ord(ch) >= 0x80}
    s |= {ch for ch in EXTRA_CHARS if ord(ch) >= 0x80}
    cps = sorted(ord(ch) for ch in s)
    if any(cp > 0xFFFF for cp in cps):
        sys.exit("存在超出 BMP (U+FFFF) 的字符，当前字库索引仅支持 uint16 码点。")
    return cps


def build_size(font_path, px_size, target_center, cps):
    f = ImageFont.truetype(font_path, px_size)
    try:
        # 可变字体（如 NotoSansSC-VF）设为 500 (Medium) 字重，在相机小屏更锐利
        f.set_variation_by_axes([500])
    except Exception:
        pass

    # 用标准汉字“国”的墨迹中心确定该字号的统一垂直偏移，保证所有汉字同一水平线
    can = px_size + 16
    ref = Image.new("L", (can, can), 0)
    ImageDraw.Draw(ref).text((4, 4), "国", font=f, fill=255)
    rpx = ref.load()
    rrows = [y for y in range(can) if any(rpx[x, y] > 30 for x in range(can))]
    ref_center = (rrows[0] + rrows[-1]) / 2.0
    base_dy = int(round(target_center - ref_center))

    meta = []  # (adv, xoff, yoff, w, h, bit_offset)
    bits = []
    for cp in cps:
        ch = chr(cp)
        adv = max(1, int(round(f.getlength(ch))))
        W = max(can, adv + 12)
        m = Image.new("L", (W, can), 0)
        ImageDraw.Draw(m).text((4, 4), ch, font=f, fill=255)
        px = m.load()
        cols = [x for x in range(W) if any(px[x, y] > 30 for y in range(can))]
        rows = [y for y in range(can) if any(px[x, y] > 30 for x in range(W))]
        off = len(bits)
        if cols and rows:
            x0, x1 = cols[0], cols[-1] + 1
            y0, y1 = rows[0], rows[-1] + 1
            w, h = x1 - x0, y1 - y0
            xoff = x0 - 4
            yoff = y0 + base_dy
            for y in range(y0, y1):
                for x in range(x0, x1):
                    v = px[x, y]
                    bits.append(min(3, (v + 42) // 85))
            meta.append((adv, xoff, yoff, w, h, off))
        else:
            meta.append((adv, 0, 0, 0, 0, off))

    packed = bytearray()
    for i in range(0, len(bits), 4):
        b0 = bits[i]
        b1 = bits[i + 1] if i + 1 < len(bits) else 0
        b2 = bits[i + 2] if i + 2 < len(bits) else 0
        b3 = bits[i + 3] if i + 3 < len(bits) else 0
        packed.append(b0 | (b1 << 2) | (b2 << 4) | (b3 << 6))
    return meta, packed


def fmt_arr(vals, per_line=24):
    lines = []
    for i in range(0, len(vals), per_line):
        lines.append("    " + ", ".join(str(v) for v in vals[i:i + per_line]) + ",")
    return "\n".join(lines)


def main():
    font_path = pick_font()
    cps = load_chars()
    n = len(cps)

    all_meta = []
    all_bits = bytearray()
    size_bit_base = []
    size_stats = []
    for idx, (px_size, center) in enumerate(SIZES):
        meta, packed = build_size(font_path, px_size, center, cps)
        base_px = len(all_bits) * 4
        size_bit_base.append(base_px)
        all_meta.append([(a, xo, yo, w, h, off + base_px) for (a, xo, yo, w, h, off) in meta])
        all_bits.extend(packed)
        size_stats.append((px_size, len(packed)))

    lines = [
        "/* font_zh.inc - 由 tools/font/make_font_zh.py 自动生成，请勿手工修改。",
        f" * 字体来源: {os.path.basename(font_path)} (SIL Open Font License 1.1)。",
        f" * 按需收录 {n} 个简体中文字符/标点，4 种字号 (13/17/21/24 px)，2-bit 抗锯齿位图。 */",
        f"#define ZH_N {n}",
        "typedef struct { unsigned char adv; signed char xoff, yoff; unsigned char w, h; unsigned int off; } zh_glyph_t;",
        f"static const unsigned short zh_cp[ZH_N] = {{",
        fmt_arr(cps, 16),
        "};",
    ]
    for sidx, meta in enumerate(all_meta):
        lines.append(f"static const zh_glyph_t zh_g{sidx}[ZH_N] = {{")
        row = []
        for a, xo, yo, w, h, off in meta:
            row.append(f"{{{a},{xo},{yo},{w},{h},{off}}}")
            if len(row) == 6:
                lines.append("    " + ", ".join(row) + ",")
                row = []
        if row:
            lines.append("    " + ", ".join(row) + ",")
        lines.append("};")
    lines.append("static const zh_glyph_t *const zh_tbl[4] = { zh_g0, zh_g1, zh_g2, zh_g3 };")
    lines.append(f"static const unsigned char zh_bits[{len(all_bits)}] = {{")
    lines.append(fmt_arr(all_bits, 24))
    lines.append("};")

    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")

    stat_str = ", ".join(f"{sz}px={b/1024:.1f}KB" for sz, b in size_stats)
    print(f"{OUT}: {n} 字符, 共 {len(all_bits)/1024:.1f} KB ({stat_str})")


if __name__ == "__main__":
    main()
