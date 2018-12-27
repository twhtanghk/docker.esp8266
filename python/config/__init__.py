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
  def __init__(self, model):
    self.model = model

  def factory(self, req, res):
    pkg = (
      'sta',
      'pwm'
    )
    for i in pkg:
      lib = __import__(i)
      lib.model.factory()
    yield from ok(res)

  def reset(self, req, res):
    yield from ok(res)
    import machine
    machine.reset()

  def get(self, req, res):
    req.parse_qs()
    yield from ok(res, model.load(req.form['name'][0]))

  def set(self, req, res):
    yield from req.read_form_data()
    cfg = model.load()
    for key, value in req.form.items():
      cfg[key] = value
    model.save(cfg)
    yield from get(req, res)

  def reset(self, req, res):
    yield from ok(res)
    model.reset()

  def crud(self, req, res):
    ret = {
      'GET': get,
      'PUT': set
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
