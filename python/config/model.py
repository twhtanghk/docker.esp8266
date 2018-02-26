import ujson

pkg = (
  'ap',
  'sta',
  'pwm'
)

def boot():
  for i in pkg:
    lib = __import__(i)
    lib.model.boot()

def load(filename):
  f = open(filename)
  data = ujson.loads(f.read())
  f.close()
  import gc
  gc.collect()
  return data

def save(filename, data):
  f = open(filename, 'w')
  f.write(ujson.dumps(data))
  f.close()

def reset():
  import machine
  machine.reset()

def factory():
  for i in pkg:
    lib = __import__(i)
    lib.model.factory()
