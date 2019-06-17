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
  def __init__(self, socket):
    self.socket = socket
    (method, url, version) = socket.readline().decode('utf-8').split(" ")
    self.action = "%s %s" % (method, url)
    self.header = self._header()
    self.body = {}
    if b'Content-Length' in self.header:
      self.body = self._body()

  def _header(self):
    ret = {}
    while True:
      l = self.socket.readline()
      if l == b"\r\n":
        break
      k, v = l.split(b":", 1)
      ret[k] = v.strip()
    return ret

  def _body(self):
    len = int(self.header[b'Content-Length'])
    return ujson.loads(self.socket.recv(len))

class Res:
  def __init__(self, socket):
    self.socket = socket
    self.header = {}

  def set(self, header):
    self.header.update(header)

  def flushHeaders(self):
    for k, v in self.header.items():
      self.socket.write("%s: %s\r\n" % (k, v))

  def ok(self, data=None):
    self.socket.write("HTTP/2 200\r\n")
    self.flushHeaders()
    if data != None:
      data = ujson.dumps(data)
      self.socket.write("Content-Length: %s\r\n" % len(data))
      self.socket.write(data)
    self.socket.write("\r\n")

  def err(self, code, msg):
    self.socket.write("HTTP/2 %s %s\r\n\r\n" % (code, msg))

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
    self.socket.write("HTTP/2 200\r\n")
    self.flushHeaders()
    try:
      import pkg_resources
      with pkg_resources.resource_stream(__name__, fname) as f:
        buf = bytearray(64)
        while True:
          l = f.readinot(buf)
          if not l:
            break
          self.socket.write(buf)
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

  def handle(self, socket):
    try:
      res = Res(socket)
      req = Req(socket)
      logger(req, res)
      json(req, res)
      cors(req, res)
      for route in self.routes:
        if route['action'].match(req.action):
          route['mw'](req, res)
          return
      res.err(404, 'Not Found')
    except Exception as e:
      print(e)
      res.err(500, 'Internal Server Error')
    finally:
      socket.close()

  def run(self, host='0.0.0.0', port=80):
    import usocket
    server = usocket.socket()
    server.bind((host, port))
    server.listen(1)
    while True:
      (socket, sockaddr) = server.accept()
      self.handle(socket)
