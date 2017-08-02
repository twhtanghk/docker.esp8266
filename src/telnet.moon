log = require 'log'
Wlan = require 'wlan'

class Telnet
  @config: (opts = {}) ->
    with net.createServer net.TCP
      \listen 23, (conn) ->
        fifo = {}
        fifo_drained = true
        sender = (c) ->
          if #fifo > 0
            c\send table.remove(fifo, 1)
          else
            fifo_drained = true
        s_output = (str) ->
          table.insert fifo, str
          if conn and fifo_drained
            fifo_drained = false
            sender conn

        node.output s_output, 0

        with conn
          \on 'receive', (c, l) ->
            node.input l

          \on 'disconnection', (c) ->
            node.output nil

          \on 'sent', sender

        log.info "Welcome to NodeMCU world."

Telnet.config()

return Telnet
