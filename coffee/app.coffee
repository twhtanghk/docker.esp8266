http = require 'http'
wifi = require 'Wifi'

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
