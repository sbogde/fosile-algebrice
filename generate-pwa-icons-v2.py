#!/usr/bin/env python3
"""Generate 10 more PWA icon options focused on algebraic symbols (512x512)"""
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
    
    # Option 11: Submodule ⊆ with N ⊆ M
    def create_option11():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        # Large subset symbol
        draw.arc([100, 140, size-100, size-140], 90, 270, fill='#3498db', width=35)
        draw.line([150, size-140, size-150, size-140], fill='#3498db', width=35)
        
        font_huge = get_font(180, bold=True)
        font_large = get_font(140, bold=True)
        
        # N ⊆ M
        draw.text((170, 200), "N", fill='#e74c3c', anchor="mm", font=font_large)
        draw.text((size-170, 200), "M", fill='#2ecc71', anchor="mm", font=font_huge)
        
        # Bottom label
        font_small = get_font(60)
        draw.text((size//2, size-80), "submodule", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option11.png')
        print("✅ Option 11: N ⊆ M submodule")
    
    # Option 12: Ideal ◁ symbol with I ◁ R
    def create_option12():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        # Large triangular ideal symbol
        points = [(size//2 + 80, size//2 - 100), 
                 (size//2 + 80, size//2 + 100), 
                 (size//2 - 120, size//2)]
        draw.polygon(points, outline='#f39c12', width=30)
        draw.line([size//2 - 120, size//2 - 120, size//2 - 120, size//2 + 120], 
                 fill='#f39c12', width=30)
        
        font_huge = get_font(200, bold=True)
        font_large = get_font(150, bold=True)
        
        # I ◁ R
        draw.text((140, 120), "I", fill='#e67e22', anchor="mm", font=font_large)
        draw.text((size-120, 120), "R", fill='#9b59b6', anchor="mm", font=font_huge)
        
        # Bottom label
        font_small = get_font(60)
        draw.text((size//2, size-80), "ideal", fill='#bdc3c7', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option12.png')
        print("✅ Option 12: I ◁ R ideal")
    
    # Option 13: Quotient R/I with division bar
    def create_option13():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(220, bold=True)
        font_large = get_font(180, bold=True)
        
        # R over I with thick division bar
        draw.text((size//2, 150), "R", fill='#ecf0f1', anchor="mm", font=font_huge)
        draw.line([80, size//2, size-80, size//2], fill='#e74c3c', width=25)
        draw.text((size//2, size-150), "I", fill='#3498db', anchor="mm", font=font_large)
        
        # Corner decorations - quotient symbols
        font_small = get_font(70)
        draw.text((100, 100), "~", fill='#f39c12', anchor="mm", font=font_small)
        draw.text((size-100, 100), "~", fill='#f39c12', anchor="mm", font=font_small)
        draw.text((100, size-100), "≡", fill='#16c79a', anchor="mm", font=font_small)
        draw.text((size-100, size-100), "≡", fill='#16c79a', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option13.png')
        print("✅ Option 13: R/I quotient")
    
    # Option 14: Homomorphism φ: R → S with arrow
    def create_option14():
        img = Image.new('RGB', (size, size), color='#16202c')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(200, bold=True)
        font_med = get_font(140, bold=True)
        
        # R → S
        draw.text((130, size//2), "R", fill='#3498db', anchor="mm", font=font_huge)
        draw.text((size-130, size//2), "S", fill='#2ecc71', anchor="mm", font=font_huge)
        
        # Arrow
        arrow_y = size//2
        draw.line([210, arrow_y, size-210, arrow_y], fill='#e74c3c', width=20)
        draw.polygon([(size-210, arrow_y-25), (size-210, arrow_y+25), (size-170, arrow_y)], 
                    fill='#e74c3c')
        
        # φ above arrow
        draw.text((size//2, size//2 - 100), "φ", fill='#f39c12', anchor="mm", font=font_med)
        
        # Bottom label
        font_small = get_font(55)
        draw.text((size//2, size-70), "homomorphism", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option14.png')
        print("✅ Option 14: φ: R → S homomorphism")
    
    # Option 15: Isomorphism R ≅ S
    def create_option15():
        img = Image.new('RGB', (size, size), color='#1e2761')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(220, bold=True)
        
        # R ≅ S
        draw.text((120, size//2), "R", fill='#e74c3c', anchor="mm", font=font_huge)
        draw.text((size-120, size//2), "S", fill='#e74c3c', anchor="mm", font=font_huge)
        
        # ≅ symbol (three lines with curves)
        center_x = size//2
        center_y = size//2
        
        # Top wave
        y1 = center_y - 50
        draw.arc([center_x-80, y1-15, center_x-40, y1+15], 180, 0, fill='#16c79a', width=12)
        draw.arc([center_x-40, y1-15, center_x, y1+15], 0, 180, fill='#16c79a', width=12)
        draw.arc([center_x, y1-15, center_x+40, y1+15], 180, 0, fill='#16c79a', width=12)
        draw.arc([center_x+40, y1-15, center_x+80, y1+15], 0, 180, fill='#16c79a', width=12)
        
        # Bottom wave
        y2 = center_y + 50
        draw.arc([center_x-80, y2-15, center_x-40, y2+15], 180, 0, fill='#16c79a', width=12)
        draw.arc([center_x-40, y2-15, center_x, y2+15], 0, 180, fill='#16c79a', width=12)
        draw.arc([center_x, y2-15, center_x+40, y2+15], 180, 0, fill='#16c79a', width=12)
        draw.arc([center_x+40, y2-15, center_x+80, y2+15], 0, 180, fill='#16c79a', width=12)
        
        # Middle line
        draw.line([center_x-80, center_y, center_x+80, center_y], fill='#16c79a', width=12)
        
        # Bottom label
        font_small = get_font(55)
        draw.text((size//2, size-70), "isomorphism", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option15.png')
        print("✅ Option 15: R ≅ S isomorphism")
    
    # Option 16: Direct sum ⊕ with modules
    def create_option16():
        img = Image.new('RGB', (size, size), color='#2d4059')
        draw = ImageDraw.Draw(img)
        
        # Large circle
        draw.ellipse([100, 100, size-100, size-100], outline='#ea5455', width=18)
        
        # Plus inside
        draw.line([size//2, 160, size//2, size-160], fill='#f9a826', width=30)
        draw.line([160, size//2, size-160, size//2], fill='#f9a826', width=30)
        
        # Modules in corners
        font_large = get_font(110, bold=True)
        positions = [(110, 110), (size-110, 110), (110, size-110), (size-110, size-110)]
        labels = ["M₁", "M₂", "M₃", "M₄"]
        
        for pos, label in zip(positions, labels):
            draw.text(pos, label[0], fill='#3498db', anchor="mm", font=font_large)
        
        # Bottom label
        font_small = get_font(60)
        draw.text((size//2, size-60), "direct sum", fill='#bdc3c7', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option16.png')
        print("✅ Option 16: M₁⊕M₂⊕M₃⊕M₄ direct sum")
    
    # Option 17: Tensor product ⊗
    def create_option17():
        img = Image.new('RGB', (size, size), color='#0f3460')
        draw = ImageDraw.Draw(img)
        
        # Large circle
        draw.ellipse([100, 100, size-100, size-100], outline='#16c79a', width=18)
        
        # X inside (tensor symbol)
        draw.line([180, 180, size-180, size-180], fill='#f39c12', width=30)
        draw.line([180, size-180, size-180, 180], fill='#f39c12', width=30)
        
        # Modules
        font_large = get_font(140, bold=True)
        draw.text((150, 140), "M", fill='#e74c3c', anchor="mm", font=font_large)
        draw.text((size-150, 140), "N", fill='#3498db', anchor="mm", font=font_large)
        
        # Bottom label
        font_small = get_font(60)
        draw.text((size//2, size-60), "tensor product", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option17.png')
        print("✅ Option 17: M ⊗ N tensor product")
    
    # Option 18: Kernel ker(φ) with arrow going to zero
    def create_option18():
        img = Image.new('RGB', (size, size), color='#1a1a2e')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(180, bold=True)
        font_large = get_font(140, bold=True)
        
        # ker
        draw.text((size//2, 120), "ker", fill='#e74c3c', anchor="mm", font=font_large)
        
        # Arrow down
        draw.line([size//2, 200, size//2, 340], fill='#3498db', width=20)
        draw.polygon([(size//2-25, 340), (size//2+25, 340), (size//2, 380)], 
                    fill='#3498db')
        
        # 0 at bottom
        draw.text((size//2, size-90), "0", fill='#2ecc71', anchor="mm", font=font_huge)
        
        # Decorative elements
        draw.ellipse([size//2-60, size-150, size//2+60, size-30], 
                    outline='#f39c12', width=8)
        
        img.save('docs/pwa-icon-option18.png')
        print("✅ Option 18: ker(φ) → 0 kernel")
    
    # Option 19: Exact sequence with arrows
    def create_option19():
        img = Image.new('RGB', (size, size), color='#2c3e50')
        draw = ImageDraw.Draw(img)
        
        font_large = get_font(120, bold=True)
        
        # Vertical exact sequence: 0 → A → B → C → 0
        y_positions = [80, 160, 280, 400, 480]
        labels = ["0", "A", "B", "C", "0"]
        colors = ['#2ecc71', '#e74c3c', '#3498db', '#f39c12', '#2ecc71']
        
        for i, (y, label, color) in enumerate(zip(y_positions, labels, colors)):
            draw.text((size//2, y), label, fill=color, anchor="mm", font=font_large)
            
            # Arrows between
            if i < len(y_positions) - 1:
                y_start = y + 40
                y_end = y_positions[i+1] - 40
                draw.line([size//2, y_start, size//2, y_end], fill='#16c79a', width=15)
                draw.polygon([(size//2-20, y_end), (size//2+20, y_end), (size//2, y_end+30)], 
                           fill='#16c79a')
        
        # Side label
        font_small = get_font(55)
        draw.text((size-80, size//2), "exact", fill='#95a5a6', anchor="mm", font=font_small, angle=90)
        
        img.save('docs/pwa-icon-option19.png')
        print("✅ Option 19: 0→A→B→C→0 exact sequence")
    
    # Option 20: Generator ⟨g⟩ with brackets
    def create_option20():
        img = Image.new('RGB', (size, size), color='#16202c')
        draw = ImageDraw.Draw(img)
        
        font_huge = get_font(280, bold=True)
        
        # Large angle brackets
        draw.line([100, size//2-150, 160, size//2], fill='#3498db', width=25)
        draw.line([160, size//2, 100, size//2+150], fill='#3498db', width=25)
        
        draw.line([size-100, size//2-150, size-160, size//2], fill='#3498db', width=25)
        draw.line([size-160, size//2, size-100, size//2+150], fill='#3498db', width=25)
        
        # g inside
        draw.text((size//2, size//2), "g", fill='#e74c3c', anchor="mm", font=font_huge)
        
        # Bottom label
        font_small = get_font(60)
        draw.text((size//2, size-70), "generator", fill='#95a5a6', anchor="mm", font=font_small)
        
        img.save('docs/pwa-icon-option20.png')
        print("✅ Option 20: ⟨g⟩ generator")
    
    # Generate all options
    print("Generating 10 more algebraic PWA icon options (512x512)...\n")
    create_option11()
    create_option12()
    create_option13()
    create_option14()
    create_option15()
    create_option16()
    create_option17()
    create_option18()
    create_option19()
    create_option20()
    
    print("\n✅ Created 10 more PWA icon options (11-20)!")
    print("\n📋 Algebraic concepts covered:")
    print("   11. N ⊆ M (submodule)")
    print("   12. I ◁ R (ideal)")
    print("   13. R/I (quotient)")
    print("   14. φ: R → S (homomorphism)")
    print("   15. R ≅ S (isomorphism)")
    print("   16. M₁⊕M₂⊕M₃⊕M₄ (direct sum)")
    print("   17. M ⊗ N (tensor product)")
    print("   18. ker(φ) → 0 (kernel)")
    print("   19. 0→A→B→C→0 (exact sequence)")
    print("   20. ⟨g⟩ (generator)")
    print("\nPreview them and choose your favorite!")
    
except ImportError:
    print("⚠️  PIL/Pillow not available")
    print("   Install with: pip install Pillow")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
