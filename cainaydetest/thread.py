import time
import threading

def cal_square(numbers):
	print("calculate square number")
	for n in numbers:
		time.sleep(1)
		print ('square:', n*n)

def cal_cube(numbers):
	print("calculate cube number")
	for n in numbers:
		time.sleep(1)
		print ('square:', n*n*n)

arr = [3, 1, 7, 2, 1]
t = time.time()
thr1 = threading.Thread(target=cal_square, args=(arr,))
thr2 = threading.Thread(target=cal_cube, args=(arr,))
thr1.start()
thr2.start()
print ("done in ", time.time()- t)