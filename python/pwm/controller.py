import picoweb
from pwm import model
from util import error, notFound

def get(req, res):
  yield from picoweb.jsonify(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  device = req.form['device']
  cfg = model.cfg()
  if device not in cfg:
    error(req, res, "{} not found".format(device))
  model.set(req.form)
  model.get(req, res)

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  logger.info('{} {}'.format(req.method, req.path))
  yield from ret.get(req.method, notFound)(req, res)

app = picoweb.WebApp(__name__)
app.route('/')(method)
