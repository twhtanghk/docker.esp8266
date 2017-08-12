class Router
  routes: {}

  new: (ctrls = {}) =>
    table.foreach ctrls, (k, v) ->
      ctls = require "controller"
      @routes[k] = ctls[v.controller][v.action]

  process: (req, res, next) =>
    if @routes["#{req.method} #{req.url}"] != nil
      @routes["#{req.method} #{req.url}"](req, res)
    else
      if next != nil
        next()

  METHOD: (method, path, mw) =>
    table.insert @routes, "#{method} #{path}": mw

  use: (path, mw) =>
    @METHOD 'GET', path, mw

  get: (path, mw) =>
    @METHOD 'GET', path, mw

return Router
