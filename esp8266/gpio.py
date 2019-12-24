import uasyncio as asyncio
from machine import Pin

pin13 = Pin(13, Pin.OUT, Pin.PULL_UP)
elapsed = 30 * 60 # default 30 min

def pin(req):
  ret = int(req.url_match.group(1))
  if ret not in [0, 2, 4, 5, 12, 13, 14, 15, 16]:
    raise Exception('Invalid pin')
  return Pin(ret, Pin.OUT)

def val(req):
  ret = req.body['val']
  if ret not in [0, 1]:
    raise Exception('Invalid pin value')
  return ret

def set(req, res):
  try:
    pin(req).value(val(req))
    yield from res.ok()
  except ValueError:
    yield from res.err(500, 'Invalid pin')
  except Exception as e:
    yield from res.err(500, str(e))
 
def get(req, res):
  try:
    global elapsed
    yield from res.ok({"elapsed": elapsed, "val": pin(req).value()})
  except Exception as e:
    yield from res.err(500, str(e))

def interval(req, res):
  try:
    global elapsed
    elapsed = int(req.body['elapsed'])
    yield from res.ok()
  except Exception as e:
    yield from res.err(500, str(e))

async def switch():
  while True:
    global pin13
    global elapsed
    pin13.value(int(not pin13.value()))
    await asyncio.sleep(elapsed)

loop = asyncio.get_event_loop()
task = switch()
loop.create_task(task)
