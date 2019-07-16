import network
import ubinascii

ap_if = network.WLAN(network.AP_IF)
mac = ap_if.config('mac')
mac = ubinascii.hexlify(mac).decode('utf-8')[6:]
ap = {
  'essid': 'Micropython-{}'.format(mac),
  'password': 'micropythoN'
}
ap_if.config(essid=ap['essid'], password=ap['password'])
ap_if.active(True)

sta = {
  'ssid': 'ssid',
  'passwd': 'passwd'
}
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.config(dhcp_hostname=ap['essid'])
sta_if.connect(sta['ssid'], sta['passwd'])
