from project import pkg
from microdot import Microdot
from log import info

app = Microdot()

@app.before_request
def log(req):
  info(__name__, '{} {}'.format(req.method, req.path))

for i in pkg:
  lib = __import__(i)
  app.mount(lib.app, url_prefix=i)

app.run(port=80)
