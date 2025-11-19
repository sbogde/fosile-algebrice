#!/usr/bin/env python3
"""Extract TikZ diagrams from LaTeX and convert to SVG"""
import re
import subprocess
import os
import sys

def extract_tikzcd_diagrams(latex_file):
    """Extract all tikzcd environments from LaTeX file"""
    with open(latex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all tikzcd environments (including those in math mode)
    pattern = r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    return diagrams

def create_standalone_tex(diagram, index, output_dir):
    """Create a standalone LaTeX file for a single diagram"""
    tex_content = r"""\documentclass[tikz,border=2pt]{standalone}
\usepackage{tikz-cd}
\begin{document}
""" + diagram + r"""
\end{document}
"""
    
    tex_file = os.path.join(output_dir, f'diagram_{index}.tex')
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(tex_content)
    
    return tex_file

def compile_to_svg(tex_file, pdflatex_path):
    """Compile LaTeX to PDF then convert to SVG"""
    base_name = tex_file.replace('.tex', '')
    
    # Compile to PDF
    subprocess.run([pdflatex_path, '-interaction=nonstopmode', tex_file],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   cwd=os.path.dirname(tex_file))
    
    pdf_file = base_name + '.pdf'
    svg_file = base_name + '.svg'
    
    # Convert PDF to SVG using pdf2svg or dvisvgm
    if os.path.exists(pdf_file):
        # Try pdf2svg first
        try:
            subprocess.run(['pdf2svg', pdf_file, svg_file],
                          check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to dvisvgm via PDF
            try:
                subprocess.run(['dvisvgm', '--pdf', pdf_file, '-o', svg_file],
                              check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"Warning: Could not convert {pdf_file} to SVG. Install pdf2svg or dvisvgm.")
                return None
    
    return svg_file if os.path.exists(svg_file) else None

def main():
    if len(sys.argv) < 3:
        print("Usage: extract-tikz.py <latex_file> <pdflatex_path>")
        sys.exit(1)
    
    latex_file = sys.argv[1]
    pdflatex_path = sys.argv[2]
    
    # Create output directory
    output_dir = 'docs/diagrams'
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract diagrams
    diagrams = extract_tikzcd_diagrams(latex_file)
    print(f"Found {len(diagrams)} TikZ diagrams")
    
    # Process each diagram
    for i, diagram in enumerate(diagrams):
        print(f"Processing diagram {i+1}/{len(diagrams)}...")
        tex_file = create_standalone_tex(diagram, i, output_dir)
        svg_file = compile_to_svg(tex_file, pdflatex_path)
        
        if svg_file:
            print(f"  Created {svg_file}")
        
        # Clean up intermediate files
        for ext in ['.tex', '.pdf', '.aux', '.log']:
            try:
                os.remove(tex_file.replace('.tex', ext))
            except FileNotFoundError:
                pass
    
    print(f"Done! Created {len(diagrams)} diagrams in {output_dir}/")

if __name__ == '__main__':
    main()
