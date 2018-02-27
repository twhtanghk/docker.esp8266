def cfg():
  from ap import model
  mac = model.interface.config('mac')
  import ubinascii
  mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
  return {
    'essid': 'Micropython-{}'.format(mac),
    'password': 'micropythoN'
  }
