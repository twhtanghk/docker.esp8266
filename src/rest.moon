Req = require "req"
Res = require "res"
log = require "log"
ctrl = require "device"

with net.createServer net.TCP
  \listen 80, (conn) ->
    conn\on "receive", (client, data) ->
      req = Req client, data
      res = Res client
      route = "#{req.method} #{req.url}"      
      verbose = (msg) ->
        log.info "#{route}: #{msg}"
      client\on 'sent', ->
        req = nil
        res = nil
        data = nil
        client = nil
        collectgarbage()
        log.debug "heap: #{node.heap()}"

      switch true

        when route\find("GET /status") != nil
          ret = {}
          for name, device in pairs ctrl
            ret[name] = device\value()
          ret['heap'] = node.heap()
          client\on 'sent', ->
            verbose 'get status'
          res\send ret

        when route\find("PUT /motor/%a+/%d+") != nil
          device, val = route\match "PUT /motor/(%a+)/(%d+)"
          val = tonumber val
          ctrl[device]\speed val
          client\on 'sent', ->
            verbose "#{device} speed #{val}"
          res\send ""

        when route\find("PUT /sw/%a+/toggle") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\toggle()          
          client\on 'sent', ->
            verbose "toggle sw #{name}"
          res\send ""

        when route\find("PUT /sw/%a+/on") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\on()          
          client\on 'sent', ->
            verbose "on sw #{name}"
          res\send ""

        when route\find("PUT /sw/%a+/off") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\off()          
          client\on 'sent', ->
            verbose "off sw #{name}"
          res\send ""

	when route\find("GET /reset") != nil
          client\on 'sent', ->
            verbose "reset"
          res\send "", ->
            node.restart()

        else
          res\status 404
          client\on 'sent', ->
            verbose "not found"
          res\send ""
