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
    Motor = require 'motor'
    motor = Motor name: name
    try = require 'error'
    try
      do: ->
        motor\speed val
        res\send ""
      catch: (err) ->
        res\notFound err
    
{ :SysCtrl, :MotorCtrl }
