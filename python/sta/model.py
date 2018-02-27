import ubinascii
import ujson
import network
from config import model
import logging
logger = logging.getLogger(__name__)

interface = network.WLAN(network.STA_IF)
interface.active(True)

filename = '/sta.json'

def factory():
  from sta import factory
  model.save(filename, factory.cfg())

def boot():
  from util import exists
  if not exists(filename):
    factory()
  cfg = model.load(filename)
  interface.config(dhcp_hostname=cfg['dhcp_hostname'])
  if 'ssid' in cfg:
    interface.connect(cfg['ssid'], cfg['passwd'])
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
  cfg = model.load(filename)
  if 'name' in opts:
    name = opts['name'][0]
    interface.config(dhcp_hostname=name)
    cfg['dhcp_hostname'] = name
  if 'ssid' in opts and 'passwd' in opts:
    ssid = opts['ssid'][0]
    passwd = opts['passwd'][0]
    interface.connect(ssid, passwd)
    cfg['ssid'] = ssid
    cfg['passwd'] = passwd
  model.save(filename, cfg)

def scan():
  nets = []
  for net in interface.scan():
    if net[0] not in nets:
      nets.append(net[0])
  return nets
