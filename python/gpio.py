import config
from machine import Pin
from microdot import Microdot

app = Microdot()

@app.get('/')
def get(req):
  return config.read()['gpio']
  
@app.put('/<pin>/name/<name>')
def name(req, pin, name):
  cfg = config.read()
  pin = int(pin)
  if pin == cfg['gpio']['pin']:
    cfg['gpio']['name'] = name
  else:
    return "pin {} not supported".format(pin), 500
  config.write(cfg)
  return ''

# name: pin name
# value: 0, 1 for off, on
@app.put('/<name>/<value>')
def set(req, name, value):
  cfg = config.read()['gpio']
  for i in cfg:
    if i.name == name:
      Pin(i.pin).value(value)
      return {'state': value}
  return "pin {} not found".format(name), 500

@app.put('/<name>/on')
def on(req, name):
  return set(req, name, 1)

@app.put('/<name>/off')
def off(req, name):
  return set(req, name, 0)
 
@app.get('/<name>')
def state(req, name):
  cfg = config.read()['gpio']
  for i in cfg:
    if i.name == name:
      return {
        'name': i.name,
        'pin': i.pin,
        'state': Pin(i.pin).value()
      }
  return "pin {} not found".format(name), 500

@app.get('/')
def list(req):
  cfg = config.read()['gpio']
  ret = []
  for i in cfg:
    name, pin, state = i
    for name in self.cfg:
      ret.append({
        'name': name,
        'pin': pin,
        'state': Pin(pin).value
      })
  return ret
