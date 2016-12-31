module.exports =
  identity: (a) ->
    a
  extend: (object, sources) ->
    for k, v of sources
      object[k] = v
    return object
  defaults: (object, sources) ->
    for k, v of sources
      if not k of object
        object[k] = v
    return object
  pick: (object, paths...) ->
    ret = {}
    for i in paths
      ret[i] = object[i]
    return ret
