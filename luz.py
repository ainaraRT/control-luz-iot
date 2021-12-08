import sys
import RPi.GPIO as gpio
gpio.setwarnings(False)

idGpio = int(sys.argv[1])
status = sys.argv[2]

print(idGpio)
print(status)

gpio.setmode(gpio.BCM)
gpio.setup(idGpio, gpio.OUT)

if status == 'on':
	gpio.output(idGpio, True)

if status == 'off':
	gpio.output(idGpio, False)