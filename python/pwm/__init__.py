import ujson
from config import Config
from util import handler, ok
import ure as re
import logging
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
      'pin': int(req.form['pin'][0]),
      'default': int(req.form['default'][0])
    }
    model.update(req.params)
    yield from ok(res)

  def duty(self, req, res):
    req.params = {
      'device': req.url_match.group(1)
    }
    yield from req.read_form_data()
    req.params['value'] = int(req.form['value'][0])
    model.duty(req.params)
    yield from ok(res)
  
  def crud(self, req, res):
    req.params = {
      'device': req.url_match.group(1)
    }
    ret = {
      'GET': read,
      'PUT': update
    }
    yield from ret[req.method](req, res)

class Model(Config):
  def __init__(self):
    Config.__init__(self, 'pwm.json')

  def factory(self):
    return {
      'fan': {
        'pin': 12,
        'default': 600
      }
    }

  def device(self, pin):
    import machine
    return machine.PWM(machine.Pin(pin))

  def setup(self):
    from util import exists
    self.cfg = self.load(filename)
    for name in self.cfg:
      pin = self.cfg[name]['pin']
      default = self.cfg[name]['default']
      dev = self.device(pin)
      dev.freq(1024)
      dev.duty(default)
    logger.info(ujson.dumps(cfg))

  def list(self):
    for name in self.cfg:
      pin = self.cfg[name]['pin']
      self.cfg[name] = {
        'pin': pin,
        'default': cfg[name]['default'],
        'value': device(pin).duty()
      }
    return self.cfg
    
  def read(self, opts):
    name = opts['device']
    pin = self.cfg[name]['pin']
    self.cfg[name]['value'] = self.device(pin).duty()
    return self.cfg[name]

  def update(self, opts):
    self.cfg[opts['device']] = {
      'pin': opts['pin'],
      'default': opts['default']
    }
    self.save(cfg)
  
  def duty(self, opts):
    device(self.cfg['pin']).duty(opts['value'])

model = Model()
ctl = Controller(model)
