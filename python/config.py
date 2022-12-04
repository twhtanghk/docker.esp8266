from microdot import Microdot
import ujson as json

app = Microdot()
filename = '/config.json'
import network
ap = network.WLAN(network.AP_IF)
import ubinascii
mac = ubinascii.hexlify(ap.config('mac')).decode('utf-8')[6:]
name = 'nmea0183-{}'.format(mac)
initCfg = {
  'log': {
    'ip': '192.168.43.2',
    'port': 8888
  },
  'ap': {
    'essid': name,
    'password': '12345678'
  },
  'sta': {
    'dhcp_hostname': name,
    'ssid': None,
    'passwd': None
  },
  'uart': {
    'baudrate': 115200,
    'bits': 8,
    'parity': None,
    'stop': 1
  }
}

def read():
  f = open(filename)
  ret = json.load(f)
  f.close()
  return ret

def write(data):
  f = open(filename, 'w')
  f.write(json.dumps(data))
  f.close()

try:
  import os
  os.stat(filename)
except OSError:
  write(initCfg)

@app.get('/reset')
def reset(req):
  import machine
  machine.reset()
  return ''

@app.get('/factory')
def factory(req):
  write(initCfg)
  return ''

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
  write(data)
  return ''
