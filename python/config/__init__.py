import ujson
import picoweb
from util import handler, ok

class Config:
  def __init__(self, filename):
    self.filename = filename

  def setup(self):
    return

  def boot(self):
    from util import exists
    if not exists(self.filename):
      self.factory()

  def load(self):
    f = open(self.filename)
    data = ujson.load(f)
    f.close()
    return data

  def save(self, data):
    f = open(self.filename, 'w')
    ujson.dump(data, f)
    f.close()
    return self

class Controller:
  def __init__(self):
    return

  def factory(self, req, res):
    import pkg
    for i in pkg.list:
      lib = __import__(i)
      lib.model.factory()
    yield from ok(res)

  def reset(self, req, res):
    yield from ok(res)
    import machine
    machine.reset()

  def crud(self, req, res):
    ret = {
      'GET': self.get,
      'PUT': self.set
    }
    yield from ret[req.method](req, res)

ctl = Controller()
