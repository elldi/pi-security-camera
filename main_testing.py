#!/usr/bin/env python

from flask import Flask, render_template, Response, request, redirect
from io import BytesIO
import test_thread

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('live.html')

def gen():
	f = open('image_stream.jpg', 'rb')
	fs = f.read()
	for image in BytesIO(fs):
		image.seek(0)
		yield (b'--frame\r\n'
              	b'Content-Type: image/jpeg\r\n\r\n' + image.read() + b'\r\n')
		image.seek(0)
		image.truncate()
	camera.stop_recording()

@app.route('/video_feed')
def video_feed():
		return Response(gen(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	thread1 = test_thread.myThread("Testing")
	thread1.start()
	app.run(host = '0.0.0.0', debug = False, threaded = True)
