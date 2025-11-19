#!/bin/bash
# Build script for LaTeX to Website conversion

set -e  # Exit on error

# Path to the LaTeX source
LATEX_SOURCE="../antiques-roadshow-algebra-ro/main.tex"

echo "================================================"
echo "  LaTeX to Website Builder"
echo "================================================"
echo ""

# Check if LaTeX source exists
if [ ! -f "$LATEX_SOURCE" ]; then
  echo "❌ Error: LaTeX source not found at $LATEX_SOURCE"
  exit 1
fi

# Check for required tools
echo "Checking dependencies..."
command -v pandoc >/dev/null 2>&1 || { 
  echo "❌ Error: pandoc is not installed."
  echo "   Install with: brew install pandoc"
  exit 1
}

command -v pdflatex >/dev/null 2>&1 || { 
  echo "❌ Error: pdflatex is not installed."
  echo "   Install with: brew install --cask mactex"
  exit 1
}

echo "✅ All dependencies found"
echo ""

# Create docs directory
echo "Creating output directory..."
mkdir -p docs
echo "✅ Directory created"
echo ""

# Compile PDF (in the source directory)
echo "Compiling LaTeX to PDF..."
cd ../antiques-roadshow-algebra-ro
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1
pdflatex -interaction=nonstopmode main.tex > /dev/null 2>&1  # Second pass for references
cd - > /dev/null

if [ -f ../antiques-roadshow-algebra-ro/main.pdf ]; then
  cp ../antiques-roadshow-algebra-ro/main.pdf docs/thesis.pdf
  echo "✅ PDF generated: docs/thesis.pdf"
else
  echo "⚠️  Warning: PDF generation may have failed"
fi
echo ""

# Convert to HTML
echo "Converting LaTeX to HTML with pandoc..."
pandoc "$LATEX_SOURCE" \
  --standalone \
  --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js \
  --toc \
  --toc-depth=2 \
  --css=style.css \
  --from=latex+raw_tex \
  --metadata header-includes='<script src="https://tikzjax.com/v1/tikzjax.js"></script>' \
  -o docs/index.html

echo "✅ HTML generated: docs/index.html"
echo ""

# Clean up auxiliary files in the LaTeX source directory
echo "Cleaning up LaTeX auxiliary files..."
cd ../antiques-roadshow-algebra-ro
rm -f *.aux *.log *.toc *.out
cd - > /dev/null
echo "✅ Cleanup complete"
echo ""

echo "================================================"
echo "  ✅ Website build complete!"
echo "================================================"
echo ""
echo "Output location: docs/"
echo "  • HTML: docs/index.html"
echo "  • PDF:  docs/thesis.pdf"
echo ""
echo "To preview locally, run:"
echo "  cd docs && python3 -m http.server 8000"
echo ""
echo "Then open: http://localhost:8000"
echo ""
