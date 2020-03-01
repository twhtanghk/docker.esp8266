import time
from machine import Pin
from opto import Opto
from stepper import Stepper

class Antenna(Stepper):
  def __init__(self, reverse=-2):
    def cb(pin):
      self.irq = True
    self.reverse = reverse
    self.irq = False
    self.opto = Opto()
    self.opto.on(Pin.IRQ_RISING, cb) 
    super(Antenna, self).__init__()

  def step(self, count):
    if count == 0:
      return 0
    direction = 1 if count > 0 else -1
    count = abs(count)
    for x in range(1, count + 1):
      for bit in self.HALF_STEP[::direction]:
        self.pin1(bit[0])
        self.pin2(bit[1])
        self.pin3(bit[2])
        self.pin4(bit[3])
        time.sleep_ms(self.delay)
        if self.irq:
          self.reset()
          super(Antenna, self).step(self.reverse * direction)
          return direction * (x + self.reverse)
    self.reset()
    return direction * x

  def reset(self):
    super(Antenna, self).reset()
    self.irq = False

antenna = Antenna()

def angle(req, res):
  try:
    yield from res.ok(antenna.angle(float(req.url_match.group(1))))
  except Exception as e:
    yield from res.err(500, str(e))