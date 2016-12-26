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
  
routes =
  'all *':
    ctrl: ctrls.sys
    method: 'bodyParser'
  'all *':
    ctrl: ctrls.sys
    method: 'dumpReq'
  'get /index.html':
    ctrl: ctrls.sys
    method: 'templates'
  'get /index.js':
    ctrl: ctrls.sys
    method: 'templates'
  'get /sys/status':
    ctrl: ctrls.sys
    method: 'status'
  'put /sys/reset':
    ctrl: ctrls.sys
    method: 'reset'
  'get /sys/ap':
    ctrl: ctrls.ap
    method: 'findOne'
  'put /sys/ap':
    ctrl: ctrls.ap
    method: 'update'
  'get /sys/sta':
    ctrl: ctrls.sta
    method: 'findOne'
  'get /sys/sta/aplist':
    ctrl: ctrls.sta
    method: 'find'

router = new Router()

for route, opts of routes
  [method, url] = route.split(' ')
  router[method](url, opts)
