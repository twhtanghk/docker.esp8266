import uasyncio as asyncio
from machine import Pin

pin = Pin(13, Pin.OUT, Pin.PULL_UP)
elapsed = 30 * 60 # default 30 min

def set(req, res):
  try:
    pin = int(req.url_match.group(1))
    if pin not in [0, 2, 4, 5, 12, 13, 14, 15, 16]:
      raise Exception('Invalid pin')
    val = req.body['val']
    if val not in [0, 1]:
      raise Exception('Invalid pin value')
    Pin(pin, Pin.OUT).value(val)
    yield from res.ok()
  except ValueError:
    yield from res.err(500, 'Invalid pin')
  except Exception as e:
    yield from res.err(500, str(e))
 
def get(req, res):
  pin = req.url_match[1]
  yield from res.ok(Pin(pin, Pin.IN).value())

def interval(req, res):
  try:
    global elapsed
    elapsed = req.body['elapsed']
    global task
    asyncio.cancel(task)
    task = switch()
    loop.create_task(task)
    yield from res.ok()
  except Exception as e:
    yield from res.err(500, str(e))

async def switch():
  while True:
    global pin
    global elapsed
    pin.value(int(not pin.value()))
    await asyncio.sleep(elapsed)

loop = asyncio.get_event_loop()
task = switch()
loop.create_task(task)
