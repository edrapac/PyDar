from scapy.all import *
import pandas as pd
import threading
import queue
import time
import random
import os
import sys

data_frame = pd.DataFrame(columns=["SSID", "Signal Strength (dBm)"])
data_frame.set_index("SSID", inplace=True)

def channel_hop():
    while True:
        try:
            stream = os.system('./channelHop.sh')
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
                # #remove these comments, test driver code print('SSID: %s | Signal Strength: %s dBm' %(str(packet.info,'UTF8'),packet.dBm_AntSignal)) # packet.info is an 802.11 specific field that gives us the SSID of the beacon frame
                # need to start threading first
                ssid = str(packet.info, 'UTF8')
                dbm = str(packet.dBm_AntSignal)
                pdframe(ssid, dbm)
    except Exception as e:
        print(e)
        pass  # bad packet or something, best to just pass it


def printFrame(q):
    while True:
        print(data_frame.to_string())

        # unfortunately no better way to do this than to feed clear directly to the OS to clear stdout
        time.sleep(0.5)
        os.system("clear")


def pdframe(ssid, dbm):  # Updates the pdframe to contain the newest beacon frame and associated information
    SSID = ssid
    data_frame.loc[SSID] = (dbm)


if __name__ == "__main__":
    x = threading.Thread(target=printFrame, args=(data_frame,))
    x.daemon = True  # daemonize the thread otherwise it will be dependent on the sniffing
    x.start()
    
    y = threading.Thread(target=channel_hop)
    y.daemon = True
    y.start()


    sniff(iface='wlan1mon', prn=callback)
