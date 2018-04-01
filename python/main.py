import ure as re
import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import config
import ap
import sta
import pwm
import gpio
import util

routes = [
  ('/cfg', util.handler(config.crud)),
  ('/cfg/reset', util.handler(config.reset)),
  ('/cfg/factory', util.handler(config.factory)),
  ('/sta', util.handler(sta.crud)),
  ('/sta/scan', util.handler(sta.scan)),
  ('/ap', util.handler(ap.crud)),
  ('/pwm', util.handler(pwm.list)),
  (re.compile('^/pwm/(\w+)$'), util.handler(pwm.crud)),
  (re.compile('^/pwm/(\w+)/duty$'), util.handler(pwm.duty)),
  ('/gpio', util.handler(gpio.list)),
  (re.compile('^/gpio/(\w+)$'), util.handler(gpio.crud)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)
