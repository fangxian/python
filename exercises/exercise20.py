import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(1):
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    lower_green=np.array([50,50,50])
    upper_green=np.array([70,255,255])
    lower_red=np.array([5,50,50])
    upper_red=np.array([10,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    mask1=cv2.inRange(hsv,lower_green,upper_green)
    mask2=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask+mask1+mask2)
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask1)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
