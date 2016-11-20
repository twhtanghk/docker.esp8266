split = (str, delim = "\r\n") ->
  result, pat, lastPos = {}, "(.-)#{delim}()", 1
  for part, pos in string.gfind(str, pat) do
    table.insert(result, part)
    lastPos = pos
  table.insert(result, string.sub(str, lastPos))
  return result

join = (strs, delim = ", ") ->
  table.concat strs, delim

return {
  split: split
  join: join
}
