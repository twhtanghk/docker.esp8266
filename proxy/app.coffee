log = require './log.coffee'
Router = require './router.coffee'

class App extends Router
  @order: [
    'reqLogger'
    '$custom'
    '404'
  ]

  _process: (req, res) ->
    middleware = require './middleware.coffee'
    handle = (array) ->
      if array == null
        return
      if array instanceof Array and array.length == 0
        return
      [first, next...] = array
      log.debug first
      middleware[first] req, res, ->
        handle next
    handle App.order

module.exports = new App()
