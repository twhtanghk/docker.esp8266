import ujson
from config import model
import logging
logger = logging.getLogger(__name__)

def device(pin):
  import machine
  return machine.PWM(machine.Pin(pin))

filename = '/pwm.json'

def factory():
  from pwm import factory
  model.save(filename, factory.cfg())

def boot():
  from util import exists
  if not exists(filename):
    factory()
  cfg = model.load(filename)
  for name in cfg:
    pin = cfg[name]['pin']
    default = cfg[name]['default']
    dev = device(pin)
    dev.freq(1024)
    dev.duty(default)
  logger.info(ujson.dumps(cfg))

def get():
  cfg = model.load(filename)
  for name in cfg:
    pin = cfg[name]['pin']
    dev = device(pin)
    cfg[name]['value'] = dev.duty()
  return cfg

def update(opts):
  cfg = model.load(filename)
  cfg[opts['device']] = {
    'pin': opts['pin'],
    'default': opts['default']
  }
  model.save(filename, cfg)
  
def duty(opts):
  cfg = model.load(filename)[opts['device']]
  device(cfg['pin']).duty(opts['value'])
