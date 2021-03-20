from scapy.all import *
import pandas as pd
import threading
import queue
import time
import random
import os
import sys
import re
'''
Define some globals
'''
class Scanner ():
    def __init__(self):
        iface_reg = re.compile("wl\w+mon")
        stream = os.popen("iw dev").read()
        self.data_frame = pd.DataFrame(columns=["SSID", "Signal Strength (dBm)"])
        
        self.data_frame.set_index("SSID", inplace=True)
        if re.search(iface_reg,stream):
            self.iface = re.findall(iface_reg,stream)[0]
        else:
            print("No Monitor Mode interfaces detected! Exiting!")
            sys.exit(1)

    def channel_hop(self):
        while True:
            try:
                stream = os.system('./channelHop.sh '+self.iface)
                time.sleep(2)
            except KeyboardInterrupt:
                print('Ctrl+c detected, shutting down')
                sys.exit(1)
            except Exception as e:
                print('Non keyboard interrupt exception detected! Printing now')
                print(e)
    
    def callback(self,packet):  # processes sniffed packets and calls the pdframe method
        try:
            if packet.haslayer(Dot11):  # check if the packet has an 802.11 layer ie Wifi
                if packet.type == 0 and packet.subtype == 8:  # here we start accessing 802.11 specific fields
                    ssid = str(packet.info, 'UTF8')
                    dbm = str(packet.dBm_AntSignal)
                    
                    SSID = ssid
                    self.data_frame.loc[SSID] = (dbm)
                    current_frame = self.data_frame.to_string()
                    #return self.data_frame.to_string() uncomment this line to turn on print debugging in console
                    
                    with open("log.txt","w") as file:
                        file.write(current_frame)
                        file.write('\n')
        except Exception as e:
            print(e)
            pass  # bad packet or something, best to just pass it
    def getIface(self):
        return self.iface

    # instead of printFrame we call this, despite not using this method I am going to leave it implemented for potential use later
    def getDataFrame(self):
        return self.data_frame.to_string() # may need to remove the tostring method call


    def pdframe(self,ssid, dbm):  # Updates the pdframe to contain the newest beacon frame and associated information
        SSID = ssid
        self.data_frame.loc[SSID] = (dbm)
    
    def run(self):
        # probably ok to start this thread from within the Scanner class instance as opposed to the app file... I think
        
        y = threading.Thread(target=self.channel_hop) #call channel hopping on a monitor mode interface as passed by the command
        y.daemon = True
        y.start()

        sniff(iface=self.iface, prn=self.callback, count=40) 



if __name__ == "__main__":
    newScanner = Scanner()
    newScanner.run()

