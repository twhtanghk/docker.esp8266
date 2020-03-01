import http
import system
import heading
import antenna
import stepper
import opto

app = http.App()
app.options('.*', http.preflight)
app.get('/factory', system.factory)
app.get('/reboot', system.reboot)
app.get('/ap', system.getAP)
app.put('/ap', system.configAP)
app.get('/sta', system.getSTA)
app.get('/sta/scan', system.hotspot)
app.put('/sta', system.configSTA)
app.put('/heading/boat/(-?\d*[.]?\d*)$', heading.boat)
app.put('/heading/antenna/(-?\d*[.]?\d*)$', heading.antenna)
app.put('/antenna/(-?\d*[.]?\d*)$', antenna.angle)
app.put('/stepper/(-?\d*[.]?\d*)$', stepper.angle)
app.get('/opto', opto.get)
app.get('(.*)', http.static)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(heading.adjust())
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
loop.run_forever()
