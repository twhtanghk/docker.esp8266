import picoweb
import ure as re
import uasyncio as asyncio
import logging
logger = logging.getLogger(__name__)

headers = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, PUT, GET, DELETE, OPTIONS'
}

def exists(filename):
  try:
    import os
    os.stat(filename)
    return True
  except OSError:
    return False

def ok(res, data={}):
  import ujson
  yield from picoweb.start_response(res, "application/json", headers=headers)
  yield from res.awrite(ujson.dumps(data))

def cors(req, res):
  yield from picoweb.start_response(res, headers=headers)
  yield from res.aclose()

def error(res, msg='bad request'):
  yield from picoweb.start_response(res, status='400', headers=headers)
  yield from res.awrite("{}\r\n".format(msg))

def handler(f):
  def ret(req, res):
    logger.info('{} {}'.format(req.method, req.path))
    try:
      if req.method == 'OPTIONS':
        yield from cors(req, res)
      else:
        yield from f(req, res)
      import gc
      gc.collect()
    except Exception as e:
      import sys
      sys.print_exception(e)
      yield from error(res, '"{}"'.format(str(e)))
  return ret

def static(req, res):
  file = '../static' + req.url_match.group(1)
  mime = picoweb.get_mime_type(file)
  app = picoweb.WebApp(__name__)
  if b'gzip' in req.headers[b'Accept-Encoding']:
    gz = file + '.gz'
    try:
      import os
      os.stat(gz)
      yield from app.sendfile(res, gz, mime, {'Content-Encoding': 'gzip'})
      return
    except OSError:
      pass
  yield from app.sendfile(res, file, mime)

def uart(**kwargs):
  id = kwargs.get('id', 2)
  baudrate = kwargs.get('baudrate', 4800)
  bits = kwargs.get('bits', 8)
  parity = kwargs.get('parity', None)
  stop = kwargs.get('stop', 1)
  from machine import UART
  uart = UART(id, baudrate=baudrate, bits=bits, parity=parity, stop=stop)
  return [
    asyncio.StreamReader(uart),
    asyncio.StreamWriter(uart, {})
  ]

async def net(**kwargs):
  return await asyncio.open_connection(**kwargs)

async def pipe(reader, writer, pin, write = 0):
  while True:
    line = await reader.readline()
    pin.value(write)
    await writer.awrite(line)
    logger.info(line)
    await asyncio.sleep_ms(200)
    if write == 1:
      pin.value(0)

def uartServer(**kwargs):
  try:
    from machine import Pin
    pin = Pin(kwargs.get('pin', 5), Pin.OUT)
    port = kwargs.get('port', 2947)
    uart2 = uart()
    loop = asyncio.get_event_loop()
    def cb(reader, writer):
      tcp2uart = loop.create_task(pipe(reader, uart2[1], pin, 1))
      uart2tcp = loop.create_task(pipe(uart2[0], writer, pin, 0))
    server = loop.run_until_complete(asyncio.start_server(cb, host='', port=port))
    logger.info(server)
    return server
  except Exception as e:
    import sys
    logger.info('uart')
    sys.print_exception(e)

def inetd(**kwargs):
  try:
    loop = asyncio.get_event_loop()
    async def task():
      await uartServer()
    loop.create_task(task())
  except Exception as e:
    import sys
    logger.info('inetd')
    sys.print_exception(e)
