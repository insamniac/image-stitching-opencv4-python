# USAGE
# python image_stitching.py --images images/scottsdale --output output.png --crop 1

# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
import timeit


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images",  type=str, required=True,  help="path to input directory of images to stitch")
ap.add_argument("-o", "--output",  type=str, required=False, help="path to the output image")
ap.add_argument("-c", "--crop",    type=int, default=0,      help="whether to crop out largest rectangular region")
ap.add_argument("-t", "--cthresh", type=float, default=1.0,  help="change the panoConfidenceThresh setting")
args = vars(ap.parse_args())



# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []


def max_contours(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        return max(cnts, key=cv2.contourArea)


def display_images(title,img,title2, img2):
        cv2.imshow(f'{title}', img)
        cv2.imshow(f'{title2}', img2)
        print("press a button")
        cv2.waitKey(0)

def display_image(title,img):
        cv2.imshow(f'{title}', img)
        print("waiting for press button")
        cv2.waitKey(0)

def draw_kp(path, image):
        orb = cv2.ORB_create(edgeThreshold=50, patchSize=31, nlevels=8, fastThreshold=20, scaleFactor=1, WTA_K=2,scoreType=cv2.ORB_FAST_SCORE, firstLevel=0, nfeatures=50000)
#        orb=cv2.xfeatures2d.VGG_create()
#        orb = cv2.ORB_create(nfeatures=100000, scoreType=cv2.ORB_FAST_SCORE)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kp, des = orb.detectAndCompute(gray, None)
        print({'path':path, 'des':des})
        #kp = orb.detect(image)
        lastgood=True
        streak=0
        if len(kp) > 200:
            streak+=1
            print(f'path: {path}, kpcount: {len(kp)}, streak: {streak} ')
            image_kp=cv2.drawKeypoints(image, kp, None, color=(0,255,0), flags=cv2.DrawMatchesFlags_DEFAULT)
            lastgood=True
        else:
            lastgood=False
            streak=0


#orb = cv2.ORB_create()
#orb = cv2.ORB_create(edgeThreshold=50, patchSize=31, nlevels=8, fastThreshold=20, scaleFactor=1, WTA_K=2,scoreType=cv2.ORB_FAST_SCORE, firstLevel=0, nfeatures=50000)
orb = cv2.ORB_create(scaleFactor=2, scoreType=cv2.ORB_FAST_SCORE, nfeatures=100000)
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#matcher = cv2.BFMatcher()

def show_matches(img1, img2):
        kp1, desc1 =  orb.detectAndCompute(img1,None)
        kp2, desc2 =  orb.detectAndCompute(img2,None)

        matches = matcher.match(desc1, desc2)
        print(len(matches))

# Draw first 10 matches.
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        #img3 = cv2.drawMatches(img1,kp1,img2,kp2,ms,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        display_image('yay',img3)


# loop over the image paths, load each one, and add them to our
# images to stich list

for imagePath in imagePaths:
        image = cv2.imread(imagePath)
#        mc=max_contours(image)
        images.append(image)

print(len(images))

for i in range( len(images) - 1):
        i1=images[i]
        i2=images[i+1]
        show_matches(i1, i2)



