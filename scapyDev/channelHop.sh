#!/bin/bash

# Loop to hop channels, needs to be run as root 
set -eou pipefail

while true;
	channel=$(($RANDOM % 13+1))
	do echo "Channel is now being set to: $channel"
	iw dev wlan1mon set channel "$channel"
	current_frequency=$(iwconfig wlan1mon | grep -o -E Frequency:[0-9].[0-9]+[[:space:]]GHz)
	echo "Current interface operating frequency set to $current_frequency"
	sleep 2
	done;	

