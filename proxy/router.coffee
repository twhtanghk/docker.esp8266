log = require './log.coffee'

class Router
  constructor: (@routes = {}) ->
    return

  _process: (req, res) ->
    if "#{req.method} #{req.url}" of @routes
      matched = @routes["#{req.method} #{req.url}"]
      log.debug matched
      controller = require './controller.coffee'
      controller[matched.controller][matched.method](req, res)

  process: (req, res) ->
    res = require('./res.coffee')(res)
    @_process req, res

module.exports = Router
