module.exports = (res) ->
  res.headers =
    'Content-Type': 'application/json'

  orgWriteHead = res.writeHead

  res.headersSent = false

  res.writeHead = (statusCode, headers) ->
    orgWriteHead.call res, statusCode, headers
    res.headersSent = true
    res

  res.status = (code) ->
    res.writeHead code, res.headers
    res

  res.notFound = (data = 'Not Found') ->
    res
      .status 404
      .end()
    res

  res.serverError = (data = 'Internal Server Error') ->
    res
      .status 500
      .end()
    res

  res.set = (headers) ->
    for k, v of headers
      res.headers[k] = v
    res.headers

  return res
