from config import Config
from util import ok
import usyslog
import ujson
import usocket
import logging

class Logger(logging.Logger):
  def log(self, level, msg, *args):
    if level >= (self.level or logging._level):
      msg = "{}:{}:{}:{}".format(logging._level_dict[level], self.name, msg, args)
      if hasattr(model, 'address') and model.address != None:
        logging._stream.sendto(msg, model.address)

def getLogger(name):
  if name in logging._loggers:
    return logging._loggers[name]
  l = Logger(name)
  logging._loggers[name] = l
  return l

logger = getLogger(__name__)

class Model(Config):
  def __init__(self):
    Config.__init__(self, 'log.json')

  def factory(self):
    self.save({
      'ip': '192.168.0.104',
      'port': 514,
      'active': False
    })

  def boot(self):
    Config.boot(self)
    cfg = self.load()
    if cfg['active']:
      client = usyslog.UDPClient(ip=cfg['ip'], port=cfg['port'])
      self.address = usocket.getaddrinfo(cfg['ip'], cfg['port'])[0][4]
      self.stream = client._sock
      logging.basicConfig(stream=client._sock)
    else:
      self.address = None
    logger.info(ujson.dumps(cfg))

  def _set(self, opts={}):
    cfg = self.load()
    cfg.update(opts)
    self.save(cfg)
    self.boot()
    return cfg 

  def status(self, req, res):
    yield from ok(res, self.load())

  def set(self, req, res):
    yield from req.read_form_data()
    req.form['port'] = int(req.form['port'])
    req.form['active'] = req.form['active'] == 'true'
    yield from ok(res, self._set(req.form))

model = Model()
