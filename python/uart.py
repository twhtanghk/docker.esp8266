import config
from machine import UART
from microdot import Microdot

app = Microdot()

cfg = config.read()['uart']
interface = UART(0)
interface.init(**cfg)

@app.get('/')
def get(req):
  return cfg

def valid(data):
  if data['baudrate'] not in [300, 600, 1200, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 250000, 460800]:
    raise ValueError('baudrate')
  if data['bits'] not in [7, 8]:
    raise ValueError('bits')
  if data['parity'] not in [None, 0, 1]:
    raise ValueError('parity')
  if data['stop'] not in [1, 2]:
    raise ValueError('stop')

@app.put('/')
def set(req):
  opts = req.json
  valid(opts)
  cfg = config.read()
  cfg['uart'] = opts
  config.write(cfg)
  return ''
