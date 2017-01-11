log = require "log"

class Router
  new: (@routes = {}) =>
    return

  _process: (req, res) ->
    if "#{req.method} #{req.url}" of @routes
      matched = @routes["#{req.method} #{req.url}"]
      log.debug matched
      ctls = require "controller"
      ctls[matched.controller][matched.method](req, res)

  process: (req, res) ->
    res = require('./res.coffee')(res)
    @_process req, res

return Router
