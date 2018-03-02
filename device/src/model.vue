<script lang='coffee'>
Queue = require 'promise-queue'
queue = new Queue(1, Infinity)
fetch = (url, opts) ->
  queue.add ->
    window.fetch url, opts

module.exports =
  param: (data) ->
    ret = new URLSearchParams()
    for k, v of data
      ret.set k, v
    ret

  opts: (method, data) ->
    method: method
    body: module.exports.param data
    headers:
      'Content-Type': 'application/x-www-form-urlencoded'

  method: (method, url, data) ->
    error = (res) ->
      if res.status != 200
        throw new Error res.statusText
      res
    switch method
      when 'GET'
        if data?
          url = "#{url}?#{module.exports.param data}"
        fetch url
          .then error
      when 'POST', 'PUT', 'DELETE'
        fetch url, module.exports.opts(method, data)
          .then error
      else
        Promise.reject new Error "unknown http method #{method}"
    
  get: (url, data) ->
    module.exports.method 'GET', url, data

  post: (url, data) ->
    module.exports.method 'POST', url, data

  put: (url, data) ->
    module.exports.method 'PUT', url, data

  del: (url, data) ->
    module.exports.method 'DELETE', url, data
</script>
