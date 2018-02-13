import ubinascii
import ujson
import network
from config import model
import logging
logger = logging.getLogger(__name__)

interface = network.WLAN(network.STA_IF)
interface.active(True)

def boot():
  cfg = model.load()
  opts = cfg['wlan']['sta']
  interface.config(dhcp_hostname=opts['dhcp_hostname'])
  if 'ssid' in opts:
    interface.connect(opts['ssid'], opts['passwd'])
  logger.info(ujson.dumps(get()))

def get():
  ret = {}
  for prop in ['mac', 'dhcp_hostname']:
    ret[prop] = interface.config(prop)
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['isconnected'] = interface.isconnected()
  ret['curr'] = interface.ifconfig()
  return ret

def set(opts):
  cfg = model.load()
  if 'name' in opts:
    name = opts['name'][0]
    interface.config(dhcp_hostname=name)
    cfg['wlan']['sta']['dhcp_hostname'] = name
  if 'ssid' in opts and 'passwd' in opts:
    ssid = opts['ssid'][0]
    passwd = opts['passwd'][0]
    interface.connect(ssid, passwd)
    cfg['wlan']['sta']['ssid'] = ssid
    cfg['wlan']['sta']['passwd'] = passwd
  model.save(cfg)

def scan():
  nets = []
  for net in interface.scan():
    if net[0] not in nets:
      nets.append(net[0])
  return nets
