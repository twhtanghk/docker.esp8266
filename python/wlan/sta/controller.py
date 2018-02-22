import gc
import picoweb
from wlan.sta import model
from util import notFound

def get(req, res):
  yield from picoweb.jsonify(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  model.set(req.form)
  yield from picoweb.jsonify(res, {})

def scan(req, res):
  nets = model.scan()
  yield from picoweb.jsonify(res, nets)
  gc.collect()

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret.get(req.method, notFound)(req, res)
  gc.collect()

app = picoweb.WebApp(__name__)
app.route('/')(method)
app.route('/scan')(scan)
