class DHT:
  def __init__(self, pin=4):
    self.pin = pin
    import dht
    import machine
    self.sensor = dht.DHT11(machine.Pin(self.pin))

  def _json(self):
    self.sensor.measure()
    return {
      'temperature': self.sensor.temperature(),
      'humidity': self.sensor.humidity()
    }

  def json(self, req, res):
    try:
      yield from res.ok(self._json())
    except:
      yield from res.err(500, 'DHT error')     

sensor = DHT()

async def publish(topic='iot/humidity', interval=10):
  from mqtt import client
  import ujson
  from uasyncio import sleep
  while True:
    try:
      client.publish(topic, ujson.dumps(sensor._json()))
      await sleep(interval)
    except:
      pass
