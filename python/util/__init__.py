def notFound(req, res):
  yield from picoweb.start_response(res, status='404')
  yield from res.awrite('404\r\n')
