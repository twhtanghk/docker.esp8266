from project import pkg
from microdot import Microdot, send_file
from log import info

app = Microdot()

@app.before_request
def log(req):
  info(__name__, '{} {}'.format(req.method, req.path))

for i in pkg:
  lib = __import__(i)
  app.mount(lib.app, url_prefix=i)

def mime(path):
  if path.endswith('.html'):
    return 'text/html'
  elif path.endswith('.js'):
    return 'text/javascript'
  elif path.endswith('.css'):
    return 'text/css'

@app.get('/')
def index(req):
  return static(req, '/index.html')

@app.route('/<path:path>')
def static(req, path):
  if '..' in path:
    return 'Not found', 404
  try:
    import os
    file = 'dist/{}.gz'.format(path)
    os.stat(file)
    res = send_file(file)
    res.headers["Content-Encoding"] = "gzip"
    res.headers["Content-Type"] = mime(path)
    return res
  except OSError:
    return 'Not found', 404

app.run(port=80)
