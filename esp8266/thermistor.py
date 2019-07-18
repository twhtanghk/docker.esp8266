import math
import machine

pot = machine.ADC(0)
# default voltage=3.3v, 10kOhm in series with esp8266 built-in 220kOhm & 100kOhm
# voltage divider
class Thermistor:
  def __init__(self, r=[10 + 220, 100], c=[1.814728032e-3, 1.715646806e-4, 0.4148612028e-7]):
    self.r = r
    self.coeff = c

  def resistance(self):
    return ((3.3 * 1024 / pot.read() - 1) * self.r[1] - self.r[0]) * 1000

  def k(self):
    r = self.resistance()
    temp = math.log(r)
    c = self.coeff
    return {
      'r': r,
      'k': 1 / (c[0] + (c[1] + (c[2] * temp * temp)) * temp)
    }

  def c(self):
    ret = self.k()
    ret['c'] = ret['k'] - 273.15
    return ret

  def f(self):
    ret = self.c()
    ret['f'] = (ret['c'] * 9 / 5) + 32
    return ret

  def _json(self):
    return self.f()

  def json(self, req, res):
    yield from res.ok(self._json())

sensor = Thermistor()

async def publish(topic='iot/thermistor', interval=10):
  from mqtt import client
  import ujson
  from uasyncio import sleep
  while True:
    client.publish(topic, ujson.dumps(sensor._json()))
    await sleep(interval)
