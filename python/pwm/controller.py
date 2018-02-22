import picoweb
from pwm import model
import logging
logger = logging.getLogger(__name__)
from util import error, notFound

def get(req, res):
  yield from picoweb.jsonify(res, model.get())

def set(req, res):
  yield from req.read_form_data()
  opts = {
    'device': req.form['device'][0],
    'value': int(req.form['value'][0])
  }
  try:
    model.set(opts)
    yield from picoweb.jsonify(res, {})
  except:
    error(req, res, "{} not found".format(opts['device']))

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  logger.info('{} {}'.format(req.method, req.path))
  yield from ret.get(req.method, notFound)(req, res)
  import gc
  gc.collect()

app = picoweb.WebApp(__name__)
app.route('/')(method)
