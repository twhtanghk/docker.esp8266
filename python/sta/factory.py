def cfg():
  from sta import model
  mac = model.interface.config('mac')
  import ubinascii
  mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
  return {
    'dhcp_hostname': 'ESP-{}'.format(mac)
  }
