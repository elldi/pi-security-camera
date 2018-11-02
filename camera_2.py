#!/usr/bin/env python

import threading
import time
from picamera import PiCamera
from io import BytesIO



class myThread(threading.Thread):
	frame = None

	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name

	def get_frame(self):
		self.frame

	def run(self):
		print "Starting camera capture"
		my_file = open("image_stream.jpg", 'wb')
		counter = 0
		with PiCamera() as camera:
			camera.start_preview()
			time.sleep(2)
			stream = BytesIO()
			for foo in camera.capture_continuous(stream, 'bmp', use_video_port=True):
				# Store frame
				stream.seek(0)
				self.frame = stream.read()
				# Reset stream
				stream.seek(0)
				stream.truncate()
