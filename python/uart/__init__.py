from config import Config
from util import ok
import ujson
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/uart.json')

  def factory(self):
    self.save({
      'enable': False,
      'speed': 4800,
      'bits': 8,
      'parity': None,
      'stop': 1,
    })
    return self

  def setup(self):
    self.cfg = self.load()
    if self.cfg['enable']:
      from machine import UART
      self.uart = UART(2,
        baudrate=self.cfg['speed'],
        bits=self.cfg['bits'],
        parity=self.cfg['parity'],
        stop=self.cfg['stop']
      )
      import uasyncio as asyncio
      self.reader = asyncio.StreamReader(self.uart)
      self.writer = asyncio.StreamWriter(self.uart, {})
      async def task():
        while True:
          line = await self.reader.readline()
          logger.info(line)
      loop = asyncio.get_event_loop()
      loop.create_task(task())

  def set(self, cfg):
    self.cfg = cfg
    self.save(cfg)
    return self.get(name)

  def get(self):
    return self.cfg

class Controller:
  def __init__(self, model):
    self.model = model

  def read(self, req, res):
    yield from ok(res, self.model.get(name))

  def update(self, req, res):
    yield from req.read_form_data()
    name = req.params['name']
    value = ujson.loads(req.form['value'][0])
    yield from ok(res, self.model.set(name, value))

  def crud(self, req, res):
    ret = {
      'GET': self.read,
      'PUT': self.update
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
