import cv2
import numpy as np

frameWidth= 150
frameHeight= 100
cap = cv2.VideoCapture(1) #not any with my link change 1 to 0 if not working
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass
while True:
    _, img =cap.read()
    cap.set(10, 1000 )

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hsv_blur=cv2.GaussianBlur(img_hsv,(3,3),1)

    cv2.namedWindow("Callibration")
    cv2.resizeWindow("Callibration",640,220)
    cv2.createTrackbar("hue_min","Callibration",0,179,empty)
    cv2.createTrackbar("hue_max","Callibration",179,179,empty)
    cv2.createTrackbar("sat_min","Callibration",0,255,empty)
    cv2.createTrackbar("sat_max","Callibration",255,255,empty)
    cv2.createTrackbar("min_val","Callibration",0,255,empty)
    cv2.createTrackbar("max_val","Callibration",255,255,empty)

    hue_min=cv2.getTrackbarPos("hue_min","Callibration")
    hue_max=cv2.getTrackbarPos("hue_max","Callibration")
    sat_min=cv2.getTrackbarPos("sat_min","Callibration")
    sat_max=cv2.getTrackbarPos("sat_max","Callibration")
    min_val=cv2.getTrackbarPos("min_val","Callibration")
    max_val=cv2.getTrackbarPos("max_val","Callibration")
    print(min_val)

    lower=np.array([hue_min,sat_min,min_val])
    upper=np.array([hue_max,sat_max,max_val])
    masked_img=cv2.inRange(img_hsv,lower,upper)
    new_img=cv2.bitwise_and(img,img,mask=masked_img)

    cv2.resize(img,(150,100))
    cv2.resize(img_hsv,(150,100))
    cv2.resize(masked_img,(150,100))
    cv2.resize(new_img,(150,100))

    imgHor1=np.hstack((img,img_hsv))
    # imgHor2=np.hstack((masked_img,new_img))
    cv2.imshow("Unmasked",imgHor1)
    # cv2.imshow("masked",imgHor2)

    # cv2.imshow("Orignal",img)
    cv2.imshow("hsv_blur",img_hsv_blur)
    cv2.imshow("mask",masked_img)
    cv2.imshow("new",new_img)

    if cv2.waitKey(1) & 0xFF==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()



