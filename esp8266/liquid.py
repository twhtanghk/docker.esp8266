import machine
from gpio import PinError, parse

def get(req, res):
  try:
    id, pin = parse(req)
    machine.Pin(id, machine.Pin.IN)
    yield from res.ok(pin.value())
  except PinError as e:
    yield from res.err(500, 'Invalid pin')
