#!/usr/bin/env python

from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0) 

@app.route('/')
def index():
	return render_template('index.html')

def gen():
	print("Starting camera")
	while True:
		_, frame = camera.read()
		frame = cv2.imencode('.jpg', frame)[1].tobytes()
		yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
		return Response(gen(), mimetype = 'multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
	app.run(host = '0.0.0.0', debug = True, threaded = True)
