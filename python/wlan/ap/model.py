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

def boot():
  cfg = model.load()
  opts = cfg['wlan']['ap']
  interface.config(essid=opts['essid'], password=opts['password'])
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
  cfg = model.load()
  essid = opts['essid']
  password = opts['password']
  cfg['wlan']['ap']['essid'] = opts['essid']
  cfg['wlan']['ap']['password'] = opts['password']
  logger.info(ujson.dumps(cfg))
  model.save(cfg)
