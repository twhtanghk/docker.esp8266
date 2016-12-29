http = require 'http'
wifi = require 'Wifi'
router = require './router.coffee'

app = (req, res) ->
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
