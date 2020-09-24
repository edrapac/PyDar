import os
import re

reg = re.compile("wl\w+mon")

stream = os.popen("iw dev").read()

if re.search(reg,stream):
	print(re.findall(reg,stream)[0])
else:
	print(stream)