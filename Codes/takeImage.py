#!/usr/bin/env python

from picamera import PiCamera
from time import sleep
import datetime
#from checkSpace import getAvail

camera = PiCamera()

for i in range(1000):
    #print("Inside for loop")

    curr = datetime.datetime.now()
    #print("Curr hour = ",curr.hour)
    
    if curr.hour >= 21:
        sleep(12*60*60)
    else:
    #    if(getAvail() < 5):
    #        f = open("/home/pi/logs.txt","a")
    #        s = "The timestamp is: " + str(curr) + " | i:" + str(i) + "ERROR: MEMORY FULL."
    #        f.write(s + "\n")
    #        f.close()
    #        print("MEMORY FULL...!")
    #        break
    #    print("Inside else")
        
        camera.start_preview(fullscreen=False, window=(100,100,640,640))
        sleep(5)
        camera.capture('/home/pi/images/' + curr.strftime("%d_%m_%Y_%H_%M_%S") + '.jpg')
        camera.stop_preview()

        f = open("/home/pi/logs.txt","a")
        s = "The timestamp is: " + str(curr) + " | i:" + str(i)
        f.write(s + "\n")
        f.close()
        sleep(5*60 - 5)


