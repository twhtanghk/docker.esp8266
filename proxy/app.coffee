class Router
  constructor: ->
    @middlewares = []
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

  use: (middleware) ->
    @middlewares.push middleware
    @
    
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
    for mw in @middlewares
      mw req, res
    for handler in @routes[req.method]
      for url, opts of handler
        func = ->
          ctrl = opts.ctrl
          ctrl[opts.method].call ctrl, req, res
          func()
          processed = true
    if not processed
      Ctrl.notFound res
    @
  
module.exports = new Router()
