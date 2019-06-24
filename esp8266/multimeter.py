import machine

# https://forum.arduino.cc/index.php?topic=445538.0
# voltage = 1v, r1 = 220kOhm, r2 = 100kOhm
def _voltage(r1=680+680+220, r2=100):
  return machine.ADC(0).read() / 1024 * (1 + r1 / r2)

def _current(acsRange=20):
  sensitivity = {
    5: 185,
    20: 100,
    30: 66
  }
  return (_voltage() - 2.5) * 1000 / sensitivity[acsRange]
  
def voltage(req, res):
  res.ok({
    "voltage": _voltage()
  })

def current(req, res):
  res.ok({
    "current": _current()
  })
