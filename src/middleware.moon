log = require "log"
Router = require "router"

custom = (req, res, next) ->
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

    'PUT /motor/%a+/%d':
      controller: 'MotorCtrl'
      action: 'speed'
  customRouter\process req, res, next
  
reqLogger = (req, res, next) ->
  log.info "#{req.method} #{req.url}"
  next()

notFound = (req, res) ->
  res\notFound()

{ :reqLogger, :notFound, :custom }
