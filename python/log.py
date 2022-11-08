import sys
import socket
import config
from microdot import Microdot

app = Microdot()

def factory():
  return {
    'ip': '192.168.43.2',
    'port': 8888
  }

cfg = config.read()['log']
ip, port = cfg['ip'], cfg['port']

try:
  # run "socat TCP4-LISTEN:8888,fork -" on server with IP specified below
  addr = socket.getaddrinfo(ip, port)
  logger = socket.socket()
  logger.connect(addr[0][-1])
except:
  logger = sys.stdout

@app.get('/')
def get(req):
  return cfg

@app.put('/')
def set(req):
  if 'ip' in req.json and 'port' in req.json:
    cfg['ip'] = req.json['ip']
    cfg['port'] = req.json['port']
  syscfg = config.read()
  syscfg['log'] = cfg
  config.write(syscfg)
  return cfg
