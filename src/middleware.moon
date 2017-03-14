log = require "log"
Router = require "router"
Date = require 'date'

customRouter = Router
  'GET /sys/info':
    controller: 'SysCtrl'
    action: 'info'

  'GET /reset':
    controller: 'SysCtrl'
    action: 'reset'
  
reqLogger = (req, res, next) ->
  start = tmr.now()
  res.client\on 'sent', ->
    curr = tmr.now()
    elapsed = (curr - start) / 1000
    log.info "#{elapsed}ms #{req.method} #{req.url}"
    res.client\close()
  next()

notFound = (req, res, next) ->
  res\notFound()
  next()

custom = (req, res, next) ->
  customRouter\process req, res
  next()

{ :reqLogger, :notFound, :custom }
