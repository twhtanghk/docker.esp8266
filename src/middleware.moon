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
  log.info "#{req.method} #{req.url}"
  next()

notFound = (req, res) ->
  res\notFound()

custom = (req, res, next) ->
  customRouter\process req, res, next

{ :reqLogger, :notFound, :custom }
