log = require "log"
Router = require "router"

cdr = (array) ->
  ret = {}
  for i = 2, #array
    table.insert ret, array[i]
  ret

class App extends Router
  @order: {
    'reqLogger'
    'custom'
    'notFound'
  }

  _process: (req, res) =>
    handle = (array) ->
      if array == nil or #array == 0
        return
      middleware = require "middleware"
      middleware[array[1]] req, res, ->
        handle cdr array
    handle @@order

return App()
