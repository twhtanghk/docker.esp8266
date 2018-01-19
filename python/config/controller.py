import picoweb
from config import model
from util import notFound
import logging
logger = logging.getLogger(__name__)

def get(req, res):
  yield from picoweb.jsonify(res, model.load())

def set(req, res):
  yield from req.read_form_data()
  cfg = model.load()
  for key, value in req.form.items():
    cfg[key] = value
  model.save(cfg)
  yield from get(req, res)

def method(req, res):
  ret = {
    'GET': get,
    'PUT': set
  }
  logger.info('{0} {1}'.format(req.method, req.path))
  yield from ret.get(req.method, notFound)(req, res)

app = picoweb.WebApp(__name__)
app.route('/')(method)
