import cv2 
import sys




file = sys.argv[1]
eachN = int(sys.argv[2])

vid = cv2.VideoCapture(file)

count = -1
success = 1
while success: 
    success, image = vid.read() 
    count += 1
    if success and (count % eachN) == 0:
        cv2.imwrite('{0}_frame{1}.jpg'.format(file, count), image) 
        print('file written: {0}_frame{1}.jpg'.format(file,count))



