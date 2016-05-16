import cv2
#import cv2.cv as cv
import numpy as np
import sys

img = cv2.imread(str(sys.argv[1]))

gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#parameter1 = dp, the inverse ratio of resolutiom
#parameter2 = min_dist, minimum distance between detected centres
#param1 - upper threshold for internal canny edge detector
#param2 - threshold cfor centre detection higher number = less circles found

circles = cv2.HoughCircles(gimg, cv2.cv.CV_HOUGH_GRADIENT, 1, 100, param1=30, param2=90, minRadius=5, maxRadius=100)

for i in circles[0,:]:
        #draw outer
        cv2.circle(gimg, (i[0], i[1]), i[2], (0,255,0), 2)
        #drawcentre
        cv2.circle(gimg, (i[0], i[1]), 2, (0,0,255), 3) #image, centre x/y, radius, color, ?? 

'''
cv2.imshow('Stuff', cimg)
cv2.waitKey(0)
'''

cv2.imwrite('BitchymcBitchface.png', gimg)

cv2.destroyAllWindows()
