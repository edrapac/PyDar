import os
import sys

whoami = os.popen('whoami').read().rstrip() # os.popen added newlines, not sure why

if whoami != 'root': # we need root access to put the iface into monitor mode
	print('Run it as root!')
	sys.exit(0)

iw_output = os.popen('iw dev').read().rstrip()

print(iw_output)