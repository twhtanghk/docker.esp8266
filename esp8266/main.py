import http
import system
import mqtt
from multimeter import voltage, current
import humidity
import thermistor
import gpio
import pwm

router = http.Router()
router.options('.*', http.preflight)
router.get('/factory', system.factory)
router.get('/reboot', system.reboot)
router.post('/mqtt', mqtt.reset)
router.get('/ap', system.getAP)
router.put('/ap', system.configAP)
router.get('/sta/scan', system.hotspot)
router.get('/sta', system.getSTA)
router.put('/sta', system.configSTA)
router.get('/voltage', voltage)
router.get('/current', current)
router.get('/dht', humidity.sensor.json)
router.get('/thermistor', thermistor.sensor.json)
router.get('/gpio/(\d+)', gpio.get)
router.put('/gpio/(\d+)/mode', gpio.mode) # set id: 5, mode: 'in'
router.put('/gpio/(\d+)/value', gpio.set) # set id: 5, value: 1
router.get('/pwm/(\d+)', pwm.get)
router.put('/pwm/(\d+)', pwm.duty) # set id: 5, duty: 600
router.get('(.*)', http.static)

app = http.App()
app.use(http.bodyParser)
app.use(http.methodOverride)
app.use(http.logger)
app.use(http.json)
app.use(http.cors)
app.use(router.routes())

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
#loop.create_task(humidity.publish())
#loop.create_task(thermistor.publish())
loop.run_forever()
