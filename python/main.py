import ure as re
import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import config
import wlan
import pwm
import util

routes = [
  ('/cfg', util.handler(config.crud)),
  ('/cfg/reset', util.handler(config.reset)),
  ('/cfg/factory', util.handler(config.factory)),
  ('/wlan/sta', util.handler(wlan.sta.crud)),
  ('/wlan/sta/scan', util.handler(wlan.sta.scan)),
  ('/wlan/ap', util.handler(wlan.ap.crud)),
  ('/pwm', util.handler(pwm.list)),
  (re.compile('^/(\w+)$'), util.handler(pwm.crud)),
  (re.compile('^/(\w+)/duty$'), util.handler(pwm.duty)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)
