log = require "log"

log.info "Ready to start soft ap"

wifi.ap.config
  ssid:	"TT#{wifi.ap.getmac()\gsub(":", "")}"
  pwd: "12345678"
wifi.ap.setip
  ip: "192.168.1.1"
  netmask: "255.255.255.0"
  gateway: "192.168.1.1"
wifi.setmode wifi.SOFTAP
    
log.info "Soft AP started"
log.info "Heap #{node.heap()} bytes"
log.info wifi.ap.getmac()
log.info wifi.ap.getip()
