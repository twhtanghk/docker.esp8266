wifi = require 'Wifi'

wifi.getAPIP (cfg) ->
  ssid = "TT#{cfg.mac.split(':').join('')}"
  pwd = "12345678"
  wifi.startAP ssid, password: pwd, ->
    wifi.getAPDetails (cfg) ->
      console.log JSON.stringify cfg
