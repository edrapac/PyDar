import time
def test(i):
	st = 'hello '+str(i)
	print(st)
if __name__ == '__main__':
	i=0
	while True:
		test(i)
		time.sleep(2)
		i+=1