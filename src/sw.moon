class Switch
  @LOW: gpio.LOW
  @HIGH: gpio.HIGH

  new: (@pin) =>
    @value = @@LOW
    gpio.mode @pin, gpio.OUTPUT
    gpio.write @pin, @value

  state: =>
    @value

  toggle: (@value = if @value == @@LOW then @@HIGH else @@LOW) =>
    gpio.write @pin, @value
    return @
    
  on: =>
    @toggle @@HIGH

  off: =>
    @toggle @@LOW

class NSwitch extends Switch
  -- gpio state inverted
  @LOW: gpio.HIGH
  @HIGH: gpio.LOW

  state: =>
    if @value == @@LOW then gpio.LOW else gpio.HIGH

Switch: Switch, NSwitch: NSwitch
