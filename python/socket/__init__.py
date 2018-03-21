import ujson

class Config:
  def __init__(self, filename):
    self.filename = filename

  def load(self):
    f = open(self.filename)
    data = ujson.load(f)
    f.close()
    return data

  def save(self, data):
    f = open(self.filename, 'w')
    ujson.dump(data, f)
    f.close()
    return self

class Model(Config):
  def __init__(self):
    Config.__init__(self, '/socket.json')

  def factory(self):
    self.save({
      'ip': '192.168.43.1',
      'port': 2947
    })
    return self

  def boot(self):
    from util import exists
    if not exists(self.filename):
      self.factory()

  def setup(self):
    self.cfg = self.load()
    import usocket
    self.address = usocket.getaddrinfo(self.cfg['ip'], self.cfg['port'])[0][-1]
    self.socket = usocket.socket()
    self.socket.connect(self.address)
    while True:
      data = self.socket.recv(100)
      print(str(data, 'utf8'))
