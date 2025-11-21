#!/usr/bin/env python3
"""Generate PNG favicon from SVG"""
try:
    from PIL import Image, ImageDraw, ImageFont
    
    # Create a 32x32 favicon
    size = 32
    img = Image.new('RGB', (size, size), color='#2C3E50')
    draw = ImageDraw.Draw(img)
    
    # Draw a simple ring/module symbol
    # Outer circle
    draw.ellipse([4, 4, 28, 28], outline='#ECF0F1', width=2)
    # Inner elements suggesting algebra
    draw.arc([10, 10, 22, 22], 0, 180, fill='#3498DB', width=2)
    draw.line([12, 20, 20, 20], fill='#E74C3C', width=2)
    
    # Save as PNG
    img.save('docs/favicon.png')
    print("✅ Created docs/favicon.png")
    
except ImportError:
    print("⚠️  PIL/Pillow not available - skipping PNG favicon generation")
    print("   The SVG favicon will still work in modern browsers")
