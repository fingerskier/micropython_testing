from machine import Pin
import time


def blink_led():
  p = Pin(25, Pin.OUT)


  for i in range(5):
    p.on()
    time.sleep(1)
    p.off()
    time.sleep(1)


  print("Done blinking")