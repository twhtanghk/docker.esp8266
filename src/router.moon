class Router
  new: (ctrls = {}) =>
    @routes = {}
    table.foreach ctrls, (k, v) ->
      ctls = require "controller"
      table.insert @routes, 
        pattern: k
        action: ctls[v.controller][v.action]

  process: (req, res, next) =>
    nextRoute = @iter()
    cb = ->
      route = nextRoute()
      if route == nil
        if next != nil
          next()
      else
        {:pattern, :action} = route
        if "#{req.method} #{req.url}"\find(pattern) != nil
          action req, res, cb
        else
          cb()
    cb()

  iter: =>
    index = 0
    count = #@routes
    return ->
      index = index + 1
      if index <= count
        @routes[index]

  METHOD: (method, path, mw) =>
    table.insert @routes, 
      pattern: "#{method} #{path}"
      action: mw

  use: (path, mw) =>
    @METHOD '%a+', path, mw

  get: (path, mw) =>
    @METHOD 'GET', path, mw

return Router
