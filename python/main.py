import picoweb

def index(req, res):
  yield from picoweb.jsonify(res, {'loaded': True})

app = picoweb.WebApp(__name__)
app.route('/')(index)

app.run(host="0.0.0.0", port=80)
