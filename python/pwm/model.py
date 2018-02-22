import ujson
from config import model
import machine
import logging
logger = logging.getLogger(__name__)

def device(pin):
  return machine.PWM(machine.Pin(pin))

def config():
  return model.load()['pwm']

def boot():
  cfg = config()
  for name in cfg:
    pin = cfg[name]['pin']
    default = cfg[name]['default']
    dev = device(pin)
    dev.freq(1024)
    dev.duty(default)
  logger.info(ujson.dumps(cfg))

def get():
  cfg = config()
  for name in cfg:
    pin = cfg[name]['pin']
    dev = device(pin)
    cfg[name]['value'] = dev.duty()
  return cfg

def set(opts):
  cfg = config()
  name = opts['device']
  pin = cfg[name]['pin']
  value = opts['value']
  device(pin).duty(value)
  logger.info("set {} pin {} value {}".format(device, pin, value))
