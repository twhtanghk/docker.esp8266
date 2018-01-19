import picoweb
from wlan.ap import model
from util import notFound

def get(req, res):
  yield from picoweb.jsonify(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  opts = {
    'essid': req.form.get('essid', [''])[0],
    'password': req.form.get('password', [''])[0]
  }
  model.set(opts)
  yield from get(req, res)

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  yield from ret.get(req.method, notFound)(req, res)

app = picoweb.WebApp(__name__)
app.route('/')(method)
