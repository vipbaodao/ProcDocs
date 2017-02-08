import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('note.jpg')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)
# ret,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
# titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
titles = ['Gray Image','BINARY','TRUNC','TOZERO']
# images = [GrayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
images = [GrayImage, thresh2, thresh3, thresh5]
for i in range(4):
   plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])

plt.show()

edges = cv2.Canny(thresh5,5,15)
# cv2.Canny()
# invedges = edges[:, :, ::-1]
print(edges.shape)
plt.imshow(edges, 'gray')
plt.show()

lines = cv2.HoughLinesP(thresh5,1,np.pi/180,20,minLineLength=5,maxLineGap=15)
print(lines)
print(lines.shape)

#     for rho,theta in lines[loop]:
#         a = np.cos(theta)
#         b = np.sin(theta)
#         x0 = a*rho
#         y0 = b*rho
#         x1 = int(x0 + 1000*(-b))
#         y1 = int(y0 + 1000*(a))
#         x2 = int(x0 - 1000*(-b))
#         y2 = int(y0 - 1000*(a))
#         print("I am working with %f and %f..." %(rho,theta))
for loop in range(lines.shape[0]):
    x1, y1, x2, y2 = lines[loop, 0]
    print("points coordinates:", x1, y1, x2, y2)
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
invimg = img[:,:, ::-1]
plt.imshow(invimg)
plt.show()
