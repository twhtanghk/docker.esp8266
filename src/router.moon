class Router
  new: (ctrls = {}) =>
    @routes = {}
    table.foreach ctrls, (k, v) ->
      ctls = require "controller"
      table.insert @routes, 
        pattern: k
        action: ctls[v.controller][v.action]

  process: (req, res, next) =>
    for i, route in ipairs @routes
      {:pattern, :action} = route
      if "#{req.method} #{req.url}"\find(pattern) != nil
        return action req, res
    if next != nil
      next()

  METHOD: (method, path, mw) =>
    table.insert @routes, 
      pattern: "#{method} #{path}"
      action: mw

  use: (path, mw) =>
    @METHOD '%a+', path, mw

  get: (path, mw) =>
    @METHOD 'GET', path, mw

return Router
