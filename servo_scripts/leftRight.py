#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial
import sys

# Connect to USB serial port at 9600 baud
def left(usb):
   usb.write(b'l')

def right(usb):
   usb.write(b'r')

def stop(usb):
   usb.write(b's')

def exit_run(usb):
   usb.write(b'x')

# connect to Arduino
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=10)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
if sys.argv[1] == "r":
   for i in range(1000): # a bit archaic but we need a way of writing to the serial port that isnt a While true loop
      right(usb)
   print('Currently Rotating Clockwise')
elif sys.argv[1] == "l":
   for i in range(1000):
      left(usb)
   print('Currently Rotating Counterclockwise')
elif sys.argv[1] == "s":
   for i in range(1000):
      stop(usb)
   print('Rotation Stopped')
elif sys.argv[1] == "x":
   for i in range(1000):
      exit_run(usb)
else:  # unknown command
   print("Unknown command '" + command + "'.")
