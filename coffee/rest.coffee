http = require 'http'
wifi = require 'Wifi'

class Ctrl
  constructor: (opts) ->
    @headers = 'Content-Type': 'application/json'
    @url = opts.url

  matchUrl: (req) ->
    req.url == @url

  notFound: (res) ->
    res.writeHead 404, @headers
    res.end()

  process: (req, res) ->
    switch req.method
      when 'POST'
        if @matchUrl req
          @create req, res
      when 'GET'
        if @matchUrl req
          func = if req.url == @url then @findOne else @find
          func req, res
      when 'PUT'
        if @matchUrl req
          @update req, res
      when 'DELETE'
        if @matchUrl req
          @destroy req, res

  create: (req, res) ->
    notFound res

  find: (req, res) ->
    notFound res

  findOne: (req, res) ->
    notFound res

  update: (req, res) ->
    notFound res

  destroy: (req, res) ->
    notFound res

ap = new Ctrl url: '/ap'
ap.findOne = (req, res) ->
  wifi.getAPDetails (cfg) ->
    res.writeHead 200, ap.headers
    res.end JSON.stringify cfg

sta = new Ctrl url: '/sta'
sta.findOne = (req, res) ->
  wifi.getDetails (cfg) ->
    res.writeHead 200, sta.headers
    res.end JSON.stringify cfg

ctrls = [ap, sta]

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

  for ctrl in ctrls
    ctrl.process req, res
    if res.headersSent
      return

wifi.getAPIP (cfg) ->
  ssid = "TT#{cfg.mac.split(':').join('')}"
  pwd = "12345678"
  wifi.startAP ssid, password: pwd, ->
    http
      .createServer app
      .listen 80
