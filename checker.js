var checkInterval = 2; // check interval, in seconds
var fileToCheck = "log.txt";
var lastData;

function checkFile() {
    $.get(fileToCheck, function (data) {
        // Update the text if it has changed
        if (lastData !== data) {
            $( "#target" ).val( data );
            $( "#target" ).animate({
                scrollTop: $( "#target" )[0].scrollHeight - $( "#target" ).height() //update the scrolling menu with the results found in the log file
            }, 'slow');
            lastData = data;
        }
    });
}

$(document).ready(function () {
    setInterval(checkFile, 1000 * checkInterval);
});