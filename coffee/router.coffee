ctrls = require './controller.coffee'

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
    
  all: (url, opts) ->
    @post url, opts
    @get url, opts
    @put url, opts
    @delete url, opts

  options: (url, opts) ->
    @METHOD('OPTIONS', url, opts)

  post: (url, opts) ->
    @METHOD('POST', url, opts)

  get: (url, opts) ->
    @METHOD('GET', url, opts)

  put: (url, opts) ->
    @METHOD('PUT', url, opts)

  'delete': (url, opts) ->
    @METHOD('DELETE', url, opts)

  process: (req, res) ->
    for handler in @routes[req.method]
      for url, opts of handler
        func = ->
          ctrl = opts.ctrl
          ctrl[opts.method].call ctrl, req, res
          func()
          processed = true
    if not processed
      Ctrl.notFound res
  
routes =
  'options *':
    ctrl: ctrls.sys
    method: 'cors'
  'all *':
    ctrl: ctrls.sys
    method: 'bodyParser'
  'get /index.html':
    ctrl: ctrls.sys
    method: 'templates'
  'get /index.js':
    ctrl: ctrls.sys
    method: 'templates'
  'get /sys/info':
    ctrl: ctrls.sys.info
    method: 'findOne'
  'put /sys/info':
    ctrl: ctrls.sys.info
    method: 'update'
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

module.exports = router
