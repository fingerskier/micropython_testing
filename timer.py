from machine import Pin, Timer


led = Pin(4, Pin.OUT)

flash = Timer(0)  # hardware timer
# flash = Timer(-1)  # software timer


def flash_led(timer):
  led.value(not led.value())


flash.init(period=1000, mode=Timer.PERIODIC, callback=flash_led)


flash.deinit()