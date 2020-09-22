from scapy.all import *
import pandas as pd
import threading
import queue
import time
import random
import os
import sys
import argparse 

'''
Define some globals
'''
class Scanner ():
    def __init__(self):
        self.data_frame = pd.DataFrame(columns=["SSID", "Signal Strength (dBm)"])
        
        self.data_frame.set_index("SSID", inplace=True)


        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--iface',required=True)
        self.arguments = self.parser.parse_args()

    def channel_hop(self):
        while True:
            try:
                stream = os.system('./channelHop.sh '+self.arguments.iface)
                time.sleep(2)
            except KeyboardInterrupt:
                print('Ctrl+c detected, shutting down')
                sys.exit(1)
            except Exception as e:
                print('Non keyboard interrupt exception detected! Printing now')
                print(e)
    
    def callback(packet):  # processes sniffed packets and calls the pdframe method
        try:
            if packet.haslayer(Dot11):  # check if the packet has an 802.11 layer ie Wifi
                if packet.type == 0 and packet.subtype == 8:  # here we start accessing 802.11 specific fields
                    ssid = str(packet.info, 'UTF8')
                    dbm = str(packet.dBm_AntSignal)
                    pdframe(ssid, dbm)
        except Exception as e:
            print(e)
            pass  # bad packet or something, best to just pass it
    def getIface(self):
        return self.arguments.iface

    def printFrame(self):
        while True:
            print(self.data_frame.to_string())
            # unfortunately no better way to do this than to feed clear directly to the OS to clear stdout
            time.sleep(0.5)
            os.system("clear")


    def pdframe(ssid, dbm):  # Updates the pdframe to contain the newest beacon frame and associated information
        SSID = ssid
        data_frame.loc[SSID] = (dbm)



if __name__ == "__main__":
    newScanner = Scanner()
    x = threading.Thread(target=newScanner.printFrame)
    x.daemon = True  # daemonize the thread otherwise it will be dependent on the sniffing
    x.start()
    
    y = threading.Thread(target=newScanner.channel_hop) #call channel hopping on a monitor mode interface as passed by the command
    y.daemon = True
    y.start()


    sniff(iface=newScanner.getIface, prn=newScanner.callback) # main thread of execution begin sniffing as last task
