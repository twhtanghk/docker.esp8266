from config import Config
from machine import Pin
from util import ok
import ujson

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/gpio.json')
    self.pins = {}

  def factory(self):
    self.save({
      'sw13': {
        'id': 13,
        'mode': Pin.OUT
      }
    })
    return self

  def boot(self):
    from util import exists
    if not exists(self.filename):
      self.factory()

  def setup(self):
    self.cfg = self.load()
    for name in self.cfg:
      self.pins[name] = Pin(self.cfg[name]['id'], self.cfg[name]['mode'])

  def set(self, name, value):
    self.pins[name].value(value)
    return self.get(name)

  def on(self, name):
    return self.set(name, 1)

  def off(self, name):
    return self.set(name, 0)
 
  def get(self, name):
    return {
      'name': name,
      'pin': self.cfg[name]['id'],
      'value': self.pins[name].value()
    }

  def list(self):
    ret = []
    for name in self.cfg:
      ret.append(self.get(name))
    return ret

class Controller:
  def __init__(self, model):
    self.model = model

  def list(self, req, res):
    yield from ok(res, self.model.list())

  def read(self, req, res):
    yield from ok(res, self.model.get(req.params['name']))

  def update(self, req, res):
    yield from req.read_form_data()
    name = req.params['name']
    value = ujson.loads(req.form['value'][0])
    yield from ok(res, self.model.set(name, value))

  def crud(self, req, res):
    req.params = {
      'name': req.url_match.group(1)
    }
    ret = {
      'GET': self.read,
      'PUT': self.update
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
