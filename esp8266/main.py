import net
import http

def echo(req, res):
  res.ok(req.__dict__)
 
def preflight(req, res):
  res.ok()

app = http.App()
app.options('.*', preflight)
app.get('.*', echo)
app.run()
