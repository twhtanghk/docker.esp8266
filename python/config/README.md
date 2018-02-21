# config

## controller.py
- GET /cfg: get config
- PUT /cfg: set config
- GET /cfg/reset: restart esp8266
- GET /cfg/factory: restore factory default configuration

## model.py
- create default /config.json if not exist during boot
