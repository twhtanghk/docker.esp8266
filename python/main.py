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

def exists(file):
  try:
    import os
    os.stat(file)
    return True
  except OSError:
    return False

@app.get('/')
def index(req):
  return static(req, '/index.html')

@app.route('/<path:path>')
def static(req, path):
  if '..' in path:
    return 'Not found', 404
  file = 'dist/{}'.format(path)
  type = mime(path)
  if exists(file):
    res = send_file(file)
    res.headers["Content-Type"] = type
    return res
  elif exists(file + '.gz'):
    res = send_file(file + '.gz')
    res.headers["Content-Type"] = type
    res.headers["Content-Encoding"] = "gzip"
    return res
  else:
    return 'Not found', 404

app.run(port=80)
