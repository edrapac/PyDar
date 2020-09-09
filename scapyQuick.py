from scapy.all import *
import pandas as pd
import threading, queue
import time
import random
import os
import sys

df_queue = queue.Queue()


def callback(packet): # processes sniffed packets and calls the pdframe method
	try:
            if packet.haslayer(Dot11): # check if the packet has an 802.11 layer ie Wifi
                if packet.type == 0 and packet.subtype ==8: # here we start accessing 802.11 specific fields
                    # #remove these comments, test driver code print('SSID: %s | Signal Strength: %s dBm' %(str(packet.info,'UTF8'),packet.dBm_AntSignal)) # packet.info is an 802.11 specific field that gives us the SSID of the beacon frame
                    ssid = str(packet.info,'UTF8') #need to start threading first 
                    dbm = str(packet.dBm_AntSignal)
                    pdframe(ssid,dbm)
	except Exception as e:
		print(e)
		pass # bad packet or something, best to just pass it


def printFrame(q):
    df = q.get()
    print(df.to_string())




def pdframe(ssid,dbm): # constructs panda dataframes and puts them in the queue 
	data_frame = pd.DataFrame(columns=["SSID","Signal Strength (dBm)"])
	data_frame.set_index("SSID",inplace=True)
	SSID = ssid
	data_frame.loc[SSID] = (dbm)
	df_queue.put(data_frame) # update FIFO q
	

while True: #TODO make this part of main
	
	print('Starting the Thread') # test code, comment out later
        try:
                x = threading.Thread(target=pdframe,args=(df_queue,))
		x.start()
		df = df_queue.get()
		print(df.to_string())
		time.sleep(0.5)
		os.system("clear") #unfortunately no better way to do this than to feed clear directly to the OS to clear stdout
	except KeyboardInterrupt:
		print('Keyboard Interrupt detected, exiting...')
		sys.exit(0) # exit clean
                
sniff(iface='wlan1mon',prn=callback)
