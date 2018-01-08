class Motor
  @cfg: ->
    Config = require 'config'
    Config.get().motor

  -- get motor[name] config from data.json
  @params: (name) ->
    cfg = @cfg()
    if cfg[name] == nil
      error "motor[#{name}] not found"
    else
      cfg[name]

  @config: ->
    for name, params in pairs @cfg()
      {:pin, :speed} = params
      pwm.setup pin, 1000, speed
      pwm.start pin
    
  -- name: motor logical name
  new: (opts) =>
    @name = opts.name

  speed: (val = 0) =>
    motor = Motor.params @name
    pwm.setduty motor.pin, val

  stop: =>
    pwm.stop Motor.params(@name).pin

  value: =>
    pwm.getduty Motor.params(@name).pin
   
Motor.config()

return Motor
