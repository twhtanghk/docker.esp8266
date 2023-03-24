from microdot import Microdot
from machine import Pin
import ujson as json

app = Microdot()
filename = '/config.json'

# return {factory: ..., current: ...}
def read():
  f = open(filename)
  ret = json.load(f)
  f.close()
  return ret

# data: {factory: ..., current: ...}
def write(data):
  f = open(filename, 'w')
  json.dump(data, f)
  f.close()

cfg = read()
if 'current' not in cfg:
  cfg['current'] = cfg['factory']
  write(cfg)

@app.get('/reset')
def reset(req):
  import machine
  machine.reset()
  return ''

@app.get('/factory')
def factory(req):
  cfg = read()
  cfg.pop('current', None)
  write(cfg)
  return ''

@app.get('/')
def load(req):
  cfg = read()
  return cfg['current']
