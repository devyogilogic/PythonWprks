import cv2
a=cv2.imread('download.jpg',1)
print(a)
cv2.imshow('image',a)
cv2.imwrite('msdhoni.png',a)
x=cv2.waitKey()
if x==ord('a'):
    cv2.destroyAllWindows()
    
