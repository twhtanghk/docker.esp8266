import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import wlan.sta

app = picoweb.WebApp(__name__)

app.mount('/wlan', wlan.sta.app)

app.run(host="0.0.0.0", port=80)
