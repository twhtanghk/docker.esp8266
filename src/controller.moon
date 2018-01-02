log = require 'log'
Wlan = require 'wlan'

class SysCtrl
  wifi: (req, res) ->
    res\send sjson.encode Wlan.staCfg()

  info: (req, res) ->
    res\send "{name: #{wifi.sta.gethostname()}}"

  reset: (req, res) ->
    res.client\on 'disconnection', node.restart
    res\send ""

  heap: (req, res) ->
    res\send "{heap: #{node.heap()}}"

return {
  SysCtrl: SysCtrl()
}
