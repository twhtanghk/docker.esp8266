log = require "log"
Router = require "router"

class App extends Router
  order: {
    'custom'
    'notFound'
  }

  new: =>
    table.foreach @order, (k, v) ->
      middleware = require "middleware"
      @use '/', middleware[v]

return App()
