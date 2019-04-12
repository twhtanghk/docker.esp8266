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
    logger.info(ujson.dumps(self._status()))

  def _status(self):
    ret = {}
    for prop in ['mac', 'dhcp_hostname']:
      ret[prop] = self.interface.config(prop)
    ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
    ret['isconnected'] = self.interface.isconnected()
    ret['curr'] = self.interface.ifconfig()
    return ret

  def _hostname(self, opts):
    name = opts['name']
    self.interface.config(dhcp_hostname=name)
    cfg = self.load()
    cfg['dhcp_hostname'] = name
    self.save(cfg)

  def _connect(self, opts):
    ssid = opts['ssid']
    passwd = opts['passwd']
    self.interface.connect(ssid, passwd)
    cfg = self.load()
    cfg['ssid'] = ssid
    cfg['passwd'] = passwd
    self.save(cfg)

  def _scan(self):
    nets = []
    for net in self.interface.scan():
      if net[0] not in nets:
        nets.append(net[0])
    return nets

  def status(self, req, res):
    yield from ok(res, self._status())

  def set(self, req, res):
    yield from req.read_form_data()
    opts = {}
    for key, value in req.form.items():
      opts[key] = value
    if 'name' in opts:
      self._hostname(opts)
    if 'ssid' in opts and 'passwd' in opts:
      self._connect(opts)
    yield from self.status(req, res)

  def scan(self, req, res):
    yield from ok(res, self._scan())

model = Model()
