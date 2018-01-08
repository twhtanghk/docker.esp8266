class Res
  @statusMessage = {
    [200]: "OK"
    [404]: "Not Found"
  }

  new: (client) =>
    @client = client
    @statusCode = 200

  status: (code) =>
    @statusCode = code
    return @

  send: (body="") =>
    body = "HTTP/1.1 #{@statusCode} #{@@statusMessage[@statusCode]}\nContent-Type: application/json\n\n#{body}"
    @client\send body
    return @

  notFound: (msg="") =>
    @status 404
    @send msg
    
return Res
