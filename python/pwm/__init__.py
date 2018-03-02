import picoweb
from pwm import model
from util import handler, ok
import ure as re

def list(req, res):
  yield from ok(res, model.list())

def read(req, res):
  yield from ok(res, model.read(req.params))
    
def update(req, res):
  yield from req.read_form_data()
  req.params = {
    'device': req.url_match.group(1),
    'pin': int(req.form['pin'][0]),
    'default': int(req.form['default'][0])
  }
  model.update(req.params)
  yield from ok(res)

def duty(req, res):
  req.params = {
    'device': req.url_match.group(1)
  }
  yield from req.read_form_data()
  req.params['value'] = int(req.form['value'][0])
  model.duty(req.params)
  yield from ok(res)
  
def crud(req, res):
  req.params = {
    'device': req.url_match.group(1)
  }
  ret = {
    'GET': read,
    'PUT': update
  }
  yield from ret[req.method](req, res)
