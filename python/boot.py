# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)
import webrepl
webrepl.start()
import pkg
for i in pkg.list:
  lib = __import__(i)
  lib.model.boot()
  lib.model.setup()
import gc
gc.collect()
