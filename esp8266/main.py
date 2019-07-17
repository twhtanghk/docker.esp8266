import http
from multimeter import voltage, current
from humidity import sensor, publish

def echo(req, res):
  res.ok(req.__dict__)
 
def preflight(req, res):
  res.ok()

app = http.App()
app.options('.*', preflight)
app.get('/voltage', voltage)
app.get('/current', current)
app.get('/dht', sensor.json)
app.get('.*', echo)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
loop.create_task(publish())
loop.run_forever()
