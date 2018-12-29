from config import Config
from util import ok
import ujson
import logging
logger = logging.getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/ddns.json')

  def factory(self):
    self.save({
      'url': 'https://dynupdate.no-ip.com/nic/update',
      'interval': 300,
      'host': '',
      'user': '',
      'pass': ''
    })
    return self

  def setup(self):
    self.cfg = self.load()
    import uasyncio as asyncio
    async def task():
      while True:
        await asyncio.sleep(self.cfg['interval'])
        try:
          self.ddnsupdate()
        except:
          logger.error('update failed')
    loop = asyncio.get_event_loop()
    loop.create_task(task())

  def enabled(self):
    return self.cfg['user'] != '' and self.cfg['pass'] != '' and self.cfg['host'] != ''

  def ddnsupdate(self):
    if self.enabled():
      import urequests as req
      from ubinascii import b2a_base64
      auth = b2a_base64('{}:{}'.format(self.cfg['user'], self.cfg['pass']))
      headers = { 'Authorization': 'Basic {}'.format(auth) }
      url = '{}?{}={}'.format(self.cfg['url'], 'hostname', self.cfg['host'])
      res = req.get(url, headers=headers)
      logger.info(res.status_code)
      res.close()

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
