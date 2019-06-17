import network

ap = {
  'essid': 'dcmultimeter',
  'password': 'password'
}
ap_if = network.WLAN(network.AP_IF)
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
