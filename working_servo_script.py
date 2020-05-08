#WORKING SERVO SCRIPT
# You need to provide 5V of power if using the red servo!


#while True:
#        for pulse in range(50, 250, 1):
#                wiringpi.pwmWrite(18, pulse)
#                time.sleep(delay_period)
#        for pulse in range(250, 50, -1):
#                wiringpi.pwmWrite(18, pulse)
#                time.sleep(delay_period)

try:
    # Servo Control
  import time
  import wiringpi

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

  flag = 50
  delay_period = 0.01
  nav_dict = {'l':10,'L':50,'r':-10,'R':-50}
  while True:
    nav = input("Please select direction, use \'l\' for short left, \'r\' for short right, \'L\' for larger left turn and \'R\' for larger right turn: ")
    if nav in nav_dict.keys(): # ensure's proper entry 
      nav_value = int(nav_dict[nav])
      
      if (flag+nav_value)< 249 and (flag+nav_value) > 0: # if nav value is in the acceptable range
        if nav_value > 0: # positive nav value
          for i in range(flag,nav_value,1):
            wiringpi.pwmWrite(18,i)
            time.sleep(delay_period)
          flag = (flag+nav_value)
        else: #negative nav value
          print(nav_value)
          for i in range(flag,nav_value,-1):
            wiringpi.pwmWrite(18,i)
            time.sleep(delay_period)
          flag = (flag+nav_value)
          

      
      else: #if flag+nav_value will send you over 249 or under 49
        print("Too Far left or right, resetting value")
        
        if nav_value>0:
          for i in range(flag,50,-1):
            wiringpi.pwmWrite(18,i)
            time.sleep(delay_period)
          flag = 50
        else:
          for i in range(50,flag,1):
            wiringpi.pwmWrite(18,i)
            time.sleep(delay_period)
          flag = 50
          

  
    else: # Handle improper input 
      print("Improper input, please try again")
except KeyboardInterrupt:
  print("Keyboard interrupt detected, turning off!")
