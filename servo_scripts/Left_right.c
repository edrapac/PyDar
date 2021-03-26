/* 
 *  
 * Modified by edrapac to control TIANKONGRC 8120MG Continuous Servo
 Original code by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.
 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int incomingByte = 0;   // for incoming serial data

void setup() {
  Serial.begin(9600);
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}



void loop() {

        
        if (Serial.available() > 0) { // if input has been written to the serial channel
                
                // read the incoming byte:
                incomingByte = Serial.read();

                // debugging to print the letter that was sent to the arduino
                Serial.print("received: ");
                Serial.print (incomingByte);
                
                if(incomingByte == 108){ // the letter 'r' in ascii
                 Serial.println("Writing 0, rotating Clockwise"); 
                 myservo.write(0); 
                }else if(incomingByte == 114){ // the letter 'l' in ascii
                  Serial.println("Writing 180, rotating Counterclockwise"); 
                  myservo.write(180); 
                }else if(incomingByte == 115){ //the letter 's' in ascii
                  Serial.println("Writing 90, stopping rotation"); 
                  myservo.write(90); 
                }else{
                  Serial.println("Please choose an input of either r,l or s"); 
                }
                  
                 
        }

  
} 
