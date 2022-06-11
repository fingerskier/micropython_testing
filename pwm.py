from machine import PWM

led_pwm = PWM(Pin(4), freq=5, duty=128)

led_pwm.duty(32)
led_pwm.freq(32)

led_pwm.deinit()
