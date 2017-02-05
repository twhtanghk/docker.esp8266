log = require "log"
Router = require "router"

class App extends Router
  @order: {
    'reqLogger'
    '$custom'
    '404'
  }

  _process: (req, res) =>
    middleware = require "middleware"
    handle = (array) ->
      if array == nil or #array == 0
        return
      log.debug cjson.encode array
      first = table.remove array
      log.debug first
      middleware[first] req, res, ->
        log.debug array
        handle array
    handle @@order

return App()
