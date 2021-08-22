import sys
from picamera import PiCamera
from time import sleep

if len(sys.argv) != 2:
    prev_time = 10
else:
    prev_time = int(sys.argv[1])

camera = PiCamera()
camera.resolution = (2592, 1944)

camera.start_preview()
sleep(prev_time)
camera.stop_preview()