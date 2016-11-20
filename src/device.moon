SW = require "sw"
Voltmeter = require "voltmeter"
Thermistor = require "thermistor"
Motor = require "motor"

return {
  tempEvap: Thermistor(1)
  tempCond: Thermistor(2)
  voltIn: Voltmeter(3)
  motorEvap: Motor(5)
  motorCond: Motor(6)
  motorPump: Motor(7)
}
