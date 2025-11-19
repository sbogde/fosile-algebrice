-- Lua filter to replace tikzcd environments with SVG images
local diagram_counter = 0

function Math(el)
  if el.mathtype == "DisplayMath" then
    local text = el.text
    -- Check if this math block contains tikzcd
    if string.match(text, "\\begin{tikzcd}") then
      local img_path = string.format("diagrams/diagram_%d.svg", diagram_counter)
      diagram_counter = diagram_counter + 1
      
      -- Return raw HTML for the image
      local html = string.format('<p><img src="%s" alt="Commutative diagram" style="max-width: 100%%; height: auto; display: block; margin: 1em auto;"></p>', img_path)
      return pandoc.RawBlock("html", html)
    end
  end
  return el
end

function RawBlock(el)
  if el.format == "latex" then
    if string.match(el.text, "\\begin{tikzcd}") then
      local img_path = string.format("diagrams/diagram_%d.svg", diagram_counter)
      diagram_counter = diagram_counter + 1
      
      local html = string.format('<p><img src="%s" alt="Commutative diagram" style="max-width: 100%%; height: auto; display: block; margin: 1em auto;"></p>', img_path)
      return pandoc.RawBlock("html", html)
    end
  end
  return el
end
