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
  from wlan.ap import model
  mac = model.get()['mac'][6:]
  essid = "MicroPython-{}".format(mac)
  name = "ESP-{}".format(mac)
  cfg = {
   'wlan': {
     'sta': {
       'dhcp_hostname': name
     },
     'ap': {
       'essid': essid,
       'password': 'micropythoN'
     }
   }
  }
  save(cfg)
