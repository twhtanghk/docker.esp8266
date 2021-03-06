log = require "log"
Router = require "router"

class App extends Router
  order: {
    'reqLogger'
    'custom'
    'notFound'
  }

  new: =>
    super()
    table.foreach @order, (k, v) ->
      middleware = require "middleware"
      @use '/', middleware[v]

return App()
