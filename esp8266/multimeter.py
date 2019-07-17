import machine

# https://forum.arduino.cc/index.php?topic=445538.0
# voltage = 1v, r1 = 220kOhm, r2 = 100kOhm
pot = machine.ADC(0)
def _voltage(r1=220+220, r2=100):
  return pot.read() / 1024 * (1 + r1 / r2)

def _current(acsRange=5):
  sensitivity = {
    5: 185,
    20: 100,
    30: 66
  }
  return (_voltage() - 2.5) * 1000 / sensitivity[acsRange]
  
def voltage(req, res):
  yield from res.ok({
    "voltage": _voltage()
  })

def current(req, res):
  yield from res.ok({
    "current": _current()
  })
