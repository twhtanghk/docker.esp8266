import uos
from uasyncio import StreamReader, StreamWriter, sleep_ms
from machine import UART, Pin

#uos.dupterm(None, 1)
#uos.dupterm(machine.UART(0, 115200), 1)

uart = UART(0, baudrate=4800, bits=8, parity=None, stop=1)
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
  def __init__(self, DE=13):
    self.DE = Pin(DE, Pin.OUT)
    self.DE.off()
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
      print(line)
      await self.writeln(line)

  async def writeln(self, line, delay=500):
    self.DE.on()
    await sleep_ms(delay)
    await self.uart['writer'].awrite(line)
    await sleep_ms(delay)
    self.DE.off()

  async def readln(self):
    while True:
      line = await self.uart['reader'].readline()
      print(line)
      for stream in self.net:
        try:
          await stream['writer'].awrite(line)
        except OSError:
          self.net.remove(stream)
