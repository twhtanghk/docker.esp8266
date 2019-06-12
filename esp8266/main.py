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
  'passwd': 'password'
}
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.config(dhcp_hostname=ap['essid'])
sta_if.connect(sta['ssid'], sta['passwd'])

import ujson

def ok(socket, data):
  socket.write("HTTP/2 200\r\n")
  socket.write("content-type: application/json\r\n")
  socket.write("content-length: %s\r\n\r\n" % len(data))
  socket.write(data)

def err(socket, code, msg):
  socket.write("HTTP/1.1 %s %s\r\n\r\n" % (code, msg))

def handle(socket):
  (method, url, version) = socket.readline().split(b" ")
  action = "%s %s" % (method, url)
  req = socket.recv(1024)
  ok(socket, url)
  socket.close()

import usocket

server = usocket.socket()
server.bind(('0.0.0.0', 80))
server.listen(1)
while True:
  try:
    (socket, sockaddr) = server.accept()
    handle(socket)
  except:
    err(socket, 500, 'Internal Server Error')
