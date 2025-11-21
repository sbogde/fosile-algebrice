#!/usr/bin/env python3
"""Convert chosen PNG favicon to SVG"""
try:
    from PIL import Image
    
    # Read the chosen PNG
    img = Image.open('docs/favicon.png')
    
    # Get dimensions
    width, height = img.size
    
    # Start SVG
    svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
    
    # Convert pixels to SVG rectangles
    pixels = img.load()
    
    # Group same-colored adjacent pixels for efficiency
    current_color = None
    rects = []
    
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            if len(pixel) == 3:
                r, g, b = pixel
                a = 255
            else:
                r, g, b, a = pixel
            
            # Skip fully transparent pixels
            if a == 0:
                continue
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            opacity = a / 255.0
            
            # Add rectangle for this pixel
            if opacity < 1.0:
                rects.append(f'  <rect x="{x}" y="{y}" width="1" height="1" fill="{color}" opacity="{opacity:.2f}"/>')
            else:
                rects.append(f'  <rect x="{x}" y="{y}" width="1" height="1" fill="{color}"/>')
    
    svg_content += '\n'.join(rects)
    svg_content += '\n</svg>'
    
    # Save SVG
    with open('docs/favicon.svg', 'w') as f:
        f.write(svg_content)
    
    print(f"✅ Converted favicon.png to favicon.svg ({len(rects)} elements)")
    print("   Rebuild with ./build-website.sh to see changes")
    
except ImportError:
    print("⚠️  PIL/Pillow not available")
except Exception as e:
    print(f"❌ Error: {e}")
