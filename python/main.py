import ure as re
import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import config
import ap
import sta
import pwm
import gpio
import ddns
import util

pkg = ['ap', 'gpio', 'ddns', 'uart']
for i in pkg:
  lib = __import__(i)
  lib.model.setup()

routes = [
  ('/cfg', util.handler(config.crud)),
  ('/cfg/reset', util.handler(config.reset)),
  ('/cfg/factory', util.handler(config.factory)),
  ('/sta', util.handler(sta.crud)),
  ('/sta/scan', util.handler(sta.scan)),
  ('/ap', util.handler(ap.ctl.crud)),
  ('/pwm', util.handler(pwm.list)),
  (re.compile('^/pwm/(\w+)$'), util.handler(pwm.crud)),
  (re.compile('^/pwm/(\w+)/duty$'), util.handler(pwm.duty)),
  ('/gpio', util.handler(gpio.ctl.list)),
  (re.compile('^/gpio/(\w+)$'), util.handler(gpio.ctl.crud)),
  (re.compile('^/ddns$'), util.handler(ddns.ctl.crud)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)

import uasyncio as asyncio
loop = asyncio.get_event_loop()
loop.run_forever()
