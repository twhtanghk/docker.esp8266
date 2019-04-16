import ujson

def exists(filename):
  try:
    import os
    os.stat(filename)
    return True
  except OSError:
    return False

class Config:
  def __init__(self, filename):
    self.filename = filename

  def boot(self):
    if not exists(self.filename):
      self.factory()

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
