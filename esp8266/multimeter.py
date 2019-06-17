import machine

def _voltage(r1=680, r2=220):
  vin = machine.ADC(0).read()
  return vin * 3.3 / 1024 * (1 + r1 / r2)

def _current(acsRange=20):
  sensitivity = {
    5: 185,
    20: 100,
    30: 66
  }
  return (_voltage() - acsRange / 2) / sensitivity[acsRange] / 1000
  
def voltage(req, res):
  res.ok({
    "voltage": _voltage()
  })

def current(req, res):
  res.ok({
    "current": _current()
  })
