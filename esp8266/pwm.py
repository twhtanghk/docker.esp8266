import gpio
import machine

def pwm(pin):
  return machine.PWM(pin)

def get(req, res):
  try:
    id, pin = gpio.parse(req)
    yield from res.ok(pwm(pin).duty())
  except gpio.PinError as e:
    yield from res.err(500, 'Invalid pin')

def duty(req, res):
  try:
    id, pin = gpio.parse(req)
    pwm(pin).duty(int(req.body['duty']))
    yield from res.ok()
  except gpio.PinError as e:
    yield from res.err(500, 'Invalid pin')
  except ValueError:
    yield from res.err(500, 'Invalid duty value')
