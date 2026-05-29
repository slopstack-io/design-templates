#!/usr/bin/env python3
"""
Design Template Variant Generator
Takes 20 base layouts and generates 4 variants each (dark, vibrant, minimal, visual)
Total: 20 base + 80 variants = 100 layouts
"""
import os, re, sys

SRC = "/Users/admin/Projects/design-templates/layouts"

# Design system definitions
DARK = {
    "name": "dark",
    "bg_transforms": {
        "#ffffff": "#0f0f14", "#faf9f7": "#0f0f14", "#f8fafc": "#0f0f14",
        "#f8f9fa": "#0f0f14", "#f4f5f7": "#14141e", "#f0f2f5": "#14141e",
        "#f8f6ff": "#14141e", "#faf9f6": "#0f0f14", "#f8f5f1": "#14141e",
        "#f8f8f8": "#14141e", "#e8e5e0": "#1e1e2e",
    },
    "card_transforms": {
        "#ffffff": "#1a1a2e", "white": "#1a1a2e", "#ffffff;": "#1a1a2e;",
    },
    "text_transforms": {
        "#1a1a2e": "#e2e8f0", "#0f172a": "#e2e8f0", "#1e1b4b": "#e2e8f0",
        "#0c1a2a": "#e2e8f0",
    },
    "border_transforms": {
        "#e2e8f0": "#2a2a3e", "#e8e5e0": "#2a2a3e", "#e5e7eb": "#2a2a3e",
        "#ede9fe": "#2a2a3e", "#dbeafe": "#2a2a3e", "#d1fae5": "#2a2a3e",
        "#fef3c7": "#2a2a3e",
    },
    "secondary_transforms": {
        "#64748b": "#8a9bb0", "#6b7280": "#8a9bb0", "#94a3b8": "#8a9bb0",
        "#8a9bb0": "#8a9bb0",  # already dark secondary
    },
    "extra_css": """
    body { background: #0f0f14 !important; color: #e2e8f0; }
    .nav, nav { background: #0f0f14 !important; border-color: #2a2a3e !important; }
    .card, .recipe-card, .subject-card, .control-card, .restaurant-card,
    .doctor-card, .appointment-card, .message-preview, .place-card { background: #1a1a2e !important; border-color: #2a2a3e !important; color: #e2e8f0; }
    .search-bar, .compose, .booking-form, .slots-panel { background: #1a1a2e !important; border-color: #2a2a3e !important; }
    input, textarea, select { background: #14141e !important; color: #e2e8f0 !important; border-color: #2a2a3e !important; }
    table { border-color: #2a2a3e; }
    th { color: #8a9bb0; border-color: #2a2a3e; }
    td { border-color: #2a2a3e; }
    .bottom-nav { background: #0f0f14 !important; border-color: #2a2a3e !important; }
    footer { background: #0a0a12 !important; }
    """
}

VIBRANT = {
    "name": "vibrant",
    "extra_css": """
    @keyframes gradient-shift { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
    body { background: linear-gradient(135deg, #f5f3ff, #ede9fe, #fce7f3, #fef3c7) !important; background-size: 400% 400% !important; animation: gradient-shift 15s ease infinite; }
    .card, .recipe-card, .subject-card, .control-card, .restaurant-card,
    .doctor-card, .appointment-card, .message-preview, .place-card {
        background: rgba(255,255,255,0.85) !important; backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.5) !important;
        box-shadow: 0 8px 32px rgba(99,102,241,0.1) !important;
    }
    .nav, nav { background: rgba(255,255,255,0.7) !important; backdrop-filter: blur(16px) !important; }
    h1, h2, h3 { background: linear-gradient(135deg, #6366f1, #ec4899, #f59e0b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .btn-primary, .btn-book { background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899) !important; }
    .bottom-nav { background: rgba(255,255,255,0.7) !important; backdrop-filter: blur(16px) !important; }
    """
}

MINIMAL = {
    "name": "minimal",
    "extra_css": """
    body { background: #fafafa !important; }
    * { border-radius: 4px !important; }
    .card, .recipe-card, .subject-card, .control-card, .restaurant-card,
    .doctor-card, .appointment-card, .message-preview, .place-card {
        background: white !important; border: 1px solid #e5e5e5 !important;
        box-shadow: none !important; padding: 20px !important;
    }
    .nav, nav { background: white !important; border-bottom: 1px solid #e5e5e5 !important; box-shadow: none !important; }
    h1 { font-weight: 300 !important; letter-spacing: -0.03em !important; }
    h2, h3 { font-weight: 400 !important; }
    .btn-primary, .btn-book { background: #1a1a1a !important; border-radius: 4px !important; }
    .filter-chip, .category-chip { border-radius: 4px !important; border: 1px solid #e5e5e5 !important; background: transparent !important; }
    .filter-chip.active, .category-chip.active { background: #1a1a1a !important; color: white !important; border-color: #1a1a1a !important; }
    .tag, .badge { border-radius: 4px !important; }
    .bottom-nav { background: white !important; border-top: 1px solid #e5e5e5 !important; }
    .search-bar, .compose { background: white !important; border: 1px solid #e5e5e5 !important; }
    """
}

