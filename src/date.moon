log = require 'log'

class Date
  new: =>
    @sec = 0
    @usec = 0

  @now: =>
    ret = Date()
    sntp.sync "stdtime.gov.hk", =>
      ret.sec, ret.usec = rtctime.get()
    return ret

  -- retrun milli seconds for current date - adate
  __sub: (adate) =>
    return (@sec - adate.sec) * 1000  + (@usec - adate.usec) / 1000

  __tostring: =>
    tm = rtctime.epoch2cal @sec
    return "#{tm['year']}.#{tm['mon']}.#{tm['day']} #{tm['hour']}:#{tm['min']}:#{tm['sec']}"

return Date
