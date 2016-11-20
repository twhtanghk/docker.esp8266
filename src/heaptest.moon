log = require "log"

msg = (body) ->
  "HTTP/1.1 200 OK\nContent-Type: application/json\n\n#{cjson.encode(body)}"

with net.createServer net.TCP
  \listen 80, (conn) ->
    conn\on "receive", (client, data) ->
      body = msg heap: node.heap()
      client\send body, ->
        client\close()
        data = nil
        body = nil
        client = nil
        collectgarbage()
        log.debug "heap: #{node.heap()}"
