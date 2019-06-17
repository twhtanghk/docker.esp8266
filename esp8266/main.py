import net
import http

def echo(req, res):
  res.ok(req.__dict__)
 
app = http.App()
app.get('.*', echo)
app.run()
