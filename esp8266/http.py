import ujson

def ok(socket, data):
  data = ujson.dumps(data)
  socket.write("HTTP/2 200\r\n")
  socket.write("content-type: application/json\r\n")
  socket.write("content-length: %s\r\n\r\n" % len(data))
  socket.write(data)

def err(socket, code, msg):
  socket.write("HTTP/1.1 %s %s\r\n\r\n" % (code, msg))

def header(socket):
  ret = {}
  while True:
    l = socket.readline()
    if l == b"\r\n":
      break
    k, v = l.split(b":", 1)
    ret[k] = v.strip()
  return ret

def body(socket, len):
  return ujson.loads(socket.recv(len))

def handle(socket):
  (method, url, version) = socket.readline().split(b" ")
  action = "%s %s" % (method, url)
  h = header(socket)
  b = ''
  if b'Content-Length' in h:
    b = body(socket, int(h[b'Content-Length']))
  ok(socket, {'url': url, 'header': h, 'body': b})
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
