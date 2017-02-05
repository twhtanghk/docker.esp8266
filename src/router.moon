log = require "log"

class Router
  new: (@routes = {}) =>
    return

  _process: (req, res) =>
    matched = @router["#{req.method} #{req.url}"] != nil
    if matched != nil
      log.debug matched
      ctls = require "controller"
      ctls[matched.controller][matched.method](req, res)

  process: (req, res) =>
    @_process req, res

return Router
