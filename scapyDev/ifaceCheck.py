import os
import sys
import re

#define 2 simple regexes to catch linux WLAN interfaces and monitor mode interfaces, respectively
iface_reg = re.compile("wl\S+")
mon_reg = re.compile("\S+mon")

whoami = os.popen('whoami').read().rstrip() # os.popen added newlines, not sure why

if whoami != 'root': # we need root access to put the iface into monitor mode
	print('Run it as root!')
	sys.exit(0)

iw_output = os.popen('iw dev').read().rstrip()

monitor_iface = iw_output.replace('monitor', 'monitor <- WARNING: This interface is already in monitor mode') # Redundant warning here
print(monitor_iface,"\n")
result = re.findall(iface_reg,monitor_iface) # print the result of iw dev with the added warning about any monitor mode interfaces

print("Please choose one of the following interfaces to put into monitor mode: \n")
for i in range(len(result)):
    if not re.search(mon_reg,result[i]): 
    	print(i,":",result[i],"\n")
    else:
    	print("%s is already in monitor mode" %result[i]) #another redundant warning, inform user if an interface found by iw dev is already in monitor mode

try:
    
    x = int(input())
    print("Attempting to now put %s in monitor mode" % (result[x]))
    cmd = ('airmon-ng start '+result[x]) #does not have to be run as root so long as the ifaceCheck.py is ran as root instead
    
    stream = os.popen(cmd).read().rstrip()
    print(stream)
except ValueError:
    print('Invalid input, please enter a number corresponding to the interface name')

except Exception as e: #generic exception handling *shrug
    print('Exception encountered, printing now')
    print(e)
except KeyboardInterrupt:
	print("Ctrl+c detected, shutting down")
	sys.exit(0) #exit clean
