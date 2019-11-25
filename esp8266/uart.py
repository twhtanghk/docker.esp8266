from uasyncio import StreamReader, StreamWriter, sleep_ms
from machine import UART, Pin
from system import load, save

config = {
  'baudrate': 4800,
  'bits': 8,
  'parity': None,
  'stop': 1
}

uart = UART(0)
uart.init(**load(config))
uartReader = StreamReader(uart)
uartWriter = StreamWriter(uart, {})

def factory():
  save(config)
  uart.init(config)
  uartReader = StreamReader(uart)
  uartWriter = StreamWriter(uart, {})

def valid(data):
  if data['baudrate'] not in [300, 600, 1200, 4800, 9600, 19200, 38400, 57600, 115200, 230400, 250000, 460800]:
    raise ValueError('baudrate')
  if data['bits'] not in [7, 8]:
    raise ValueError('bits')
  if data['parity'] not in [None, 0, 1]:
    raise ValueError('parity')
  if data['stop'] not in [1, 2]:
    raise ValueError('stop')

def set(req, res):
  try:
    valid(req.body)
    save(req.body)
    uart.init(**req.body)
    uartReader = StreamReader(uart)
    uartWriter = StreamWriter(uart, {})
    yield from res.ok()
  except ValueError as err:
    yield from res.err(500, "Invalid {}".format(str(err)))

def get(req, res):
  yield from res.ok(load(config))

class RS485:
  def __init__(self, DE=13, activity=2):
    self.DE = Pin(DE, Pin.OUT)
    self.DE.off()
    self.activity = Pin(activity, Pin.OUT)
    self.activity.on()
    self.uart = {
      'reader': uartReader,
      'writer': uartWriter
    }
    self.net = []

  async def handle(self, reader, writer):
    self.net.append({
      'reader': reader,
      'writer': writer
    })
    while True:
      line = await reader.readline()
      if len(line) == 0:
        return
      await self.writeln(line)

  async def writeln(self, line, delay=500):
    self.DE.on()
    self.activity.off()
    print(line)
    await sleep_ms(delay)
    await self.uart['writer'].awrite(line)
    await sleep_ms(delay)
    self.DE.off()
    self.activity.on()

  async def readln(self):
    while True:
      line = await self.uart['reader'].readline()
      self.activity.off()
      print(line)
      for stream in self.net:
        try:
          await stream['writer'].awrite(line)
        except OSError:
          self.net.remove(stream)
      self.activity.on()
