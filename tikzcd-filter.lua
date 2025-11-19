-- Lua filter to handle tikzcd environments
function Math(el)
  if el.mathtype == "DisplayMath" then
    local text = el.text
    -- Check if this math block contains tikzcd
    if string.match(text, "\\begin{tikzcd}") then
      -- Replace with a placeholder message styled as a diagram
      return pandoc.RawInline("html", '<div style="border: 1px solid #ccc; padding: 1em; margin: 1em 0; background: #f9f9f9; text-align: center; font-style: italic;">[Commutative diagram - see PDF version]</div>')
    end
  end
  return el
end

function RawBlock(el)
  if el.format == "latex" then
    if string.match(el.text, "\\begin{tikzcd}") then
      return pandoc.RawBlock("html", '<div style="border: 1px solid #ccc; padding: 1em; margin: 1em 0; background: #f9f9f9; text-align: center; font-style: italic;">[Commutative diagram - see PDF version]</div>')
    end
  end
  return el
end
