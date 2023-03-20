import config
import network
import ubinascii
from microdot import Microdot

app = Microdot()

authmode = {
  network.AUTH_OPEN: 'OPEN',
  network.AUTH_WEP: 'WEP',
  network.AUTH_WPA_PSK: 'WPA_PSK',
  network.AUTH_WPA2_PSK: 'WPA2_PSK',
  network.AUTH_WPA_WPA2_PSK: 'WPA_WPA2_PSK'
}

interface = network.WLAN(network.AP_IF)
interface.active(True)

cfg = config.read()['ap']
essid, password = cfg['essid'], cfg['password']
interface.config(essid=essid, password=password)

@app.get('/')
def get(req):
  ret = {}
  for prop in ['mac', 'essid', 'hidden', 'authmode']:
    ret[prop] = interface.config(prop)
  ret['authmode'] = authmode[ret['authmode']]
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['curr'] = interface.ifconfig()
  return ret

@app.put('/')
def set(req):
  essid, password = req.json['essid'], req.json['password']
  if not essid:
    raise Exception('empty essid')
  if len(password) < 8:
    raise Exception('password min length 8')
  data = config.read()
  data['ap'] = {
    'essid': essid,
    'password': password
  }
  config.write(data)
  return ''
