import network
import ujson

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

def exists(filename):
  try:
    import os
    os.stat(filename)
    return True
  except OSError:
    return False

def config():
  import ubinascii
  mac = ap_if.config('mac')
  mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
  return {
    'name': 'TT{}'.format(mac),
    'mqtt': {
      'user': '',
      'password': ''
    }
  }

filename = '/config.json'
def load(factory):
  if not exists(filename):
    save(factory)
  f = open(filename)
  data = ujson.load(f)
  f.close()
  return data

def save(data):
  f = open(filename, 'w')
  ujson.dump(data, f)
  f.close()
  
def factoryAP():
  ap_if.active(True)
  ap_if.config(essid=config()['name'], password='password')

def factorySTA():
  sta_if.active(True)
  sta_if.config(dhcp_hostname=config()['name'])

def factory(req, res):
  factoryAP()
  factorySTA()
  save(config())
  yield from res.ok()
  
async def reboot(req, res):
  await res.ok()
  from uasyncio import sleep
  await sleep(1)
  import machine
  machine.reset()

def getAP(req, res):
  yield from res.ok({
    'essid': ap_if.config('essid'),
    'config': ap_if.ifconfig()
  })

def configAP(req, res):
  config = load()
  config['name'] = req.body['essid']
  save(config)
  ap_if.config(essid=req.body['essid'], password=req.body['password'])
  yield from res.ok()

def getSTA(req, res):
  yield from res.ok({
    'essid': sta_if.config('essid'),
    'isconnected': sta_if.isconnected(),
    'curr': sta_if.ifconfig()
  })

def configSTA(req, res):
  config = load()
  sta_if.active(True)
  sta_if.config(dhcp_hostname=config['name'])
  sta_if.connect(req.body['ssid'], req.body['password'])
  yield from res.ok()

def hotspot(req, res):
  sta_if.active(True)
  nets = []
  for net in sta_if.scan():
    if net[0] not in nets:
      nets.append(net[0])
  yield from res.ok(nets)
