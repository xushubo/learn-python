import threading, multiprocessing



print(multiprocessing.cpu_count())

'''def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target=loop)
	t.start()'''