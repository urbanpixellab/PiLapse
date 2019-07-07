from time import sleep
import picamera
from datetime import datetime
import os
import shutil
#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

now = datetime.now()
path = 'IMAGES/' + now.strftime("%Y-%m-%d-%H-%M-%S")
os.mkdir(path)
WAIT_TIME = 15
camera = picamera.PiCamera()
camera.resolution = (2400,1600)




def copyFile(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

while True:
	
	name = datetime.now()
	filename = '/' + name.strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
	##new
	camera.start_preview()
	sleep(3)
	camera.capture(path+filename,False,False,False,20)
	camera.stop_preview()

	## old camera.capture(path+filename)
	copyFile(path+filename,'preview.jpg')
	sleep(WAIT_TIME-3)
