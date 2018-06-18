# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
webrepl.start()
from config import model as cfg
cfg.boot()
pkg = ['ap', 'gpio', 'ddns', 'uart', 'net']
for i in pkg:
  lib = __import__(i)
  lib.model.boot()
import gc
gc.collect()
