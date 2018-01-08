Config = require 'config'
cfg = Config.get().motor

class Motor
  @config: (name, opts) ->
    {:pin, :speed} = opts
    pwm.setup pin, 1000, speed
    pwm.start pin

  @params: (name) ->
    cfg[name] or error "motor[#{name}] not found"

  @speed: (name, val) ->
    pwm.setduty Motor.params(name).pin, val
   
  @stop: (name) ->
    pwm.stop Motor.params(name).pin

  @value: (name) ->
    pwm.getduty Motor.params(name).pin

-- init all motors defined in data.json
for name, opts in pairs cfg
  Motor.config name, opts

return Motor
