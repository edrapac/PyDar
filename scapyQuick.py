from scapy.all import *
import pandas as pd
import threading
import queue
import time
import random
import os
import sys

df_queue = queue.Queue()


def callback(packet):  # processes sniffed packets and calls the pdframe method
    '''
    TODO:
    Need to implement channel hopping, right now it seems like the sniff function just picks an arbitrary channel 
    and doesnt deviate, we need to ensure even coverage
    Essentially the flow seems to be 
    1. Get device in mon mode
    2. Sniff and do everything we do in this file
    3. sudo iw dev wlan1mon set channel [new_channel]
    4. Repeat
    This might require that we either use some kind of subproccessing or we call our scapy sniff script from bash or the like
    '''
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
        df = q.get()
        print(df.to_string())

        # unfortunately no better way to do this than to feed clear directly to the OS to clear stdout
        time.sleep(0.5)
        os.system("clear")


def pdframe(ssid, dbm):  # constructs panda dataframes and puts them in the queue
    data_frame = pd.DataFrame(columns=["SSID", "Signal Strength (dBm)"])
    data_frame.set_index("SSID", inplace=True)
    SSID = ssid
    data_frame.loc[SSID] = (dbm)
    df_queue.put(data_frame)  # update FIFO q


print('Starting the Thread')  # test code, comment out later
'''
while True:  # TODO make this part of main

    try:
        x = threading.Thread(target=printFrame, args=(df_queue,))
        x.start()
    except KeyboardInterrupt:
        print('Keyboard Interrupt detected, exiting...')
        sys.exit(0)  # exit cleaiiin
'''
if __name__ == "__main__":

    x = threading.Thread(target=printFrame, args=(df_queue,))
    x.daemon = True  # daemonize the thread otherwise it will be dependent on the sniffing
    x.start()

    sniff(iface='wlan1mon', prn=callback)
