import uasyncio as asyncio
from antenna import antenna as rotate

heading = {
  'boat': 0.0,
  'antenna': 0.0
}

async def adjust(interval=5):
  while True:
    heading['antenna'] -= (rotate.angle(heading['antenna'] - heading['boat']))
    await asyncio.sleep(interval)

def boat(req, res):
  heading['boat'] = float(req.url_match.group(1))
  yield from res.ok()

def antenna(req, res):
  heading['antenna'] = float(req.url_match.group(1))
  yield from res.ok()
