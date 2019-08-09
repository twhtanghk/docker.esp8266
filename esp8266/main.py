import http
import system
import mqtt
from multimeter import voltage, current
import humidity
import thermistor
import gpio
import pwm

app = http.App()
app.options('.*', http.preflight)
app.get('/factory', system.factory)
app.get('/reboot', system.reboot)
app.post('/mqtt', mqtt.reset)
app.get('/ap', system.getAP)
app.put('/ap', system.configAP)
app.get('/sta', system.getSTA)
app.get('/sta/scan', system.hotspot)
app.put('/sta', system.configSTA)
app.get('/voltage', voltage)
app.get('/current', current)
app.get('/dht', humidity.sensor.json)
app.get('/thermistor', thermistor.sensor.json)
app.get('/gpio/(\d+)', gpio.get)
app.put('/gpio/(\d+)/mode', gpio.mode) # set id: 5, mode: 'in'
app.put('/gpio/(\d+)/value', gpio.set) # set id: 5, value: 1
app.get('/pwm/(\d+)', pwm.get)
app.put('/pwm/(\d+)', pwm.duty) # set id: 5, duty: 600
app.get('(.*)', http.static)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
#loop.create_task(humidity.publish())
#loop.create_task(thermistor.publish())
loop.run_forever()
