import logging
logging.basicConfig(level=logging.INFO)

import picoweb
import config
import wlan
import pwm

app = picoweb.WebApp(__name__)

app.mount('/cfg', config.app)
app.mount('/wlan/sta', wlan.sta.app)
app.mount('/wlan/ap', wlan.ap.app)
app.mount('/pwm', pwm.app)

app.run(host="0.0.0.0", port=80)
