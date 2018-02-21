def cfg():
  from wlan.ap import model
  mac = model.get()['mac'][6:]
  essid = "MicroPython-{}".format(mac)
  name = "ESP-{}".format(mac)
  return {
   'wlan': {
     'sta': {
       'dhcp_hostname': name
     },
     'ap': {
       'essid': essid,
       'password': 'micropythoN'
     }
   },
   'pwm': {
     'fan': {
       'pin': 12,
       'default': 500
     }
   }
  }
