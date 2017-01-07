class Router
  constructor: ->
    @routes =
      OPTIONS: []
      POST: []
      GET: []
      PUT: []
      DELETE: []

  @order: [
    'reqLogger'
    '$custom'
    'static'
    '404'
  ]

  # opts = ctrl: ctrl, method: method
  METHOD: (method, url, opts) ->
    ret = {}
    ret[url] = opts
    @routes[method].push ret

  all: (url, opts) ->
    @post url, opts
    @get url, opts
    @put url, opts
    @delete url, opts
    @

  options: (url, opts) ->
    @METHOD('OPTIONS', url, opts)
    @

  post: (url, opts) ->
    @METHOD('POST', url, opts)
    @

  get: (url, opts) ->
    @METHOD('GET', url, opts)
    @

  put: (url, opts) ->
    @METHOD('PUT', url, opts)
    @

  'delete': (url, opts) ->
    @METHOD('DELETE', url, opts)
    @

  process: (req, res) ->
    res = require('./res.coffee')(res)
    middleware = require './middleware.coffee'
    handle = (array) ->
      if array == null
        return
      if array instanceof Array and array.length == 0
        return
      [first, next...] = array
      console.log first
      mw = middleware[first]
      mw req, res, ->
        handle next 
    handle Router.order

module.exports = new Router()
