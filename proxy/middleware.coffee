module.exports =
  reqLogger: (req, res, next) ->
    start = new Date()
    res.on 'end', ->
      end = new Date()
      elapsed = (end - start).toFixed 2
      console.log "#{start.toString()} #{elapsed}ms #{req.method} #{req.url}"
    next()

  bodyParser: (req, res, next) ->
    req.on 'data', (data) ->
      req.body = JSON.parse data
    next()

  cors: (req, res, next) ->
    res.set
      'Access-Control-Allow-Origin': '*'
      'Access-Control-Allow-Methods': 'OPTIONS, POST, GET, PUT, DELETE'
      'Access-Control-Allow-Headers': 'Content-Type'
      'Access-Control-Max-Age': 86400
    if req.method == 'OPTIONS'
      res.writeHead 200, res.headers
      res.end()
    next()

  static: (req, res, next) ->
    files = require './static.coffee'
    if not (req.url of files)
      return next()
    ext = (path) ->
      ret = path.split '.'
      ret[ret.length - 1]
    switch ext req.url
      when 'html'
        res.writeHead 200, 'Content-Type': 'text/html'
      when 'js'
        res.writeHead 200, 'Content-Type': 'application/javascript'
    res.end atob files[req.url]

  '404': (req, res, next) ->
    if res.headersSent
      return next()
    res.notFound()

  '$custom': (req, res, next) ->
    next()
