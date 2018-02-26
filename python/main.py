import ure as re
import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import config
import ap
import sta
import pwm
import util

routes = [
  ('/cfg', util.handler(config.crud)),
  ('/cfg/reset', util.handler(config.reset)),
  ('/cfg/factory', util.handler(config.factory)),
  ('/wlan/sta', util.handler(sta.crud)),
  ('/wlan/sta/scan', util.handler(sta.scan)),
  ('/wlan/ap', util.handler(ap.crud)),
  ('/pwm', util.handler(pwm.list)),
  (re.compile('^/pwm/(\w+)$'), util.handler(pwm.crud)),
  (re.compile('^/pwm/(\w+)/duty$'), util.handler(pwm.duty)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)
