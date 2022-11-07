import sys
import socket

try:
  # run "socat TCP4-LISTEN:8888,fork -" on server with IP specified below
  addr = socket.getaddrinfo('192.168.43.2', 8888)
  logger = socket.socket()
  logger.connect(addr[0][-1])
except:
  logger = sys.stdout
