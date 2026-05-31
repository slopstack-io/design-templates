# 🎨 Design Templates

128 hand-crafted app layouts for the **Frau Holle** pipeline — 20 categories × 4 design variants + mobile equivalents.

## Design Variants

Each category has 4 completely unique designs — not just color swaps, but fundamentally different layouts:

| Variant | Suffix | Style |
|---------|--------|-------|
| **Base** | (none) | Clean SaaS — professional, sidebar/grid, modern |
| **Bento** | `-bento` | Playful — colorful card grid, pill nav, emoji, pastel gradients |
| **Editorial** | `-editorial` | Magazine — serif headings, prose layout, warm tones, pull-quotes |
| **Premium** | `-premium` | Luxury — dark bg, glass cards, gold accent, max whitespace |

## Categories

### Desktop (01–12)
| # | Category |
|---|----------|
| 01 | Dashboard / Analytics |
| 02 | E-Commerce / Product Catalog |
| 03 | Content / CMS / Blog |
| 04 | Landing / Marketing Page |
| 05 | Social Feed / Community |
| 06 | Form / Intake / Survey |
| 07 | Portfolio / Gallery |
| 08 | Scheduling / Booking |
| 09 | Chat / Messaging |
| 10 | Tool / Utility |
| 11 | Finance / Investing |
| 12 | Food / Recipes |

### Native Mobile (13–20)
| # | Category |
|---|----------|
| 13 | Shop Dashboard |
| 14 | Card Manager / Banking |
| 15 | Education / Learning |
| 16 | Smart Home / IoT |
| 17 | Travel / Outdoor |
| 18 | Health / Telehealth |
| 19 | Food Delivery |
| 20 | Crypto / Fintech |

## Naming Convention
```
{number}-{category}.html              → Base desktop
{number}-{category}-bento.html        → Bento desktop
{number}-{category}-editorial.html    → Editorial desktop
{number}-{category}-premium.html      → Premium desktop
{number}-{category}-mobile.html       → Base mobile (01–12 only)
{number}-{category}-mobile-bento.html → Bento mobile (01–12 only)
{number}-{category}-mobile-editorial.html → Editorial mobile (01–12 only)
{number}-{category}-mobile-premium.html   → Premium mobile (01–12 only)
```

## Frau Holle Intake Flow

1. Customer describes their app idea
2. Frau Holle determines the category (e.g. "E-Commerce")
3. Shows 4 design variant previews to the customer
4. Customer picks their preferred style
5. Solist receives the chosen template reference (e.g. `02-ecommerce-bento`) as starting point
6. Fetches the HTML template, extracts design language, builds Next.js PWA
7. Customizes content, branding, and features for the customer

## Preview

```bash
cd layouts/
python3 -m http.server 8765
# Open http://localhost:8765/01-dashboard.html
# Compare: http://localhost:8765/01-dashboard-bento.html
```

## Stats

- **128 HTML files** · ~1.3 MB total
- **20 categories** × **4 variants** each = 80 layouts
- **48 mobile equivalents** for desktop categories 01–12
- **12 desktop** + **8 native mobile** base categories
- All self-contained, responsive, German content

## License

MIT — part of the Frau Holle project by Slopstack.
