import cv2
import time
import random
cap=cv2.VideoCapture('md.avi')

while (cap.isOpened()):
    
    flag,frame=cap.read()
    if flag==True:
            #out.write(frame)
            a=random.randint(100,500)
            
            cv2.imshow('image',frame)
            cv2.imwrite('{}.jpg'.format(a),frame)
            a=cv2.waitKey(1)
            if(a==ord('a')):
              break
cap.release()
#out.release()
cv2.destroyAllWindows()
