import ubinascii
import network
from config import model

interface = network.WLAN(network.STA_IF)
interface.active(True)

def boot():
  cfg = model.load()
  opts = cfg['wlan']['sta']
  interface.config(dhcp_hostname=opts['dhcp_hostname'])
  if 'ssid' in opts:
    interface.connect(opts.ssid, opts.passwd)

def get():
  ret = {}
  for prop in ['mac', 'dhcp_hostname']:
    ret[prop] = interface.config(prop)
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['curr'] = interface.ifconfig()
  return ret

def set(opts):
  cfg = model.load()
  name = opts.get('name', [''])[0]
  if name is not None:
    interface.config(dhcp_hostname=name)
    cfg['wlan']['sta']['dhcp_hostname'] = name
  ssid = opts.get('ssid', [''])[0]
  passwd = opts.get('passwd', [''])[0]
  if ssid is not None:
    interface.connect(ssid, passwd)
    cfg['wlan']['sta']['ssid'] = ssid
    cfg['wlan']['sta']['passwd'] = passwd

def scan():
  nets = []
  for net in interface.scan():
    if net[0] not in nets:
      nets.append(net[0])
  return nets
