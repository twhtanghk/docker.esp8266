import picoweb
from wlan.ap import model
from util import handler, ok

def get(req, res):
  yield from ok(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  opts = {
    'essid': req.form.get('essid', [''])[0],
    'password': req.form.get('password', [''])[0]
  }
  if not opts['essid']:
    raise Exception('empty essid')
  if len(opts['password']) < 8:
    raise Exception('password min length 8')
  model.set(opts)
  yield from get(req, res)

def crud(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret[req.method](req, res)
