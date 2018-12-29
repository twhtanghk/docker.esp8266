import ure as re
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import picoweb
import config
import ap
import sta
import pwm
import gpio
import ddns
import util
import pkg

for i in pkg.list:
  lib = __import__(i)
  lib.model.setup()

util.inetd()

routes = [
  ('/cfg', util.handler(config.ctl.read)),
  ('/cfg/reset', util.handler(config.ctl.reset)),
  ('/cfg/factory', util.handler(config.ctl.factory)),
  ('/sta', util.handler(sta.ctl.crud)),
  ('/sta/scan', util.handler(sta.ctl.scan)),
  ('/ap', util.handler(ap.ctl.crud)),
  ('/pwm', util.handler(pwm.ctl.list)),
  (re.compile('^/pwm/(\w+)$'), util.handler(pwm.ctl.crud)),
  (re.compile('^/pwm/(\w+)/duty$'), util.handler(pwm.ctl.duty)),
  ('/gpio', util.handler(gpio.ctl.list)),
  (re.compile('^/gpio/(\w+)$'), util.handler(gpio.ctl.crud)),
  (re.compile('^/ddns$'), util.handler(ddns.ctl.crud)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)
