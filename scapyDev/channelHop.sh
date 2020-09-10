#!/bin/bash

# Loop to hop channels, needs to be run as root 

while true;
	channel=$(($RANDOM % 14+1))
	do echo $channel;
	sleep 1
	done;	
