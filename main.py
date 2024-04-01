import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey , ReleaseKey
from directkeys import space_pressed
import time

detector=HandDetector(detectionCon=0.8 , maxHands= 1)

space_key_pressed=pressed=space_pressed

time.sleep(2.0)

current_key_pressed = set()
video=cv2.VideoCapture(0)

while True:
   ret,frame=video.read()
   keyPressed=False
   spacePressed=False
   key_count=0
   key_pressed=0
   hands,image=detector.findHands(frame)
   cv2.rectangle(image, (0,480) , (115,425)  , (0 , 0 , 0) , -2)
   if hands:
    lmList=hands[0]
    fingersUp=detector.fingersUp(lmList)
    print(fingersUp)
    #if fingersUp!=[1,1,0,0,0]:
           # cv2.putText(frame, 'run' , (17,460) , cv2.FONT_HERSHEY_COMPLEX ,1 ,(255 , 255 , 255) ,1, cv2.LINE_AA)
    #if fingersUp==[0,0,0,0,0]:
       # cv2.putText(frame, 'run' , (20,460) , cv2.FONT_HERSHEY_COMPLEX ,1 ,(255 , 255 , 255) ,1, cv2.LINE_AA)
    if fingersUp==[0,0,0,0,0]:
        cv2.putText(frame, 'jump' , (17,460) , cv2.FONT_HERSHEY_COMPLEX ,1 ,(255 , 255 , 255) ,1, cv2.LINE_AA)
        PressKey(space_key_pressed)==True
        spacePressed=True
        current_key_pressed.add(space_key_pressed)
        key_pressed=space_key_pressed
        keyPressed=True
        key_count=key_count+1

    elif key_count==1 and len(current_key_pressed)==2:
        for key in current_key_pressed:
            if key_pressed != key:
                ReleaseKey(key)
        current_key_pressed = set()
        for key in current_key_pressed:
            ReleaseKey(key)
            current_key_pressed=set()
  
   cv2.imshow("Frame",frame)
   k=cv2.waitKey(1)
   if k==ord('q'):
    break

video.release()
cv2.destroyAllWindows()


