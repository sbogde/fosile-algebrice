#!/bin/bash
# Netlify build script - serves pre-built static files

set -e

echo "================================================"
echo "  Netlify Deployment"
echo "================================================"
echo ""

# Check if pre-built files exist
if [ ! -f "docs/index.html" ]; then
  echo "❌ Error: Pre-built files not found in docs/"
  echo "   Run ./build-website.sh locally first and commit the docs/ folder"
  exit 1
fi

echo "✅ Pre-built website found in docs/"
echo "✅ Ready to deploy!"
echo ""
echo "================================================"
echo "  ✅ Deployment ready!"
echo "================================================"
