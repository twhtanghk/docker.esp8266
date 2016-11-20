str = require "str"

class Req
  new: (client, data) =>
    lines = str.split data
    @method, @url, @version = string.match lines[1], "(.*) (.*) HTTP/(.*)"
    @headers = {}
    for line in *lines[2,] do
      key, value = string.match line, "(.*): (.*)"
      if key != nil
        @headers[key] = value

return Req
