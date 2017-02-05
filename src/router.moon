log = require "log"

class Router
  new: (@routes = {}) =>
    return

  _process: (req, res) =>
    matched = @routes["#{req.method} #{req.url}"]
    if matched != nil
      ctls = require "controller"
      ctls[matched.controller][matched.action](req, res)

  process: (req, res) =>
    @_process req, res

return Router
