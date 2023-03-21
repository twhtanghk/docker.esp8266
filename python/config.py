from microdot import Microdot
from machine import Pin
import ujson as json

app = Microdot()
filename = '/config.json'

def read():
  f = open(filename)
  ret = json.load(f)
  f.close()
  return ret

def write(data):
  f = open(filename, 'w')
  f.write(json.dumps(data))
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

@app.put('/')
def save(req):
  cfg = read()
  # validate json data before write back
  cfg['current'] = req.json
  write(cfg)
  return ''
