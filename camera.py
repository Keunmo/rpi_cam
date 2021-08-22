import sys, time
from picamera import PiCamera
from time import sleep

if len(sys.argv) != 2:
    pic_num = 1
else:
    pic_num = int(sys.argv[1])

camera = PiCamera()

camera.resolution = (2592, 1944)
# camera.framerate = 15

camera.start_preview()
for i in range(pic_num):
    sleep(3)
    phototime = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    camera.capture('./pic/%s.jpg' % phototime)
    print("picture {} saved!".format(phototime))

camera.stop_preview()
