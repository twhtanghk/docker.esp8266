import time
from machine import Pin

class Stepper():
  FULL_ROTATION = int(4075.7728395061727 / 8) # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

  HALF_STEP = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
  ]

  def __init__(self, pin1=14, pin2=12, pin3=13, pin4=15, delay=2):
    self.pin1 = Pin(pin1, Pin.OUT)
    self.pin2 = Pin(pin2, Pin.OUT)
    self.pin3 = Pin(pin3, Pin.OUT)
    self.pin4 = Pin(pin4, Pin.OUT)
    self.delay = delay
    self.reset()
        
  def step(self, count):
    if count == 0:
      return
    direction = 1 if count > 0 else -1
    count = abs(count)
    for x in range(count):
      for bit in self.HALF_STEP[::direction]:
        self.pin1(bit[0]) 
        self.pin2(bit[1]) 
        self.pin3(bit[2]) 
        self.pin4(bit[3]) 
        time.sleep_ms(self.delay)
    self.reset()
        
  def angle(self, degree):
    self.step(int(self.FULL_ROTATION * degree / 360))

  def reset(self):
    self.pin1(0) 
    self.pin2(0) 
    self.pin3(0) 
    self.pin4(0) 

stepper = Stepper()

def step(req, res):
  try:
    count = int(req.url_match.group(1))
    stepper.step(count)
    yield from res.ok()
  except Exception as e:
    yield from res.err(500, str(e))

def angle(req, res):
  try:
    degree = int(req.url_match.group(1))
    stepper.angle(degree)
    yield from res.ok()
  except Exception as e:
    yield from res.err(500, str(e))
