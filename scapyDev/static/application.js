
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) { // newnumber is emitted from app.py, it is the name of the incoming event 
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number);
        numbers_string = '';
        for (var i = 0; i < numbers_received.length; i++){
            numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>'; // generate a paragraph tag with the contents of the random number
        }
        $('#log').html(numbers_string);
    });

});

/**
Application.js logic just takes care of receiving input
from the socket and then formatting the data as it comes in
for better "pretty" client output.
**/