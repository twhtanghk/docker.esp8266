import http
import system
import mqtt
from multimeter import voltage, current
import humidity
import thermistor

def echo(req, res):
  yield from res.ok(req.__dict__)
 
def preflight(req, res):
  yield from res.ok()

app = http.App()
app.options('.*', preflight)
app.get('/factory', system.factory)
app.get('/reboot', system.reboot)
app.post('/mqtt', mqtt.reset)
app.post('/ap', system.configAP)
app.get('/hotspot', system.hotspot)
app.post('/sta', system.configSTA)
app.get('/voltage', voltage)
app.get('/current', current)
app.get('/dht', humidity.sensor.json)
app.get('/thermistor', thermistor.sensor.json)
app.get('.*', echo)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
loop.create_task(humidity.publish())
loop.create_task(thermistor.publish())
loop.run_forever()
