# micorpython.esp8266

## boot.py
initialize system by
- call [config.model.boot](config)
- call [wlan.ap.model.boot](wlan/ap)
- call [wlan.sta.model.boot](wlan/sta)
- call [pwm.model.boot](pwm)

## main.py
start web app for routes
- /cfg: [config](config)
- /wlan/ap: [station]((wlan/ap)
- /wlan/sta: [station]((wlan/sta)
