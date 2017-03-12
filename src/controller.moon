log = require 'log'

class SysCtrl
  info: (req, res) ->
    res\send cjson.encode name: wifi.sta.gethostname()

  reset: (req, res) ->
    res.client\on 'sent', node.restart
    res\send ""

return {
  SysCtrl: SysCtrl()
}
