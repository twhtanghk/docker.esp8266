import ujson
import network
import picoweb
import logging
logger = logging.getLogger(__name__)

class STA:
  def __init__(self):
    self.interface = network.WLAN(network.STA_IF)
    self.interface.active()

  def get(self):
    return self.interface.ifconfig()

  def set(self, opts):
    self.interface.connect(opts.ssid[0], opts.passwd[0])

  def scan(self):
    wlan = network.WLAN(mode=network.WLAN.STA)
    nets = wlan.scan()
    return nets

sta = STA()
app = picoweb.WebApp(__name__)

def get(req, res):
  yield from picoweb.jsonify(res, sta.get())

def set(req, res):
  yield from req.read_form_data()
  sta.set(req.form)
  yield from get(req, res)

def notFound(req, res):
  yield from picoweb.start_response(res, status='404')
  yield from res.awrite('404\r\n')

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  logger.info('{0} {1}'.format(req.method, req.path))
  yield from ret.get(req.method, notFound)(req, res)

app.route('/sta')(method)
