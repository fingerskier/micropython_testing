import network, json, time
import urequests as ureq


with open('config.json') as f:
  config = json.load(f)


wlan = network.WLAN(network.STA_IF)

wlan.active(True)