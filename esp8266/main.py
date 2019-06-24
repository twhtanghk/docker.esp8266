import http
from multimeter import voltage, current

def echo(req, res):
  res.ok(req.__dict__)
 
def preflight(req, res):
  res.ok()

app = http.App()
app.options('.*', preflight)
app.get('/voltage', voltage)
app.get('/current', current)
app.get('.*', echo)
app.run()
