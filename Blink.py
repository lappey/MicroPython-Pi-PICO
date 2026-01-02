import machine
import time
led_external = machine.Pin(15, machine.Pin.OUT)
led_onboard = machine.Pin("LED", machine.Pin.OUT)

while True:
    led_onboard.toggle()
    time.sleep(2)
    led_external.toggle()