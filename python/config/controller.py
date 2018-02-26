import picoweb
from config import model
from util import handler, ok

def get(req, res):
  yield from ok(res, model.load())

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
  from wlan.ap import controller
  yield from controller.get(req, res)

def crud(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret[req.method](req, res)
