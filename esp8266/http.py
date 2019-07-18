import ujson

def logger(req, res):
  print(req.action)

def json(req, res):
  res.set({
    "Content-Type": "application/json"
  })

def cors(req, res):
  res.set({
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, PUT, GET, DELETE, OPTIONS'
  })

class Req:
  def __init__(self, reader):
    self.reader = reader

  def parse(self):
    l = yield from self.reader.readline()
    (method, url, version) = l.decode('utf-8').split(" ")
    self.action = "%s %s" % (method, url)
    self.header = yield from self._header()
    self.body = {}
    if b'Content-Length' in self.header:
      self.body = yield from self._body()

  def _header(self):
    ret = {}
    while True:
      l = yield from self.reader.readline()
      if l == b"\r\n":
        break
      k, v = l.split(b":", 1)
      ret[k] = v.strip()
    return ret

  def _body(self):
    len = int(self.header[b'Content-Length'])
    data = yield from self.reader.readexactly(len)
    return ujson.loads(data)

class Res:
  def __init__(self, writer):
    self.writer = writer
    self.header = {}

  def set(self, header):
    self.header.update(header)

  def flushHeaders(self):
    for k, v in self.header.items():
      yield from self.writer.awrite("%s: %s\r\n" % (k, v))

  def ok(self, data=None):
    yield from self.writer.awrite("HTTP/2 200\r\n")
    yield from self.flushHeaders()
    if data != None:
      data = ujson.dumps(data)
      yield from self.writer.awrite("Content-Length: %s\r\n\r\n" % len(data))
      yield from self.writer.awrite(data)
    else:
      yield from self.writer.awrite("\r\n")

  def err(self, code, msg):
    yield from self.writer.awrite("HTTP/2 %s %s\r\n\r\n" % (code, msg))

  def mime(self, fname):
    if fname.endswith('.html'):
      return 'text/html'
    if fname.endswith('.css'):
      return 'text/css'
    if fname.endswith('.png') or fname.endswith('.jpg'):
      return 'image'
    return 'text/plain'
    
  def sendfile(self, fname):
    self.set({
      "Content-Type": self.mime(fname)
    })
    yield from self.writer.awrite("HTTP/2 200\r\n")
    self.flushHeaders()
    try:
      import pkg_resources
      with pkg_resources.resource_stream(__name__, fname) as f:
        buf = bytearray(64)
        while True:
          l = f.readinot(buf)
          if not l:
            break
          yield from self.writer.awrite(buf, 0, l)
    except Exception as e:
      print(e)
      self.err(500, 'Internal Server Error')
  
import ure as re

class App:
  def __init__(self):
    self.routes = []

  def method(self, method, url, mw):
    self.routes.append({
      'action': re.compile('%s %s' % (method, url)),
      'mw': mw
    })

  def options(self, url, mw):
    self.method('OPTIONS', url, mw)

  def get(self, url, mw):
    self.method('GET', url, mw)

  def post(self, url, mw):
    self.method('POST', url, mw)

  def put(self, url, mw):
    self.method('PUT', url, mw)

  def delete(self, url, mw):
    self.method('DELETE', url, mw)

  def all(self, url, mw):
    self.method('.*', url, mw)

  def handle(self, reader, writer):
    try:
      res = Res(writer)
      req = Req(reader)
      yield from req.parse()
      logger(req, res)
      json(req, res)
      cors(req, res)
      for route in self.routes:
        if route['action'].match(req.action):
          yield from route['mw'](req, res)
          return
      res.err(404, 'Not Found')
    except Exception as e:
      print(e)
      res.err(500, 'Internal Server Error')
    finally:
      yield from writer.aclose()
