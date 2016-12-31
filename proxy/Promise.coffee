_ = require './lodash.coffee'

Promise
  .mapSeries = (array, mapper = _.identity) ->
    if array == null
      return Promise.resolve null
    if array instanceof Array and array.length == 0
      return Promise.resolve []
    ret = []
    [first, next...] = array
    Promise
      .resolve first
      .then (firstValue) ->
        ret.push mapper first
      .then ->
        Promise.mapSeries next, mapper
      .then (nextValue) ->
        ret.concat nextValue

module.exports = Promise
