from machine import ADC

import time


sensor = ADC(Pin(32))

while True:
  print(sensor.read())
  time.sleep(0.1)