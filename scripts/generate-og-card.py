#!/usr/bin/env python3
"""
Regenerate assets/og-card.png — the 1200x630 social share card used for
og:image / twitter:image (wired up in _config.yml).

Usage:
    python3 -m venv .venv && .venv/bin/pip install Pillow
    # Fonts aren't committed to the repo; fetch the three variable TTFs used here:
    mkdir -p scripts/fonts
    curl -sL -o scripts/fonts/Fraunces.ttf \
        "https://raw.githubusercontent.com/google/fonts/main/ofl/fraunces/Fraunces%5BSOFT,WONK,opsz,wght%5D.ttf"
    curl -sL -o scripts/fonts/Inter.ttf \
        "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf"
    curl -sL -o scripts/fonts/JetBrainsMono.ttf \
        "https://raw.githubusercontent.com/google/fonts/main/ofl/jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"
    .venv/bin/python scripts/generate-og-card.py

Edit the copy below (HEADLINE / SUBHEAD / META) to match the site, then re-run.
Keep it in sync with assets/css/main.css's dark-mode palette and the hero
front-matter code sample in index.html.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path(__file__).resolve().parent / "fonts"
OUT_PATH = ROOT / "assets" / "og-card.png"
LOGO_PATH = ROOT / "assets" / "hiyd-logo-90.png"

W, H = 1200, 630

# Dark-mode palette from assets/css/main.css
BG = (23, 19, 12)
PANEL = (34, 28, 19)
INK = (242, 234, 217)
INK_SOFT = (200, 189, 159)
INK_FAINT = (148, 136, 108)
LINE = (51, 42, 26)
LINE_STRONG = (69, 56, 36)
ACCENT = (87, 181, 127)
ACCENT_INK = (141, 214, 168)

HEADLINE = "Write Jekyll posts on your iPhone and iPad."
SUBHEAD = ["Draft Markdown with front matter, then publish", "straight to your GitHub repository."]
META = ["FREE", "IOS & IPADOS 18.6+", "NO ACCOUNT"]

FRONT_MATTER_FILENAME = "2026-09-10-hello-world.md"
FRONT_MATTER_ROWS = [
    ("", "---"),
    ("title: ", "Hello, world"),
    ("date: ", "2026-09-10 09:24 +0100"),
    ("author: ", "Sam"),
    ("tags: ", "[jekyll, ios, writing]"),
    ("draft: ", "false"),
    ("", "---"),
]
FRONT_MATTER_BODY = ["Written on the train, committed", "before the next stop."]

MARGIN = 64


def inter(size, weight=400, opsz=None):
    f = ImageFont.truetype(str(FONT_DIR / "Inter.ttf"), size)
    f.set_variation_by_axes([opsz or min(32, max(14, size)), weight])
    return f


def fraunces(size, weight=700, opsz=None):
    f = ImageFont.truetype(str(FONT_DIR / "Fraunces.ttf"), size)
    # axes order: [Optical Size, Weight, Softness, Wonky] — keep Soft/Wonky at
    # 0 to match the non-wonky static instances loaded on the site itself.
    f.set_variation_by_axes([opsz or min(144, max(9, size)), weight, 0, 0])
    return f


def mono(size, weight=500):
    f = ImageFont.truetype(str(FONT_DIR / "JetBrainsMono.ttf"), size)
    f.set_variation_by_axes([weight])
    return f


def text_w(draw, s, font):
    b = draw.textbbox((0, 0), s, font=font)
    return b[2] - b[0]


def tracked_text(draw, xy, s, font, fill, tracking=0):
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=font, fill=fill)
        x += text_w(draw, ch, font) + tracking
    return x


def draw_measured(draw, xy, s, font, fill):
    draw.text(xy, s, font=font, fill=fill)
    return xy[0] + text_w(draw, s, font)


def wrap(draw, s, font, max_w):
    words = s.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)

    # Soft accent glow, bottom-right, behind the card.
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse([W - 520, H - 320, W + 220, H + 280], fill=150)
    glow = glow.filter(ImageFilter.GaussianBlur(110))
    tint = Image.new("RGB", (W, H), ACCENT)
    img = Image.composite(tint, img, glow.point(lambda p: int(p * 0.16)))

    draw = ImageDraw.Draw(img)

    # Logo + wordmark + eyebrow
    logo_size = 52
    logo = Image.open(LOGO_PATH).convert("RGBA").resize((logo_size * 3, logo_size * 3), Image.LANCZOS)
    mask = Image.new("L", logo.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, *logo.size], radius=int(logo_size * 3 * 0.28), fill=255)
    logo.putalpha(mask)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
    img.paste(logo, (MARGIN, MARGIN), logo)

    wm_font = fraunces(30, 700)
    wm_x = MARGIN + logo_size + 16
    wm_x2 = draw_measured(draw, (wm_x, MARGIN + (logo_size - 30) // 2 - 3), "Hiyd", wm_font, INK)

    eyebrow_font = mono(17, 600)
    ex = wm_x2 + 28
    tracked_text(draw, (ex, MARGIN + (logo_size - 17) // 2 - 1), "THE JEKYLL COMPANION APP", eyebrow_font, ACCENT_INK, tracking=2)

    # Headline + subhead
    head_font = fraunces(60, 700, 72)
    y = 172
    for line in wrap(draw, HEADLINE, head_font, 640):
        draw.text((MARGIN, y), line, font=head_font, fill=INK)
        y += 70

    sub_font = inter(25, 400, 20)
    y += 14
    for line in SUBHEAD:
        draw.text((MARGIN, y), line, font=sub_font, fill=INK_SOFT)
        y += 36

    # Bottom meta row
    meta_font = mono(16, 500)
    meta_y = H - 96
    x = MARGIN
    for i, item in enumerate(META):
        color = ACCENT_INK if i == 0 else INK_FAINT
        x = tracked_text(draw, (x, meta_y), item, meta_font, color, tracking=2)
        if i < len(META) - 1:
            x += 16
            draw.ellipse([x - 2, meta_y + 7, x + 2, meta_y + 11], fill=INK_FAINT)
            x += 16

    # Front-matter card, right side (mirrors the hero sample on the homepage)
    card_w, card_h = 430, 372
    card_x, card_y = W - MARGIN - card_w, (H - card_h) // 2 + 6
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=18, fill=PANEL, outline=LINE, width=1)

    bar_h = 44
    draw.line([(card_x, card_y + bar_h), (card_x + card_w, card_y + bar_h)], fill=LINE, width=1)
    for cx in (card_x + 22, card_x + 40, card_x + 58):
        draw.ellipse([cx - 5, card_y + bar_h // 2 - 5, cx + 5, card_y + bar_h // 2 + 5], fill=LINE_STRONG)
    draw.text((card_x + 80, card_y + bar_h // 2 - 9), FRONT_MATTER_FILENAME, font=mono(14, 500), fill=INK_FAINT)

    code_font, code_bold = mono(16, 500), mono(16, 700)
    pad_x, pad_y, line_gap = 26, 26, 25
    cy = card_y + bar_h + pad_y
    for key, val in FRONT_MATTER_ROWS:
        x = card_x + pad_x
        if key:
            x = draw_measured(draw, (x, cy), key, code_bold, ACCENT_INK)
            draw.text((x, cy), val, font=code_font, fill=INK_SOFT)
        else:
            draw.text((x, cy), val, font=code_font, fill=INK_FAINT)
        cy += line_gap

    cy += 14
    body_font = mono(15, 400)
    for line in FRONT_MATTER_BODY:
        draw.text((card_x + pad_x, cy), line, font=body_font, fill=INK_FAINT)
        cy += 22

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT_PATH, optimize=True)
    print(f"saved {OUT_PATH} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
