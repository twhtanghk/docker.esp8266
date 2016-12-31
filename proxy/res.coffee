module.exports = (res) ->
  defaultHeaders =
    'Content-Type': 'application/json'
    'Access-Control-Allow-Origin': '*'

  orgWriteHead = res.writeHead

  res.headersSent = false

  res.writeHead = (statusCode, headers) ->
    orgWriteHead.call res, statusCode, headers
    headerSent = true
    res

  res.status = (code) ->
    res.writeHead code, defaultHeaders
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

  return res
