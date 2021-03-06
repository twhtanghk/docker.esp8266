log = require './log.coffee'
Router = require './router.coffee'

customRouter = new Router
  'GET /sys/info':
    controller: 'SysCtrl'
    method: 'info'
  
module.exports =
  reqLogger: (req, res, next) ->
    start = new Date()
    res.on 'end', ->
      end = new Date()
      elapsed = (end - start).toFixed 2
      log.info "#{start.toString()} #{elapsed}ms #{req.method} #{req.url}"
    next()

  '404': (req, res, next) ->
    if res.headersSent
      return next()
    res.notFound()

  '$custom': (req, res, next) ->
    customRouter.process req, res
    if not res.headersSent
      return next()
