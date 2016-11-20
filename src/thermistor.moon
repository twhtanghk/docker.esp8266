-- see http://www.instructables.com/id/ESP8266-with-Multiple-Analog-Sensors/
-- for details to connect multiple sensors
Switch = require("sw").Switch
ln = require "ln"

class Thermistor
  @r2: 10000

  new: (enablePin) =>
    @enable = Switch(enablePin)
    adc.force_init_mode adc.INIT_ADC

  k: =>
    @enable\on()
    value = adc.read(0)
    @enable\off()
    ret = 0
    if value != 0
      r1 = @@r2 * ((1024 / value) - 1)
      temp = ln r1
      ret = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temp * temp)) * temp)
    ret

  c: =>
    @k() - 273.15

  f: =>
    (@c() * 9 / 5) + 32

  value: =>
    @c()

return Thermistor
