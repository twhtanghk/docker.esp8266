LEVEL =
  debug: 0
  error: 1
  info: 2

dflLevel = 'debug'

log = (level, msg) ->
  if LEVEL[level] >= LEVEL[dflLevel]
    print msg

return { 
  debug: (msg) ->
    log 'debug', msg
  info: (msg) ->
    log 'info', msg
  error: (msg) ->
    log 'error', msg
}
