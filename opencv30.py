import cv2
import numpy as np 
img=cv2.imread('sudoko.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,100,apertureSize=3)# aperture is just to get straight lines 
# if we increased it will get scattering lines 
cv2.imshow('image1',edges)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
# it doesnt consider all the points on image it gives random subset of points which are sufficient to draw lines
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


