require "wlan"
require "app"

Req = require "req"
Res = require "res"
log = require "log"
app = require "app"

with net.createServer net.TCP
  \listen 80, (conn) ->
    conn\on "receive", (client, data) ->
      req = Req client, data
      res = Res client
      route = "#{req.method} #{req.url}"      
      app\process req, res
      clean = ->
        client\close()
        req = nil
        res = nil
        data = nil
        client = nil
        collectgarbage()
