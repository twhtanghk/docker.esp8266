import ujson
from config import model
import machine
import logging
logger = logging.getLogger(__name__)

def config():
  return model.load()['pwm']

def boot():
  cfg = config()
  for device in cfg:
    pin = cfg[device]['pin']
    default = cfg[device]['default']
    dev = machine.PWM(machine.Pin(pin))
    dev.freq(1024)
    dev.duty(default)
  logger.info(ujson.dumps(cfg))

def get():
  cfg = cfg()
  for device in cfg:
    pin = cfg[device]['pin']
    dev = machine.PWM(machine.Pin(pin))
    cfg[device]['value'] = dev.duty()
  return cfg

def set(opts):
  cfg = cfg()
  device = opts['device']
  pin = cfg[device].pin
  value = opts['value']
  machine.Pin(pin).duty(value)
  logger.info("set {} pin {} value {}".format(device, pin, value))
