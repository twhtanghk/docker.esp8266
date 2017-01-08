LEVEL =
  debug: 0
  error: 1
  info: 2
  verbose: 3

dflLevel = 'debug'

log = (level, msg) ->
  if LEVEL[level] >= LEVEL[dflLevel]
    console.log msg

module.exports =
  debug: (msg) ->
    log 'debug', msg
  error: (msg) ->
    log 'error', msg
  info: (msg) ->
    log 'info', msg
  verbose: (msg) ->
    log 'verbose', msg
