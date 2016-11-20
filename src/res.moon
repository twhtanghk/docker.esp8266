class Res
  statusCode: 200

  @statusMessage = {
    [100]: "Continue"
    [101]: "Switching"
    [200]: "OK"
    [201]: "Created"
    [202]: "Accepted"
    [203]: "Non-Authoritative"
    [204]: "No"
    [205]: "Reset"
    [206]: "Partial"
    [300]: "Multiple"
    [301]: "Moved"
    [302]: "Found"
    [303]: "See"
    [304]: "Not"
    [305]: "Use"
    [307]: "Temporary"
    [400]: "Bad"
    [401]: "Unauthorized"
    [402]: "Payment"
    [403]: "Forbidden"
    [404]: "Not"
    [405]: "Method"
    [406]: "Not"
    [407]: "Proxy"
    [408]: "Request"
    [409]: "Conflict"
    [410]: "Gone"
    [411]: "Length"
    [412]: "Precondition"
    [413]: "Request"
    [414]: "Request-URI"
    [415]: "Unsupported"
    [416]: "Requested"
    [417]: "Expectation"
    [500]: "Internal"
    [501]: "Not"
    [502]: "Bad"
    [503]: "Service"
    [504]: "Gateway"
    [505]: "HTTP"
  }

  new: (client) =>
    @client = client

  status: (code) =>
    @statusCode = code
    return @

  send: (body="", cb) =>
    body = "HTTP/1.1 #{@statusCode} #{@@statusMessage[@statusCode]}\nContent-Type: application/json\n\n#{cjson.encode(body)}"
    @client\send body, cb
    return @
    
return Res
