class Router
  constructor: ->
    @routes =
      POST: {}
      GET: {}
      PUT: {}
      DELETE: {}

  # opts = ctrl: ctrl, method: method
  METHOD: (method, url, opts) ->
    @routes[method][url] = opts

  post: (url, opts) ->
    @METHOD('POST', url, opts)

  get: (url, opts) ->
    @METHOD('GET', url, opts)

  put: (url, opts) ->
    @METHOD('PUT', url, opts)

  'delete': (url, opts) ->
    @METHOD('DELETE', url, opts)

  process: (req, res) ->
    for url, opts of @routes[req.method]
      if url == req.url
        ctrl = opts.ctrl
        return ctrl[opts.method].call ctrl, req, res
    Ctrl.notFound res
  
router = new Router()

router.get '/ap', 
  ctrl: ap
  method: 'findOne'
router.get '/sta',
  ctrl: sta
  method: 'findOne'
router.get '/sta/aplist', 
  ctrl: sta
  method: 'find'
