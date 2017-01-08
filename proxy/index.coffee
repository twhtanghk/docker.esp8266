http = global.require 'http'
wifi = global.require 'Wifi'
log = require './log.coffee'

mac = ->
  new Promise (resolve, reject) ->
    wifi.getAPIP (cfg) ->
      resolve cfg.mac

startAP = (opts)->
  new Promise (resolve, reject) ->
    wifi.startAP opts.ssid, {authMode: 'wpa2', password: opts.pwd}, (err) ->
      if err?
        reject err
      else
        resolve()

mac()
  .then (mac) ->
    "TT#{mac.split(':').join('')}"
  .then (ssid) ->
    startAP 
       ssid: ssid
       pwd: "12345678"
  .then ->
    http
      .createServer (req, res) ->
        require './app.coffee'
          .process req, res
      .listen 80
  .catch log.error
