_.extend Promise,
  mapSeries = (array, mapper) ->
    [first, next...] = array
    if not first?
      return null
    if first instanceof Promise
      first
        .then (firstValue) ->
          ret.push firstValue
        .catch Promise.reject
    else
      ret.push mapper first
    if next?
      Promise.mapSeries.apply next, mapper
        .then (nextValue) ->
          ret.concat nextValue
    else
      Promise.resolve ret
