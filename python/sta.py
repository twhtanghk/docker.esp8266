from config import Config
from util import ok
import ubinascii
import ujson
import network
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, 'sta.json')
    self.interface = network.WLAN(network.STA_IF)
    self.interface.active(True)

  def factory(self):
    mac = self.interface.config('mac')
    import ubinascii
    mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
    self.save({
      'dhcp_hostname': 'ESP-{}'.format(mac)
    })

  def setup(self):
    cfg = self.load()
    self.interface.config(dhcp_hostname=cfg['dhcp_hostname'])
    if 'ssid' in cfg:
      self.interface.connect(cfg['ssid'], cfg['passwd'])
    logger.info(ujson.dumps(self.get()))

  def get(self):
    ret = {}
    for prop in ['mac', 'dhcp_hostname']:
      ret[prop] = self.interface.config(prop)
    ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
    ret['isconnected'] = self.interface.isconnected()
    ret['curr'] = self.interface.ifconfig()
    return ret

  def set(self, opts):
    cfg = self.model.load(filename)
    if 'name' in opts:
      name = opts['name']
      self.interface.config(dhcp_hostname=name)
      cfg['dhcp_hostname'] = name
    if 'ssid' in opts and 'passwd' in opts:
      ssid = opts['ssid']
      passwd = opts['passwd']
      self.interface.connect(ssid, passwd)
      cfg['ssid'] = ssid
      cfg['passwd'] = passwd
    self.model.save(cfg)

  def scan(self):
    nets = []
    for net in self.interface.scan():
      if net[0] not in nets:
        nets.append(net[0])
    return nets

class Controller:
  def __init__(self, model):
    self.model = model

  def get(self, req, res):
    yield from ok(res, model.load())

  def set(self, req, res):
    yield from req.read_form_data()
    cfg = self.model.load()
    for key, value in req.form.items():
      cfg[key] = value
    model.save(cfg)
    yield from self.get(req, res)

  def scan(self, req, res):
    nets = self.model.scan()
    yield from ok(res, nets)

  def crud(self, req, res):
    ret = {
      'GET': self.get,
      'PUT': self.set
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
