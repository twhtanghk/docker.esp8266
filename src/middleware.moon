log = require "log"
Router = require "router"
Date = require 'date'

customRouter = Router
  'GET /sys/info':
    controller: 'SysCtrl'
    action: 'info'
  
return {
  reqLogger: (req, res, next) ->
    start = tmr.now()
    res.on 'end', ->
      curr = tmr.now()
      elapsed = (curr - start) / 1000
      log.info "#{start.toString()} #{elapsed}ms #{req.method} #{req.url}"
    next()

  '404': (req, res, next) ->
    if res\headersSent
      return next()
    res\notFound()

  '$custom': (req, res, next) ->
    customRouter\process req, res
    if not res.headersSent
      return next()
}
