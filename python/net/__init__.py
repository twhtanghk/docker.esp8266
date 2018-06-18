from config import Config
from util import ok
import ujson
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/net.json')

  def factory(self):
    self.save({
      'host': None,
      'port': None,
    })
    return self

  def setup(self):
    self.cfg = self.load()
    if self.enabled():
      import uasyncio as asyncio
      async def gps():
        try:
          await asyncio.sleep(10)
          reader, writer = await asyncio.open_connection(host=self.cfg['host'], port=self.cfg['port'])
          self.reader = reader
          self.writer = writer
        except:
          logger.info('connection error')
      loop = asyncio.get_event_loop()
      loop.run_until_complete(gps())
      async def task():
        import uart
        while true:
          line = await self.reader.readline()
          logger.info(line)
          uart.model.writer.awrite(line)
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
