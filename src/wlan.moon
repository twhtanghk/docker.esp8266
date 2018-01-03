log = require "log"

class STA
  @config: ->
    Config = require 'config'
    cfg = Config.get().sta
    wifi.sta.sethostname cfg.name
    wifi.sta.config
      ssid: cfg.ssid
      pwd: cfg.pwd
      auto: true
      save: true

  @get: ->
    {:ssid} = wifi.sta.getconfig true
    ssid: ssid

  @set: (cfg) ->
    wifi.sta.config cfg
    Config = require 'config'
    ret = Config.get()
    ret.sta = cfg
    Config.set ret

class AP
  @config: ->
    Config = require 'config'
    cfg = Config.get().ap
    wifi.ap.config cfg
    wifi.ap.setip cfg
    log.debug sjson.encode ap: AP.get()

  @get: ->
    {:ssid} = wifi.ap.getconfig true
    ip, nm, gw = wifi.ap.getip()
    return {
      ssid: ssid
      ip: ip
      nm: nm
      gw: gw
    }

  @set: (cfg) ->
    wifi.ap.config cfg
    Config = require 'config'
    ret = Config.get()
    ret.ap = cfg
    Config.set ret

wifi.setmode wifi.STATIONAP, true
wifi.eventmon.register wifi.eventmon.STA_GOT_IP, ->
  log.debug "STA: #{sjson.encode STA.get()}"
wifi.eventmon.register wifi.eventmon.AP_STACONNECTED, (opts) ->
  log.debug "AP: #{opts.MAC} connected"

STA.config()
AP.config()

return {
  STA: STA
  AP: AP
}
