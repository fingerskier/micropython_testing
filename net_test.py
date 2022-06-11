import json
import network


wlan = network.WLAN(network.STA_IF)

wlan.active(True)

wlan.scan()

wlan.isconnected()

wlan.config('mac')

wlan.ifconfig()


with open('config.json') as f:
  config = json.load(f)

wlan.connect(config['ssid'], config['password'])


while not wlan.isconnected:
  pass


wlan.ifconfig()

wlan.active(False)