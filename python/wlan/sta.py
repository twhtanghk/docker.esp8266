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
    ssid = opts.get('ssid', [''])[0]
    passwd = opts.get('passwd', [''])[0]
    self.interface.active(True)
    self.interface.connect(ssid, passwd)

  def scan(self):
    nets = []
    for net in self.interface.scan():
      nets.append(net[0])
    return nets

sta = STA()
app = picoweb.WebApp(__name__)

def get(req, res):
  yield from picoweb.jsonify(res, sta.get())

def set(req, res):
  yield from req.read_form_data()
  sta.set(req.form)
  yield from get(req, res)

def scan(req, res):
  nets = sta.scan()
  yield from picoweb.jsonify(res, nets)
  
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
app.route('/sta/scan')(scan)
