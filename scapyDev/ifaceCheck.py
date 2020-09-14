import os
import sys
import re

iface_reg = re.compile("wlan\S+")

whoami = os.popen('whoami').read().rstrip() # os.popen added newlines, not sure why

if whoami != 'root': # we need root access to put the iface into monitor mode
	print('Run it as root!')
	sys.exit(0)

iw_output = os.popen('iw dev').read().rstrip()

monitor_iface = iw_output.replace('monitor', 'monitor <- WARNING: This interface is already in monitor mode')
print(monitor_iface)
result = re.findall(iface_reg,monitor_iface)
for i in range(len(result)):
    print(i,":",result[i],"\n")
x= input("Please choose one of the following interfaces to put into monitor mode: ")

try:
    print("Attempting to now put %s in monitor mode" % (result[x]))
except Exception as e:
    print('Exception encountered, printing now')
    print(e)
