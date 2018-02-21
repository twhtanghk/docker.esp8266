import picoweb

def notFound(req, res):
  yield from picoweb.start_response(res, status='404')
  yield from res.awrite('404\r\n')

def error(req, res, msg='bad request'):
  yield from picoweb.start_response(res, status='401')
  yield from res.awrite("{}\r\n".format(msg))
