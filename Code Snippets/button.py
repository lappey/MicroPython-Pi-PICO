import machine
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
print(button.value())