VISUAL = {
    "name": "visual",
    "extra_css": """
    body { background: #0a0a0a !important; color: white; }
    .card, .recipe-card, .subject-card, .restaurant-card,
    .doctor-card, .place-card {
        background: #111 !important; border: none !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
    }
    .nav, nav { background: rgba(10,10,10,0.9) !important; backdrop-filter: blur(16px) !important; border-color: #222 !important; }
    h1, h2, h3 { color: white !important; -webkit-text-fill-color: white !important; }
    p, span, td, th { color: #ccc !important; }
    .recipe-img, .place-img, .restaurant-img, .food-img,
    .subject-icon, .hero, .map-area, .room-card,
    .product-img, .article-img, .gallery-img {
        position: relative; overflow: hidden;
    }
    .recipe-img::after, .place-img::after, .restaurant-img::after,
    .food-img::after, .room-card::after {
        content: ''; position: absolute; inset: 0;
        background: linear-gradient(transparent 50%, rgba(0,0,0,0.8));
    }
    .btn-primary, .btn-book { background: white !important; color: black !important; }
    .bottom-nav { background: rgba(10,10,10,0.95) !important; border-color: #222 !important; }
    .search-bar { background: #1a1a1a !important; border-color: #333 !important; }
    input, textarea, select { background: #1a1a1a !important; color: white !important; border-color: #333 !important; }
    table { border-color: #222; } th { color: #888; border-color: #222; } td { border-color: #222; }
    """
}

def get_base_layouts():
    """Get all 20 base layout files"""
    files = sorted([f for f in os.listdir(SRC) if f.endswith('.html') and '-' in f])
    # Exclude already existing variants
    bases = []
    for f in files:
        # Check if it's a base file (no -dark, -light, -vibrant, -minimal, -visual suffix)
        for suffix in ['-dark', '-light', '-vibrant', '-minimal', '-visual']:
            if suffix in f:
                break
        else:
            bases.append(f)
    return bases

def generate_variant(content, variant, base_filename):
    """Generate a variant from a base layout"""
    new_content = content
    
    # Apply variant-specific CSS transforms
    if variant["name"] == "dark":
        for old, new in DARK["bg_transforms"].items():
            new_content = new_content.replace(old, new)
        for old, new in DARK["card_transforms"].items():
            new_content = new_content.replace(old, new)
        for old, new in DARK["text_transforms"].items():
            new_content = new_content.replace(old, new)
        for old, new in DARK["border_transforms"].items():
            new_content = new_content.replace(old, new)
        for old, new in DARK["secondary_transforms"].items():
            new_content = new_content.replace(old, new)
    
    # Inject variant CSS before </style>
    variant_css = variant["extra_css"]
    new_content = new_content.replace("</style>", variant_css + "\n</style>")
    
    # Update title
    base_name = base_filename.replace('.html', '')
    title_map = {
        "dark": "🌙 Dark",
        "vibrant": "🎨 Vibrant", 
        "minimal": "◻️ Minimal",
        "visual": "📸 Visual",
    }
    old_title = re.search(r'<title>(.*?)</title>', new_content)
    if old_title:
        orig = old_title.group(1)
        new_content = new_content.replace(f'<title>{orig}</title>', f'<title>{orig} — {title_map[variant["name"]]}</title>')
    
    return new_content

def main():
    bases = get_base_layouts()
    print(f"Found {len(bases)} base layouts")
    
    variants = [DARK, VIBRANT, MINIMAL, VISUAL]
    total = 0
    
    for base_file in bases:
        base_path = os.path.join(SRC, base_file)
        with open(base_path, 'r') as f:
            content = f.read()
        
        base_name = base_file.replace('.html', '')
        
        for variant in variants:
            variant_content = generate_variant(content, variant, base_file)
            variant_file = f"{base_name}-{variant['name']}.html"
            variant_path = os.path.join(SRC, variant_file)
            
            with open(variant_path, 'w') as f:
                f.write(variant_content)
            
            total += 1
            print(f"  ✓ {variant_file}")
    
    print(f"\nGenerated {total} variants + {len(bases)} bases = {total + len(bases)} total layouts")

if __name__ == "__main__":
    main()
