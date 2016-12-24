http = require 'http'
wifi = require 'Wifi'

class Router
  constructor: ->
    @routes =
      POST: {}
      GET: {}
      PUT: {}
      DELETE: {}

  # opts = ctrl: ctrl, method: method
  METHOD: (method, url, opts) ->
    @routes[method][url] = opts

  post: (url, opts) ->
    @METHOD('POST', url, opts)

  get: (url, opts) ->
    @METHOD('GET', url, opts)

  put: (url, opts) ->
    @METHOD('PUT', url, opts)

  'delete': (url, opts) ->
    @METHOD('DELETE', url, opts)

  process: (req, res) ->
    for url, opts of @routes[req.method]
      if url == req.url
        ctrl = opts.ctrl
        return ctrl[opts.method].call ctrl, req, res
    Ctrl.notFound res
  
class Ctrl
  @headers:
    'Content-Type': 'application/json'

  @notFound: (res) ->
    res.writeHead 404, Ctrl.headers
    res.end()

  create: (req, res) ->
    Ctrl.notFound res

  find: (req, res) ->
    Ctrl.notFound res

  findOne: (req, res) ->
    Ctrl.notFound res

  update: (req, res) ->
    Ctrl.notFound res

  destroy: (req, res) ->
    Ctrl.notFound res

ap = new Ctrl()
ap.findOne = (req, res) ->
  wifi.getAPDetails (cfg) ->
    res.writeHead 200, ap.headers
    res.end JSON.stringify cfg

sta = new Ctrl url: '/sta'
# get current station config details
sta.findOne = (req, res) ->
  wifi.getDetails (cfg) ->
    res.writeHead 200, sta.headers
    res.end JSON.stringify cfg
# scan and list available ap to be connected
sta.find = (req, res) ->
  wifi.scan (aplist) ->
    res.writeHead 200, sta.headers
    res.end JSON.stringify aplist

router = new Router()
router.get '/ap', 
  ctrl: ap
  method: 'findOne'
router.get '/sta',
  ctrl: sta
  method: 'findOne'
router.get '/sta/aplist', 
  ctrl: sta
  method: 'find'

app = (req, res) ->
  writeHead = res.writeHead
  res.writeHead = (statusCode, headers) ->
    writeHead.call res, statusCode, headers
    res.headersSent = true

  write = res.write
  res.write = (data) ->
    write.call res, data
    res.headersSent = true

  end = res.end
  res.end = (data) ->
    end.call res, data
    res.headersSent = true

  router.process req, res

mac = ->
  new Promise (resolve, reject) ->
    wifi.getAPIP (cfg) ->
      resolve cfg.mac

startAP = (opts)->
  new Promise (resolve, reject) ->
    wifi.startAP opts.ssid, password: opts.pwd, resolve

mac()
  .then (mac) ->
    "TT#{mac.split(':').join('')}"
  .then (ssid) ->
    startAP 
       ssid: ssid
       pwd: "12345678"
  .then ->
    http
      .createServer app
      .listen 80
