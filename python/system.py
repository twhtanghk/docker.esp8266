from util import ok

class System:
  def boot(self):
    return

  def factory(self, req, res):
    import pkg
    for i in pkg.list:
      lib = __import__(i)
      lib.model.factory()
    yield from ok(res)

  def reset(self, req, res):
    yield from ok(res)
    import machine
    machine.reset()

  def read(self, req, res):
    data = {}
    import pkg
    for i in pkg.list:
      lib = __import__(i)
      data[i] = lib.model.load()
    yield from ok(res, data)

model = System()
