from machine import Pin


button1 = Pin(26, Pin.IN)


def button_press(pin):
  print(pin)


button1.irq(trigger=Pin.IRQ_FALLING, handler=button_press)
