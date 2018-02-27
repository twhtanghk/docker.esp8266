# micorpython.esp8266

## boot.py
initialize system for ap, sta, pwm

## main.py
start web app for routes
- GET /cfg: return system config in json
- GET /cfg/factory: restore factory default settings for ap, sta, pwm
- GET /cfg/reset: restart system
- GET /ap: get ap config
- PUT /ap: set ap config with parameters essid, password
- GET /sta: get sta config
- PUT /sta: set sta config with parameters name (dhcp_hostname), ssid, passwd 
- GET /sta/scan: scan for available wifi access point
- GET /pwm: get list of pwm devices {fan: {pin: 12, default: 600}, ...}
- GET /pwm/:name: get config for specified device name
- PUT /pwm/:name: set config for specified device name for parameters pin, default
- PUT /pwm/:name/duty: set duty (value) for the specified device name
- GET *: get static files in gzip compression content-encoding
