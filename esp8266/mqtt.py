import net
from umqtt.robust import MQTTClient

client = MQTTClient(net.ap['essid'], 'mqtt.flespi.io', port=1883, user='', password='')
try:
  client.connect()
except OSError as e:
  pass
