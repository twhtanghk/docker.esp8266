-- setup pin to contorl motor speed
class Motor
  new: (@pin) =>
    pwm.setup @pin, 1000, 0
    pwm.start @pin

  speed: (val = 0) =>
    pwm.setduty @pin, val

  stop: =>
    pwm.stop @pin

  value: =>
    pwm.getduty @pin
   
return Motor
