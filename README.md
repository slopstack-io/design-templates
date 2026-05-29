# 🎨 Design Templates

100 base app layouts for the **Frau Holle** pipeline — 20 categories × 5 design variants each.

## Design Variants

Each category has 5 visual directions:

| Variant | Suffix | Style |
|---------|--------|-------|
| **Base** | (none) | Original design — clean, professional |
| **Dark** | `-dark` | Dark mode, glowing accents, deep backgrounds |
| **Vibrant** | `-vibrant` | Colorful gradients, glass morphism, bold energy |
| **Minimal** | `-minimal` | Stripped down, thin borders, maximum whitespace |
| **Visual** | `-visual` | Image-heavy, editorial, photography-driven |

## Categories

| # | Category | Base Theme | Mobile |
|---|----------|-----------|--------|
| 01 | Dashboard / Analytics | 🌙 Dark | Desktop |
| 02 | E-Commerce / Product Catalog | ☀️ Light | Desktop |
| 03 | Content / CMS / Blog | ☀️ Light | Desktop |
| 04 | Landing / Marketing Page | ☀️ Light | Desktop |
| 05 | Social Feed / Community | 🌙 Dark | Desktop |
| 06 | Form / Intake / Survey | ☀️ Light | Desktop |
| 07 | Portfolio / Gallery | ☀️ Light | Desktop |
| 08 | Scheduling / Booking | ☀️ Light | Desktop |
| 09 | Chat / Messaging | ☀️ Light | Desktop |
| 10 | Tool / Utility | 🌙 Dark | Desktop |
| 11 | Finance / Investing | ☀️ Light | Desktop |
| 12 | Food / Recipes | ☀️ Light | Desktop |
| 13 | Shop Dashboard | ☀️ Light | Mobile |
| 14 | Card Manager / Banking | ☀️ Light | Mobile |
| 15 | Education / Learning | 🟣 Purple | Mobile |
| 16 | Smart Home / IoT | 🌙 Dark Teal | Mobile |
| 17 | Travel / Outdoor | 🌙 Dark Blue | Mobile |
| 18 | Health / Telehealth | 🟠 Orange | Mobile |
| 19 | Food Delivery | 🔴 Red | Mobile |
| 20 | Crypto / Fintech | 🟣 Indigo | Mobile |

## Usage

### Preview
```bash
cd layouts/
python3 -m http.server 8765
# Open http://localhost:8765/01-dashboard-vibrant.html
```

### Frau Holle Intake Flow
1. Customer describes their app idea
2. Frau Holle determines the category (e.g. "E-Commerce")
3. Shows 5 design variant previews to the customer
4. Customer picks their preferred style
5. Solist receives the chosen template as starting point
6. Customizes content, branding, and features

### Regenerate Variants
```bash
python3 generate-variants.py
```

## Naming Convention
```
{number}-{category}.html           → Base variant
{number}-{category}-dark.html      → Dark mode variant
{number}-{category}-vibrant.html   → Colorful/gradient variant
{number}-{category}-minimal.html   → Minimal/clean variant
{number}-{category}-visual.html    → Image-heavy/editorial variant
```

## Tech Stack (planned)
- Next.js + Tailwind CSS
- shadcn/ui components
- Each layout will have a Next.js template equivalent

## Stats
- **100 HTML files** · **1.3MB total**
- **20 categories** × **5 variants** each
- **12 desktop** + **8 mobile** base layouts
- All self-contained, responsive, German content

## License
MIT — part of the Frau Holle project by Slopstack.
