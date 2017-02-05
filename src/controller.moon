log = require 'log'

class SysCtrl
  info: (req, res) ->
    log.debug res.statusCode
    res\send cjson.encode name: wifi.sta.gethostname()

return {
  SysCtrl: SysCtrl()
}
