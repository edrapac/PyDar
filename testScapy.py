from scapy.all import *
import sys

try:
    sniff(iface='wlan1mon',prn=lambda x: x.show())
except KeyBoardInterrupt:
    print('Keyboard interrupt detected, exiting now')
    sys.exit(0) #clean exit
