log = require "log"

class Date
  new: =>
    @sec = 0
    @usec = 0

  @now: =>
    ret = Date()
    log.debug cjson.encode ret
    sntp.sync "stdtime.gov.hk", =>
      ret.sec, ret.usec = rtctime.get()
      log.debug ret
    return ret

  __tostring: =>
    log.debug @sec
    tm = rtctime.epoch2cal @sec
    return "#{tm['year']}.#{tm['mon']}.#{tm['day']} #{tm['hour']}:#{tm['min']}:#{tm['sec']}"

return Date
