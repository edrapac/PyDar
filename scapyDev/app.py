from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from threading import Thread, Event
from scapy.all import *
import pandas as pd
import queue
import time
import random
import os
import sys
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.config['DEBUG'] = True


socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)
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
                    # self.pdframe(ssid, dbm)
                    SSID = ssid
                    self.data_frame.loc[SSID] = (dbm)
                    return self.data_frame.to_string()
        except Exception as e:
            print(e)
            pass  # bad packet or something, best to just pass it
    def getIface(self):
        return self.iface

    # instead of printFrame we call this 
    def getDataFrame(self):
        return self.data_frame.to_string() # may need to remove the tostring method call


    def pdframe(self,ssid, dbm):  # Updates the pdframe to contain the newest beacon frame and associated information
        SSID = ssid
        self.data_frame.loc[SSID] = (dbm)
    
    def run(self):
        # probably ok to start this thread from within the Scanner class instance as opposed to the app file... I think
        
        #y = threading.Thread(target=self.channel_hop) #call channel hopping on a monitor mode interface as passed by the command
        #y.daemon = True
        #y.start()

        sniff(iface=self.iface, prn=self.callback)
#random number Generator Thread
thread = Thread()
thread_stop_event = Event() # used to stop a thread mid execution if needed
newScanner = Scanner()
def createScanner(): # we eventually wanna tear this out and use the Scanner methods
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    #infinite loop of magical random numbers
    print("Constructing Scanner")
    
    

    while not thread_stop_event.isSet():
        print('entering thread')
        
        socketio.emit('newdataframe', {'frame': "hello"}, namespace='/test') # emit the newnumber event to the /test endpoiint
        socketio.sleep(2)
    while true:
        print('eeeeeeee')


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test') # upon a connection to the test endpoint, start a bcakground thread
def test_connect():
    # need visibility of the global thread object
    global thread #globalizes the thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread") # TODO remove prints as stdout isnt needed 
        thread = socketio.start_background_task(createScanner)
        print('starting thread 2')
        thread2 = socketio.start_background_task(newScanner.run()) 

@socketio.on('disconnect', namespace='/test') #upon disconnect to the /test endpoint
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0')
