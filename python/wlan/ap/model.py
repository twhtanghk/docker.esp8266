import ubinascii
import network
from config import model

interface = network.WLAN(network.AP_IF)
interface.active(True)

def boot():
  cfg = model.load()
  opts = cfg['wlan']['ap']
  interface.config(essid=opts['essid'], password=opts['password'])

def get():
  ret = {}
  for prop in ['mac', 'essid', 'hidden', 'authmode']:
    ret[prop] = interface.config(prop)
  ret['mac'] = ubinascii.hexlify(ret['mac']).decode('utf-8')
  ret['curr'] = interface.ifconfig()
  return ret

def set( opts):
  interface.config(essid=opts['essid'], password=opts['password'])
  # update config.json
  cfg = model.load()
  cfg['wlan']['ap']['essid'] = opts['essid']
  cfg['wlan']['ap']['password'] = opts['password']
  model.save(cfg)
