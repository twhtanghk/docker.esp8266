# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import uos
#replStream = uos.dupterm(None, 1) # disable REPL on UART(0)
# enable repl on UART(0) by uos.dupterm(replStream, 1)
import gc
#import webrepl
#webrepl.start()
import gc
gc.collect()
