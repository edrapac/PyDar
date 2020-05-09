#WORKING SERVO SCRIPT
# You need to provide 5V of power if using the red servo!

import time
import wiringpi
import sys
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
# This is what sets the pwm frequency, 50 Hz (typical servo) which is determined via pwmSetRange/pwmSetClock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while True:
	try:
		for pulse in range(50, 250, 1):
			print('sending pulse')
			wiringpi.pwmWrite(18, pulse)
			time.sleep(delay_period)
		for pulse in range(250, 50, -1):
			wiringpi.pwmWrite(18, pulse)
			time.sleep(delay_period)
	except KeyboardInterrupt:
		sys.exit(0)
