#!/usr/bin/env python

import threading
import time
from picamera import PiCamera



class myThread(threading.Thread):
   def __init__(self, name):
	threading.Thread.__init__(self)
	self.name = name

   def run(self):
	print "Starting camera capture"
	my_file = open("image_stream.jpg", 'wb')
	counter = 0
	with PiCamera() as camera:
	   while(True):
		camera.start_preview()
	   	camera.capture(my_file)
		counter = counter + 1
		if counter == 5:
		   break 
	my_file.close()


## thread1 = myThread("Camera Capture Thread")


## thread1.start()


print "Exiting Main Thread"
