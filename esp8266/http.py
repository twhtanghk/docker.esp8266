import ujson

async def preflight(req, res, next):
  await res.ok()

async def logger(req, res, next):
  print(req.action)
  await next()

async def json(req, res, next):
  res.set({
    "Content-Type": "application/json"
  })
  await next()

async def cors(req, res, next):
  res.set({
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, PUT, GET, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, X-HTTP-Method-Override'
  })
  await next()

async def methodOverride(req, res, next):
  try:
    (method, url) = req.action.split(" ")
    method = req.header['X-HTTP-Method-Override']
    req.action = "%s %s" % (method, url)
  except KeyError:
    pass
  await next()
    
async def headerParser(req, res):
  l = await req.reader.readline()
  (method, url, version) = l.decode('utf-8').split(" ")
  req.action = "%s %s" % (method, url)
  req.header = {}
  while True:
    l = await req.reader.readline()
    if l == b"\r\n":
      break
    k, v = l.decode('utf-8').split(":", 1)
    req.header[k] = v.strip()

async def bodyParser(req, res, next):
  await headerParser(req, res)
  req.body = None
  try:
    len = int(req.header['Content-Length'])
    if len != 0:
      data = await req.reader.readexactly(len)
      req.body = ujson.loads(data)
  except KeyError:
    pass
  await next()

async def static(req, res, next):
  file = req.url_match.group(1)
  if file == '/':
    file = '/index.html'
  file = 'static' + file
  if 'gzip' in req.header['Accept-Encoding']:
    gz = file + '.gz'
    try:
      import os
      os.stat(gz)
      res.set({'Content-Encoding': 'gzip'})
      await res.sendfile(gz)
      return
    except OSError:
      pass
  await res.sendfile(file)
  await next()

class Req:
  def __init__(self, reader):
    self.reader = reader

class Res:
  def __init__(self, writer):
    self.writer = writer
    self.header = {}

  def set(self, header):
    self.header.update(header)

  async def flushHeaders(self):
    for k, v in self.header.items():
      await self.writer.awrite("%s: %s\r\n" % (k, v))
    await self.writer.awrite("\r\n")

  async def ok(self, data={}):
    await self.writer.awrite("HTTP/1.1 200 OK\r\n")
    data = ujson.dumps(data)
    await self.writer.awrite("Content-Length: %s\r\n" % len(data))
    await self.flushHeaders()
    await self.writer.awrite(data)

  async def err(self, code, msg):
    await self.writer.awrite("HTTP/1.1 %s %s\r\n\r\n" % (code, msg))

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
    
  async def sendfile(self, fname):
    try:
      f = open(fname, 'rb')
      self.set({
        "Content-Type": self.mime(fname)
      })
      await self.writer.awrite("HTTP/1.1 200 OK\r\n")
      await self.flushHeaders()
      buf = bytearray(64)
      while True:
        l = f.readinto(buf)
        if not l:
          break
        await self.writer.awrite(buf, 0, l)
    except Exception as e:
      print(e)
      await self.err(500, 'Internal Server Error')
  
import ure as re

def compose(mw):
  if not isinstance(mw, list):
    raise TypeError("Middleware stack must be an array")
  for fn in mw:
    if not callable(fn):
      raise TypeError("Middleware must be composed of functions")

  async def ret(req, res, next):
    async def dispatch(i):
      if i == len(mw):
        await next()
      else:
        async def remaining():
          await dispatch(i + 1)
        await mw[i](req, res, remaining) 
    await dispatch(0)

  return ret

class Router:
  def __init__(self):
    self.stack = []

  def method(self, method, url, mw):
    self.stack.append({
      'orgAction': '%s %s' % (method, url),
      'action': re.compile('^%s %s$' % (method, url)),
      'mw': mw
    })
    return self

  def options(self, url, mw):
    return self.method('OPTIONS', url, mw)

  def get(self, url, mw):
    return self.method('GET', url, mw)

  def post(self, url, mw):
    return self.method('POST', url, mw)

  def put(self, url, mw):
    return self.method('PUT', url, mw)

  def delete(self, url, mw):
    return self.method('DELETE', url, mw)

  def all(self, url, mw):
    return self.method('.*', url, mw)

  def routes(self):
    async def ret(req, res, next):
      matched = []
      for i in self.stack:
        if i['action'].match(req.action):
          req.url_match = i['action'].match(req.action)
          matched.append(i['mw'])
      await compose(matched)(req, res, next)
    return ret

class App:
  def __init__(self):
    self.mw = []
  
  def use(self, mw):
    self.mw.append(mw)

  async def handle(self, reader, writer):
    try:
      res = Res(writer)
      req = Req(reader)
      def noop():
        return
      await compose(self.mw)(req, res, noop)
    except Exception as e:
      print('exception %s' % e)
      await res.err(500, 'Internal Server Error')
    finally:
      await res.writer.aclose()
