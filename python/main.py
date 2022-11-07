from microdot import Microdot
import config

app = Microdot()
app.mount(config.app, url_prefix='/cfg')
for i in config.pkg:
  lib = __import__(i)
  app.mount(lib.app, url_prefix=i)
app.run(port=80)
