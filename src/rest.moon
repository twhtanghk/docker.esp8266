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
      clean = ->
        client\close()
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
          res\send ret, ->
            verbose 'get status'
            clean()

        when route\find("PUT /motor/%a+/%d+") != nil
          device, val = route\match "PUT /motor/(%a+)/(%d+)"
          val = tonumber val
          ctrl[device]\speed val
          res\send "", ->
            verbose "#{device} speed #{val}"
            clean()

        when route\find("PUT /sw/%a+/toggle") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\toggle()          
          res\send "", ->
            verbose "toggle sw #{name}"
            clean()

        when route\find("PUT /sw/%a+/on") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\on()          
          res\send "", ->
            verbose "on sw #{name}"
            clean()

        when route\find("PUT /sw/%a+/off") != nil
          name = route\match "PUT /sw/(%a+)/toggle"
          ctrl[name]\off()          
          res\send "", ->
            verbose "off sw #{name}"
            clean()

	when route\find("GET /reset") != nil
          res\send "", ->
            verbose "reset"
            clean()
            node.restart()

        else
          res\status 404
          res\send "", ->
            verbose "not found"
            clean()
