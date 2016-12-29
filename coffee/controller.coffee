class Ctrl
  @headers:
    'Content-Type': 'application/json'
    'Access-Control-Allow-Origin': '*'

  @notFound: (res) ->
    res.writeHead 404, Ctrl.headers
    res.end "404: Not Found"

  create: (req, res) ->
    Ctrl.notFound res

  find: (req, res) ->
    Ctrl.notFound res

  findOne: (req, res) ->
    Ctrl.notFound res

  update: (req, res) ->
    Ctrl.notFound res

  destroy: (req, res) ->
    Ctrl.notFound res

sys = new Ctrl()
sys.dumpReq = (req, res) ->
  req.on 'end', (data) ->
    console.log JSON.stringify req

sys.bodyParser = (req, res) ->
  body = ''
  req.on 'data', (data) ->
    body += data
  req.on 'end', ->
    req.body = JSON.parse body

sys.templates = (req, res) ->
  path = req.url.split('.')
  switch path[path.length - 1]
    when 'js'
      res.writeHead 200, 'Content-Type': 'application/javscript' 
    when 'html'
      res.writeHead 200, 'Content-Type': 'text/html'
  res.end templates[req.url]

sys.status = (req, res) ->
  res.writeHead 200, Ctrl.headers
  res.end JSON.stringify 
    name: wifi.getHostname()

sys.reset = (req, res) ->
  res.writeHead 200, Ctrl.headers
  res.end()
  reset()

ap = new Ctrl()
ap.findOne = (req, res) ->
  wifi.getAPDetails (cfg) ->
    res.writeHead 200, Ctrl.headers
    res.end JSON.stringify cfg
ap.update = (req, res) ->
  wifi
    .startAP _.pick(req.body, 'ssid'), _.pick(req.body, 'authMode', 'password', 'channel'), ->
    wifi.save()

sta = new Ctrl()
# get current station config details
sta.findOne = (req, res) ->
  wifi.getDetails (cfg) ->
    res.writeHead 200, Ctrl.headers
    res.end JSON.stringify cfg

# scan and list available ap to be connected
sta.find = (req, res) ->
  wifi.scan (aplist) ->
    res.writeHead 200, Ctrl.headers
    res.end JSON.stringify aplist

module.exports =
  sys: sys
  ap: ap
  sta: sta
