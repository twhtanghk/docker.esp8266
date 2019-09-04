import http
import system
import pwm

app = http.App()
app.options('.*', http.preflight)
app.get('/factory', system.factory)
app.get('/reboot', system.reboot)
app.get('/ap', system.getAP)
app.put('/ap', system.configAP)
app.get('/sta', system.getSTA)
app.get('/sta/scan', system.hotspot)
app.put('/sta', system.configSTA)
app.get('/pwm/(\d+)', pwm.get)
app.put('/pwm/(\d+)', pwm.duty) # set id: 5, duty: 600
app.get('(.*)', http.static)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
loop.run_forever()
