import sys
import socket
import config
from microdot import Microdot

app = Microdot()
logger = None

cfg = config.read()['current']
name, ip, port = cfg['ap']['essid'], cfg['log']['ip'], cfg['log']['port']

try:
  # run "socat TCP4-LISTEN:8888,fork -" on server with IP specified below
  addr = socket.getaddrinfo(ip, port)
  logger = socket.socket()
  logger.connect(addr[0][-1])
except:
  logger = sys.stdout

@app.get('/')
def get(req):
  return {'ip': ip, 'port': port}

@app.put('/')
def set(req):
  if 'ip' in req.json and 'port' in req.json:
    syscfg = config.read()
    syscfg['current']['log']['ip'] = req.json['ip']
    syscfg['current']['log']['port'] = req.json['port']
    config.write(syscfg)
    return syscfg['current']['log']
  return {error: 'params ip and port not available'}, 500

def info(module, msg):
  logger.write('{}/{}: {}\n'.format(name, module, msg))
