'''
import cv2
functions to use
VideoCapture: this function captures the content  of a video  argument:
integer vaLUE depend on the camera
read : read the content of the frames if True reading
write: write the content  to frame  to make a video
VideoWriter_fourcc: select  the codec xvid
VideoWriter:use to select the  video make  , codec , frame / sec ,pixel
flip:to flip the frame
waitKey(integer value)
release : this will release  the resources used by python
destroyAllWindows
'''
import cv2
cap=cv2.VideoCapture(0)
codec=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('mdslow.avi',codec,5.0,(640,480))
while (cap.isOpened()):
    flag,frame=cap.read()
    if flag==True:
            out.write(frame)
            cv2.imshow('image',frame)
            a=cv2.waitKey(1)
            if(a==ord('a')):
              break
cap.release()
out.release()
cv2.destroyAllWindows()
