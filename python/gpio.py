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
        'mode': Pin.OPEN_DRAIN,
        'pull': Pin.PULL_UP,
        'value': 1
      }
    })
    return self

  def boot(self):
    Config.boot(self)
    self.cfg = self.load()
    for name in self.cfg:
      self.pins[name] = Pin(self.cfg[name]['id'], self.cfg[name]['mode'], self.cfg[name]['pull'])
      self.pins[name].value(self.cfg[name]['value'])

  def _set(self, name, value):
    self.pins[name].value(value)
    return self._get(name)

  def _on(self, name):
    return self.set(name, 1)

  def _off(self, name):
    return self.set(name, 0)
 
  def _get(self, name):
    return {
      'name': name,
      'pin': self.cfg[name]['id'],
      'mode': self.cfg[name]['mode'],
      'pull': self.cfg[name]['pull'],
      'value': self.pins[name].value()
    }

  def _list(self):
    ret = []
    for name in self.cfg:
      ret.append(self._get(name))
    return ret

  def list(self, req, res):
    yield from ok(res, self._list())

  def read(self, req, res):
    yield from ok(res, self._get(req.params['name']))

  def update(self, req, res):
    yield from req.read_form_data()
    name = req.url_match.group(1)
    value = ujson.loads(req.form['value'][0])
    yield from ok(res, self._set(name, value))

model = Model()
