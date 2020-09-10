# Simple script to make sure that sniffing is working as intended. Change the wlan1mon iface to whatever iface you want. 
# Yes, I know this can be done from scapy's interactive menu but the idea here is that we want to make sure that that 
# functionality can be called from a python file with no issues
from scapy.all import *
import sys

try:
    sniff(iface='wlp4s0mon',prn=lambda x: x.show())
except KeyBoardInterrupt:
    print('Keyboard interrupt detected, exiting now')
    sys.exit(0) #clean exit
