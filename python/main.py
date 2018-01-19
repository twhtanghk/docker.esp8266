import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import wlan
import config

app = picoweb.WebApp(__name__)

app.mount('/cfg', config.app)
app.mount('/wlan/sta', wlan.sta.app)
app.mount('/wlan/ap', wlan.ap.app)

app.run(host="0.0.0.0", port=80)
