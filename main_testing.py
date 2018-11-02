#!/usr/bin/env python

from flask import Flask, render_template, Response, request, redirect
from io import BytesIO
import camera_2

app = Flask(__name__)


thread1 = camera_2.myThread("testing")
thread1.start()

@app.route('/')
def index():
	return render_template('live.html')

def gen():
	while True:
	   image = thread1.get_frame()
	   yield (b'--frame\r\n'
           b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

@app.route('/video_feed')
def video_feed():
		return Response(gen(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = False, threaded = True)
