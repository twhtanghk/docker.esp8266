from microdot import Microdot
import ujson as json

app = Microdot()
filename = '/config.json'

@app.get('/reset')
def reset(req):
  import machine
  machine.reset()
  return ''

@app.get('/factory')
def factory(req):
  from project import pkg
  ret = {}
  for i in pkg:
    if i != 'config':
      lib = __import__(i)
      ret[i] = lib.factory()
  return ''

def read():
  try:
    f = open(filename)
    ret = json.load(f)
    f.close()
    return ret
  except:
    ret = factory(None)
    write(ret)
    return ret

def write(data):
  f = open(filename, 'w')
  f.write(json.dumps(data))
  f.close()

@app.get('/')
def load(req):
  ret = read()
  try:
    del ret['ap']['password']
    del ret['sta']['passwd']
  except KeyError:
    pass
  return ret

@app.put('/')
def save(req):
  # validate json data before write back
  data = req.json
  write()
  return ''
