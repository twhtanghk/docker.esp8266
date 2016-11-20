ln = (x) ->
  ret = 0
  last = (x - 1) / (x + 1)
  sq = last * last
  for i = 1, 10000, 2
    ret += (1 / i) * last
    last *= sq
  return 2 * ret

return ln
