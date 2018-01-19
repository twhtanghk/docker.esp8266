import ujson

name = 'config.json'

def load():
  f = open(name)
  data = ujson.loads(f.read())
  f.close()
  return data

def save(data):
  f = open(name, 'w')
  f.write(ujson.dumps(data))
  f.close()

def test():
  from wlan.ap import model
  from wlan.sta import model
  curr = {
    'ap': model.get(),
    'sta': model.get()
  }
  cfg = load()
  cfg['wlan']['ap']['essid'] = "MicroPython-{}".format(curr['ap']['mac'][6:])
  cfg['wlan']['sta']['dhcp_hostname'] = "ESP-{}".format(curr['sta']['mac'][6:])
  save(cfg)
