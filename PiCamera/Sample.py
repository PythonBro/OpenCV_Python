import time
import picamera

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(2)
#	camera.capture('/home/pi/test.jpg')
camera.stop_preview()
