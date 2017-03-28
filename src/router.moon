log = require "log"
ctls = require "controller"

cdr = (array) ->
  ret = {}
  for i = 2, #array
    table.insert ret, array[i]
  ret

class Router
  routes: {}

  new: (ctrls = {}) =>
    table.foreach ctrls, (k, v) ->
      log.debug k
      entry = {}
      entry[k] = (req, res) ->
        ctls[v.controller][v.action](req, res)
      table.insert @routes, entry

  process: (req, res) =>
    handle = (array) ->
      if array == nil or #array == 0
        return
      matched = @routes[1]["#{req.method} #{req.url}"]
      table.foreach @routes[1], (k, v) ->
        log.debug "#{#array} #{k}"
      if matched != nil
        @matched req, res, ->
          handle cdr array
      else
        handle cdr array
    handle @routes

  METHOD: (method, path, mw) =>
    table.insert @routes, "#{method} #{path}": mw

  use: (path, mw) =>
    @METHOD 'GET', path, mw

  get: (path, mw) =>
    @METHOD 'GET', path, mw

return Router
