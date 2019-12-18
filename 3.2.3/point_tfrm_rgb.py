
import numpy as np
import cv2

def apply_point_trfm(img1, c, B):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            valr = c*img1[i,j][2] + b #Image scaling function from lab manual
            valg = c*(img1[i,j][1]) + b #Image scaling function from lab manual
            valb = c*(img1[i,j][0]) + b #Image scaling function from lab manual
            if valr > 255: #preventing a value greater than the 255 limit.
                img1[i,j][2] = 255
            elif valr < 0: #preventing a value less than the 0 limit
                img1[i,j][2] = 0
            else:
                img1[i,j][2] = valr
            if valg > 255: #preventing a value greater than the 255 limit.
                img1[i,j][1] = 255  
            elif valg < 0: #preventing a value less than the 0 limit
                img1[i,j][1] = 0
            else:
                img1[i,j][1] = valg
            if valb > 255: #preventing a value greater than the 255 limit.
                img1[i,j][0] = 255  
            elif valb < 0: #preventing a value less than the 0 limit
                img1[i,j][0] = 0
            else:
                img1[i,j][0] = valb
    return img1

img = cv2.imread('mandrill.png', 1)

c = float(input("Please enter your value for c: "))

b = float(input("Please enter your value for b between 0 and 255: "))

while (b > 255):

    if b > 255:
        
        b = float(input("Invalid input, please enter your value for b between 0 and 255: "))

img2 = apply_point_trfm(img, c, b)

cv2.imwrite('mandrill_new.png', img2)