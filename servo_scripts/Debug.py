#!/usr/bin/env python3
"""Control an Arduino over the USB port."""

# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.


# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial


# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  r - Begin Servo Rotation Clockwise")
   print("  l - Begin Servo Rotation Counterclockwise")
   print("  s - Stop current rotation, if rotating")
   print("  x - Stop rotation, and then Exit program")


# Main

# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=10)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
   command = input("Enter command: ")
   
   if command == "r":  # Rotate Clockwise
      usb.write(b'led_on')  # send command to Arduino
      print("Rotating Clockwise")
   
   elif command == "l":  # Rotate Counterclockwise
      usb.write(b'l')  # send command to Arduino
      print("Rotating Counterclockwise")
   
   elif command == "s":  #Stop Rotation
      print("Stopping Rotation")
      usb.write(b's')

   elif command == "x":  # exit program
      print("Stopping Rotation and exiting program")
      usb.write(b's')
      exit()

   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()
