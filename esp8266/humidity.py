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
    res.ok(self._json())
