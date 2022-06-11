import json
import network


wlan = network.WLAN(network.AP_IF)

wlan.active(True)

wlan.config(essid="pico-test")