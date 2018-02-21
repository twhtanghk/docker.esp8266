# wlan station settings

## controller.py
- GET /wlan/sta: get config
- PUT /wlan/sta: set config for name, ssid and password, connect to access point with specified ssid and password if any
- GET /wlan/sta/scan: scan for access points and return list of available access points

## model.py
- load existing station config and try to connect the last recorded access point during boot
