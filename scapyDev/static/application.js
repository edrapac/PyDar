
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var frames_received = [];

    //receive details from server
    socket.on('newdataframe', function(msg) { // newdataframe is emitted from app.py, it is the name of the incoming event 
        console.log("Received frame" + msg.frame);
        //maintain a list of ten numbers
        if (frames_received.length >= 20){
            frames_received.shift()
        }            
        frames_received.push(msg.frame);
        frame_string = '';
        for (var i = 0; i < frames_received.length; i++){
            frame_string = frame_string + '<p>' + frames_received[i].toString() + '</p>'; // generate a paragraph tag with the contents of the frame
        }
        $('#log').html(frame_string);
    });

});

/**
Application.js logic just takes care of receiving input
from the socket and then formatting the data as it comes in
for better "pretty" client output.
**/