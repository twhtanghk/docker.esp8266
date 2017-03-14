log = require 'log'

class SysCtrl
  info: (req, res) ->
    res\send "{#{name}: #{wifi.sta.gethostname()}}"

  reset: (req, res) ->
    res.client\on 'disconnection', node.restart
    res\send ""

return {
  SysCtrl: SysCtrl()
}
