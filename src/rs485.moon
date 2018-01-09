Config = require 'config'
cfg = Config.get().rs485

class RS485
  -- port: network port (default 485) to create socket for UART connection
  -- id: 0, 1 (default) for standard uart pins, or alternate pins GPIO13 & 15
  -- baud: 115200 bps (default)
  -- databits: 8 (default)
  -- parity: uart.PARITY_NONE (default)
  -- stopbits: uart.STOPBITS_1 (default)
  -- echo: 0 (default disable)
  @config: (opts) ->
    {:port, :id, :baud, :databits, :parity, :stopbits, :echo} = opts
    port = port or 485
    id = id or 0
    baud = baud or 115200
    databits = databits or 8
    parity = parity or uart.PARITY_NONE
    stopbits = stopbits or uart.STOPBITS_1
    echo = echo or 1
    uart.alt id
    uart.setup id, baud, databits, parity, stopbits, echo
    with net.createServer net.TCP
      \listen port, (conn) ->
        toSocket = (data) ->
          conn\send data
          require('log').info "rs485 in: #{data}"
        uart.on 'data', '\r', toSocket, 0
        with conn
          \on 'receive', (client, data) ->
            uart.write id, data
            require('log').info "rs485 out: #{data}"
          \on 'disconnection', ->
            require('log').info "connection closed for port #{port}"

RS485.config cfg

return RS485
