import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
#	camera.capture('/home/pi/test.jpg')
    camera.stop_preview()
