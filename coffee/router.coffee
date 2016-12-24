class Router
  constructor: ->
    @routes =
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

  post: (url, opts) ->
    @METHOD('POST', url, opts)

  get: (url, opts) ->
    @METHOD('GET', url, opts)

  put: (url, opts) ->
    @METHOD('PUT', url, opts)

  'delete': (url, opts) ->
    @METHOD('DELETE', url, opts)

  process: (req, res) ->
    processed = false
    for handler in @routes[req.method]
      for url, opts of handler
        func = ->
          ctrl = opts.ctrl
          ctrl[opts.method].call ctrl, req, res
        if url == '*'
          func()
        if url == req.url
          func()
          processed = true
    if not processed
      Ctrl.notFound res
  
router = new Router()

router.all '*',
  ctrl: sys
  method: 'bodyParser'
router.all '*',
  ctrl: sys
  method: 'dumpReq'
router.get '/ap', 
  ctrl: ap
  method: 'findOne'
router.get '/sta',
  ctrl: sta
  method: 'findOne'
router.get '/sta/aplist', 
  ctrl: sta
  method: 'find'
