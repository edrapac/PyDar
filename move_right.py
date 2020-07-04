#WORKING SERVO SCRIPT
# You need to provide 5V of power if using the red servo!

import time
import wiringpi
import sys
import logging

logging.basicConfig(filename="move_right_error.log",format='%(asctime)s %(message)s',filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

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

'''
The longer the delay period, the more reliable the overall duty cycle of the servo seems to be. This is a slower option but a delay peroid of about 0.05 always produces consistent results
'''

delay_period = 0.04
file = open("stateful","r+")
counter = 0
status = file.readline()
if('right' in status):
    file.close()
    logger.error("Servo attempted to move past 180 degrees")
    print("Error: You are attempting to move the servo past 180 degrees. This and repeated attempts to move right will continue to fail")
    sys.exit(1)
else:
    for pulse in range(249, 50, -1):
        print('sending pulse')
        counter +=1
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)
    file.write('pointing right')
    file.close()
