from config import Config
from util import ok
import network
import ujson
import ubinascii
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  authmode = {
    network.AUTH_OPEN: 'OPEN',
    network.AUTH_WEP: 'WEP',
    network.AUTH_WPA_PSK: 'WPA_PSK',
    network.AUTH_WPA2_PSK: 'WPA2_PSK',
    network.AUTH_WPA_WPA2_PSK: 'WPA_WPA2_PSK'
  }

  def __init__(self):
    Config.__init__(self, '/ap.json')
    self.interface = network.WLAN(network.AP_IF)
    self.interface.active(True)

  def factory(self):
    mac = self.interface.config('mac')
    mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
    self.save({
      'essid': 'Micropython-{}'.format(mac),
      'password': 'micropyhonN'
    })

  def setup(self):
    self.cfg = self.load()
    self.interface.config(essid=self.cfg['essid'], password=self.cfg['password'])
    logger.info(ujson.dumps(self.get()))

  def get(self):
    ret = {}
    for prop in ['mac', 'essid', 'hidden', 'authmode']:
      ret[prop] = self.interface.config(prop)
    ret['authmode'] = self.authmode[ret['authmode']]
    ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
    ret['curr'] = self.interface.ifconfig()
    return ret

  def set(self, opts):
    cfg = model.load(filename)
    essid = opts['essid']
    password = opts['password']
    self.cfg['essid'] = opts['essid']
    self.cfg['password'] = opts['password']
    logger.info(ujson.dumps(self.cfg))
    self.save(cfg)

class Controller:
  def __init__(self, model):
    self.model = model

  def get(self, req, res):
    yield from ok(res, model.get())

  def set(self, req, res):
    yield from req.read_form_data()
    opts = {
      'essid': req.form.get('essid', [''])[0],
      'password': req.form.get('password', [''])[0]
    }
    if not opts['essid']:
      raise Exception('empty essid')
    if len(opts['password']) < 8:
      raise Exception('password min length 8')
    model.set(opts)
    yield from get(req, res)

  def crud(self, req, res):
    ret = {
      'GET': self.get,
      'PUT': self.set
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
