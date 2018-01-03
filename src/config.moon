log = require 'log'

class Config
  @file: 'data.json'

  @get: ->
    with file.open(Config.file)
      return sjson.decode \read()

  @set: (cfg) ->
    with file.open Config.file, 'w'
      \write sjson.encode cfg
      \close()

  @debug: ->
    log.debug sjson.encode Config.get()

  @test: ->
    cfg = Config.get()
    log.debug sjson.encode get: cfg
    cfg.sta.name = "TT#{wifi.ap.getmac()\gsub(":", "")}"
    cfg.ap.ssid = "TT#{wifi.ap.getmac()\gsub(":", "")}"
    Config.set cfg
    log.debug sjson.encode set: cfg

return Config
