from project import pkg
from microdot import Microdot

app = Microdot()
for i in pkg:
  lib = __import__(i)
  app.mount(lib.app, url_prefix=i)
app.run(port=80)
