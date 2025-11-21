#!/bin/bash
# Netlify build script - HTML only (no PDF compilation)

set -e

# Path to the LaTeX source
LATEX_SOURCE="../antiques-roadshow-algebra-ro/main.tex"

echo "================================================"
echo "  Building Website for Netlify"
echo "================================================"
echo ""

# Check if LaTeX source exists
if [ ! -f "$LATEX_SOURCE" ]; then
  echo "❌ Error: LaTeX source not found at $LATEX_SOURCE"
  exit 1
fi

# Create docs directory
echo "Creating output directory..."
mkdir -p docs
mkdir -p docs/diagrams
echo "✅ Directory created"
echo ""

# Copy pre-generated diagrams if they exist locally
# (You'll need to commit these to the repo)
if [ -d "docs/diagrams" ] && [ "$(ls -A docs/diagrams/*.svg 2>/dev/null)" ]; then
  echo "✅ Using pre-generated diagrams"
else
  echo "⚠️  Warning: No pre-generated diagrams found"
  echo "   Run ./build-website.sh locally first and commit docs/diagrams/*.svg"
fi
echo ""

# Convert to HTML
echo "Converting LaTeX to HTML with pandoc..."
pandoc "$LATEX_SOURCE" \
  --standalone \
  --mathjax \
  --toc \
  --toc-depth=2 \
  --css=style.css \
  --lua-filter=tikzcd-filter.lua \
  -o docs/index.html

echo "✅ HTML generated: docs/index.html"
echo ""

# Copy CSS if it exists
if [ -f "docs/style.css" ]; then
  echo "✅ CSS file found"
fi

echo "================================================"
echo "  ✅ Netlify build complete!"
echo "================================================"
