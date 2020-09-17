#!/bin/bash

# Loop to hop channels, needs to be run as root 
set -eou pipefail
iface=$1 # the interface being passed as an arg to this script from the main scapy program
while true;
	channel=$(($RANDOM % 13+1))
	do echo "Channel is now being set to: $channel"
	iw dev "$1" set channel "$channel"
	current_frequency=$(iwconfig "$1" | grep -o -E Frequency:[0-9].[0-9]+[[:space:]]GHz)
	echo "Current interface operating frequency set to $current_frequency"
	done;	

