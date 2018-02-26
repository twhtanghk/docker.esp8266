import picoweb
from wlan.sta import model
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

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret[req.method](req, res)

app = picoweb.WebApp(__name__, serve_static=False)
app.route('/')(handler(method))
app.route('/scan')(handler(scan))
