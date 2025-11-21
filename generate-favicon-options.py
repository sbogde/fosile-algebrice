#!/usr/bin/env python3
"""Generate multiple favicon options"""
try:
    from PIL import Image, ImageDraw, ImageFont
    
    size = 64  # Higher resolution for better quality
    
    # Option 1: Module M with dimension arrows
    def create_option1():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", 40)
        except:
            font = None
        
        # Draw M for Module
        draw.text((size//2, size//2), "M", fill='#16C79A', anchor="mm", font=font)
        # Dimension arrows
        draw.line([10, 15, 25, 15], fill='#E94560', width=2)
        draw.polygon([(25, 12), (25, 18), (30, 15)], fill='#E94560')
        img.save('docs/favicon-option1.png')
        print("✅ Created option 1: Module M with arrows")
    
    # Option 2: Ring ⊕ (direct sum)
    def create_option2():
        img = Image.new('RGB', (size, size), color='#2d4059')
        draw = ImageDraw.Draw(img)
        
        # Circle (ring)
        draw.ellipse([12, 12, 52, 52], outline='#ea5455', width=3)
        # Plus inside (direct sum)
        draw.line([32, 20, 32, 44], fill='#f07b3f', width=3)
        draw.line([20, 32, 44, 32], fill='#f07b3f', width=3)
        img.save('docs/favicon-option2.png')
        print("✅ Created option 2: Ring with direct sum")
    
    # Option 3: Infinity symbol (infinite dimension)
    def create_option3():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Infinity symbol using arcs
        draw.arc([8, 20, 28, 44], 90, 270, fill='#16c79a', width=4)
        draw.arc([36, 20, 56, 44], 270, 90, fill='#16c79a', width=4)
        draw.line([28, 26, 36, 38], fill='#16c79a', width=4)
        draw.line([28, 38, 36, 26], fill='#16c79a', width=4)
        img.save('docs/favicon-option3.png')
        print("✅ Created option 3: Infinity symbol")
    
    # Option 4: Abstract module diagram (dots and arrows)
    def create_option4():
        img = Image.new('RGB', (size, size), color='#1e2761')
        draw = ImageDraw.Draw(img)
        
        # Three nodes
        positions = [(16, 16), (48, 16), (32, 48)]
        for pos in positions:
            draw.ellipse([pos[0]-5, pos[1]-5, pos[0]+5, pos[1]+5], fill='#f9a826')
        
        # Arrows between nodes
        draw.line([21, 16, 43, 16], fill='#5d5fef', width=2)
        draw.line([20, 22, 28, 42], fill='#5d5fef', width=2)
        draw.line([44, 22, 36, 42], fill='#5d5fef', width=2)
        img.save('docs/favicon-option4.png')
        print("✅ Created option 4: Abstract module diagram")
    
    # Option 5: Stylized "D" for Dimension
    def create_option5():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 44)
        except:
            font = None
        
        # Large D
        draw.text((size//2, size//2), "D", fill='#ecf0f1', anchor="mm", font=font)
        # Small subscript u for uniform
        try:
            small_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 16)
        except:
            small_font = None
        draw.text((44, 42), "u", fill='#3498db', anchor="mm", font=small_font)
        
        # Decorative arc
        draw.arc([8, 8, 24, 24], 0, 90, fill='#e74c3c', width=2)
        img.save('docs/favicon-option5.png')
        print("✅ Created option 5: D for Dimension")
    
    # Option 6: Mathematical bracket notation [M]
    def create_option6():
        img = Image.new('RGB', (size, size), color='#34495e')
        draw = ImageDraw.Draw(img)
        
        # Left bracket
        draw.line([15, 12, 15, 52], fill='#f39c12', width=3)
        draw.line([15, 12, 20, 12], fill='#f39c12', width=3)
        draw.line([15, 52, 20, 52], fill='#f39c12', width=3)
        
        # Right bracket
        draw.line([49, 12, 49, 52], fill='#f39c12', width=3)
        draw.line([44, 12, 49, 12], fill='#f39c12', width=3)
        draw.line([44, 52, 49, 52], fill='#f39c12', width=3)
        
        # M inside
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Times New Roman.ttf", 30)
        except:
            font = None
        draw.text((size//2, size//2), "M", fill='#ecf0f1', anchor="mm", font=font)
        
        img.save('docs/favicon-option6.png')
        print("✅ Created option 6: Bracketed M")
    
    # Generate all options
    create_option1()
    create_option2()
    create_option3()
    create_option4()
    create_option5()
    create_option6()
    
    print("\n✅ Created 6 favicon options!")
    print("Preview them and choose your favorite")
    
except ImportError:
    print("⚠️  PIL/Pillow not available")
    print("   Install with: pip install Pillow")
