http = require 'http'

class Ctrl
  headers:
    'Content-Type': 'application/json'

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

  constructor: (opts) ->
    @url = opts.url

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

class APCtrl extends Ctrl
  find: (req, res) ->
    wifi.getAPDetails (cfg) ->
      res.writeHead 200, @headers
      res.end JSON.stringify cfg

ctrls = [
  new APCtrl url: '/ap'
]

app = (req, res) ->
  writeHead = res.writeHead
  res.writeHead = (statusCode, headers) ->
    writeHead statusCode, headers
    res.headersSent = true

  write = res.write
  res.write = (data) ->
    write = data
    res.headersSent = true

  for ctrl in ctrls
    ctrl.process req, res
    if res.headersSent
      return

server = http
  .createServer app
  .listen 80
