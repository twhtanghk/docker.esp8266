import picoweb
from pwm import model
from util import handler, ok
import ure as re

def list(req, res):
  if req.method != 'GET':
    raise Exception('{} {} not found'.format(req.method, req.path))
  yield from ok(res, model.get())

def read(req, res):
  yield from ok(res, model.read(req.params))
    
def update(req, res):
  yield from req.read_form_data()
  req.param['value'] = int(req.form['value'][0])
  model.set(req.params)
  yield from ok(res)

def duty(req, res):
  g = url['crud'].match(req.path)
  req.params = {
    'device': g.group(1)
  }
  yield from req.read_form_data()
  req.param['value'] = int(req.form['value'][0])
  model.duty(req.params)
  yield from ok(res)
  
def crud(req, res):
  g = url['crud'].match(req.path)
  req.params = {
    'device': g.group(1)
  }
  ret = {
    'GET': read,
    'PUT': update
  }
  yield from ret[req.method](req, res)
