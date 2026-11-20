#!/usr/bin/env python3
"""Rigenera module/iride/lang_en.inc e lang_zh.inc da tools/i18n/en.py e zh.py.

Uso: python3 tools/i18n/gen.py [--mancanti]
"""
import codecs
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'module', 'iride')
sys.path.insert(0, HERE)
from en import EN  # noqa: E402
from zh import ZH  # noqa: E402

SKIP_FILES = {'font_small.inc', 'font_zh.inc', 'icons_small.inc', 'bench.inc', 'lang_en.inc', 'lang_zh.inc'}
LIT = r'"(?:[^"\\\n]|\\.)*"'
SEQ = re.compile(r'(%s)((?:\s*(?:/\*.*?\*/)?\s*%s)*)' % (LIT, LIT), re.S)
SPEC = re.compile(r'%[-+ #0]*\d*(?:\.\d+)?[a-zA-Z%]')


def literals():
    """Stringhe del codice (le letterali vicine unite, come fa il compilatore)."""
    out = set()
    for name in sorted(os.listdir(SRC)):
        if not (name.endswith('.inc') or name.endswith('.c')) or name in SKIP_FILES:
            continue
        text = open(os.path.join(SRC, name), encoding='utf-8').read()
        for m in SEQ.finditer(text):
            s = ''.join(p[1:-1] for p in re.findall(LIT, m.group(0)))
            if re.search(r'[A-Za-z]', s):
                out.add(s)
    return out


def write_lang(table, filename, sym, macro, header):
    rows, bad = [], []
    for k, v in table.items():
        if SPEC.findall(k) != SPEC.findall(v):
            bad.append(f'{k}  =>  {v}')
            continue
        rows.append((codecs.decode(k, 'unicode_escape').encode('latin-1'), k, v))
    rows.sort()
    if bad:
        sys.exit(f'{filename}: formati diversi (%d e %s devono restare uguali e in ordine):\n  ' + '\n  '.join(bad))
    with open(os.path.join(SRC, filename), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(header)
        fh.write(f'static const char *const {sym}[][2] = {{\n')
        for _, k, v in rows:
            fh.write(f'    {{ "{k}", "{v}" }},\n')
        fh.write(f'}};\n#define {macro} ((int)COUNT({sym}))\n')
    print(f'{len(rows)} traduzioni in {filename}')


def main():
    now = literals()
    write_lang(
        EN,
        'lang_en.inc',
        'lang_en',
        'LANG_EN_N',
        '/* lang_en.inc - Iride in inglese: testo italiano -> testo inglese.\n'
        ' * Generato da tools/i18n/gen.py da tools/i18n/en.py: non modificare a mano.\n'
        ' * Ordinato per strcmp: tr() cerca per bisezione. I formati tengono gli stessi %d/%s. */\n\n',
    )
    write_lang(
        ZH,
        'lang_zh.inc',
        'lang_zh',
        'LANG_ZH_N',
        '/* lang_zh.inc - Iride 简体中文翻译：意大利语原文 -> 简体中文 (UTF-8)。\n'
        ' * 由 tools/i18n/gen.py 从 tools/i18n/zh.py 生成，请勿手工修改。\n'
        ' * 按 strcmp 字节序排列供二分查找；格式占位符 %d/%s 与原文严格一致。 */\n\n',
    )
    missing_zh = sorted(set(EN) - set(ZH))
    if missing_zh:
        sys.exit(f'zh.py 缺少 {len(missing_zh)} 条 en.py 中存在的翻译:\n  ' + '\n  '.join(missing_zh))
    if '--mancanti' in sys.argv:
        for s in sorted(now - set(EN)):
            print('  da tradurre:', s)
        for s in sorted(set(EN) - now):
            print('  non nel codice (macro o lettera singola?):', s)


if __name__ == '__main__':
    main()
