import ujson

def preflight(req, res):
  yield from res.ok()

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

def headerParser(req, res):
  l = yield from req.reader.readline()
  (method, url, version) = l.decode('utf-8').split(" ")
  req.action = "%s %s" % (method, url)
  req.header = {}
  while True:
    l = yield from req.reader.readline()
    if l == b"\r\n":
      break
    k, v = l.split(b":", 1)
    req.header[k] = v.strip()

def bodyParser(req, res):
  yield from headerParser(req, res)
  if b'Content-Length' in req.header:
    len = int(req.header[b'Content-Length'])
    data = yield from req.reader.readexactly(len)
    req.body = ujson.loads(data)
  else:
    req.body = {}

def static(req, res):
  file = req.url_match.group(1)
  if file == '/':
    file = '/index.html'
  file = 'static' + file
  if b'gzip' in req.header[b'Accept-Encoding']:
    gz = file + '.gz'
    try:
      import os
      os.stat(gz)
      res.set({'Content-Encoding': 'gzip'})
      yield from res.sendfile(gz)
      return
    except OSError:
      pass
  yield from res.sendfile(file)

class Req:
  def __init__(self, reader):
    self.reader = reader

class Res:
  def __init__(self, writer):
    self.writer = writer
    self.header = {}

  def set(self, header):
    self.header.update(header)

  def flushHeaders(self):
    for k, v in self.header.items():
      yield from self.writer.awrite("%s: %s\r\n" % (k, v))
    yield from self.writer.awrite("\r\n")

  def ok(self, data=None):
    yield from self.writer.awrite("HTTP/1.1 200 OK\r\n")
    if data != None:
      data = ujson.dumps(data)
      yield from self.writer.awrite("Content-Length: %s\r\n" % len(data))
      yield from self.flushHeaders()
      yield from self.writer.awrite(data)
    else:
      yield from self.writer.awrite("\r\n")

  def err(self, code, msg):
    yield from self.writer.awrite("HTTP/1.1 %s %s\r\n\r\n" % (code, msg))

  def mime(self, fname):
    if fname.endswith('.gz'):
      fname = fname[:-len('.gz')]
    if fname.endswith('.html'):
      return 'text/html'
    if fname.endswith('.css'):
      return 'text/css'
    if fname.endswith('.png') or fname.endswith('.jpg'):
      return 'image'
    return 'text/plain'
    
  def sendfile(self, fname):
    try:
      f = open(fname, 'rb')
      self.set({
        "Content-Type": self.mime(fname)
      })
      yield from self.writer.awrite("HTTP/1.1 200 OK\r\n")
      yield from self.flushHeaders()
      buf = bytearray(64)
      while True:
        l = f.readinto(buf)
        if not l:
          break
        yield from self.writer.awrite(buf, 0, l)
    except Exception as e:
      print(e)
      yield from self.err(500, 'Internal Server Error')
  
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
      yield from bodyParser(req, res)
      logger(req, res)
      json(req, res)
      cors(req, res)
      for route in self.routes:
        if route['action'].match(req.action):
          req.url_match = route['action'].match(req.action)
          yield from route['mw'](req, res)
          return
      res.err(404, 'Not Found')
    except Exception as e:
      print(e)
      res.err(500, 'Internal Server Error')
    finally:
      yield from writer.aclose()
