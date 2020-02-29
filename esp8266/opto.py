import time
from machine import Pin

class Opto():
  def __init__(self, pin=2):
    self.pin = Pin(pin, Pin.IN)
        
  def value(self):
    return self.pin()
        
opto = Opto()

def get(req, res):
  try:
    yield from res.ok(opto.value())
  except Exception as e:
    yield from res.err(500, str(e))
