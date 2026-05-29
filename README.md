# 🎨 Design Templates

12 base app layouts for the **Frau Holle** pipeline — standalone HTML/CSS templates for rapid prototyping.

Each layout is a self-contained HTML file with embedded CSS, responsive design, and German placeholder content. Frau Holle selects the matching layout based on the customer's intake, then Solist customizes it.

## Layouts

| # | Category | Theme | Style Reference |
|---|----------|-------|-----------------|
| 01 | Dashboard / Analytics | 🌙 Dark | Linear, Sentry |
| 02 | E-Commerce / Product Catalog | ☀️ Light | Stripe, Airbnb |
| 03 | Content / CMS / Blog | ☀️ Light | Notion, Mintlify |
| 04 | Landing / Marketing Page | ☀️ Light | Apple, Framer |
| 05 | Social Feed / Community | 🌙 Dark | Spotify, Pinterest |
| 06 | Form / Intake / Survey | ☀️ Light | Cal.com, Airtable |
| 07 | Portfolio / Gallery | ☀️ Light | Airbnb, Figma |
| 08 | Scheduling / Booking | ☀️ Light | Cal.com |
| 09 | Chat / Messaging | ☀️ Light | Intercom |
| 10 | Tool / Utility | 🌙 Dark | Vercel, IDE |
| 11 | Finance / Investing | ☀️ Light | Wise, Coinbase |
| 12 | Food / Recipes | ☀️ Light | Food Magazine |

## Usage

### Preview locally
```bash
cd layouts/
python3 -m http.server 8765
# Open http://localhost:8765/01-dashboard.html
```

### Integrate with Solist
1. Solist reads the customer's intake → determines app type
2. Selects matching layout from this repo
3. Customizes content, colors, components via shadcn/ui
4. Deploys to Vercel

## Tech Stack (planned)
- Next.js + Tailwind CSS
- shadcn/ui components
- Each layout will have a Next.js template equivalent

## Structure
```
layouts/
  01-dashboard.html
  02-ecommerce.html
  03-content-cms.html
  04-landing-page.html
  05-social-feed.html
  06-form-intake.html
  07-portfolio-gallery.html
  08-scheduling.html
  09-chat-messaging.html
  10-tool-utility.html
  11-finance.html
  12-food.html
```

## License
MIT — part of the Frau Holle project by Slopstack.
