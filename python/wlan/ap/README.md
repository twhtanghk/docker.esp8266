# wlan access point settings

## controller.py
- GET /wlan/ap: get config
- PUT /wlan/ap: set config for essid (required) and password (min 8 chars)

## model.py
- load existing ap config and initialize esp8266 during boot
