from uln2003 import Stepper, HALF_STEP, FULL_ROTATION

stepper = Stepper(HALF_STEP, 14, 12, 13, 15)

from machine import Pin

def stop(p):
  stepper.irq()

endSwitch = Pin(2, Pin.IN, Pin.PULL_UP)
endSwitch.irq(trigger=Pin.IRQ_FALLING, handler=stop)

from compass import heading
from time import sleep

def head(target, interval=2):
  while True:
    curr = heading()[0]
    diff = (target - curr) % 360
    print("%s %s %s" % (target, curr, diff))
    stepper.step(FULL_ROTATION * diff / 360)
    sleep(interval)
