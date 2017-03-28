log = require "log"
Router = require "router"
middleware = require "middleware"

class App extends Router
  order: {
    'reqLogger'
    'custom'
    'notFound'
  }

  new: =>
    table.foreach @order, (k, v) ->
      @use '/', middleware[v]

return App()
