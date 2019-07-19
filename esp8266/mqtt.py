import system
from umqtt.robust import MQTTClient
from umqtt.simple import MQTTException

config = system.load()
client = MQTTClient(config['name'], 'mqtt.flespi.io', port=1883, user=config['mqtt']['user'], password=config['mqtt']['password'])
try:
  client.connect()
except OSError as e:
  print('mqtt connect error')
  pass
except MQTTException as e:
  print('mqtt user and password not yet defined')
  pass

def reset(req, res):
  config = system.load()
  config['mqtt']['user'] = req.body['user']
  config['mqtt']['password'] = req.body['password']
  system.save(config)
  yield from res.ok()
