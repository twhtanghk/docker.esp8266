log = require "log"
Router = require "router"

customRouter = Router
  'GET /sys/wifi':
    controller: 'SysCtrl'
    action: 'wifi'

  'GET /sys/reset':
    controller: 'SysCtrl'
    action: 'reset'

  'GET /sys/heap':
    controller: 'SysCtrl'
    action: 'heap'
  
reqLogger = (req, res, next) ->
  start = tmr.now()
  res.client\on 'sent', ->
    curr = tmr.now()
    elapsed = (curr - start) / 1000
    log.info "#{res.statusCode} #{elapsed}ms #{req.method} #{req.url}"
    res.client\close()
  next()

notFound = (req, res, next) ->
  res\notFound()
  next()

custom = (req, res, next) ->
  customRouter\process req, res
  next()

{ :reqLogger, :notFound, :custom }
