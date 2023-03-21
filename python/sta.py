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
if 'ssid' in cfg and 'passwd' in cfg:
  interface.connect(cfg['ssid'], cfg['passwd'])

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
    cfg['sta']['dhcp_hostname'] = name
  if 'ssid' in opts and 'passwd' in opts:
    ssid = opts['ssid']
    passwd = opts['passwd']
    interface.connect(ssid, passwd)
    cfg['sta']['ssid'] = ssid
    cfg['sta']['passwd'] = passwd
  config.write(cfg)
  return ''

@app.get('/scan')
def scan(req):
  nets = []
  for net in interface.scan():
    if net[0] not in nets:
      nets.append(net[0])
  return nets
