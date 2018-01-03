class Router
  routes: {}

  new: (ctrls = {}) =>
    table.foreach ctrls, (k, v) ->
      ctls = require "controller"
      @routes[k] = ctls[v.controller][v.action]

  process: (req, res, next) =>
    for pattern, func in pairs @routes
      if "#{req.method} #{req.url}"\find(pattern) != nil
        return func req, res
    if next != nil
      next()

  METHOD: (method, path, mw) =>
    table.insert @routes, "#{method} #{path}": mw

  use: (path, mw) =>
    @METHOD 'GET', path, mw

  get: (path, mw) =>
    @METHOD 'GET', path, mw

return Router
