#!/usr/bin/env python3
"""Generate 10 PWA icon options (512x512) for mathematics thesis"""
try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    size = 512
    
    # Helper to get font
    def get_font(font_size, bold=False):
        font_paths = [
            "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Times New Roman.ttf",
            "/System/Library/Fonts/Supplemental/Georgia Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Georgia.ttf",
            None
        ]
        for path in font_paths:
            try:
                if path:
                    return ImageFont.truetype(path, font_size)
            except:
                continue
        return None
    
    # Option 1: Large ℤₙ with gradient background
    def create_option1():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        # Gradient-like effect with circles
        for i in range(5):
            alpha = int(255 * (0.1 + i * 0.15))
            r = size//2 - i * 40
            draw.ellipse([size//2-r, size//2-r, size//2+r, size//2+r], 
                        fill=f'#{30+i*5:02x}{50+i*10:02x}{70+i*15:02x}')
        
        font_large = get_font(320, bold=True)
        font_small = get_font(100)
        
        draw.text((size//2, size//2 + 20), "ℤ", fill='#ECF0F1', anchor="mm", font=font_large)
        draw.text((400, 360), "n", fill='#3498DB', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option1.png')
        print("✅ Option 1: Large ℤₙ with gradient")
    
    # Option 2: ℤ̂ₙ with prominent hat
    def create_option2():
        img = Image.new('RGB', (size, size), color='#2C3E50')
        draw = ImageDraw.Draw(img)
        
        # Background accent
        draw.ellipse([50, 50, size-50, size-50], outline='#34495E', width=8)
        
        # Large hat
        draw.line([120, 120, size//2, 60, size-120, 120], fill='#E74C3C', width=18)
        
        font_large = get_font(300, bold=True)
        font_small = get_font(90)
        
        draw.text((size//2, size//2 + 50), "ℤ", fill='#ECF0F1', anchor="mm", font=font_large)
        draw.text((390, 370), "n", fill='#16C79A', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option2.png')
        print("✅ Option 2: ℤ̂ₙ with prominent hat")
    
    # Option 3: Module diagram with nodes
    def create_option3():
        img = Image.new('RGB', (size, size), color='#1e2761')
        draw = ImageDraw.Draw(img)
        
        # Three large nodes in triangle
        positions = [(size//4, size//4), (3*size//4, size//4), (size//2, 3*size//4)]
        for pos in positions:
            draw.ellipse([pos[0]-50, pos[1]-50, pos[0]+50, pos[1]+50], 
                        fill='#f9a826', outline='#f39c12', width=6)
        
        # Arrows between nodes
        draw.line([positions[0][0]+40, positions[0][1], positions[1][0]-40, positions[1][1]], 
                 fill='#5d5fef', width=12)
        draw.line([positions[0][0]+20, positions[0][1]+40, positions[2][0]-30, positions[2][1]-40], 
                 fill='#5d5fef', width=12)
        draw.line([positions[1][0]-20, positions[1][1]+40, positions[2][0]+30, positions[2][1]-40], 
                 fill='#5d5fef', width=12)
        
        # Center label
        font_med = get_font(120, bold=True)
        draw.text((size//2, size//2), "M", fill='#ffffff', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option3.png')
        print("✅ Option 3: Module diagram")
    
    # Option 4: Ring with direct sum ⊕
    def create_option4():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Large ring
        draw.ellipse([80, 80, size-80, size-80], outline='#ea5455', width=20)
        
        # Direct sum symbol
        draw.line([size//2, 180, size//2, size-180], fill='#f07b3f', width=25)
        draw.line([180, size//2, size-180, size//2], fill='#f07b3f', width=25)
        
        # Small module symbols in corners
        font_small = get_font(60)
        corners = [(140, 140), (size-140, 140), (140, size-140), (size-140, size-140)]
        for i, pos in enumerate(corners):
            draw.text(pos, f"M{i+1}", fill='#16c79a', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option4.png')
        print("✅ Option 4: Ring with ⊕")
    
    # Option 5: Dimension with arrows
    def create_option5():
        img = Image.new('RGB', (size, size), color='#34495e')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(350, bold=True)
        font_small = get_font(80)
        
        # Large D
        draw.text((size//2, size//2), "D", fill='#ecf0f1', anchor="mm", font=font_huge)
        
        # Subscript u
        draw.text((380, 380), "u", fill='#3498db', anchor="mm", font=font_small)
        
        # Dimensional arrows
        arrow_y = 100
        draw.line([80, arrow_y, size-120, arrow_y], fill='#e74c3c', width=15)
        draw.polygon([(size-120, arrow_y-20), (size-120, arrow_y+20), (size-80, arrow_y)], 
                    fill='#e74c3c')
        
        arrow_y = size - 100
        draw.line([size-80, arrow_y, 120, arrow_y], fill='#2ecc71', width=15)
        draw.polygon([(120, arrow_y-20), (120, arrow_y+20), (80, arrow_y)], 
                    fill='#2ecc71')
        
        img.save('docs/pwa-icon-option5.png')
        print("✅ Option 5: Dimension D with arrows")
    
    # Option 6: Abstract algebraic structure
    def create_option6():
        img = Image.new('RGB', (size, size), color='#2d4059')
        draw = ImageDraw.Draw(img)
        
        # Nested circles suggesting structure
        for i in range(4):
            r = 200 - i * 40
            alpha = 100 + i * 40
            draw.ellipse([size//2-r, size//2-r, size//2+r, size//2+r], 
                        outline=f'#ea5455', width=8)
        
        # Center symbol
        font_large = get_font(200, bold=True)
        draw.text((size//2, size//2), "R", fill='#f9f9f9', anchor="mm", font=font_large)
        
        # Corner decorations
        font_small = get_font(70)
        draw.text((100, 100), "∈", fill='#f07b3f', anchor="mm", font=font_small)
        draw.text((size-100, 100), "⊆", fill='#f07b3f', anchor="mm", font=font_small)
        draw.text((100, size-100), "⊕", fill='#f07b3f', anchor="mm", font=font_small)
        draw.text((size-100, size-100), "∩", fill='#f07b3f', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option6.png')
        print("✅ Option 6: Nested ring structure")
    
    # Option 7: Infinity for infinite dimension
    def create_option7():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Large infinity symbol
        center_y = size//2
        draw.arc([60, center_y-120, 220, center_y+120], 90, 270, fill='#16c79a', width=35)
        draw.arc([size-220, center_y-120, size-60, center_y+120], 270, 90, fill='#16c79a', width=35)
        
        # Connecting lines
        draw.line([220, center_y-80, size-220, center_y+80], fill='#16c79a', width=35)
        draw.line([220, center_y+80, size-220, center_y-80], fill='#16c79a', width=35)
        
        # Text overlay
        font_med = get_font(100, bold=True)
        draw.text((size//2, size-100), "dim", fill='#f9a826', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option7.png')
        print("✅ Option 7: Infinity dimension")
    
    # Option 8: Commutative square
    def create_option8():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        # Square vertices
        margin = 140
        vertices = [
            (margin, margin),
            (size-margin, margin),
            (size-margin, size-margin),
            (margin, size-margin)
        ]
        
        # Draw nodes
        for v in vertices:
            draw.ellipse([v[0]-35, v[1]-35, v[0]+35, v[1]+35], 
                        fill='#3498db', outline='#2980b9', width=4)
        
        # Draw arrows
        draw.line([vertices[0][0]+30, vertices[0][1], vertices[1][0]-30, vertices[1][1]], 
                 fill='#e74c3c', width=12)
        draw.line([vertices[1][0], vertices[1][1]+30, vertices[2][0], vertices[2][1]-30], 
                 fill='#e74c3c', width=12)
        draw.line([vertices[3][0]+30, vertices[3][1], vertices[2][0]-30, vertices[2][1]], 
                 fill='#e74c3c', width=12)
        draw.line([vertices[0][0], vertices[0][1]+30, vertices[3][0], vertices[3][1]-30], 
                 fill='#e74c3c', width=12)
        
        # Diagonal (dashed effect with dots)
        for i in range(8):
            t = i / 7
            x = int(vertices[0][0] + (vertices[2][0] - vertices[0][0]) * t)
            y = int(vertices[0][1] + (vertices[2][1] - vertices[0][1]) * t)
            draw.ellipse([x-8, y-8, x+8, y+8], fill='#f39c12')
        
        # Center label
        font_med = get_font(100, bold=True)
        draw.text((size//2, size//2), "□", fill='#ecf0f1', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option8.png')
        print("✅ Option 8: Commutative square")
    
    # Option 9: Matrix-style brackets
    def create_option9():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        # Large brackets
        bracket_width = 25
        margin = 80
        
        # Left bracket
        draw.line([margin+50, margin, margin, margin], fill='#f39c12', width=bracket_width)
        draw.line([margin, margin, margin, size-margin], fill='#f39c12', width=bracket_width)
        draw.line([margin, size-margin, margin+50, size-margin], fill='#f39c12', width=bracket_width)
        
        # Right bracket
        draw.line([size-margin-50, margin, size-margin, margin], fill='#f39c12', width=bracket_width)
        draw.line([size-margin, margin, size-margin, size-margin], fill='#f39c12', width=bracket_width)
        draw.line([size-margin, size-margin, size-margin-50, size-margin], fill='#f39c12', width=bracket_width)
        
        # Matrix of letters
        font_large = get_font(150, bold=True)
        positions = [
            (size//3, size//3), (2*size//3, size//3),
            (size//3, 2*size//3), (2*size//3, 2*size//3)
        ]
        letters = ['M', 'N', 'P', 'Q']
        
        for i, (pos, letter) in enumerate(zip(positions, letters)):
            draw.text(pos, letter, fill='#ecf0f1', anchor="mm", font=font_large)
        
        img.save('docs/pwa-icon-option9.png')
        print("✅ Option 9: Matrix brackets")
    
    # Option 10: Uniform dimension badge
    def create_option10():
        img = Image.new('RGB', (size, size), color='#16202c')
        draw = ImageDraw.Draw(img)
        
        # Badge/shield background
        points = [
            (size//2, 50),
            (size-80, size//3),
            (size-80, 2*size//3),
            (size//2, size-50),
            (80, 2*size//3),
            (80, size//3)
        ]
        draw.polygon(points, fill='#34495e', outline='#2c3e50', width=8)
        
        # Inner glow
        draw.polygon([(p[0], p[1]+20) for p in points[:-1]] + [points[-1]], 
                    fill='#2c3e50', outline='#34495e', width=4)
        
        font_huge = get_font(200, bold=True)
        font_med = get_font(80, bold=True)
        
        # U for Uniform
        draw.text((size//2, size//2 - 30), "U", fill='#3498db', anchor="mm", font=font_huge)
        
        # dim subscript
        draw.text((size//2, size//2 + 120), "dim", fill='#e74c3c', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option10.png')
        print("✅ Option 10: Uniform dimension badge")
    
    # Generate all options
    print("Generating 10 PWA icon options (512x512)...\n")
    create_option1()
    create_option2()
    create_option3()
    create_option4()
    create_option5()
    create_option6()
    create_option7()
    create_option8()
    create_option9()
    create_option10()
    
    print("\n✅ Created 10 PWA icon options!")
    print("\nPreview them and choose your favorite, then:")
    print("  cp docs/pwa-icon-option#.png docs/icon-512.png")
    print("  python3 -c \"from PIL import Image; img = Image.open('docs/icon-512.png'); img.resize((192, 192), Image.LANCZOS).save('docs/icon-192.png')\"")
    
except ImportError:
    print("⚠️  PIL/Pillow not available")
    print("   Install with: pip install Pillow")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
