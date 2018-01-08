{:AP, :STA} = require 'wlan'

SysCtrl =
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

MotorCtrl =
  speed: (req, res) ->
    name, val = req.url\match '/motor/(%a+)/(%d+)'
    try = require 'error'
    try
      do: ->
        Motor = require 'motor'
        Motor.speed name, val
        res\send ""
      catch: (err) ->
        res\notFound err
    
{ :SysCtrl, :MotorCtrl }
