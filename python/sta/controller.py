import picoweb
from sta import model
from util import handler, ok

def get(req, res):
  yield from ok(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  model.set(req.form)
  yield from ok(res)

def scan(req, res):
  nets = model.scan()
  yield from ok(res, nets)

def crud(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret[req.method](req, res)
