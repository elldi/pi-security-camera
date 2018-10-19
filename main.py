#!/usr/bin/env python

from flask import Flask, render_template, Response, request, redirect
## import cv2
from picamera import PiCamera
from io import BytesIO

app = Flask(__name__)
## camera = cv2.VideoCapture(0)
camera = PiCamera()

@app.route('/')
def index():
	return render_template('live.html')

def gen():
	##with camera  as camera:
	image_stream = BytesIO()
	for image in camera.capture_continuous(image_stream, 'jpeg', use_video_port=True):
		image_stream.seek(0)
		yield (b'--frame\r\n'
              	b'Content-Type: image/jpeg\r\n\r\n' + image_stream.read() + b'\r\n')
		image_stream.seek(0)
		image_stream.truncate()
	camera.stop_recording()

@app.route('/video_feed')
def video_feed():
		return Response(gen(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = False, threaded = True)
