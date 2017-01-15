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
      first = array\remove 1
      log.debug first
      middleware[first] req, res, ->
        handle array
    handle @@order

return App()