log = require 'log'
{:AP, :STA} = require 'wlan'

class SysCtrl
  wifi: (req, res) ->
    res\send sjson.encode 
      ap: AP.get()
      sta: STA.get()

  reset: (req, res) ->
    res.client\on 'sent', ->
      node.restart()
    res\send ""

  heap: (req, res) ->
    res\send "{heap: #{node.heap()}}"

return {
  SysCtrl: SysCtrl()
}
