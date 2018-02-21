# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
from config import model as cfg
cfg.boot()
from wlan.ap import model as ap
ap.boot()
from wlan.sta import model as sta
sta.boot()
import gc
gc.collect()
