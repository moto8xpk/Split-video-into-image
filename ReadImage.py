# import cv2
# import numpy as np
#
#
# img= cv2.imread('img-korea.jpg',0)
# cv2.imwrite('ima-korea.png',img)
# cv2.imshow('hello world opencv',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('video.MOV')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #
    # # Saves image of the current frame in jpg file
    # name = './data/frame' + str(currentFrame) + '.jpg'
    # print ('Creating...' + name)
    # cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1
print('done:',currentFrame)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
