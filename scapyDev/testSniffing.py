# Simple script to make sure that sniffing is working as intended. Change the wlan1mon iface to whatever iface you want. 
# Yes, I know this can be done from scapy's interactive menu but the idea here is that we want to make sure that that 
# functionality can be called from a python file with no issues
from scapy.all import *
import sys
import os 

try:
    sniff(iface='wlp4s0mon',count=2,prn=lambda x: x.show())
    test_shell_out = input("Woud you like to also test calling a shell script?")
    if test_shell_out.upper() == 'Y':
    	print('trying now')
    	stream = os.system('./channelHop.sh')
    	print(stream)
except KeyboardInterrupt:
    print('Keyboard interrupt detected, exiting now')
    sys.exit(0) #clean exit
