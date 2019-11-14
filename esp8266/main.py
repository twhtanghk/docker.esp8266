import http
import system
import uart

app = http.App()
app.options('.*', http.preflight)
app.get('/factory', system.factory)
app.get('/reboot', system.reboot)
app.get('/ap', system.getAP)
app.put('/ap', system.configAP)
app.get('/sta', system.getSTA)
app.get('/sta/scan', system.hotspot)
app.put('/sta', system.configSTA)
app.put('/uart', uart.config)
app.get('(.*)', http.static)

rs485 = uart.RS485()

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.create_task(asyncio.start_server(app.handle, '0.0.0.0', 80))
loop.create_task(asyncio.start_server(rs485.handle, '0.0.0.0', 23))
loop.create_task(rs485.readline())
loop.run_forever()
