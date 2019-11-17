import uos
from uasyncio import StreamReader, StreamWriter, sleep_ms
from machine import UART, Pin

#uos.dupterm(None, 1)
#uos.dupterm(machine.UART(0, 115200), 1)

uart = UART(2, baudrate=4800, bits=8, parity=None, stop=1)
uartReader = StreamReader(uart)
uartWriter = StreamWriter(uart, {})

def config(req, res):
  baudrate = req.body['baudrate']
  bits = req.body['bits']
  parity = req.body['parity']
  stop = req.body['stop']
  uart = uart.init(baudrate=baudrate, bits=bits, parity=parity, stop=stop)
  uartReader = StreamReader(uart)
  uartWriter = StreamWriter(uart, {})
  yield from res.ok()

class RS485:
  def __init__(self, DE=15, RE=2):
    self.DE = Pin(DE, Pin.OUT, Pin.PULL_DOWN)
    self.RE = Pin(RE, Pin.OUT, Pin.PULL_DOWN)
    self.upstream = {
      'reader': uartReader,
      'writer': uartWriter
    }
    self.downstream = []

  async def handle(self, reader, writer):
    self.downstream.append({
      'reader': reader,
      'writer': writer
    })
    while True:
      line = await reader.readline()
      if len(line) == 0:
        return
      print(line)
      await self.writeln(line)

  async def writeln(self, line, delay=500):
    self.DE.on()
    self.RE.on()
    await sleep_ms(delay)
    await self.upstream['writer'].awrite(line)
    await sleep_ms(delay)
    self.DE.off()
    self.RE.off()

  async def readline(self):
    while True:
      line = await self.upstream['reader'].readline()
      print(line)
      for stream in self.downstream:
        try:
          await stream['writer'].awrite(line)
        except OSError:
          self.downstream.remove(stream)
