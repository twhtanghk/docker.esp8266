log = require "log"

class Wlan
  @config: (opts = {}) ->
    name = "TT#{wifi.ap.getmac()\gsub(":", "")}"

    wifi.setmode wifi.STATIONAP, true

    wifi.ap.config
      ssid: name
      pwd: "12345678"
    wifi.ap.setip
      ip: "192.168.4.1"
      netmask: "255.255.255.0"
      gateway: "192.168.4.1"
    
    wifi.sta.sethostname name
    wifi.sta.config
      ssid: 'SSID'
      pwd: '12345678'
      auto: true
      save: true
    wifi.sta.connect()

    log.debug "AP: #{sjson.encode @@apCfg()}"
    log.debug "STA: #{sjson.encode @@staCfg()}"

  @staCfg: ->
    ssid: wifi.sta.getconfig(true).ssid

  @apCfg: ->
    ip: wifi.ap.getip()

Wlan.config()

return Wlan
