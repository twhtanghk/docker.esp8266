from config import Config
from util import ok
import ujson

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/ddns.json')
    self.pins = {}

  def factory(self):
    self.save({
      'url': 'https://dynupdate.no-ip.com/nic/update'
      'enable': False,
      'interval': 5000,
      'host': '',
      'user': '',
      'pass': ''
    })
    return self

  def boot(self):
    from util import exists
    if not exists(self.filename):
      self.factory()

  def setup(self):
    self.cfg = self.load()
    import asyncio as asyncio
    async def dnsupdate(cfg):
      if cfg.enable:
        print('dnsupdate')
      await asyncio.sleep_ms(cfg.interval)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dnsupdate())   

  def set(self, cfg):
    self.cfg = cfg
    self.save(cfg)
    return self.get(name)

  def get(self):
    return self.cfg

class Controller:
  def __init__(self, model):
    self.model = model

  def list(self, req, res):
    yield from ok(res, self.model.list())

  def read(self, req, res):
    yield from ok(res, self.model.get(name))

  def update(self, req, res):
    yield from req.read_form_data()
    name = req.params['name']
    value = ujson.loads(req.form['value'][0])
    yield from ok(res, self.model.set(name, value))

  def crud(self, req, res):
    req.params = {
      'name': req.url_match.group(1)
    }
    ret = {
      'GET': self.read,
      'PUT': self.update
    }
    yield from ret[req.method](req, res)

model = Model()
ctl = Controller(model)
