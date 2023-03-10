import time
from machine import Pin
from lib import config

print(f'Hello, World! Application: {config.appName}')

led = Pin("LED", Pin.OUT)

while True:
    led.high()
    time.sleep(1)
    led.low()
    time.sleep(1)
