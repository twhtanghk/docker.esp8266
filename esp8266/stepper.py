from machine import Pin
from uln2003 import Stepper, HALF_STEP

device = Stepper(HALF_STEP, Pin(14), Pin(12), Pin(13), Pin(15), delay=5)
