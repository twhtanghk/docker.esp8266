import config
import network
import ubinascii
from microdot import Microdot

app = Microdot()
interface = network.WLAN(network.STA_IF)
interface.active(True)

cfg = config.read()['current']['sta']
if 'dhcp_hostname' in cfg:
  interface.config(dhcp_hostname=cfg['dhcp_hostname'])

@app.get('/')
def get(req):
  ret = {}
  for prop in ['mac', 'dhcp_hostname']:
    ret[prop] = interface.config(prop)
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['isconnected'] = interface.isconnected()
  ret['curr'] = interface.ifconfig()
  return ret

@app.put('/')
def set(req):
  opts = req.json
  cfg = config.read()
  if 'name' in opts:
    name = opts['name']
    interface.config(dhcp_hostname=name)
    cfg['current']['sta']['dhcp_hostname'] = name
    config.write(cfg)
  if 'ssid' in opts and 'passwd' in opts:
    ssid, passwd = opts['ssid'], opts['passwd']
    interface.connect(ssid, passwd)
  return ''

@app.get('/scan')
def scan(req):
  nets = []
  for net in interface.scan():
    if net[0] not in nets:
      nets.append(net[0])
  return nets
