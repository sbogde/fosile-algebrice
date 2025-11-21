#!/usr/bin/env python3
"""Generate 10 more PWA icon options - universal math symbols (512x512)"""
try:
    from PIL import Image, ImageDraw, ImageFont
    import math
    
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
    
    # Option 21: π (Pi) - universal math symbol
    def create_option21():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        # Gradient-like circles
        for i in range(6):
            r = size//2 - i * 35
            alpha = 30 + i * 15
            draw.ellipse([size//2-r, size//2-r, size//2+r, size//2+r], 
                        fill=f'#{alpha:02x}{50+i*10:02x}{70+i*15:02x}')
        
        font_huge = get_font(400, bold=True)
        draw.text((size//2, size//2 + 30), "π", fill='#ecf0f1', anchor="mm", font=font_huge)
        
        # Bottom label
        font_small = get_font(50)
        draw.text((size//2, size-60), "mathematics", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option21.png')
        print("✅ Option 21: π (Pi)")
    
    # Option 22: Σ (Sigma) - summation
    def create_option22():
        img = Image.new('RGB', (size, size), color='#16202c')
        draw = ImageDraw.Draw(img)
        
        # Large circle background
        draw.ellipse([60, 60, size-60, size-60], fill='#34495e', outline='#2ecc71', width=12)
        
        font_huge = get_font(380, bold=True)
        draw.text((size//2, size//2 + 20), "Σ", fill='#2ecc71', anchor="mm", font=font_huge)
        
        # Small numbers
        font_small = get_font(70)
        draw.text((size-140, size-120), "∞", fill='#e74c3c', anchor="mm", font=font_small)
        draw.text((size-140, 120), "n=1", fill='#3498db', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option22.png')
        print("✅ Option 22: Σ (Sigma summation)")
    
    # Option 23: ∞ (Infinity) - iconic math symbol
    def create_option23():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        # Glowing effect with multiple infinity traces
        center_y = size//2
        for i in range(4):
            width = 40 - i * 8
            offset = i * 10
            
            # Left loop
            draw.arc([60+offset, center_y-140+offset, 240-offset, center_y+140-offset], 
                    90, 270, fill='#e74c3c', width=width)
            # Right loop
            draw.arc([size-240+offset, center_y-140+offset, size-60-offset, center_y+140-offset], 
                    270, 90, fill='#3498db', width=width)
            
            # Connecting curves
            draw.line([240-offset, center_y-90, size-240+offset, center_y+90], 
                     fill='#f39c12', width=width)
            draw.line([240-offset, center_y+90, size-240+offset, center_y-90], 
                     fill='#f39c12', width=width)
        
        # Bottom text
        font_med = get_font(60, bold=True)
        draw.text((size//2, size-70), "INFINITE", fill='#16c79a', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option23.png')
        print("✅ Option 23: ∞ (Infinity)")
    
    # Option 24: √ (Square root) with expression
    def create_option24():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Large square root symbol
        draw.line([100, size//2, 140, size//2 + 60], fill='#16c79a', width=30)
        draw.line([140, size//2 + 60, 180, 100], fill='#16c79a', width=30)
        draw.line([180, 100, size-80, 100], fill='#16c79a', width=30)
        
        # Expression under root
        font_large = get_font(150, bold=True)
        draw.text((size//2 + 20, size//2 + 40), "x² + y²", fill='#ecf0f1', anchor="mm", font=font_large)
        
        img.save('docs/pwa-icon-option24.png')
        print("✅ Option 24: √(x² + y²)")
    
    # Option 25: x² + y = z (classic equation)
    def create_option25():
        img = Image.new('RGB', (size, size), color='#2d4059')
        draw = ImageDraw.Draw(img)
        
        # Blackboard style background
        draw.rectangle([40, 40, size-40, size-40], fill='#1e2f3e', outline='#95a5a6', width=8)
        
        font_huge = get_font(140, bold=True)
        
        # Equation: x² + y = z
        draw.text((size//2, 150), "x² + y = z", fill='#ecf0f1', anchor="mm", font=font_huge)
        
        # Decorative elements
        draw.text((size//2, 320), "a³ + b³ = c³", fill='#3498db', anchor="mm", font=font_huge)
        
        # Small pi and infinity
        font_med = get_font(100)
        draw.text((100, size-100), "π", fill='#e74c3c', anchor="mm", font=font_med)
        draw.text((size-100, size-100), "∞", fill='#f39c12', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option25.png')
        print("✅ Option 25: x² + y = z (blackboard)")
    
    # Option 26: ∫ (Integral) - calculus symbol
    def create_option26():
        img = Image.new('RGB', (size, size), color='#34495e')
        draw = ImageDraw.Draw(img)
        
        # Large integral symbol using curves
        # Top curve
        draw.arc([size//2 - 60, 60, size//2 + 60, 180], 180, 0, fill='#3498db', width=35)
        # Vertical line
        draw.line([size//2, 120, size//2, size-120], fill='#3498db', width=35)
        # Bottom curve
        draw.arc([size//2 - 60, size-180, size//2 + 60, size-60], 0, 180, fill='#3498db', width=35)
        
        # Expression
        font_large = get_font(120, bold=True)
        draw.text((size//2 + 140, size//2), "f(x)dx", fill='#ecf0f1', anchor="mm", font=font_large)
        
        # Limits
        font_small = get_font(70)
        draw.text((size//2 + 90, 100), "∞", fill='#e74c3c', anchor="mm", font=font_small)
        draw.text((size//2 + 90, size-100), "0", fill='#2ecc71', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option26.png')
        print("✅ Option 26: ∫ (Integral)")
    
    # Option 27: Multiple operation symbols (+, −, ×, ÷)
    def create_option27():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(200, bold=True)
        
        # Four quadrants with operations
        positions = [
            (size//4, size//4, "+", '#e74c3c'),
            (3*size//4, size//4, "−", '#3498db'),
            (size//4, 3*size//4, "×", '#2ecc71'),
            (3*size//4, 3*size//4, "÷", '#f39c12')
        ]
        
        for x, y, op, color in positions:
            draw.text((x, y), op, fill=color, anchor="mm", font=font_huge)
        
        # Central circle
        draw.ellipse([size//2-80, size//2-80, size//2+80, size//2+80], 
                    fill='#2c3e50', outline='#ecf0f1', width=8)
        font_med = get_font(100, bold=True)
        draw.text((size//2, size//2), "=", fill='#ecf0f1', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option27.png')
        print("✅ Option 27: +−×÷ (Operations)")
    
    # Option 28: Geometric shapes (triangle, circle, square)
    def create_option28():
        img = Image.new('RGB', (size, size), color='#16202c')
        draw = ImageDraw.Draw(img)
        
        # Triangle (top)
        triangle = [(size//2, 100), (140, 220), (size-140, 220)]
        draw.polygon(triangle, fill='#e74c3c', outline='#c0392b', width=6)
        
        # Circle (bottom left)
        draw.ellipse([80, 280, 240, 440], fill='#3498db', outline='#2980b9', width=6)
        
        # Square (bottom right)
        draw.rectangle([size-240, 280, size-80, 440], fill='#2ecc71', outline='#27ae60', width=6)
        
        # Bottom label
        font_small = get_font(55)
        draw.text((size//2, size-50), "GEOMETRY", fill='#ecf0f1', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option28.png')
        print("✅ Option 28: △○□ (Geometry)")
    
    # Option 29: Calculator/grid style
    def create_option29():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        # Calculator screen
        draw.rectangle([60, 60, size-60, 180], fill='#1a1a2e', outline='#34495e', width=6)
        
        font_screen = get_font(80, bold=True)
        draw.text((size//2, 120), "123.456", fill='#2ecc71', anchor="mm", font=font_screen)
        
        # Button grid
        font_button = get_font(90, bold=True)
        buttons = [
            [(100, 250, "7"), (220, 250, "8"), (340, 250, "9")],
            [(100, 350, "4"), (220, 350, "5"), (340, 350, "6")],
            [(100, 450, "1"), (220, 450, "2"), (340, 450, "3")]
        ]
        
        for row in buttons:
            for x, y, num in row:
                draw.rectangle([x-40, y-40, x+40, y+40], fill='#34495e', outline='#7f8c8d', width=4)
                draw.text((x, y), num, fill='#ecf0f1', anchor="mm", font=font_button)
        
        # Special buttons
        draw.rectangle([size-100-40, 350-40, size-100+40, 350+40], fill='#e74c3c', outline='#c0392b', width=4)
        draw.text((size-100, 350), "=", fill='#ecf0f1', anchor="mm", font=font_button)
        
        img.save('docs/pwa-icon-option29.png')
        print("✅ Option 29: Calculator")
    
    # Option 30: Graph/coordinate system
    def create_option30():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Axes
        draw.line([size//2, 60, size//2, size-60], fill='#ecf0f1', width=8)
        draw.line([60, size//2, size-60, size//2], fill='#ecf0f1', width=8)
        
        # Arrows
        draw.polygon([(size//2-15, 70), (size//2+15, 70), (size//2, 50)], fill='#ecf0f1')
        draw.polygon([(size-70, size//2-15), (size-70, size//2+15), (size-50, size//2)], fill='#ecf0f1')
        
        # Parabola y = x²
        points = []
        for i in range(-6, 7):
            x = size//2 + i * 30
            y = size//2 - (i * i * 5)
            points.append((x, y))
        
        for i in range(len(points)-1):
            draw.line([points[i], points[i+1]], fill='#e74c3c', width=10)
        
        # Labels
        font_small = get_font(60, bold=True)
        draw.text((size-80, size//2 - 50), "x", fill='#3498db', anchor="mm", font=font_small)
        draw.text((size//2 + 50, 70), "y", fill='#2ecc71', anchor="mm", font=font_small)
        
        # Equation
        font_med = get_font(80, bold=True)
        draw.text((size//2 + 150, 150), "y=x²", fill='#f39c12', anchor="mm", font=font_med)
        
        img.save('docs/pwa-icon-option30.png')
        print("✅ Option 30: y=x² (Graph)")
    
    # Generate all options
    print("Generating 10 universal math icon options (512x512)...\n")
    create_option21()
    create_option22()
    create_option23()
    create_option24()
    create_option25()
    create_option26()
    create_option27()
    create_option28()
    create_option29()
    create_option30()
    
    print("\n✅ Created 10 more PWA icon options (21-30)!")
    print("\n🎓 Universal math symbols:")
    print("   21. π (Pi)")
    print("   22. Σ (Sigma summation)")
    print("   23. ∞ (Infinity)")
    print("   24. √(x² + y²) (Square root)")
    print("   25. x² + y = z (Blackboard equations)")
    print("   26. ∫f(x)dx (Integral)")
    print("   27. +−×÷= (Basic operations)")
    print("   28. △○□ (Geometric shapes)")
    print("   29. Calculator (Numbers)")
    print("   30. y=x² (Graph/parabola)")
    print("\nThese will clearly say 'MATH' to anyone!")
    
except ImportError:
    print("⚠️  PIL/Pillow not available")
    print("   Install with: pip install Pillow")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
