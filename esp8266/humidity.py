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
    yield from res.ok(self._json())

sensor = DHT()

async def publish(topic='iot/humidity', interval=10):
  from mqtt import client
  import ujson
  from uasyncio import sleep
  while True:
    client.publish(topic, ujson.dumps(sensor._json()))
    await sleep(interval)
