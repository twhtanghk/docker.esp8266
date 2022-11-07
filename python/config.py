from microdot import Microdot
import ujson as json

pkg = [
  'ap',
  'sta'
]
app = Microdot()
filename = '/config.json'

@app.get('/reset')
def reset(req):
  import machine
  machine.reset()
  return ''

@app.get('/factory')
def factory(req):
  ret = {}
  for i in pkg:
    lib = __import__(i)
    ret[i] = lib.factory()
  return ret

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
  return read()

@app.put('/')
def save(req):
  # validate json data before write back
  data = req.json
  write()
  return ''
