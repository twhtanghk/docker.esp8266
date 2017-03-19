Wlan = require "wlan"
Req = require "req"
Res = require "res"
log = require "log"
app = require "app"

with net.createServer net.TCP
  \listen 80, (conn) ->
    conn\on "receive", (client, data) ->
      req = Req client, data
      res = Res client
      client\on 'disconnection', ->
        req.client = nil
        req = nil
        res.client = nil
        res = nil
        data = nil
        client = nil
        conn = nil
        collectgarbage()
      app\process req, res
