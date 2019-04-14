import ujson
from config import Config
from util import handler, ok
import ure as re
import log as logging
logger = logging.getLogger(__name__)

class Controller:
  def __init__(self, model):
    self.model = model

  def list(self, req, res):
    yield from ok(res, model.list())

  def read(self, req, res):
    yield from ok(res, model.read(req.params))
    
  def update(self, req, res):
    yield from req.read_form_data()
    req.params = {
      'device': req.url_match.group(1),
      'pin': int(req.form['pin']),
      'default': int(req.form['default'])
    }
    model.update(req.params)
    yield from ok(res)

  def duty(self, req, res):
    req.params = {
      'device': req.url_match.group(1)
    }
    yield from req.read_form_data()
    req.params['value'] = int(req.form['value'])
    self.model.duty(req.params)
    yield from ok(res)
  
  def crud(self, req, res):
    req.params = {
      'device': req.url_match.group(1)
    }
    ret = {
      'GET': self.read,
      'PUT': self.update
    }
    yield from ret[req.method](req, res)

class Model(Config):
  def __init__(self):
    Config.__init__(self, 'pwm.json')

  def factory(self):
    self.save({
      'fan': {
        'pin': 12,
        'default': 600
      }
    })

  def device(self, pin):
    import machine
    return machine.PWM(machine.Pin(pin))

  def boot(self):
    Config.boot(self)
    cfg = self.load()
    for name in cfg:
      pin = cfg[name]['pin']
      default = cfg[name]['default']
      dev = self.device(pin)
      dev.freq(1024)
      dev.duty(default)
    logger.info(ujson.dumps(cfg))

  def list(self):
    cfg = self.load()
    for name in cfg:
      pin = cfg[name]['pin']
      cfg[name] = {
        'pin': pin,
        'default': cfg[name]['default'],
        'value': self.device(pin).duty()
      }
    return cfg
    
  def read(self, opts):
    cfg = self.load()
    name = opts['device']
    pin = cfg[name]['pin']
    cfg[name]['value'] = self.device(pin).duty()
    return cfg[name]

  def update(self, opts):
    cfg = self.load()
    cfg[opts['device']] = {
      'pin': opts['pin'],
      'default': opts['default']
    }
    self.save(cfg)
  
  def duty(self, opts):
    cfg = self.load()
    self.device(cfg[opts['device']]['pin']).duty(opts['value'])

model = Model()
ctl = Controller(model)
