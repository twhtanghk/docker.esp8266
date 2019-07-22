import machine

class PinError(Exception):
  pass

def validPin(pin):
  if pin not in [0, 2, 4, 5, 12, 13, 14, 15, 16]:
    raise PinError
  return machine.Pin(pin)

def parse(req):
  id = int(req.url_match.group(1))
  return (id, validPin(id))

def mode(req, res):
  try:
    id, pin = parse(req)
    mode = req.body['mode']
    if type(mode) == str:
      mode = {'in': machine.Pin.IN, 'out': machine.Pin.OUT}[mode]
    if type(mode) != int:
      raise KeyError
    machine.Pin(id, mode)
    yield from res.ok()
  except PinError as e:
    yield from res.err(500, 'Invalid pin')
  except KeyError as e:
    yield from res.err(500, 'Invalid mode')

def get(req, res):
  try:
    id, pin = parse(req)
    yield from res.ok(pin.value())
  except Exception:
    yield from res.err(500, 'Invalid pin')

def set(req, res):
  try:
    id, pin = parse(req)
    pin.value(req.body['value'])
    yield from res.ok()
  except PinError:
    yield from res.err(500, 'Invalid pin')
