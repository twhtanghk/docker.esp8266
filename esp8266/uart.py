import uos
from uasyncio import StreamReader, StreamWriter
from machine import UART

uos.dupterm(None, 1)
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
  def __init__(self):
    self.upstream = {
      'reader': uartReader,
      'writer': uartWriter
    }
    self.downstream = []

  def handle(self, reader, writer):
    self.downstream.append({
      'reader': reader,
      'writer': writer
    })

  async def readline():
    line = await self.upstream['reader'].readline()
    for stream in self.downstream:
      stream.writer.write(line)
      await stream.writer.drain()
