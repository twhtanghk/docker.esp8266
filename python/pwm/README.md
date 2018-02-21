# pwm settings

## controller.py
- GET /pwm: get config for all pwm devices
- PUT /pwm: set config for device (required) and value (0-1024 required)

## model.py
- load existing config for all pwm devices and initialize those devices during boot
