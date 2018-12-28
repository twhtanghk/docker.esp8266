# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
pkg = ['ap', 'sta', 'gpio', 'ddns', 'pwm']
for i in pkg:
  lib = __import__(i)
  lib.model.boot()
import gc
gc.collect()
