import ujson
import picoweb
from config import model
from util import handler, ok

def get(req, res):
  req.parse_qs()
  yield from ok(res, model.load(req.form['name'][0]))

def set(req, res):
  yield from req.read_form_data()
  cfg = model.load()
  for key, value in req.form.items():
    cfg[key] = value
  model.save(cfg)
  yield from get(req, res)

def reset(req, res):
  yield from ok(res)
  model.reset()

def factory(req, res):
  model.factory()
  import ap
  yield from ap.get(req, res)

def crud(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret[req.method](req, res)

class Config:
  def __init__(self, filename):
    self.filename = filename

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
