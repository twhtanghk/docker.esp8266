import config
from machine import Pin
from microdot import Microdot

pins = {}
cfg = config.read()['current']['gpio']
for i in cfg:
  mode, pin, name, value = i['mode'], i['pin'], i['name'], i['value']
  pins[name] = Pin(pin, mode, value=value)

app = Microdot()

@app.get('/')
def get(req):
  return config.read()['current']['gpio']
  
@app.post('/<pin>/<name>/<mode>')
def create(req, pin, name):
  cfg = config.read()
  pin = int(pin)
  cfg['current']['gpio'].append({
    'pin': pin,
    'name': name,
    'mode': mode
  })
  config.write(cfg)
  return get(req)

@app.put('/<name>/toggle')
def toggle(req, name):
  return set(req, 0 if pins[name].value() == '1' else 1)
  
@app.put('/<name>/on')
def on(req, name):
  return set(req, name, 1)

@app.put('/<name>/off')
def off(req, name):
  return set(req, name, 0)
 
# name: pin name
# value: 0, 1 for off, on
@app.put('/<name>/<value>')
def set(req, name, value):
  try:
    value = int(value)
    if value not in [0, 1]:
      return "Invalid value {}".format(value), 500
    pins[name].value(value) 
    return state(req, name)
  except:
    return "pin {} not found".format(name), 500

@app.get('/all')
def list(req):
  ret = []
  for name in pins:
    ret.append({
      'name': name,
      'state': pins[name].value()
    })
  return ret

@app.get('/<name>')
def state(req, name):
  try:
      return {'state': str(pins[name].value())}
  except:
    return "pin {} not found".format(name), 500

