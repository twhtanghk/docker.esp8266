# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from config import model as cfg
cfg.boot()
from gpio import model
model.boot()
import gc
gc.collect()
