import ujson
import ubinascii
import network
from config import model
import logging
logger = logging.getLogger(__name__)

interface = network.WLAN(network.AP_IF)
interface.active(True)
authmode = {
  network.AUTH_OPEN: 'OPEN',
  network.AUTH_WEP: 'WEP',
  network.AUTH_WPA_PSK: 'WPA_PSK',
  network.AUTH_WPA2_PSK: 'WPA2_PSK',
  network.AUTH_WPA_WPA2_PSK: 'WPA_WPA2_PSK'
}

filename = '/ap.json'

def factory():
  from ap import factory
  model.save(filename, factory.cfg())

def boot():
  from util import exists
  if not exists(filename):
    factory()
  cfg = model.load(filename)
  interface.config(essid=cfg['essid'], password=cfg['password'])
  logger.info(ujson.dumps(get()))

def get():
  ret = {}
  for prop in ['mac', 'essid', 'hidden', 'authmode']:
    ret[prop] = interface.config(prop)
  ret['authmode'] = authmode[ret['authmode']]
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['curr'] = interface.ifconfig()
  return ret

def set(opts):
  cfg = model.load(filename)
  essid = opts['essid']
  password = opts['password']
  cfg['essid'] = opts['essid']
  cfg['password'] = opts['password']
  logger.info(ujson.dumps(cfg))
  model.save(cfg)
