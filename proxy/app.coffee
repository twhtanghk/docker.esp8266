class Router
  constructor: ->
    @routes =
      OPTIONS: []
      POST: []
      GET: []
      PUT: []
      DELETE: []

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
    for name in middleware.order
      middleware[name](req, res)

module.exports = new Router()
