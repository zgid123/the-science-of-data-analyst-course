-- Pandoc filter applied by build_report.py to every report build.
-- House style: en dash instead of em dash; ordered lists numbered (1), (2), (3) …
-- Code and math are left untouched (Str elements only; OrderedList attributes only).
-- Figures: a build in language L uses figure.L.png beside figure.png when it exists (labels drawn in L).

function Str(el)
  if el.text:find("—", 1, true) then
    el.text = el.text:gsub("—", "–")
  end
  return el
end

function OrderedList(el)
  el.listAttributes = pandoc.ListAttributes(el.listAttributes.start, "Decimal", "TwoParens")
  return el
end

local figure_lang = nil

function Meta(meta)
  if meta.figure_lang then figure_lang = pandoc.utils.stringify(meta.figure_lang) end
end

function Image(el)
  if figure_lang and el.src:match("%.png$") then
    local localized = el.src:gsub("%.png$", "." .. figure_lang .. ".png")
    local f = io.open(localized, "r")
    if f then f:close(); el.src = localized end
  end
  return el
end

return {{Meta = Meta}, {Str = Str, OrderedList = OrderedList, Image = Image}}
