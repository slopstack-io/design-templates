# 🎨 Design Templates

80 hand-crafted app layouts for the **Frau Holle** pipeline — 20 categories × 4 unique design variants each.

## Design Variants

Each category has 4 completely unique designs — not just color swaps, but fundamentally different layouts:

| Variant | Suffix | Style |
|---------|--------|-------|
| **Base** | (none) | Clean SaaS — professional, sidebar/grid, modern |
| **Bento** | `-bento` | Playful — colorful card grid, pill nav, emoji, pastel gradients |
| **Editorial** | `-editorial` | Magazine — serif headings, prose layout, warm tones, pull-quotes |
| **Premium** | `-premium` | Luxury — dark bg, glass cards, gold accent, max whitespace |

## Categories

| # | Category | Type |
|---|----------|------|
| 01 | Dashboard / Analytics | Desktop |
| 02 | E-Commerce / Product Catalog | Desktop |
| 03 | Content / CMS / Blog | Desktop |
| 04 | Landing / Marketing Page | Desktop |
| 05 | Social Feed / Community | Desktop |
| 06 | Form / Intake / Survey | Desktop |
| 07 | Portfolio / Gallery | Desktop |
| 08 | Scheduling / Booking | Desktop |
| 09 | Chat / Messaging | Desktop |
| 10 | Tool / Utility | Desktop |
| 11 | Finance / Investing | Desktop |
| 12 | Food / Recipes | Desktop |
| 13 | Shop Dashboard | Mobile |
| 14 | Card Manager / Banking | Mobile |
| 15 | Education / Learning | Mobile |
| 16 | Smart Home / IoT | Mobile |
| 17 | Travel / Outdoor | Mobile |
| 18 | Health / Telehealth | Mobile |
| 19 | Food Delivery | Mobile |
| 20 | Crypto / Fintech | Mobile |

## Preview

```bash
cd layouts/
python3 -m http.server 8765
# Open http://localhost:8765/01-dashboard.html
# Compare: http://localhost:8765/01-dashboard-bento.html
```

## Frau Holle Intake Flow

1. Customer describes their app idea
2. Frau Holle determines the category (e.g. "E-Commerce")
3. Shows 4 design variant previews to the customer
4. Customer picks their preferred style
5. Solist receives the chosen template as starting point
6. Customizes content, branding, and features

## Naming Convention

```
{number}-{category}.html              → Base (SaaS/Clean)
{number}-{category}-bento.html        → Bento (Playful)
{number}-{category}-editorial.html    → Editorial (Magazine)
{number}-{category}-premium.html      → Premium (Luxury)
```

## Stats

- **80 HTML files** · **797 KB total**
- **20 categories** × **4 variants** each
- **12 desktop** + **8 mobile** base layouts
- All self-contained, responsive, German content

## License

MIT — part of the Frau Holle project by Slopstack.
