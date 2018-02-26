import picoweb
import ure as re
import logging
logger = logging.getLogger(__name__)

def exists(filename):
  try:
    import os
    os.stat(filename)
    return True
  except OSError:
    return False

def ok(res, data={}):
  yield from picoweb.jsonify(res, data)

def error(res, msg='bad request'):
  yield from picoweb.start_response(res, status='400')
  yield from res.awrite("{}\r\n".format(msg))

def handler(f):
  def ret(req, res):
    logger.info('{} {}'.format(req.method, req.path))
    try:
      yield from f(req, res)
      import gc
      gc.collect()
    except Exception as e:
      import sys
      sys.print_exception(e)
      yield from error(res)
  return ret

def static(req, res):
  file = '..' + req.url_match.group(1)
  mime = picoweb.get_mime_type(file)
  app = picoweb.WebApp(__name__)
  if b'gzip' in req.headers[b'Accept-Encoding']:
    gz = file + '.gz'
    try:
      import os
      os.stat(gz)
      yield from app.sendfile(res, gz, mime, {'Content-Encoding': 'gzip'})
      return
    except OSError:
      pass
  yield from app.sendfile(res, file, mime)
