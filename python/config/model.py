import ujson

name = 'config.json'

def boot():
  try:
    import os
    os.stat(name)
  except OSError:
    factory()

def load():
  f = open(name)
  data = ujson.loads(f.read())
  f.close()
  return data

def save(data):
  f = open(name, 'w')
  f.write(ujson.dumps(data))
  f.close()

def reset():
  import machine
  machine.reset()

def factory():
  from config.factory import cfg
  save(cfg())
