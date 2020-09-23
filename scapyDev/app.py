from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
from sniffer import Scanner

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
app.config['DEBUG'] = True


socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event() # used to stop a thread mid execution if needed

def randomNumberGenerator(): # we eventually wanna tear this out and use the Scanner methods
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    #infinite loop of magical random numbers
    print("Making random numbers")
    newtest = test()
    while not thread_stop_event.isSet(): # if the thread stop command hasnt been issued
        number = test.test()
        
        socketio.emit('newnumber', {'number': number}, namespace='/test') # emit the newnumber event to the /test endpoiint
        socketio.sleep(5)


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
        thread = socketio.start_background_task(randomNumberGenerator) 

@socketio.on('disconnect', namespace='/test') #upon disconnect to the /test endpoint
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0')