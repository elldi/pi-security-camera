#!/usr/bin/env python
from io import BytesIO
from picamera import PiCamera
import time

## Testing PiCamera 
my_stream = BytesIO()
camera = PiCamera()
camera.start_preview()
camera.resolution = (1024, 768)
start = time.time()

for foo in camera.capture_continuous(my_stream, 'jpeg', use_video_port=True):
   diff = time.time() - start 
   if diff > 10:
      break
