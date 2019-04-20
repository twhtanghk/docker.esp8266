import ure as re
import picoweb
import system
import ap
import sta
import log
import pwm
import gpio
import ddns
import util

util.inetd()

routes = [
  ('/cfg', util.handler2({'GET': system.model.read})),
  ('/cfg/reset', util.handler2({'GET': system.model.reset})),
  ('/cfg/factory', util.handler2({'GET': system.model.factory})),
  ('/sta', util.handler2({'GET': sta.model.status, 'PUT': sta.model.set})),
  ('/sta/scan', util.handler(sta.model.scan)),
  ('/ap', util.handler2({'GET': ap.model.get, 'PUT': ap.model.set})),
  ('/log', util.handler2({'GET': log.model.status, 'PUT': log.model.set})),
  ('/pwm', util.handler2({'GET': pwm.model.list})),
  (re.compile('^/pwm/(\w+)$'), util.handler2({'GET': gpio.model.read, 'PUT': pwm.model.update})),
  (re.compile('^/pwm/(\w+)/duty$'), util.handler2({'PUT': pwm.model.duty})),
  ('/gpio', util.handler2({'GET': gpio.model.list})),
  (re.compile('^/gpio/(\w+)$'), util.handler2({'GET': gpio.model.read, 'PUT': gpio.model.update})),
  (re.compile('^/ddns$'), util.handler(ddns.ctl.crud)),
  (re.compile('^(.*)$'), util.handler(util.static))
]
app = picoweb.WebApp(__name__, routes, False)
app.run(host="0.0.0.0", port=80)
