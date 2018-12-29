from config import Config
from util import ok
import ujson
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/gps.json')

  def factory(self):
    self.save({
      'host': None,
      'port': 2947,
      'uart': 2,
      'baudrate': 4800,
      'bits': 8,
      'parity': None,
      'stop': 1
    })
    return self

  def setup(self):
    self.cfg = self.load()
    if self.enabled():
      import uasyncio as asyncio
      loop = asyncio.get_event_loop()
      async def task():
        import util
        self.gps = await util.uartServer()
      loop.create_task(task())

  def enabled(self):
    return self.cfg['host'] != None and self.cfg['port'] != None

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
