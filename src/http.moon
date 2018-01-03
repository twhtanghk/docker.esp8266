log = require "log"

class Http
  @config: (opts = {}) ->
    with net.createServer net.TCP
      \listen 80, (conn) ->
        conn\on "receive", (client, data) ->
          Req = require "req"
          Res = require "res"

          req = Req client, data
          res = Res client
          client\on 'sent', ->
            client\close()
            req.client = nil
            req = nil
            res.client = nil
            res = nil
            data = nil
            client = nil
            conn = nil
            collectgarbage()

          app = require "app"
          app\process req, res

Http.config()

return Http
