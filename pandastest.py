import pandas as pd
import threading, queue
import time
import random
import os
import sys

df_queue = queue.Queue()

def pdframe(q):
	random_str=-(random.randint(60,80))
	random_str = str(random_str)
	data_frame = pd.DataFrame(columns=["SSID","Signal Strength (dBm)"])
	data_frame.set_index("SSID",inplace=True)
	SSID = 'Network1'
	data_frame.loc[SSID] = (random_str)
	q.put(data_frame)
	

while True:
	try:
		x = threading.Thread(target=pdframe,args=(df_queue,))
		x.start()
		df = df_queue.get()
		print(df.to_string())
		time.sleep(0.5)
		os.system("clear") #unfortunately no better way to do this than to feed clear directly to the OS to clear stdout
	except KeyboardInterrupt:
		print('Keyboard Interrupt detected, exiting...')
		sys.exit(0) # exit clean 